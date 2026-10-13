"""The workflow charts as one directed graph, read from the Markdown sources with the audit's Mermaid parser.

A reader stands at a node of one diagram and follows its solid arrows; dotted arrows are pointers and are not
followed. Besides the arrows, a reader moves between diagrams in four ways:

- a "Continue in part n" terminator opens the entries of part n on the same page (the entries that name the
  part the reader comes from, when any do);
- a phase box Pn, or a "To Pn" / "Continue on the spine at Pn" terminator, opens the entries of phase n's page;
- a "Representation k: ..." box opens the entries of that representation page;
- a phase box or a branch box drawn on another page lets the reader continue on that page's chart from the same
  box (a count reader leaves the P2 chart at the P3 box and goes on in the B1 chart, which draws P3 too).

A leaf ref sends the reader to read that leaf's section and back; it never moves the reader to another chart. Two
parts of one page connect only through their terminators.
"""
import re
from collections import defaultdict, deque

import audit_flowcharts as audit

PHASE_BOX = re.compile(r"^P(\d+)$")
BOX = re.compile(r"^(?:P\d+|B\d)$")
TO_PHASE = re.compile(r"^(?:To|Continue on the spine at) P(\d+)\b")
TO_PART = re.compile(r"\bin part (\d+)$")
REPRESENTATION = re.compile(r"^Representation (\d):")
PHASE_PAGE = re.compile(r"^01-workflow/p(\d\d)-[^/]+(?:\.md|/index\.md)$")
REPRESENTATION_PAGE = re.compile(r"^01-workflow/p05-representation/0(\d)-[^/]+\.md$")
# Pages whose charts make up the spine a reader walks; purpose and branch charts are added per reader.
SPINE = [PHASE_PAGE.pattern, REPRESENTATION_PAGE.pattern]


def part_numbers(label: str) -> set[int]:
    """Part numbers an entry terminator names: "From part 2", "From parts 1 and 3", "From parts 2 to 4"."""
    m = re.match(r"From parts? (\d+(?:(?:, | and | to )\d+)*)", label)
    if not m:
        return set()
    span = re.fullmatch(r"(\d+) to (\d+)", m.group(1))
    if span:
        return set(range(int(span.group(1)), int(span.group(2)) + 1))
    return {int(n) for n in re.findall(r"\d+", m.group(1))}


def phase_of_page(page: str) -> int | None:
    m = PHASE_PAGE.match(page)
    if m:
        return int(m.group(1))
    return 5 if REPRESENTATION_PAGE.match(page) else None


class Graph:
    def __init__(self, diagrams: list[audit.Diagram]):
        """`diagrams` in reading order; each `where` is "page#mermaid-n", n counting the page's parts."""
        self.diagrams: list[tuple[str, audit.Diagram]] = []
        self.labels: dict[str, set[str]] = defaultdict(set)  # full labels, <br/> included
        self.shapes: dict[str, set[str]] = defaultdict(set)
        self.edge_labels: dict[tuple[str, str], set[str]] = defaultdict(set)
        self.appears: dict[str, list[int]] = defaultdict(list)  # node -> diagrams that draw it
        self.moves: dict[tuple[str, int], set[tuple[str, int]]] = defaultdict(set)
        by_page: dict[str, list[int]] = defaultdict(list)
        for d in diagrams:
            page = d.where.split("#", 1)[0]
            di = len(self.diagrams)
            self.diagrams.append((page, d))
            by_page[page].append(di)
            for nid in d.used_ids:
                self.appears[nid].append(di)
            for nid, node in d.nodes.items():
                self.labels[nid].add(node.label)
                self.shapes[nid].add(node.shape)
            for e in d.edges:
                self.edge_labels[(e.source, e.target)].add(e.label)
                if not e.dotted:
                    self.moves[(e.source, di)].add((e.target, di))
        self._link(by_page)

    @classmethod
    def from_site(cls, site: audit.Site) -> "Graph":
        return cls(audit.collect_diagrams(site))

    def page(self, di: int) -> str:
        return self.diagrams[di][0]

    def _entries(self, di: int) -> list[tuple[str, int]]:
        d = self.diagrams[di][1]
        incoming = {e.target for e in d.edges}
        return [(n, di) for n, node in d.nodes.items() if node.shape == "terminator" and n not in incoming]

    def _link(self, by_page: dict[str, list[int]]) -> None:
        phase_entries: dict[int, list[tuple[str, int]]] = {}
        representation_entries: dict[int, list[tuple[str, int]]] = {}
        for page, dis in by_page.items():
            m = PHASE_PAGE.match(page)
            if m:
                phase_entries[int(m.group(1))] = self._entries(dis[0])
            m = REPRESENTATION_PAGE.match(page)
            if m:
                representation_entries[int(m.group(1))] = self._entries(dis[0])
        for page, dis in by_page.items():
            for k, di in enumerate(dis, 1):
                d = self.diagrams[di][1]
                for nid in d.used_ids:
                    box = PHASE_BOX.match(nid)
                    if box and int(box.group(1)) in phase_entries:
                        self.moves[(nid, di)].update(phase_entries[int(box.group(1))])
                for nid, node in d.nodes.items():
                    label = audit.label_first_line(node.label)
                    rep = REPRESENTATION.match(label)
                    if rep and int(rep.group(1)) in representation_entries:
                        self.moves[(nid, di)].update(representation_entries[int(rep.group(1))])
                    if node.shape != "terminator":
                        continue
                    phase = TO_PHASE.match(label)
                    if phase and int(phase.group(1)) in phase_entries:
                        self.moves[(nid, di)].update(phase_entries[int(phase.group(1))])
                    part = TO_PART.search(label)
                    if part and not label.startswith("From") and int(part.group(1)) <= len(dis):
                        self.moves[(nid, di)].update(self._part_entries(d, label, k, dis[int(part.group(1)) - 1]))

    def _part_entries(self, d: audit.Diagram, label: str, k: int, target: int) -> list[tuple[str, int]]:
        """Entries of part `target` that a "... in part n" terminator of part k opens: those naming part k, and among
        them those sharing the terminator's qualifier ("A check failed: continue in part 4" opens "From parts 1 to 3:
        a check failed"); an unqualified terminator opens the entries no qualified sibling claims."""
        entries = self._entries(target)
        text = {e: audit.label_first_line(self.diagrams[e[1]][1].nodes[e[0]].label).lower() for e in entries}
        own = [e for e in entries if k in part_numbers(text[e])] or entries
        qualifier = label.split(": ", 1)[0].lower() if ": " in label else ""
        if qualifier:
            return [e for e in own if qualifier in text[e]] or own
        siblings = {audit.label_first_line(n.label).split(": ", 1)[0].lower() for n in d.nodes.values()
                    if n.shape == "terminator" and ": " in n.label and TO_PART.search(audit.label_first_line(n.label))}
        return [e for e in own if not any(q in text[e] for q in siblings)] or own

    def _walk(self, start: set[tuple[str, int]], dst: str, pages: list[str] | None,
              avoid: set[str]) -> set[tuple[str, int]]:
        """Every copy of `dst` a reader standing at the `start` states can arrive at."""
        def allowed(di: int) -> bool:
            return pages is None or any(re.match(p, self.page(di)) for p in pages)

        start = {s for s in start if allowed(s[1])}
        seen, queue, found = set(start), deque(start), set()
        while queue:
            u, di = queue.popleft()
            if u == dst:
                found.add((u, di))
            nxt = set(self.moves[(u, di)])
            if BOX.match(u):
                nxt.update((u, dj) for dj in self.appears[u] if self.page(dj) != self.page(di))
            for v, dj in nxt:
                if (v, dj) not in seen and v not in avoid and allowed(dj):
                    seen.add((v, dj))
                    queue.append((v, dj))
        return found

    def _start(self, src: str) -> set[tuple[str, int]]:
        if src not in self.appears:
            raise KeyError(f"unknown chart node {src}")
        return {(src, di) for di in self.appears[src]}

    def reach(self, src: str, dst: str, pages: list[str] | None = None, avoid: set[str] = frozenset()) -> bool:
        """Whether a reader at `src` can arrive at `dst` reading only the diagrams on `pages` (regexes; None = every
        page) and never passing a node in `avoid`."""
        self._start(dst)
        return bool(self._walk(self._start(src), dst, pages, set(avoid)))

    def ordered(self, route: list[str], pages: list[str] | None = None, avoid: set[str] = frozenset()) -> bool:
        """Whether one reader walks the route in order: each leg starts where the previous leg arrived."""
        states = self._start(route[0])
        for nid in route[1:]:
            self._start(nid)
            states = self._walk(states, nid, pages, set(avoid))
            if not states:
                return False
        return True

    def edge(self, a: str, b: str, text: str) -> bool:
        return any(text in label for label in self.edge_labels.get((a, b), ()))

    def label_has(self, nid: str, text: str) -> bool:
        return any(text in label for label in self.labels.get(nid, ()))

    def answers(self, nid: str) -> set[str]:
        return {label for (a, _), labels in self.edge_labels.items() if a == nid for label in labels}

    def spine_phases(self, nid: str) -> set[int]:
        return {p for di in self.appears[nid] if (p := phase_of_page(self.page(di))) is not None}
