"""Audit the flowchart framework: Mermaid diagrams, the leaf-node inventory, and the glossary.

Run from the repository root: python scripts/audit_flowcharts.py [--root PATH]
Exit status 1 when any error-level finding exists; warnings never fail the run.
Rules: planning/2026-10-06-flowchart-framework-design.md, sections 10 and 11.

Pages are rendered with the Markdown extensions configured in mkdocs.yml, so diagram sources,
heading anchors and links are the ones MkDocs produces, not a re-parse of the raw source.
"""
from __future__ import annotations

import argparse
import posixpath
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

import markdown
import yaml
from mkdocs.config import load_config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.utils.meta import get_data
from pymdownx.snippets import SnippetMissingError

ERROR, WARNING = "error", "warning"
AUDIT_SKIP_MARKER = "%% audit: skip"
FOUNDATION_PHASE = "F"
FOUNDATION_DIR = "00-foundations/"
SECTION_DIRS = ("reference", "01-workflow")
# H2 headings that structure a chapter rather than teach a content unit (documented in DESIGN-SYSTEM.md).
STRUCTURAL_H2 = frozenset({
    "Sub-diagram", "Branch sub-diagram", "Phase guide", "Question order", "Part 0 hooks", "Relation to P9",
    "Routing variables", "Branches", "Quick navigation", "Purpose selector", "Representation selector",
    "Master diagram", "How to read the diagrams", "Sub-chart", "P10 inference for this purpose",
    "P11 metrics for this purpose", "Topics carried over from the previous outline", "References",
})
GLOSSARY_DIR = "glossary"
GLOSSARY_INDEX_NAME = "index.yml"
INVENTORY_PATH = ("flowcharts", "inventory.yml")


@dataclass(frozen=True)
class Finding:
    level: str  # ERROR or WARNING
    where: str
    message: str

    def __str__(self) -> str:
        return f"{self.level.upper():7} {self.where}: {self.message}"


@dataclass(frozen=True)
class Node:
    id: str
    shape: str  # rect | diamond | terminator | subroutine | data
    label: str


@dataclass
class Diagram:
    where: str
    nodes: dict[str, Node] = field(default_factory=dict)  # ids with a quoted, allowed shape
    used_ids: set[str] = field(default_factory=set)  # every id written in a node position
    classes: dict[str, set[str]] = field(default_factory=dict)
    clusters: set[str] = field(default_factory=set)  # subgraph ids; never nodes
    problems: list[str] = field(default_factory=list)  # syntax the audit rejects

    def is_ref(self, node_id: str) -> bool:
        node = self.nodes[node_id]
        return node.shape == "subroutine" or "ref" in self.classes.get(node_id, set())

    def is_leaf(self, node_id: str) -> bool:
        node = self.nodes[node_id]
        return node.shape == "rect" and not self.is_ref(node_id) and not node_id.endswith("_FLAG")


# ---------------------------------------------------------------- Mermaid parsing

SHAPES = {"([": "terminator", "[[": "subroutine", "[/": "data", "[": "rect", "{": "diamond"}
CLOSERS = {"([": "])", "[[": "]]", "[/": "/]", "[": "]", "{": "}"}
# Every node opener Mermaid accepts, longest first, so an unlisted shape is named rather than misread.
MERMAID_OPENERS = ("(((", "((", "([", "[[", "[(", "[/", "[\\", "{{", "(", "[", "{", ">")
NODE_ID_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
TOKEN_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)(.*)$", re.S)
QUOTED_RE = re.compile(r'"(?:[^"\\]|\\.)*"')
# `A -- text --> B` and `A -. text .-> B` carry the edge text between two halves of the arrow.
TEXT_EDGE_RE = re.compile(r"(?<=\s)(?:--|==|-\.)\s+[^\x00|]+?\s+(?:-->|==>|\.->|---|===|-\.-|--[ox]|==[ox])(?=\s|$)")
EDGE_RE = re.compile(r"\s*(?:<|(?<=\s)[ox])?[-=.]{2,}(?:>|[ox](?=[\s|]|$))?(?:\|[^|]*\|)?\s*")
CLASS_RE = re.compile(r"^class\s+(\S+)\s+([A-Za-z_][\w-]*)\s*;?$")
SUBGRAPH_RE = re.compile(r"^subgraph\s+([A-Za-z_][A-Za-z0-9_]*)?")
IGNORED_LINE_RE = re.compile(r"^(?:graph|flowchart)\b|^(?:classDef|style|linkStyle|direction)\s|^end\s*;?$")
URL_RE = re.compile(r"https?://|href\s*=", re.I)
BR_RE = re.compile(r"<br\s*/?>", re.I)


def label_first_line(label: str) -> str:
    return BR_RE.split(label, 1)[0].strip()


def _parse_node(piece: str, labels: list[str], d: Diagram) -> None:
    m = TOKEN_RE.match(piece)
    if not m:
        d.problems.append(f"cannot read node expression {piece!r}")
        return
    nid, rest = m.group(1), m.group(2).strip()
    if not NODE_ID_RE.match(nid):
        d.problems.append(f"node id {nid!r} is not SCREAMING_SNAKE_CASE")
    d.used_ids.add(nid)
    if not rest:
        return
    if rest.startswith(":::"):
        d.problems.append(f"node {nid} uses inline :::class; assign classes with class statements")
        return
    opener = next((o for o in MERMAID_OPENERS if rest.startswith(o)), None)
    if opener is None:
        d.problems.append(f"cannot read node expression {piece!r}")
        return
    if opener not in SHAPES:
        d.problems.append(f"node {nid} uses shape {opener!r}, which the notation does not allow")
        return
    label = re.fullmatch(r"\x00(\d+)\x00" + re.escape(CLOSERS[opener]), rest[len(opener):])
    if not label:
        return  # unquoted label: not a definition; reported as used without a shaped definition
    shape = SHAPES[opener]
    previous = d.nodes.get(nid)
    if previous and previous.shape != shape:
        d.problems.append(f"node {nid} is drawn as {previous.shape} and as {shape}; Mermaid renders the last")
    d.nodes[nid] = Node(nid, shape, labels[int(label.group(1))][1:-1])


def parse_diagram(source: str, where: str) -> Diagram:
    d = Diagram(where=where)
    for raw in source.splitlines():
        line = raw.strip().rstrip(";").strip()
        if not line or line.startswith("%%") or IGNORED_LINE_RE.match(line):
            continue
        if URL_RE.search(line):
            d.problems.append(f"diagram contains a URL ({line!r}); node links come from the inventory")
        if re.match(r"^click\b", line):
            d.problems.append(f"click directive {line!r}; node links come from the inventory")
            continue
        cls = CLASS_RE.match(line)
        if cls:
            for node_id in cls.group(1).split(","):
                if node_id:
                    d.classes.setdefault(node_id, set()).add(cls.group(2))
            continue
        sub = SUBGRAPH_RE.match(line)
        if sub:
            if sub.group(1):
                d.clusters.add(sub.group(1))
            continue
        labels: list[str] = []

        def mask(m: re.Match) -> str:
            labels.append(m.group(0))
            return f"\x00{len(labels) - 1}\x00"

        masked = TEXT_EDGE_RE.sub(" --> ", QUOTED_RE.sub(mask, line))
        for part in EDGE_RE.split(masked):
            for piece in part.split("&"):
                if piece.strip():
                    _parse_node(piece.strip(), labels, d)
    return d


# ---------------------------------------------------------------- rendering pipeline

URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:|^//")
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
TEXT_EXCLUDED_TAGS = {"code", "pre", "script", "style"}


@dataclass(frozen=True)
class Heading:
    level: int
    id: str
    text: str


@dataclass(frozen=True)
class PageRender:
    html: str
    anchors: frozenset[str]
    headings: tuple[Heading, ...]
    mermaid_sources: tuple[str, ...]
    links: tuple[str, ...]  # raw href values; resolve with resolve_link()
    text: str  # visible prose outside code, diagrams and heading permalinks
    meta: dict


class _RenderCollector(HTMLParser):
    """Collect headings, mermaid sources, link targets and prose from rendered page HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.headings: list[Heading] = []
        self.mermaid: list[str] = []
        self.links: list[str] = []
        self.text: list[str] = []
        self._stack: list[tuple[str, str]] = []  # (tag, role)
        self._heading: tuple[int, str, list[str]] | None = None
        self._mermaid: list[str] | None = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        role = ""
        if tag == "div" and "mermaid" in classes and self._mermaid is None:
            role, self._mermaid = "mermaid", []
        elif tag in HEADING_TAGS and a.get("id"):
            role, self._heading = "heading", (int(tag[1]), a["id"], [])
        elif tag == "a" and "headerlink" in classes:
            role = "permalink"
        if tag == "a" and a.get("href") and role != "permalink":
            self.links.append(a["href"])
        self._stack.append((tag, role))

    def handle_endtag(self, tag):
        while self._stack:
            open_tag, role = self._stack.pop()
            if role == "mermaid":
                self.mermaid.append("".join(self._mermaid))
                self._mermaid = None
            elif role == "heading":
                level, hid, parts = self._heading
                self.headings.append(Heading(level, hid, "".join(parts).strip()))
                self._heading = None
            if open_tag == tag:
                break

    def handle_data(self, data):
        if self._mermaid is not None:
            self._mermaid.append(data)
            return
        if any(role == "permalink" or tag in TEXT_EXCLUDED_TAGS for tag, role in self._stack):
            return
        if self._heading is not None:
            self._heading[2].append(data)
        self.text.append(data)


def load_site_config(config_file: Path) -> MkDocsConfig:
    return load_config(config_file=str(config_file))


def site_markdown(cfg: MkDocsConfig) -> markdown.Markdown:
    return markdown.Markdown(extensions=cfg["markdown_extensions"], extension_configs=cfg["mdx_configs"])


def render_page(md: markdown.Markdown, text: str) -> PageRender:
    """Render page source the way MkDocs does: front matter stripped, configured extensions applied."""
    body, meta = get_data(text)
    md.reset()
    html = md.convert(body)
    collector = _RenderCollector()
    collector.feed(html)
    collector.close()
    headings = tuple(collector.headings)
    return PageRender(html, frozenset(h.id for h in headings), headings, tuple(collector.mermaid),
                      tuple(collector.links), " ".join(collector.text), meta if isinstance(meta, dict) else {})


def resolve_link(href: str, page: str) -> str | None:
    """Docs-relative `path.md#anchor` (or `path.md`) for a link on `page`; None for external links."""
    if URL_SCHEME_RE.match(href):
        return None
    path, _, anchor = href.partition("#")
    target = posixpath.normpath(posixpath.join(posixpath.dirname(page), unquote(path))) if path else page
    return f"{target}#{anchor}" if anchor else target


class Site:
    """One MkDocs project: its config, a Markdown renderer built from it, and cached page renders."""

    def __init__(self, config: MkDocsConfig, docs_dir: Path) -> None:
        self.config = config
        self.docs_dir = docs_dir
        self.md = site_markdown(self.config)
        self.findings: list[Finding] = []
        self._pages: dict[str, PageRender | None] = {}

    def page(self, rel: str) -> PageRender | None:
        """Rendered page, or None when it does not exist or fails to render (recorded as a finding)."""
        if rel not in self._pages:
            path = self.docs_dir / rel
            render = None
            if path.is_file():
                try:
                    render = render_page(self.md, path.read_text(encoding="utf-8"))
                except SnippetMissingError as exc:
                    self.findings.append(Finding(ERROR, rel, f"page does not render: {exc}"))
            self._pages[rel] = render
        return self._pages[rel]

    def pages_under(self, sub: str) -> list[str]:
        base = self.docs_dir / sub
        return sorted(p.relative_to(self.docs_dir).as_posix() for p in base.rglob("*.md")) if base.is_dir() else []

    def nav_pages(self) -> list[str]:
        """`nav:` flattened into docs-relative page paths in reading order."""
        pages: list[str] = []

        def walk(item) -> None:
            if isinstance(item, str):
                if not URL_SCHEME_RE.match(item):
                    pages.append(item)
            elif isinstance(item, list):
                for i in item:
                    walk(i)
            elif isinstance(item, dict):
                for v in item.values():
                    walk(v)

        walk(self.config["nav"] or [])
        return pages


def collect_diagrams(site: Site) -> list[Diagram]:
    diagrams = []
    for rel in site.pages_under(""):
        page = site.page(rel)
        if page is None:
            continue
        for n, src in enumerate(page.mermaid_sources, 1):
            if AUDIT_SKIP_MARKER in src:
                continue
            diagrams.append(parse_diagram(src, f"{rel}#mermaid-{n}"))
    return diagrams


# ---------------------------------------------------------------- inventory

SECTION_RE = re.compile(r"^[\w./-]+\.md#[\w-]+$")
SECTION_FORMAT = "path/file.md#anchor"


def split_section(section: str) -> tuple[str, str]:
    """(`path.md`, `anchor`) of a section string that matches SECTION_RE."""
    file, anchor = section.split("#", 1)
    return file, anchor
MARKDOWN_LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
REQUIRED_ROW_KEYS = ("id", "label", "phase", "areas", "section")
MASTER_PHASE = "MASTER"
MASTER_IDS = frozenset(f"P{i}" for i in range(12))
BRANCH_IDS = frozenset(f"B{i}" for i in range(1, 8))
PHASES = MASTER_IDS | BRANCH_IDS | {MASTER_PHASE, FOUNDATION_PHASE}
AREAS = range(1, 35)


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects a mapping with the same key twice (PyYAML keeps the last silently)."""


def _construct_unique_mapping(loader: _UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate key {key!r}", key_node.start_mark)
        seen.add(key)
    return loader.construct_mapping(node, deep=deep)


_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)


def load_yaml(path: Path, key: str) -> tuple[list, list[Finding]]:
    """The list under top-level `key`, or a finding naming the file when the YAML or its shape is invalid."""
    try:
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
    except yaml.YAMLError as exc:
        return [], [Finding(ERROR, path.name, f"invalid YAML: {exc}")]
    if not isinstance(data, dict) or not isinstance(data.get(key), list):
        return [], [Finding(ERROR, path.name, f"top level must be a mapping with a `{key}` list")]
    return data[key], []


def row_problem(raw: object) -> str | None:
    """Why an inventory row is malformed, or None."""
    if not isinstance(raw, dict):
        return "row must be a mapping"
    missing = [k for k in REQUIRED_ROW_KEYS if k not in raw]
    if missing:
        return f"missing keys {missing}"
    rid, phase, areas = raw["id"], raw["phase"], raw["areas"]
    if not isinstance(rid, str) or not NODE_ID_RE.match(rid):
        return f"id {rid!r} must be a SCREAMING_SNAKE_CASE string"
    if not isinstance(raw["label"], str) or not raw["label"].strip():
        return "label must be a non-empty string"
    if phase not in PHASES:
        return f"phase {phase!r} must be one of P0-P11, B1-B7, {MASTER_PHASE} or {FOUNDATION_PHASE}"
    if not isinstance(areas, list) or not all(type(a) is int and a in AREAS for a in areas):
        return f"areas {areas!r} must be a list of area numbers 1-34"
    if not isinstance(raw["section"], str) or not SECTION_RE.match(raw["section"]):
        return f"section {raw['section']!r} must look like {SECTION_FORMAT}"
    if (rid in MASTER_IDS) != (phase == MASTER_PHASE):
        return f"phase {MASTER_PHASE} is for the master boxes P0-P11 and only them (id {rid}, phase {phase})"
    if rid in BRANCH_IDS:
        return None if phase != FOUNDATION_PHASE else f"branch entry {rid} cannot be a foundation row"
    if phase == MASTER_PHASE:
        return None
    if not rid.startswith(f"{phase}_"):
        return f"id {rid} must carry the owner prefix {phase}_"
    return None


@dataclass(frozen=True)
class Row:
    id: str
    label: str
    phase: str
    areas: tuple[int, ...]
    section: str

    @property
    def file(self) -> str:
        return split_section(self.section)[0]

    @property
    def anchor(self) -> str:
        return split_section(self.section)[1]


def load_inventory(path: Path) -> tuple[list[Row], list[Finding]]:
    if not path.is_file():
        return [], [Finding(ERROR, str(path), "inventory file does not exist")]
    raw_rows, findings = load_yaml(path, "nodes")
    rows: list[Row] = []
    seen: set[str] = set()
    for i, raw in enumerate(raw_rows):
        where = f"{path.name}#nodes[{i}]"
        problem = row_problem(raw)
        if problem:
            findings.append(Finding(ERROR, where, problem))
            continue
        if raw["id"] in seen:
            findings.append(Finding(ERROR, where, f"duplicate inventory id {raw['id']}"))
            continue
        seen.add(raw["id"])
        rows.append(Row(raw["id"], raw["label"], raw["phase"], tuple(raw["areas"]), raw["section"]))
    return rows, findings


def resolve_section(section: str, site: Site) -> str | None:
    """Why `path.md#anchor` does not resolve to a rendered heading, or None when it does."""
    if not SECTION_RE.match(section):
        return f"{section!r} must look like {SECTION_FORMAT}"
    file, anchor = split_section(section)
    page = site.page(file)
    if page is None:
        return f"file {file} does not exist"
    if anchor not in page.anchors:
        return f"anchor #{anchor} not found in {file}"
    return None


def check_inventory_targets(rows: list[Row], site: Site) -> list[Finding]:
    findings: list[Finding] = []
    for r in rows:
        problem = resolve_section(r.section, site)
        if problem:
            findings.append(Finding(ERROR, r.id, f"section {problem}"))
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
    defined = _defined_ids(diagrams)
    for d in diagrams:
        for nid in d.nodes:
            if not d.is_ref(nid) and defined[nid] != d.where:
                findings.append(Finding(ERROR, d.where, f"node {nid} already defined in {defined[nid]}"))
    for d in diagrams:
        findings.extend(Finding(ERROR, d.where, problem) for problem in d.problems)
        for nid in sorted(d.used_ids - set(d.nodes) - d.clusters):
            findings.append(Finding(ERROR, d.where, f"node {nid} is used but has no quoted, shaped definition in this diagram"))
    return findings


def check_refs(diagrams: list[Diagram], rows: list[Row]) -> list[Finding]:
    defined = _defined_ids(diagrams)
    foundation = {r.id for r in rows if r.phase == FOUNDATION_PHASE}
    findings: list[Finding] = []
    for d in diagrams:
        for nid in d.nodes:
            if d.is_ref(nid) and nid not in defined and nid not in foundation:
                findings.append(Finding(ERROR, d.where, f"ref {nid} has no definition in any diagram and is not a foundation inventory row"))
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
            findings.append(Finding(ERROR, where, f"leaf {nid} has no inventory row"))
    for d in diagrams:
        for nid, node in d.nodes.items():
            row = by_id.get(nid)
            if row and label_first_line(node.label) != row.label:
                findings.append(Finding(ERROR, d.where, f"node {nid} label {label_first_line(node.label)!r} differs from its inventory label {row.label!r}"))
    for r in rows:
        if r.phase == FOUNDATION_PHASE:
            if r.id not in refs:
                findings.append(Finding(ERROR, r.id, "foundation row is not referenced by any ref node"))
        elif r.id not in leaves:
            findings.append(Finding(ERROR, r.id, "inventory row has no leaf definition in any diagram"))
    return findings


# ---------------------------------------------------------------- sections

def check_sections(site: Site, rows: list[Row], terms: list[dict]) -> list[Finding]:
    """Every non-index page under SECTION_DIRS is a method page (in the inventory) or a linked theory page.

    A theory page is linked when a link on a method page resolves to it, or when a glossary derivation
    links to one of its anchors in the exact docs-relative `path.md#anchor` form.
    """
    method_files = {r.file for r in rows}
    linked: set[str] = set()
    for f in sorted(method_files):
        page = site.page(f)
        if page is not None:
            linked.update(target.split("#", 1)[0] for href in page.links if (target := resolve_link(href, f)))
    for t in terms:
        for target in MARKDOWN_LINK_RE.findall(str(t.get("derivation") or "")):
            if resolve_section(target, site) is None:
                linked.add(split_section(target)[0])
    findings: list[Finding] = []
    for sub in SECTION_DIRS:
        for rel in site.pages_under(sub):
            if rel.endswith("/index.md") or rel in method_files:
                continue
            page = site.page(rel)
            if page is None:
                continue
            if page.meta.get("kind") == "theory":
                if rel not in linked:
                    findings.append(Finding(ERROR, rel, "theory page is not linked from any method section or glossary derivation"))
            else:
                findings.append(Finding(ERROR, rel, "page is neither in the inventory (method) nor marked kind: theory"))
    return findings


def check_headings(site: Site, rows: list[Row], terms: list[dict]) -> list[Finding]:
    """Every H2 under SECTION_DIRS is a content unit (an inventory or glossary anchor) or a structural heading."""
    units: dict[str, set[str]] = {}
    for section in [r.section for r in rows] + [str(t.get("reference") or "") for t in terms]:
        if SECTION_RE.match(section):
            file, anchor = split_section(section)
            units.setdefault(file, set()).add(anchor)
    findings: list[Finding] = []
    for sub in SECTION_DIRS:
        for rel in site.pages_under(sub):
            page = site.page(rel)
            for h in page.headings if page else ():
                if h.level == 2 and h.id not in units.get(rel, set()) and h.text not in STRUCTURAL_H2:
                    findings.append(Finding(ERROR, f"{rel}#{h.id}", f"H2 {h.text!r} is neither an inventory or glossary anchor nor a structural heading"))
    return findings


# ---------------------------------------------------------------- glossary

def load_glossary(glossary_dir: Path) -> tuple[list[dict], list[Finding]]:
    terms: list[dict] = []
    findings: list[Finding] = []
    seen: dict[str, str] = {}
    for yml in sorted(glossary_dir.glob("*.yml")):
        if yml.name == GLOSSARY_INDEX_NAME:
            continue
        raw_terms, f = load_yaml(yml, "terms")
        findings += f
        for i, t in enumerate(raw_terms):
            name = t.get("term") if isinstance(t, dict) else None
            if not isinstance(name, str) or not name:
                findings.append(Finding(ERROR, f"{yml.name}#terms[{i}]", "term must be a mapping with a non-empty `term` string"))
                continue
            if name in seen:
                findings.append(Finding(ERROR, yml.name, f"term {name!r} also defined in {seen[name]}"))
                continue
            seen[name] = yml.name
            t["_file"] = yml.name
            terms.append(t)
    return terms, findings


def glossary_file_for(reference_file: str) -> str:
    """The glossary file a term belongs in: named after its reference page, or the directory of an index.md."""
    path = Path(reference_file)
    return f"{path.parent.name if path.name == 'index.md' else path.stem}.yml"


def _depends_on(t: dict) -> list[str] | None:
    deps = t.get("depends_on")
    return deps if isinstance(deps, list) and all(isinstance(d, str) for d in deps) else None


def check_glossary(terms: list[dict], site: Site) -> list[Finding]:
    findings: list[Finding] = []
    by_name = {t["term"]: t for t in terms}
    for t in terms:
        where = f"{t['_file']}:{t['term']}"
        ref = str(t.get("reference") or "")
        problem = resolve_section(ref, site)
        if problem:
            findings.append(Finding(ERROR, where, f"reference {problem}"))
        elif (home := glossary_file_for(split_section(ref)[0])) != t["_file"]:
            findings.append(Finding(ERROR, where, f"term belongs in {GLOSSARY_DIR}/{home}, the file named after its reference page"))
        if "depends_on" in t and _depends_on(t) is None:
            findings.append(Finding(ERROR, where, "depends_on must be a list of term names"))
            continue
        if t.get("foundation"):
            if not ref.startswith(FOUNDATION_DIR):
                findings.append(Finding(ERROR, where, f"foundation term must be homed under {FOUNDATION_DIR}"))
            if _depends_on(t):
                findings.append(Finding(ERROR, where, "foundation term cannot depend on other terms"))
            continue
        if "depends_on" not in t:
            findings.append(Finding(WARNING, where, "no derivation chain yet (depends_on absent)"))
            continue
        for dep in _depends_on(t):
            if dep not in by_name:
                findings.append(Finding(ERROR, where, f"depends_on {dep!r} is not a glossary term"))

    # Three-colour depth-first walk: each term is expanded once, each cycle reported once.
    state: dict[str, str] = {}
    cycles: set[tuple[str, ...]] = set()

    def walk(name: str, stack: list[str]) -> None:
        t = by_name[name]
        if t.get("foundation") or state.get(name) == "done" or _depends_on(t) is None:
            return
        if state.get(name) == "open":
            loop = stack[stack.index(name):]
            start = loop.index(min(loop))
            cycles.add(tuple(loop[start:] + loop[:start]))
            return
        state[name] = "open"
        deps = [d for d in _depends_on(t) if d in by_name]
        if not deps:
            findings.append(Finding(ERROR, f"{t['_file']}:{name}", "chain ends at a non-foundation term"))
        for d in deps:
            walk(d, stack + [name])
        state[name] = "done"

    for t in terms:
        walk(t["term"], [])
    for loop in sorted(cycles):
        first = by_name[loop[0]]
        findings.append(Finding(ERROR, f"{first['_file']}:{loop[0]}", f"cycle: {' -> '.join(loop + (loop[0],))}"))
    return findings


# ---------------------------------------------------------------- first mention

def first_mention_warnings(site: Site, terms: list[dict]) -> list[Finding]:
    texts: list[tuple[str, str]] = []
    for p in site.nav_pages():
        page = site.page(p)
        if page is not None:
            texts.append((p, page.text))
    findings: list[Finding] = []
    for t in terms:
        ref_file = str(t.get("reference") or "").split("#", 1)[0]
        pattern = re.compile(r"(?<!\w)" + re.escape(t["term"]) + r"(?!\w)", re.I)
        for p, text in texts:
            if pattern.search(text):
                if p != ref_file:
                    findings.append(Finding(WARNING, f"{t['_file']}:{t['term']}",
                                            f"first mentioned on {p}, reference points to {ref_file}"))
                break
    return findings


# ---------------------------------------------------------------- driver

def run_all(config_file: Path, docs_dir: Path) -> list[Finding]:
    return audit_site(Site(load_site_config(config_file), docs_dir))


def audit_site(site: Site) -> list[Finding]:
    findings: list[Finding] = []
    rows, f = load_inventory(site.docs_dir.joinpath(*INVENTORY_PATH))
    findings += f
    glossary_dir = site.docs_dir / GLOSSARY_DIR
    terms, f = load_glossary(glossary_dir) if glossary_dir.is_dir() else ([], [])
    findings += f
    diagrams = collect_diagrams(site)
    findings += check_diagrams(diagrams)
    findings += check_refs(diagrams, rows)
    findings += check_nodes_vs_inventory(diagrams, rows)
    findings += check_inventory_targets(rows, site)
    findings += check_sections(site, rows, terms)
    findings += check_headings(site, rows, terms)
    findings += check_glossary(terms, site)
    findings += first_mention_warnings(site, terms)
    findings += site.findings
    return sorted(set(findings), key=lambda x: (x.level != ERROR, x.where, x.message))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    cfg = load_site_config(args.root / "mkdocs.yml")
    findings = audit_site(Site(cfg, Path(cfg["docs_dir"])))
    for f in findings:
        print(f)
    errors = sum(f.level == ERROR for f in findings)
    print(f"{errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
