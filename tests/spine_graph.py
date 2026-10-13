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
    def __init__(self, site: audit.Site):
        self.diagrams: list[tuple[str, audit.Diagram]] = []
        self.labels: dict[str, set[str]] = defaultdict(set)  # full labels, <br/> included
        self.shapes: dict[str, set[str]] = defaultdict(set)
        self.edge_labels: dict[tuple[str, str], set[str]] = defaultdict(set)
        self.appears: dict[str, list[int]] = defaultdict(list)  # node -> diagrams that draw it
        self.moves: dict[tuple[str, int], set[tuple[str, int]]] = defaultdict(set)
        by_page: dict[str, list[int]] = defaultdict(list)
        for d in audit.collect_diagrams(site):
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
                        target = dis[int(part.group(1)) - 1]
                        entries = self._entries(target)
                        own = [(n, t) for n, t in entries
                               if k in part_numbers(audit.label_first_line(self.diagrams[t][1].nodes[n].label))]
                        self.moves[(nid, di)].update(own or entries)

    def reach(self, src: str, dst: str, pages: list[str] | None = None, avoid: set[str] = frozenset()) -> bool:
        """Whether a reader at `src` can arrive at `dst` reading only the diagrams on `pages` (regexes; None = every
        page) and never passing a node in `avoid`."""
        for nid in (src, dst):
            if nid not in self.appears:
                raise KeyError(f"unknown chart node {nid}")

        def allowed(di: int) -> bool:
            return pages is None or any(re.match(p, self.page(di)) for p in pages)

        start = [(src, di) for di in self.appears[src] if allowed(di)]
        seen, queue = set(start), deque(start)
        while queue:
            u, di = queue.popleft()
            if u == dst:
                return True
            nxt = set(self.moves[(u, di)])
            if BOX.match(u):
                nxt.update((u, dj) for dj in self.appears[u] if self.page(dj) != self.page(di))
            for v, dj in nxt:
                if (v, dj) not in seen and v not in avoid and allowed(dj):
                    seen.add((v, dj))
                    queue.append((v, dj))
        return False

    def ordered(self, route: list[str], **scope) -> bool:
        return all(self.reach(a, b, **scope) for a, b in zip(route, route[1:]))

    def edge(self, a: str, b: str, text: str) -> bool:
        return any(text in label for label in self.edge_labels.get((a, b), ()))

    def label_has(self, nid: str, text: str) -> bool:
        return any(text in label for label in self.labels.get(nid, ()))

    def answers(self, nid: str) -> set[str]:
        return {label for (a, _), labels in self.edge_labels.items() if a == nid for label in labels}

    def spine_phases(self, nid: str) -> set[int]:
        return {p for di in self.appears[nid] if (p := phase_of_page(self.page(di))) is not None}
