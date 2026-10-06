# scripts/audit_flowcharts.py
"""Audit the flowchart framework: Mermaid diagrams, the leaf-node inventory, and the glossary.

Run: python scripts/audit_flowcharts.py [--root PATH]
Exit status 1 when any error-level finding exists; warnings never fail the run.
Rules: planning/2026-10-06-flowchart-framework-design.md, sections 10 and 11.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from markdown.extensions.toc import slugify, unique

AUDIT_SKIP_MARKER = "%% audit: skip"
FOUNDATION_PHASE = "F"
SECTION_DIRS = ("reference", "01-workflow")
FIRST_MENTION_PREFIXES = ("00-foundations/", "reference/")


@dataclass(frozen=True)
class Finding:
    level: str  # "error" or "warning"
    where: str
    message: str


@dataclass(frozen=True)
class Node:
    id: str
    shape: str  # rect | diamond | terminator | subroutine | data
    label: str


@dataclass
class Diagram:
    where: str
    nodes: dict[str, Node] = field(default_factory=dict)
    edge_ids: set[str] = field(default_factory=set)
    classes: dict[str, set[str]] = field(default_factory=dict)

    def is_ref(self, node_id: str) -> bool:
        node = self.nodes[node_id]
        return node.shape == "subroutine" or "ref" in self.classes.get(node_id, set())

    def is_leaf(self, node_id: str) -> bool:
        node = self.nodes[node_id]
        return node.shape == "rect" and not self.is_ref(node_id) and not node_id.endswith("_FLAG")


# ---------------------------------------------------------------- Mermaid parsing

FENCE_RE = re.compile(r"^```mermaid[^\n]*\n(.*?)^```[ \t]*$", re.M | re.S)
SHAPES = {"([": "terminator", "[[": "subroutine", "[/": "data", "[": "rect", "{": "diamond"}
NODE_RE = re.compile(
    r'(?<![\w-])([A-Z][A-Z0-9_]*)(\(\[|\[\[|\[/|\[|\{)"((?:[^"\\]|\\.)*)"(\]\)|\]\]|/\]|\]|\})'
)
CLASS_RE = re.compile(r"^\s*class\s+([A-Z0-9_,\s]+?)\s+([A-Za-z_][\w-]*)\s*$", re.M)
ARROW_RE = re.compile(r"\s*(?:-->|-\.->|==>|-\.-|---)\s*(?:\|[^|]*\|)?\s*")
ID_RE = re.compile(r"^([A-Z][A-Z0-9_]*)")
SKIP_LINE_RE = re.compile(r"^\s*(%%|graph\b|flowchart\b|classDef\b|class\b|subgraph\b|end\b|direction\b)")
QUOTED_RE = re.compile(r'"(?:[^"\\]|\\.)*"')


def extract_mermaid_blocks(text: str) -> list[tuple[int, str]]:
    """Return (line_number_of_fence, source) for every ```mermaid fence."""
    blocks = []
    for m in FENCE_RE.finditer(text):
        blocks.append((text.count("\n", 0, m.start()) + 1, m.group(1)))
    return blocks


def parse_diagram(source: str, where: str) -> Diagram:
    d = Diagram(where=where)
    for m in NODE_RE.finditer(source):
        node_id, opener, label = m.group(1), m.group(2), m.group(3)
        d.nodes.setdefault(node_id, Node(node_id, SHAPES[opener], label))
    for m in CLASS_RE.finditer(source):
        for node_id in re.split(r"[,\s]+", m.group(1).strip()):
            if node_id:
                d.classes.setdefault(node_id, set()).add(m.group(2))
    for raw in source.splitlines():
        line = raw.strip()
        if not line or SKIP_LINE_RE.match(line) or not ARROW_RE.search(line):
            continue
        unquoted = QUOTED_RE.sub('""', line)
        for part in ARROW_RE.split(unquoted):
            for piece in part.split("&"):
                m = ID_RE.match(piece.strip())
                if m:
                    d.edge_ids.add(m.group(1))
    return d


def collect_diagrams(docs_dir: Path) -> list[Diagram]:
    diagrams = []
    for md in sorted(docs_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for line_no, src in extract_mermaid_blocks(text):
            if AUDIT_SKIP_MARKER in src:
                continue
            diagrams.append(parse_diagram(src, f"{md.relative_to(docs_dir).as_posix()}:{line_no}"))
    return diagrams


# ---------------------------------------------------------------- anchors and front matter

FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*\n", re.S)
CODE_FENCE_RE = re.compile(r"^```.*?^```[ \t]*$", re.M | re.S)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.M)
ATTR_ID_RE = re.compile(r"\{\s*#([\w-]+)\s*\}\s*$")
EXPLICIT_ANCHOR_RE = re.compile(r'<a\s+id="([\w-]+)"')
LINK_TEXT_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def strip_front_matter(text: str) -> str:
    m = FRONT_MATTER_RE.match(text)
    return text[m.end():] if m else text


def front_matter(text: str) -> dict:
    m = FRONT_MATTER_RE.match(text)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def heading_anchors(text: str) -> set[str]:
    """Anchors MkDocs will generate for a page: toc slugify with `_N` uniqueness, `{#id}` attrs, `<a id>` tags."""
    body = CODE_FENCE_RE.sub("", strip_front_matter(text))
    used: set[str] = set()
    for m in HEADING_RE.finditer(body):
        heading = m.group(2).rstrip("#").strip()
        attr = ATTR_ID_RE.search(heading)
        if attr:
            used.add(attr.group(1))
            continue
        unique(slugify(LINK_TEXT_RE.sub(r"\1", heading), "-"), used)
    used.update(EXPLICIT_ANCHOR_RE.findall(text))
    return used


# ---------------------------------------------------------------- inventory

SECTION_RE = re.compile(r"^[\w./-]+\.md#[\w-]+$")
REQUIRED_ROW_KEYS = ("id", "label", "phase", "areas", "section")


@dataclass(frozen=True)
class Row:
    id: str
    label: str
    phase: str
    areas: tuple[int, ...]
    section: str

    @property
    def file(self) -> str:
        return self.section.split("#", 1)[0]

    @property
    def anchor(self) -> str:
        return self.section.split("#", 1)[1]


def load_inventory(path: Path) -> tuple[list[Row], list[Finding]]:
    if not path.is_file():
        return [], [Finding("error", str(path), "inventory file does not exist")]
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rows: list[Row] = []
    findings: list[Finding] = []
    seen: set[str] = set()
    for i, raw in enumerate(data.get("nodes") or []):
        where = f"{path.name}#nodes[{i}]"
        missing = [k for k in REQUIRED_ROW_KEYS if k not in raw]
        if missing:
            findings.append(Finding("error", where, f"missing keys {missing}"))
            continue
        if not SECTION_RE.match(str(raw["section"])):
            findings.append(Finding("error", where, f"section {raw['section']!r} must look like path/file.md#anchor"))
            continue
        if raw["id"] in seen:
            findings.append(Finding("error", where, f"duplicate inventory id {raw['id']}"))
            continue
        seen.add(raw["id"])
        rows.append(Row(str(raw["id"]), str(raw["label"]), str(raw["phase"]),
                        tuple(int(a) for a in raw["areas"] or []), str(raw["section"])))
    return rows, findings


def check_inventory_targets(rows: list[Row], docs_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    anchors: dict[str, set[str]] = {}
    for r in rows:
        target = docs_dir / r.file
        if not target.is_file():
            findings.append(Finding("error", r.id, f"section file {r.file} does not exist"))
            continue
        if r.file not in anchors:
            anchors[r.file] = heading_anchors(target.read_text(encoding="utf-8"))
        if r.anchor not in anchors[r.file]:
            findings.append(Finding("error", r.id, f"anchor #{r.anchor} not found in {r.file}"))
    return findings


# ---------------------------------------------------------------- diagram checks

def _defined_ids(diagrams: list[Diagram]) -> dict[str, str]:
    """Non-ref node id -> where first defined."""
    defined: dict[str, str] = {}
    for d in diagrams:
        for nid in d.nodes:
            if not d.is_ref(nid):
                defined.setdefault(nid, d.where)
    return defined


def check_diagrams(diagrams: list[Diagram]) -> list[Finding]:
    findings: list[Finding] = []
    defined: dict[str, str] = {}
    for d in diagrams:
        for nid in d.nodes:
            if d.is_ref(nid):
                continue
            if nid in defined:
                findings.append(Finding("error", d.where, f"node {nid} already defined in {defined[nid]}"))
            else:
                defined[nid] = d.where
    for d in diagrams:
        for nid in sorted(d.edge_ids - set(d.nodes)):
            findings.append(Finding("error", d.where, f"node {nid} is used in an edge but has no shaped definition in this diagram"))
    return findings


def check_refs(diagrams: list[Diagram], rows: list[Row]) -> list[Finding]:
    defined = _defined_ids(diagrams)
    foundation = {r.id for r in rows if r.phase == FOUNDATION_PHASE}
    findings: list[Finding] = []
    for d in diagrams:
        for nid in d.nodes:
            if d.is_ref(nid) and nid not in defined and nid not in foundation:
                findings.append(Finding("error", d.where, f"ref {nid} has no definition in any diagram and is not a foundation inventory row"))
    return findings


def check_nodes_vs_inventory(diagrams: list[Diagram], rows: list[Row]) -> list[Finding]:
    findings: list[Finding] = []
    by_id = {r.id: r for r in rows}
    leaves: dict[str, str] = {}
    refs: set[str] = set()
    for d in diagrams:
        for nid in d.nodes:
            if d.is_ref(nid):
                refs.add(nid)
            elif d.is_leaf(nid):
                leaves.setdefault(nid, d.where)
    for nid, where in sorted(leaves.items()):
        if nid not in by_id:
            findings.append(Finding("error", where, f"leaf {nid} has no inventory row"))
    for r in rows:
        if r.phase == FOUNDATION_PHASE:
            if r.id not in refs:
                findings.append(Finding("error", r.id, "foundation row is not referenced by any ref node"))
        elif r.id not in leaves:
            findings.append(Finding("error", r.id, "inventory row has no leaf definition in any diagram"))
    return findings


# ---------------------------------------------------------------- sections

def check_sections(docs_dir: Path, rows: list[Row], terms: list[dict]) -> list[Finding]:
    """Every page under SECTION_DIRS is a method page (in the inventory) or a linked theory page."""
    method_files = {r.file for r in rows}
    corpus: list[str] = []
    for f in sorted(method_files):
        p = docs_dir / f
        if p.is_file():
            corpus.append(p.read_text(encoding="utf-8"))
    corpus.extend(str(t.get("derivation") or "") for t in terms)
    haystack = "\n".join(corpus)
    findings: list[Finding] = []
    for sub in SECTION_DIRS:
        base = docs_dir / sub
        if not base.is_dir():
            continue
        for md in sorted(base.rglob("*.md")):
            rel = md.relative_to(docs_dir).as_posix()
            if md.name == "index.md" or rel in method_files:
                continue
            text = md.read_text(encoding="utf-8")
            if front_matter(text).get("kind") == "theory":
                if md.name not in haystack and rel not in haystack:
                    findings.append(Finding("error", rel, "theory page is not linked from any method section or glossary derivation"))
            else:
                findings.append(Finding("error", rel, "page is neither in the inventory (method) nor marked kind: theory"))
    return findings


# ---------------------------------------------------------------- glossary

def load_glossary(glossary_dir: Path) -> tuple[list[dict], list[Finding]]:
    terms: list[dict] = []
    findings: list[Finding] = []
    seen: dict[str, str] = {}
    for yml in sorted(glossary_dir.glob("*.yml")):
        if yml.name == "index.yml":
            continue
        data = yaml.safe_load(yml.read_text(encoding="utf-8")) or {}
        for t in data.get("terms") or []:
            name = t.get("term")
            if not name:
                findings.append(Finding("error", yml.name, "term without a name"))
                continue
            if name in seen:
                findings.append(Finding("error", yml.name, f"term {name!r} also defined in {seen[name]}"))
                continue
            seen[name] = yml.name
            t["_file"] = yml.name
            terms.append(t)
    return terms, findings


def check_glossary(terms: list[dict], docs_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    by_name = {t["term"]: t for t in terms}
    anchors: dict[str, set[str]] = {}
    for t in terms:
        where = f"{t['_file']}:{t['term']}"
        ref = str(t.get("reference") or "")
        if not SECTION_RE.match(ref):
            findings.append(Finding("error", where, "reference must look like path/file.md#anchor"))
        else:
            file, anchor = ref.split("#", 1)
            target = docs_dir / file
            if not target.is_file():
                findings.append(Finding("error", where, f"reference file {file} does not exist"))
            else:
                anchors.setdefault(file, heading_anchors(target.read_text(encoding="utf-8")))
                if anchor not in anchors[file]:
                    findings.append(Finding("error", where, f"reference anchor #{anchor} not found in {file}"))
        if "depends_on" not in t and not t.get("foundation"):
            findings.append(Finding("warning", where, "no derivation chain yet (depends_on absent)"))
            continue
        for dep in t.get("depends_on") or []:
            if dep not in by_name:
                findings.append(Finding("error", where, f"depends_on {dep!r} is not a glossary term"))

    def walk(name: str, stack: list[str]) -> None:
        t = by_name[name]
        if t.get("foundation"):
            return
        if name in stack:
            findings.append(Finding("error", f"{t['_file']}:{name}", f"cycle: {' -> '.join(stack[stack.index(name):] + [name])}"))
            return
        if "depends_on" not in t:
            return  # chain not written yet; warned above
        deps = [d for d in (t.get("depends_on") or []) if d in by_name]
        if not deps:
            findings.append(Finding("error", f"{t['_file']}:{name}", "chain ends at a non-foundation term"))
            return
        for d in deps:
            walk(d, stack + [name])

    for t in terms:
        if "depends_on" in t and not t.get("foundation"):
            walk(t["term"], [])
    return findings


# ---------------------------------------------------------------- navigation and first mention

def nav_pages(mkdocs_yml: Path) -> list[str]:
    """Flatten `nav:` into page paths in reading order. BaseLoader keeps !!python tags as plain scalars."""
    cfg = yaml.load(mkdocs_yml.read_text(encoding="utf-8"), Loader=yaml.BaseLoader) or {}
    pages: list[str] = []

    def walk(item) -> None:
        if isinstance(item, str):
            pages.append(item)
        elif isinstance(item, list):
            for i in item:
                walk(i)
        elif isinstance(item, dict):
            for v in item.values():
                walk(v)

    walk(cfg.get("nav", []))
    return pages


def first_mention_warnings(pages: list[str], terms: list[dict], docs_dir: Path) -> list[Finding]:
    texts: list[tuple[str, str]] = []
    for p in pages:
        f = docs_dir / p
        if p.startswith(FIRST_MENTION_PREFIXES) and f.is_file():
            texts.append((p, CODE_FENCE_RE.sub("", strip_front_matter(f.read_text(encoding="utf-8")))))
    findings: list[Finding] = []
    for t in terms:
        ref_file = str(t.get("reference") or "").split("#", 1)[0]
        pattern = re.compile(r"(?<!\w)" + re.escape(t["term"]) + r"(?!\w)", re.I)
        for p, text in texts:
            if pattern.search(text):
                if p != ref_file:
                    findings.append(Finding("warning", f"{t.get('_file', '?')}:{t['term']}",
                                            f"first mentioned on {p}, reference points to {ref_file}"))
                break
    return findings


# ---------------------------------------------------------------- driver

def run_all(root: Path) -> list[Finding]:
    docs = root / "docs"
    findings: list[Finding] = []
    rows, f = load_inventory(docs / "flowcharts" / "inventory.yml")
    findings += f
    terms, f = load_glossary(docs / "glossary") if (docs / "glossary").is_dir() else ([], [])
    findings += f
    diagrams = collect_diagrams(docs)
    findings += check_diagrams(diagrams)
    findings += check_refs(diagrams, rows)
    findings += check_nodes_vs_inventory(diagrams, rows)
    findings += check_inventory_targets(rows, docs)
    findings += check_sections(docs, rows, terms)
    findings += check_glossary(terms, docs)
    mk = root / "mkdocs.yml"
    if mk.is_file():
        findings += first_mention_warnings(nav_pages(mk), terms, docs)
    return sorted(set(findings), key=lambda x: (x.level != "error", x.where, x.message))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    findings = run_all(args.root)
    for f in findings:
        print(f"{f.level.upper():7} {f.where}: {f.message}")
    errors = sum(f.level == "error" for f in findings)
    print(f"{errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
