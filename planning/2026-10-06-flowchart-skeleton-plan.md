# Flowchart Framework Skeleton Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the flowchart framework's skeleton and tooling: the three-axis directory layout, the master diagram plus the P1, P2, P5 and P7 sub-diagrams as exemplars, the leaf-node inventory, the audit script, the MkDocs hook, runtime node linking, the glossary schema and drawer, and CI, so that the remaining sub-diagrams (Plan B) can be drawn against a passing audit.

**Architecture:** The general flowchart is one spine: a master diagram of twelve phase boxes, each phase a sub-diagram in its own chapter under `docs/01-workflow/`. Leaf nodes are content units recorded in `docs/flowcharts/inventory.yml`, which both a Python audit and a browser script read, so links live in one place. Part 0 (`docs/00-foundations/`) holds the roots of every why-chain; the glossary drawer carries the chains.

**Tech Stack:** MkDocs 1.6 + Material 9, Python-Markdown (`toc` slugify), PyYAML, pytest; Mermaid 10 and js-yaml in the browser (already loaded by the site).

**Spec:** `planning/2026-10-06-flowchart-framework-design.md` (sections cited as "spec §N").

**Scope of this plan (Plan A):** spec §12b item 1, minus the sub-diagrams of P0, P3, P4, P6, P8–P11, the ten purpose sub-charts, the six representation sub-charts and the branch sub-charts B1–B6, which are Plan B. Plan A draws the master, P1, P7, and the top-level P2 and P5 diagrams, and leaves a one-node entry stub for each B branch so every `ref` resolves. Spec acceptance criterion 3 (every area has a leaf) is met at the end of Plan B; criteria 1, 2, 4, 5, 6 are met here.

## Global Constraints

- Do not commit or push without the user's permission (`CLAUDE.md`). Commit steps below run only if the user has granted permission for this plan; otherwise stage the files and stop at the commit step.
- No emojis anywhere in content or diagrams (`CLAUDE.md`).
- Flowchart notation follows `DESIGN-SYSTEM.md` "Decision-flowchart notation": quoted labels, `SCREAMING_SNAKE_CASE` IDs, `class` statements (never `:::`), brand `classDef` block pasted at the foot of every diagram, `TD` for decision charts.
- Node IDs are `<OWNER>_<SEMANTIC_NAME>`; master phase boxes are `P0` … `P11`; branch entry boxes are `B1` … `B7` (spec §10.1). Decision and terminator nodes carry the owner prefix too, because the audit checks uniqueness of every defined ID.
- A leaf is a defined rectangle `[ ]` that is not a `ref` and whose ID does not end in `_FLAG`. Diamonds, terminators, parallelograms, subroutine boxes and flags are not leaves (spec §10.1 as amended on 2026-10-06).
- A diagram opts out of the audit with the comment line `%% audit: skip` inside its fence. Illustrative diagrams (Part 0, the design-system showcase) opt out.
- Paths in the inventory and the glossary are `docs/`-relative source paths with `.md` and a heading anchor: `reference/10-volatility/index.md#garch` (spec §10.3). Anchors equal the Python-Markdown `toc` slugify of the heading, or an explicit `{#id}`.
- Nothing pushed to the remote may contain local references: absolute machine paths, scratchpad paths, session ids, loopback host names and addresses. Before any push: `git diff main...HEAD | grep -nE '[/]Users[/]|[/]private[/]tmp[/]|[/]var[/]folders[/]|localhos[t]|127[.]0[.]0[.]1|[.]local\b'` must print nothing.
- Python 3.11 in CI; the local interpreter is 3.14. Use only the standard library plus PyYAML and Python-Markdown in scripts.
- `mkdocs build --strict` must pass at the end of every task that touches `docs/` or `mkdocs.yml`.

## Review Focus

1. A Mermaid node written with an unquoted label (`P7_GARCH[GARCH]`) must be reported as "used in an edge but has no shaped definition", not silently accepted, because the design rule requires quoting and the parser only recognises quoted labels. Pinned in Task 1.
2. Two sub-diagrams on different pages that both define `P7_MULTI` must fail with the location of the first definition, because leaf uniqueness is the invariant the whole inventory rests on. Pinned in Task 3.
3. A heading whose text slugifies to an anchor that already exists on the page (MkDocs appends `_1`) must be checked against the suffixed anchor, otherwise the audit passes a dead link. Pinned in Task 2.
4. `mkdocs serve` must not enter a rebuild loop when the hook writes `glossary/index.yml` into `docs/`: the hook writes only when the content changed. Pinned in Task 6.
5. A glossary term with no `depends_on` key is a chain not yet written (warning), while a term with `depends_on: []` and no `foundation: true` is a chain that dead-ends (error); confusing the two would either block all content work or let dead chains through. Pinned in Task 4.

## File Structure

| Path | Responsibility |
|---|---|
| `requirements-docs.txt` | Docs and test toolchain only (MkDocs, Material, Markdown, PyYAML, pytest). `requirements.txt` stays for code examples |
| `tests/conftest.py` | Puts `scripts/` on `sys.path` |
| `scripts/audit_flowcharts.py` | Library + CLI. Parses Mermaid fences, loads inventory and glossary, computes heading anchors, runs every check, prints findings, exit status |
| `scripts/scaffold_stubs.py` | Creates missing stub pages and pending headings from the inventory; idempotent |
| `scripts/mkdocs_hooks.py` | `on_pre_build`: writes `docs/glossary/index.yml` when changed; logs audit errors as MkDocs warnings so `--strict` fails |
| `docs/flowcharts/inventory.yml` | One row per leaf node: `id`, `label`, `phase`, `areas`, `section` |
| `docs/javascripts/flowchart-links.js` | Listens for `mermaid:rendered`, loads the inventory once, makes matching SVG nodes clickable |
| `docs/javascripts/mermaid-init.js` | Existing renderer; gains a `mermaid:rendered` CustomEvent after each diagram is inserted |
| `docs/javascripts/glossary.js` | Existing drawer; loads file list from `glossary/index.yml`, renders "Why it holds", "Rests on" chips, "First developed in"; drawer-to-drawer navigation with a back stack |
| `docs/stylesheets/glossary.css`, `docs/stylesheets/extra.css` | Chip, back-button and clickable-node styles |
| `docs/00-foundations/` | Part 0 (renamed from `00-introduction/`) plus `stochastic-processes.md`, `asymptotics.md` |
| `docs/01-workflow/` | Master diagram and phase pages P0–P11; `p02-purpose/` and `p05-representation/` subdirectories |
| `docs/reference/NN-slug/index.md` × 34 | One landing page per area; pending headings appended by the scaffold |
| `planning/legacy-flowcharts/` | The three current flowchart pages, moved out of `docs/` for Plan B to mine |
| `mkdocs.yml` | New `nav:`, `hooks:`, `extra_javascript` |
| `.github/workflows/deploy.yml` | Installs `requirements-docs.txt`, runs pytest and the audit, builds with `--strict` |
| `DESIGN-SYSTEM.md`, `CLAUDE.md`, `README.md`, `book_plan.md`, `.claude/rules/writing.md`, `.gitignore` | Governance and pointers |

### `scripts/audit_flowcharts.py` public API (used by tests, the scaffold and the hook)

```python
AUDIT_SKIP_MARKER = "%% audit: skip"
FOUNDATION_PHASE = "F"

@dataclass(frozen=True) class Finding(level: str, where: str, message: str)
@dataclass(frozen=True) class Node(id: str, shape: str, label: str)        # shape in rect|diamond|terminator|subroutine|data
@dataclass class Diagram(where: str, nodes: dict[str, Node], edge_ids: set[str], classes: dict[str, set[str]])
    .is_ref(node_id) -> bool      # subroutine shape or class ref
    .is_leaf(node_id) -> bool     # rect, not ref, not *_FLAG
@dataclass(frozen=True) class Row(id, label, phase, areas: tuple[int, ...], section)   # .file, .anchor properties

extract_mermaid_blocks(text) -> list[tuple[int, str]]
parse_diagram(source, where) -> Diagram
collect_diagrams(docs_dir) -> list[Diagram]
heading_anchors(text) -> set[str]
front_matter(text) -> dict
load_inventory(path) -> tuple[list[Row], list[Finding]]
load_glossary(glossary_dir) -> tuple[list[dict], list[Finding]]
nav_pages(mkdocs_yml) -> list[str]
check_diagrams(diagrams) -> list[Finding]
check_refs(diagrams, rows) -> list[Finding]
check_nodes_vs_inventory(diagrams, rows) -> list[Finding]
check_inventory_targets(rows, docs_dir) -> list[Finding]
check_sections(docs_dir, rows, terms) -> list[Finding]
check_glossary(terms, docs_dir) -> list[Finding]
first_mention_warnings(pages, terms, docs_dir) -> list[Finding]
run_all(root) -> list[Finding]
main(argv=None) -> int
```

---

### Task 0: Development environment and baseline

**Files:**
- Create: `requirements-docs.txt`
- Create: `tests/conftest.py`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `venv/bin/python`, `venv/bin/pytest`, `venv/bin/mkdocs`; `tests/` importing from `scripts/`.

- [ ] **Step 1: Write `requirements-docs.txt`**

```text
# Documentation build and test toolchain. Code-example dependencies stay in requirements.txt.
mkdocs>=1.6.0
mkdocs-material>=9.5.0
mkdocs-material-extensions>=1.3.0
mkdocs-autorefs>=0.5.0
pymdown-extensions>=10.4.0
markdown>=3.5.0
pyyaml>=6.0.1
pytest>=7.3.0
```

- [ ] **Step 2: Create the virtual environment and install**

Run:
```bash
python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements-docs.txt
venv/bin/python -c "import mkdocs, markdown, yaml, pytest; print(mkdocs.__version__, markdown.__version__)"
```
Expected: version numbers printed, mkdocs ≥ 1.6.

- [ ] **Step 3: Write `tests/conftest.py`**

```python
"""Make scripts/ importable from the tests."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
```

- [ ] **Step 4: Add the generated glossary index to `.gitignore`**

Append to `.gitignore`:
```text

# Generated by scripts/mkdocs_hooks.py on every build
docs/glossary/index.yml
```

- [ ] **Step 5: Record the baseline**

Run: `venv/bin/mkdocs build --strict 2>&1 | tail -3`
Expected: `INFO - Documentation built in … seconds` with no `WARNING` lines. If the baseline fails, stop and report; the plan assumes a clean baseline.

Run: `venv/bin/pytest tests -q`
Expected: `no tests ran` (exit code 5 is fine at this point).

- [ ] **Step 6: Commit**

```bash
git add requirements-docs.txt tests/conftest.py .gitignore
git commit -m "chore: add docs/test toolchain requirements and pytest scaffold"
```

---

### Task 1: Audit library — Mermaid parsing and node classification

**Files:**
- Create: `scripts/audit_flowcharts.py`
- Test: `tests/test_audit_mermaid.py`

**Interfaces:**
- Produces: `Finding`, `Node`, `Diagram`, `extract_mermaid_blocks`, `parse_diagram`, `collect_diagrams`, `AUDIT_SKIP_MARKER`, `FOUNDATION_PHASE`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_audit_mermaid.py
import textwrap

import audit_flowcharts as audit


SAMPLE = textwrap.dedent('''
    %%{init: {"flowchart": {"curve": "linear"}}}%%
    graph TD
        P7_IN(["Residuals"]) --> P7_MEAN_DEP{"Mean dependence?"}
        P7_MEAN_DEP -->|"Short memory"| P7_ARMA_ERRORS["Regression with ARMA errors"]
        P7_MEAN_DEP -.->|"Already ARMA"| P6[["P6 Conditional-mean model class"]]
        P7_ARMA_ERRORS & P7_IN --> P7_MIXED_FREQ_FLAG["Set flag: mixed frequency"]
        P7_MIXED_FREQ_FLAG --> P7_OUT
        P7_DATA[/"Input data"/] --> P7_OUT
        F_WOLD[["Wold decomposition"]] -.- P7_ARMA_ERRORS
        P7_OUT(["Done"])
        class P7_IN,P7_OUT terminator
        class P7_MEAN_DEP decision
        class P6,F_WOLD ref
        classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
''')


def test_extract_mermaid_blocks_returns_line_numbers():
    text = "# Title\n\nprose\n\n```mermaid\ngraph TD\n    A[\"a\"] --> B[\"b\"]\n```\n\nmore\n\n```python\nx = 1\n```\n"
    blocks = audit.extract_mermaid_blocks(text)
    assert len(blocks) == 1
    line_no, source = blocks[0]
    assert line_no == 5
    assert 'A["a"]' in source


def test_parse_diagram_recognises_every_shape():
    d = audit.parse_diagram(SAMPLE, "p07.md:10")
    shapes = {nid: n.shape for nid, n in d.nodes.items()}
    assert shapes["P7_IN"] == "terminator"
    assert shapes["P7_MEAN_DEP"] == "diamond"
    assert shapes["P7_ARMA_ERRORS"] == "rect"
    assert shapes["P6"] == "subroutine"
    assert shapes["P7_DATA"] == "data"
    assert d.nodes["P7_ARMA_ERRORS"].label == "Regression with ARMA errors"


def test_parse_diagram_collects_edge_ids_including_chains_and_dotted_links():
    d = audit.parse_diagram(SAMPLE, "p07.md:10")
    assert {"P7_IN", "P7_MEAN_DEP", "P7_ARMA_ERRORS", "P6", "P7_MIXED_FREQ_FLAG",
            "P7_OUT", "P7_DATA", "F_WOLD"} <= d.edge_ids


def test_parse_diagram_reads_class_statements():
    d = audit.parse_diagram(SAMPLE, "p07.md:10")
    assert d.classes["P6"] == {"ref"}
    assert d.classes["P7_IN"] == {"terminator"}


def test_leaf_and_ref_classification():
    d = audit.parse_diagram(SAMPLE, "p07.md:10")
    assert d.is_leaf("P7_ARMA_ERRORS")
    assert not d.is_leaf("P7_MIXED_FREQ_FLAG")   # flag
    assert not d.is_leaf("P7_MEAN_DEP")          # diamond
    assert not d.is_leaf("P7_IN")                # terminator
    assert not d.is_leaf("P7_DATA")              # parallelogram is data, not a leaf
    assert d.is_ref("P6") and d.is_ref("F_WOLD")
    assert not d.is_leaf("P6")


def test_unquoted_label_is_not_a_definition():
    d = audit.parse_diagram('graph TD\n    A["a"] --> P7_GARCH[GARCH]\n', "x.md:1")
    assert "P7_GARCH" not in d.nodes
    assert "P7_GARCH" in d.edge_ids


def test_collect_diagrams_skips_marked_and_records_where(tmp_path):
    docs = tmp_path / "docs"
    (docs / "a").mkdir(parents=True)
    (docs / "a" / "page.md").write_text(
        "# A\n\n```mermaid\ngraph TD\n    X_A[\"a\"] --> X_B[\"b\"]\n```\n\n"
        "```mermaid\n%% audit: skip\ngraph TD\n    Y_A[\"a\"]\n```\n", encoding="utf-8")
    diagrams = audit.collect_diagrams(docs)
    assert len(diagrams) == 1
    assert diagrams[0].where == "a/page.md:3"
    assert set(diagrams[0].nodes) == {"X_A", "X_B"}
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/bin/pytest tests/test_audit_mermaid.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'audit_flowcharts'`.

- [ ] **Step 3: Write the parsing part of the module**

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/bin/pytest tests/test_audit_mermaid.py -q`
Expected: `7 passed`.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_flowcharts.py tests/test_audit_mermaid.py
git commit -m "feat(audit): parse Mermaid fences into nodes, edges and classes"
```

---

### Task 2: Audit library — heading anchors and inventory loading

**Files:**
- Modify: `scripts/audit_flowcharts.py` (append)
- Test: `tests/test_audit_inventory.py`

**Interfaces:**
- Produces: `Row`, `heading_anchors`, `front_matter`, `load_inventory`, `check_inventory_targets`, `SECTION_RE`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_audit_inventory.py
import textwrap

import audit_flowcharts as audit


def test_heading_anchors_match_mkdocs_slugify_and_unique_suffixes():
    text = textwrap.dedent('''
        ---
        kind: theory
        ---
        # P7: Error-process specification

        ## GARCH

        ## GARCH

        ## `.hypothesis-test` and `.decision-rule` boxes

        ## Custom {#my-anchor}

        <a id="assumption-0"></a>

        ```python
        # not a heading
        ```
    ''')
    anchors = audit.heading_anchors(text)
    assert "p7-error-process-specification" in anchors
    assert "garch" in anchors and "garch_1" in anchors
    assert "hypothesis-test-and-decision-rule-boxes" in anchors
    assert "my-anchor" in anchors
    assert "assumption-0" in anchors
    assert "not-a-heading" not in anchors


def test_front_matter_is_parsed_and_absent_is_empty():
    assert audit.front_matter("---\nkind: theory\n---\n# T\n") == {"kind": "theory"}
    assert audit.front_matter("# T\n") == {}


def test_load_inventory_validates_rows(tmp_path):
    inv = tmp_path / "inventory.yml"
    inv.write_text(textwrap.dedent('''
        nodes:
          - id: P7_GARCH
            label: "GARCH"
            phase: P7
            areas: [10]
            section: "reference/10-volatility/index.md#garch"
          - id: P7_GARCH
            label: "dup"
            phase: P7
            areas: []
            section: "reference/10-volatility/index.md#garch"
          - id: BAD_SECTION
            label: "x"
            phase: P7
            areas: []
            section: "reference/10-volatility/index.html#garch"
          - id: MISSING
            label: "x"
            phase: P7
    '''), encoding="utf-8")
    rows, findings = audit.load_inventory(inv)
    assert [r.id for r in rows] == ["P7_GARCH"]
    assert rows[0].file == "reference/10-volatility/index.md"
    assert rows[0].anchor == "garch"
    assert rows[0].areas == (10,)
    messages = " | ".join(f.message for f in findings)
    assert "duplicate inventory id P7_GARCH" in messages
    assert "must look like path/file.md#anchor" in messages
    assert "missing keys" in messages
    assert all(f.level == "error" for f in findings)


def test_load_inventory_missing_file_is_an_error(tmp_path):
    rows, findings = audit.load_inventory(tmp_path / "nope.yml")
    assert rows == []
    assert findings[0].level == "error"


def test_check_inventory_targets_reports_missing_file_and_anchor(tmp_path):
    docs = tmp_path / "docs"
    (docs / "reference" / "10-volatility").mkdir(parents=True)
    (docs / "reference" / "10-volatility" / "index.md").write_text("# Volatility\n\n## GARCH\n", encoding="utf-8")
    rows = [
        audit.Row("P7_GARCH", "GARCH", "P7", (10,), "reference/10-volatility/index.md#garch"),
        audit.Row("P7_SV", "SV", "P7", (10,), "reference/10-volatility/index.md#stochastic-volatility"),
        audit.Row("P7_X", "X", "P7", (10,), "reference/99-nope/index.md#x"),
    ]
    findings = audit.check_inventory_targets(rows, docs)
    where = {f.where: f.message for f in findings}
    assert "P7_GARCH" not in where
    assert "anchor #stochastic-volatility not found" in where["P7_SV"]
    assert "does not exist" in where["P7_X"]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/bin/pytest tests/test_audit_inventory.py -q`
Expected: FAIL with `AttributeError: module 'audit_flowcharts' has no attribute 'heading_anchors'`.

- [ ] **Step 3: Append anchors and inventory code to the module**

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/bin/pytest tests/test_audit_inventory.py tests/test_audit_mermaid.py -q`
Expected: `12 passed`.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_flowcharts.py tests/test_audit_inventory.py
git commit -m "feat(audit): compute MkDocs heading anchors and load the leaf inventory"
```

---

### Task 3: Audit library — diagram and inventory cross-checks

**Files:**
- Modify: `scripts/audit_flowcharts.py` (append)
- Test: `tests/test_audit_crosschecks.py`

**Interfaces:**
- Produces: `check_diagrams`, `check_refs`, `check_nodes_vs_inventory`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_audit_crosschecks.py
import audit_flowcharts as audit


def diagram(src, where):
    return audit.parse_diagram(src, where)


A = diagram('graph TD\n    P7_IN(["in"]) --> P7_MULTI{"Several?"}\n    P7_MULTI -->|"Yes"| P7_GARCH["GARCH"]\n    P7_GARCH --> P8[["P8 Estimation"]]\n    F_WOLD[["Wold"]] -.- P7_GARCH\n    class P8,F_WOLD ref\n', "p07.md:3")
B = diagram('graph TD\n    P8_IN(["in"]) --> P7_MULTI{"dup"}\n    P7_MULTI --> P8["P8 Estimation"]\n    P8 --> P8_GHOST\n', "p08.md:3")


def test_check_diagrams_flags_duplicate_definition_with_first_location():
    findings = audit.check_diagrams([A, B])
    dup = [f for f in findings if "P7_MULTI" in f.message]
    assert len(dup) == 1
    assert dup[0].where == "p08.md:3"
    assert "already defined in p07.md:3" in dup[0].message


def test_check_diagrams_flags_bare_edge_ids():
    findings = audit.check_diagrams([A, B])
    bare = [f for f in findings if "P8_GHOST" in f.message]
    assert bare and bare[0].level == "error"
    assert "no shaped definition" in bare[0].message


def test_check_refs_resolve_to_definitions_or_foundation_rows():
    rows = [audit.Row("F_WOLD", "Wold decomposition", audit.FOUNDATION_PHASE, (1,), "00-foundations/stochastic-processes.md#wold-decomposition")]
    assert audit.check_refs([A, B], rows) == []            # P8 defined in B, F_WOLD is a foundation row
    assert any("F_WOLD" in f.message for f in audit.check_refs([A], []))   # no definition, no row
    assert any("P8" in f.message for f in audit.check_refs([A], rows))     # P8 undefined without B


def test_check_nodes_vs_inventory_both_directions():
    rows = [
        audit.Row("P7_GARCH", "GARCH", "P7", (10,), "reference/10-volatility/index.md#garch"),
        audit.Row("P7_ORPHAN", "Orphan", "P7", (10,), "reference/10-volatility/index.md#orphan"),
        audit.Row("F_WOLD", "Wold decomposition", audit.FOUNDATION_PHASE, (1,), "00-foundations/stochastic-processes.md#wold-decomposition"),
        audit.Row("F_LONELY", "Lonely", audit.FOUNDATION_PHASE, (1,), "00-foundations/stochastic-processes.md#lonely"),
    ]
    findings = audit.check_nodes_vs_inventory([A, B], rows)
    messages = {f.where: f.message for f in findings}
    assert "no inventory row" in messages["p08.md:3"]        # P8 is a leaf rectangle in B
    assert "no leaf definition" in messages["P7_ORPHAN"]
    assert "not referenced by any ref node" in messages["F_LONELY"]
    assert "P7_GARCH" not in messages and "F_WOLD" not in messages
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/bin/pytest tests/test_audit_crosschecks.py -q`
Expected: FAIL with `AttributeError: ... has no attribute 'check_diagrams'`.

- [ ] **Step 3: Append the cross-checks**

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/bin/pytest tests -q`
Expected: `16 passed`.

- [ ] **Step 5: Commit**

```bash
git add scripts/audit_flowcharts.py tests/test_audit_crosschecks.py
git commit -m "feat(audit): cross-check diagram definitions, refs and the inventory"
```

---

### Task 4: Audit library — sections, glossary, first-mention scan, CLI

**Files:**
- Modify: `scripts/audit_flowcharts.py` (append)
- Test: `tests/test_audit_glossary.py`, `tests/test_audit_cli.py`

**Interfaces:**
- Produces: `load_glossary`, `check_sections`, `check_glossary`, `nav_pages`, `first_mention_warnings`, `run_all`, `main`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_audit_glossary.py
import textwrap

import audit_flowcharts as audit


def make_docs(tmp_path):
    docs = tmp_path / "docs"
    (docs / "glossary").mkdir(parents=True)
    (docs / "00-foundations").mkdir()
    (docs / "reference" / "04-estimation").mkdir(parents=True)
    (docs / "01-workflow").mkdir()
    (docs / "00-foundations" / "stochastic-processes.md").write_text("# Stochastic processes\n\n## Independence\n\n## Law of large numbers\n", encoding="utf-8")
    (docs / "reference" / "04-estimation" / "index.md").write_text("# Estimation\n\n## Joint density\n\nThe joint density is defined here. See [theory](theory.md).\n", encoding="utf-8")
    (docs / "reference" / "04-estimation" / "theory.md").write_text("---\nkind: theory\n---\n# Why MLE\n", encoding="utf-8")
    (docs / "reference" / "04-estimation" / "stray.md").write_text("# Stray\n", encoding="utf-8")
    (docs / "01-workflow" / "index.md").write_text("# Workflow\n", encoding="utf-8")
    return docs


GLOSSARY = textwrap.dedent('''
    terms:
      - term: "Independence"
        definition: "d"
        foundation: true
        reference: "00-foundations/stochastic-processes.md#independence"
      - term: "Law of large numbers"
        definition: "d"
        foundation: true
        reference: "00-foundations/stochastic-processes.md#law-of-large-numbers"
      - term: "Joint density"
        definition: "d"
        derivation: "1. because of [Why MLE](theory.md)"
        depends_on: ["Independence", "Law of large numbers"]
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Dead end"
        definition: "d"
        depends_on: []
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Not yet"
        definition: "d"
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Cycle A"
        definition: "d"
        depends_on: ["Cycle B"]
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Cycle B"
        definition: "d"
        depends_on: ["Cycle A"]
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Bad ref"
        definition: "d"
        foundation: true
        reference: "reference/04-estimation/index.md#nope"
      - term: "Unknown dep"
        definition: "d"
        depends_on: ["Ghost"]
        reference: "reference/04-estimation/index.md#joint-density"
''')


def test_load_glossary_merges_files_and_flags_duplicates(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "glossary" / "a.yml").write_text('terms:\n  - term: "X"\n    definition: "d"\n', encoding="utf-8")
    (docs / "glossary" / "b.yml").write_text('terms:\n  - term: "X"\n    definition: "d"\n  - term: "Y"\n    definition: "d"\n', encoding="utf-8")
    (docs / "glossary" / "index.yml").write_text("files: [a.yml, b.yml]\n", encoding="utf-8")
    terms, findings = audit.load_glossary(docs / "glossary")
    assert [t["term"] for t in terms] == ["X", "Y"]
    assert terms[0]["_file"] == "a.yml"
    assert any("also defined in a.yml" in f.message for f in findings)


def test_check_glossary_levels(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "glossary" / "g.yml").write_text(GLOSSARY, encoding="utf-8")
    terms, _ = audit.load_glossary(docs / "glossary")
    findings = audit.check_glossary(terms, docs)
    by_term = {}
    for f in findings:
        by_term.setdefault(f.where.split(":", 1)[-1], []).append(f)
    assert "Joint density" not in by_term
    assert "Independence" not in by_term
    assert by_term["Not yet"][0].level == "warning"
    assert "depends_on absent" in by_term["Not yet"][0].message
    assert any(f.level == "error" and "non-foundation" in f.message for f in by_term["Dead end"])
    assert any("cycle" in f.message for f in findings)
    assert any("anchor #nope not found" in f.message for f in by_term["Bad ref"])
    assert any("'Ghost' is not a glossary term" in f.message for f in by_term["Unknown dep"])


def test_check_sections_method_theory_and_stray(tmp_path):
    docs = make_docs(tmp_path)
    rows = [audit.Row("P8_JOINT", "Joint density", "P8", (4,), "reference/04-estimation/index.md#joint-density")]
    terms = [{"term": "x", "derivation": ""}]
    findings = audit.check_sections(docs, rows, terms)
    wheres = {f.where: f.message for f in findings}
    assert "reference/04-estimation/theory.md" not in wheres            # linked from index.md
    assert "neither in the inventory" in wheres["reference/04-estimation/stray.md"]
    assert "01-workflow/index.md" not in wheres                         # index pages exempt


def test_check_sections_unlinked_theory_is_an_error(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "reference" / "04-estimation" / "index.md").write_text("# Estimation\n\n## Joint density\n", encoding="utf-8")
    rows = [audit.Row("P8_JOINT", "Joint density", "P8", (4,), "reference/04-estimation/index.md#joint-density")]
    findings = audit.check_sections(docs, rows, [])
    assert any(f.where == "reference/04-estimation/theory.md" and "not linked" in f.message for f in findings)


def test_nav_pages_flattens_and_tolerates_python_tags(tmp_path):
    yml = tmp_path / "mkdocs.yml"
    yml.write_text(textwrap.dedent('''
        markdown_extensions:
          - pymdownx.emoji:
              emoji_index: !!python/name:material.extensions.emoji.twemoji
        nav:
          - Home: index.md
          - Foundations:
              - 00-foundations/a.md
              - Sub:
                  - 00-foundations/b.md
          - reference/04-estimation/index.md
    '''), encoding="utf-8")
    assert audit.nav_pages(yml) == ["index.md", "00-foundations/a.md", "00-foundations/b.md", "reference/04-estimation/index.md"]


def test_first_mention_warning_only_when_pages_differ(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "00-foundations" / "early.md").write_text("# Early\n\nThe joint density appears here first.\n", encoding="utf-8")
    terms = [{"term": "Joint density", "_file": "g.yml", "reference": "reference/04-estimation/index.md#joint-density"},
             {"term": "Independence", "_file": "g.yml", "reference": "00-foundations/stochastic-processes.md#independence"}]
    pages = ["00-foundations/early.md", "00-foundations/stochastic-processes.md", "reference/04-estimation/index.md"]
    findings = audit.first_mention_warnings(pages, terms, docs)
    assert len(findings) == 1
    assert findings[0].level == "warning"
    assert "first mentioned on 00-foundations/early.md" in findings[0].message
```

```python
# tests/test_audit_cli.py
import textwrap

import audit_flowcharts as audit


def test_main_exit_status_follows_errors(tmp_path, capsys):
    root = tmp_path
    docs = root / "docs"
    (docs / "flowcharts").mkdir(parents=True)
    (docs / "glossary").mkdir()
    (docs / "01-workflow").mkdir()
    (root / "mkdocs.yml").write_text("nav:\n  - 01-workflow/index.md\n", encoding="utf-8")
    (docs / "01-workflow" / "index.md").write_text(
        '# P0: Data\n\n```mermaid\ngraph TD\n    P0["P0 Data"] --> P1["P1 Gate"]\n```\n', encoding="utf-8")
    (docs / "flowcharts" / "inventory.yml").write_text(textwrap.dedent('''
        nodes:
          - id: P0
            label: "P0: Data"
            phase: MASTER
            areas: [31]
            section: "01-workflow/index.md#p0-data"
    '''), encoding="utf-8")
    status = audit.main(["--root", str(root)])
    out = capsys.readouterr().out
    assert status == 1
    assert "leaf P1 has no inventory row" in out
    assert out.strip().endswith("1 error(s), 0 warning(s)")

    (docs / "flowcharts" / "inventory.yml").write_text(textwrap.dedent('''
        nodes:
          - id: P0
            label: "P0: Data"
            phase: MASTER
            areas: [31]
            section: "01-workflow/index.md#p0-data"
          - id: P1
            label: "P1 Gate"
            phase: MASTER
            areas: [31]
            section: "01-workflow/index.md#p0-data"
    '''), encoding="utf-8")
    assert audit.main(["--root", str(root)]) == 0
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/bin/pytest tests/test_audit_glossary.py tests/test_audit_cli.py -q`
Expected: FAIL with `AttributeError: ... has no attribute 'load_glossary'`.

- [ ] **Step 3: Append the remaining checks and the CLI**

```python
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
```

- [ ] **Step 4: Run the whole suite**

Run: `venv/bin/pytest tests -q`
Expected: `23 passed`.

- [ ] **Step 5: Run the CLI against the real tree**

Run: `venv/bin/python scripts/audit_flowcharts.py; echo "exit $?"`
Expected: errors are reported (no inventory yet, old diagrams define unquoted nodes) and `exit 1`. This is the known-red state that Tasks 7–9 turn green.

- [ ] **Step 6: Commit**

```bash
git add scripts/audit_flowcharts.py tests/test_audit_glossary.py tests/test_audit_cli.py
git commit -m "feat(audit): section, glossary and first-mention checks with CLI exit status"
```

---

### Task 5: Scaffold script — pending stubs from the inventory

**Files:**
- Create: `scripts/scaffold_stubs.py`
- Test: `tests/test_scaffold_stubs.py`

**Interfaces:**
- Consumes: `audit_flowcharts.load_inventory`, `heading_anchors`, `slugify`, `Row`.
- Produces: `scaffold(root, dry_run=False) -> list[str]` (actions taken), `heading_for(row) -> str`, CLI `python scripts/scaffold_stubs.py [--root PATH] [--dry-run]`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_scaffold_stubs.py
import textwrap

import audit_flowcharts as audit
import scaffold_stubs as scaffold


def write_inventory(root, body):
    (root / "docs" / "flowcharts").mkdir(parents=True, exist_ok=True)
    (root / "docs" / "flowcharts" / "inventory.yml").write_text(textwrap.dedent(body), encoding="utf-8")


def test_heading_for_uses_attr_id_only_when_slug_differs():
    plain = audit.Row("P7_GARCH", "GARCH", "P7", (10,), "reference/10-volatility/index.md#garch")
    custom = audit.Row("P7_SV", "Stochastic volatility", "P7", (10,), "reference/10-volatility/index.md#sv")
    assert scaffold.heading_for(plain) == "## GARCH"
    assert scaffold.heading_for(custom) == "## Stochastic volatility {#sv}"


def test_scaffold_creates_file_appends_heading_and_is_idempotent(tmp_path):
    root = tmp_path
    (root / "docs" / "reference" / "10-volatility").mkdir(parents=True)
    (root / "docs" / "reference" / "10-volatility" / "index.md").write_text("# Volatility\n", encoding="utf-8")
    write_inventory(root, '''
        nodes:
          - id: P7_GARCH
            label: "GARCH"
            phase: P7
            areas: [10]
            section: "reference/10-volatility/index.md#garch"
          - id: P7_JUMPS
            label: "Jump diffusion"
            phase: P7
            areas: [15]
            section: "reference/15-continuous-time/index.md#jump-diffusion"
    ''')
    actions = scaffold.scaffold(root)
    assert "append #garch to reference/10-volatility/index.md" in actions
    assert "create reference/15-continuous-time/index.md" in actions
    vol = (root / "docs" / "reference" / "10-volatility" / "index.md").read_text(encoding="utf-8")
    assert "\n## GARCH\n" in vol and "Section pending" in vol and "`P7_GARCH`" in vol
    ct = (root / "docs" / "reference" / "15-continuous-time" / "index.md").read_text(encoding="utf-8")
    assert ct.startswith("# Continuous Time\n")
    assert "## Jump diffusion" in ct
    assert scaffold.scaffold(root) == []          # second run: nothing to do
    assert vol == (root / "docs" / "reference" / "10-volatility" / "index.md").read_text(encoding="utf-8")


def test_dry_run_reports_without_writing(tmp_path):
    root = tmp_path
    write_inventory(root, '''
        nodes:
          - id: P7_GARCH
            label: "GARCH"
            phase: P7
            areas: [10]
            section: "reference/10-volatility/index.md#garch"
    ''')
    actions = scaffold.scaffold(root, dry_run=True)
    assert actions == ["create reference/10-volatility/index.md", "append #garch to reference/10-volatility/index.md"]
    assert not (root / "docs" / "reference").exists()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/bin/pytest tests/test_scaffold_stubs.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'scaffold_stubs'`.

- [ ] **Step 3: Write the script**

```python
# scripts/scaffold_stubs.py
"""Create pending stub sections for inventory rows whose target file or heading is missing.

Run: python scripts/scaffold_stubs.py [--root PATH] [--dry-run]
Idempotent: a second run reports no actions. Never deletes or rewrites existing text.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_flowcharts import Row, heading_anchors, load_inventory, slugify  # noqa: E402

PENDING = (
    '!!! note "Section pending"\n'
    "    To-do item created from the flowchart inventory (node `{id}`). "
    "Write this section following the content rules in `DESIGN-SYSTEM.md`.\n"
)


def title_from_path(rel: str) -> str:
    path = Path(rel)
    stem = path.parent.name if path.stem == "index" else path.stem
    words = [w for w in stem.split("-") if not w.isdigit()]
    return " ".join(w.capitalize() for w in words)


def heading_for(row: Row) -> str:
    if slugify(row.label, "-") == row.anchor:
        return f"## {row.label}"
    return f"## {row.label} {{#{row.anchor}}}"


def scaffold(root: Path, dry_run: bool = False) -> list[str]:
    docs = root / "docs"
    rows, _ = load_inventory(docs / "flowcharts" / "inventory.yml")
    actions: list[str] = []
    for row in rows:
        target = docs / row.file
        if not target.is_file():
            actions.append(f"create {row.file}")
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    f"# {title_from_path(row.file)}\n\nPending page created from the flowchart inventory.\n",
                    encoding="utf-8",
                )
        text = target.read_text(encoding="utf-8") if target.is_file() else ""
        if row.anchor in heading_anchors(text):
            continue
        actions.append(f"append #{row.anchor} to {row.file}")
        if not dry_run:
            with target.open("a", encoding="utf-8") as fh:
                fh.write(f"\n{heading_for(row)}\n\n{PENDING.format(id=row.id)}")
    return actions


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    for action in scaffold(args.root, args.dry_run):
        print(action)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `venv/bin/pytest tests/test_scaffold_stubs.py -q`
Expected: `3 passed`.

- [ ] **Step 5: Commit**

```bash
git add scripts/scaffold_stubs.py tests/test_scaffold_stubs.py
git commit -m "feat: scaffold pending stub sections from the flowchart inventory"
```

---

### Task 6: MkDocs hook — glossary index and audit warnings

**Files:**
- Create: `scripts/mkdocs_hooks.py`
- Modify: `mkdocs.yml` (add `hooks:` after `plugins:`)
- Test: `tests/test_mkdocs_hooks.py`

**Interfaces:**
- Consumes: `audit_flowcharts.run_all`.
- Produces: `write_glossary_index(docs_dir) -> bool` (True when the file was written), `on_pre_build(config, **kwargs)`; file `docs/glossary/index.yml` with `files: [...]`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_mkdocs_hooks.py
import logging

import mkdocs_hooks as hooks


def test_write_glossary_index_lists_yml_files_and_skips_itself(tmp_path):
    g = tmp_path / "glossary"
    g.mkdir()
    (g / "b.yml").write_text("terms: []\n", encoding="utf-8")
    (g / "a.yml").write_text("terms: []\n", encoding="utf-8")
    (g / "index.yml").write_text("stale\n", encoding="utf-8")
    assert hooks.write_glossary_index(tmp_path) is True
    assert (g / "index.yml").read_text(encoding="utf-8") == "files:\n- a.yml\n- b.yml\n"


def test_write_glossary_index_does_not_rewrite_identical_content(tmp_path):
    g = tmp_path / "glossary"
    g.mkdir()
    (g / "a.yml").write_text("terms: []\n", encoding="utf-8")
    assert hooks.write_glossary_index(tmp_path) is True
    before = (g / "index.yml").stat().st_mtime_ns
    assert hooks.write_glossary_index(tmp_path) is False
    assert (g / "index.yml").stat().st_mtime_ns == before


def test_on_pre_build_logs_errors_as_warnings(tmp_path, caplog):
    docs = tmp_path / "docs"
    (docs / "glossary").mkdir(parents=True)
    (docs / "flowcharts").mkdir()
    (docs / "flowcharts" / "inventory.yml").write_text("nodes:\n  - id: X\n    label: x\n    phase: P0\n    areas: []\n    section: 'a/b.md#c'\n", encoding="utf-8")
    with caplog.at_level(logging.INFO, logger="mkdocs.plugins.tsam_hooks"):
        hooks.on_pre_build({"docs_dir": str(docs)})
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert any("inventory row has no leaf definition" in r.getMessage() for r in warnings)
    assert (docs / "glossary" / "index.yml").exists()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `venv/bin/pytest tests/test_mkdocs_hooks.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'mkdocs_hooks'`.

- [ ] **Step 3: Write the hook module**

```python
# scripts/mkdocs_hooks.py
"""MkDocs hooks: generate docs/glossary/index.yml and surface audit findings as build warnings.

Registered in mkdocs.yml under `hooks:`. Under `mkdocs build --strict` every audit error fails the build.
The index is rewritten only when its content changes, so `mkdocs serve` does not loop on its own output.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audit_flowcharts as audit  # noqa: E402

log = logging.getLogger("mkdocs.plugins.tsam_hooks")


def write_glossary_index(docs_dir: Path) -> bool:
    gdir = docs_dir / "glossary"
    files = sorted(p.name for p in gdir.glob("*.yml") if p.name != "index.yml")
    content = yaml.safe_dump({"files": files}, sort_keys=False)
    target = gdir / "index.yml"
    if target.is_file() and target.read_text(encoding="utf-8") == content:
        return False
    target.write_text(content, encoding="utf-8")
    return True


def on_pre_build(config, **kwargs) -> None:
    docs_dir = Path(config["docs_dir"])
    if write_glossary_index(docs_dir):
        log.info("wrote glossary/index.yml")
    for f in audit.run_all(docs_dir.parent):
        logger = log.warning if f.level == "error" else log.info
        logger("audit %s %s: %s", f.level, f.where, f.message)
```

- [ ] **Step 4: Register the hook in `mkdocs.yml`**

Insert after the `plugins:` block (after the `- tags` line):
```yaml
# Build hooks: glossary index generation and the flowchart/glossary audit
hooks:
  - scripts/mkdocs_hooks.py
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `venv/bin/pytest tests -q`
Expected: `29 passed`.

- [ ] **Step 6: Confirm the hook runs in a build**

Run: `venv/bin/mkdocs build 2>&1 | grep -c "audit error"; ls docs/glossary/index.yml`
Expected: a positive count (the tree is still red), and `docs/glossary/index.yml` exists. `mkdocs build --strict` is expected to FAIL from here until Task 9; the tasks in between verify with plain `mkdocs build` plus a check that the only warnings are `audit` lines:
`venv/bin/mkdocs build 2>&1 | grep WARNING | grep -v "audit error" ; echo "non-audit warnings above (expect none)"`.

- [ ] **Step 7: Commit**

```bash
git add scripts/mkdocs_hooks.py tests/test_mkdocs_hooks.py mkdocs.yml
git commit -m "feat: MkDocs hook generates glossary index and reports audit findings"
```

---

### Task 7a: Part 0 — rename to `00-foundations` and add the two new chapters

**Files:**
- Move: `docs/00-introduction/` → `docs/00-foundations/`; `overview.md` → `ols-assumptions.md`
- Create: `docs/00-foundations/stochastic-processes.md`, `docs/00-foundations/asymptotics.md`
- Modify: `mkdocs.yml` nav; `docs/00-foundations/ols-assumptions.md`; `docs/00-foundations/do-you-need-time-series-analysis.md`; `docs/appendices/A-ols-derivation.md`; `docs/appendices/C-python-environment-setup.md`; `docs/index.md`; `DESIGN-SYSTEM.md`; `README.md`

- [ ] **Step 1: Move the directory and the file**

```bash
git mv docs/00-introduction docs/00-foundations
git mv docs/00-foundations/overview.md docs/00-foundations/ols-assumptions.md
```

- [ ] **Step 2: Rewrite every path reference**

```bash
grep -rl --include='*.md' --include='*.yml' --include='*.js' '00-introduction' docs mkdocs.yml DESIGN-SYSTEM.md README.md CLAUDE.md \
  | xargs sed -i '' 's#00-introduction#00-foundations#g'
grep -rl --include='*.md' --include='*.yml' '00-foundations/overview' docs mkdocs.yml DESIGN-SYSTEM.md README.md CLAUDE.md \
  | xargs sed -i '' -E 's#00-foundations/overview\.(md|html)#00-foundations/ols-assumptions.\1#g'
grep -rn 'overview\.md\|00-introduction' docs mkdocs.yml DESIGN-SYSTEM.md README.md CLAUDE.md
```
Expected: the final grep prints nothing. (`sed -i ''` is the macOS form; on Linux use `sed -i`.)

- [ ] **Step 3: Rename the nav section**

In `mkdocs.yml`, replace the `- Introduction:` block with:
```yaml
  - Foundations:
      - 00-foundations/logic-of-statistical-analysis.md
      - 00-foundations/do-you-need-time-series-analysis.md
      - 00-foundations/ols-assumptions.md
      - 00-foundations/stochastic-processes.md
      - 00-foundations/asymptotics.md
```

- [ ] **Step 4: Mark the illustrative diagram as audit-exempt**

In `docs/00-foundations/do-you-need-time-series-analysis.md`, change the opening of the Mermaid fence from
```text
```mermaid
graph TD
```
to
```text
```mermaid
%% audit: skip
graph TD
```
Do the same for both fences in `docs/design-system-showcase.md`.

- [ ] **Step 5: Create `stochastic-processes.md`**

```markdown
# Stochastic Processes

A time series is one realisation of a stochastic process: a family of random variables indexed by time. Every error-process choice in [P7](../01-workflow/p07-error-process.md) names a stochastic process, and every diagnostic in [P3](../01-workflow/p03-exploratory-diagnostics.md) asks which properties that process has. This chapter collects the definitions and theorems those choices rest on. Each section below is the root of a derivation chain shown in the glossary drawer.

The sections are created from the flowchart inventory and written in Plan B.
```

- [ ] **Step 6: Create `asymptotics.md`**

```markdown
# Asymptotics for Dependent Data

Estimators in this book are justified by large-sample arguments: a law of large numbers makes a sample average converge to an expectation, and a central limit theorem gives the limiting distribution that standard errors and tests rely on. For time series both results need more than independence: the dependence between observations must die out fast enough. This chapter states the dependent-data versions of both theorems, the delta method, and the conditions (stationarity, ergodicity, mixing) under which they hold.

!!! note "Section pending"
    Content is written in Plan B. The glossary terms `Law of large numbers` and `Central limit theorem` are homed here.

## Law of large numbers

!!! note "Section pending"
    To be written.

## Central limit theorem

!!! note "Section pending"
    To be written.
```

- [ ] **Step 7: Build**

Run: `venv/bin/mkdocs build 2>&1 | grep WARNING | grep -v "audit error"; echo "---"; venv/bin/python scripts/audit_flowcharts.py | tail -1`
Expected: no non-audit warnings. Audit still red.

- [ ] **Step 8: Commit**

```bash
git add -A docs/00-foundations docs/design-system-showcase.md docs/appendices docs/index.md mkdocs.yml DESIGN-SYSTEM.md README.md CLAUDE.md
git commit -m "refactor: rename 00-introduction to 00-foundations and add Part 0 chapter stubs"
```

---

### Task 7b: Workflow skeleton — phase pages, purpose and representation subdirectories

**Files:**
- Create: `docs/01-workflow/index.md`, `p00-data.md`, `p01-data-type-gate.md`, `p03-exploratory-diagnostics.md`, `p04-transformations.md`, `p06-mean-model-class.md`, `p07-error-process.md`, `p08-estimation.md`, `p09-diagnostics-selection.md`, `p10-inference.md`, `p11-validation-deployment.md`; `p02-purpose/index.md` + `01-forecasting.md` … `10-simulation.md`; `p05-representation/index.md` + `01-time-domain.md` … `06-hilbert-phase.md`
- Move: `docs/01-master-flowchart/*.md` → `planning/legacy-flowcharts/`
- Modify: `mkdocs.yml` nav; `docs/00-foundations/ols-assumptions.md` (its "Next" link)

- [ ] **Step 1: Move the legacy flowchart pages out of the site**

```bash
mkdir -p planning/legacy-flowcharts
git mv docs/01-master-flowchart/01-general-flowchart.md planning/legacy-flowcharts/
git mv docs/01-master-flowchart/02-purpose-workflow.md planning/legacy-flowcharts/
git mv docs/01-master-flowchart/03-representation-workflow.md planning/legacy-flowcharts/
rmdir docs/01-master-flowchart
```

- [ ] **Step 2: Generate the phase pages**

Run this once from the repo root (it is a one-off generator; do not commit it):

```bash
venv/bin/python - <<'PY'
from pathlib import Path
W = Path("docs/01-workflow")
W.mkdir(exist_ok=True)

PHASES = [
 ("p00-data.md", "P0", "Data acquisition and cleaning", "Is the series fit to analyse?",
  "Sampling rate and resolution; timestamp alignment, time zones, daylight-saving transitions, duplicate stamps; missing-value imputation; the time-series outlier taxonomy (additive, innovation, level shift, temporary change); robust filtering; unit and metadata consistency; cumulative-to-flow conversion; anti-aliasing when downsampling; calendar effects; temporal disaggregation; data revisions and vintages.",
  ["Inspection and sampling: data quality, sampling rates, alignment", "Missing data: imputation strategies and segmentation", "Outlier detection: statistical methods for identifying and treating outliers", "Transformations: variance stabilisation, detrending, normalisation"]),
 ("p01-data-type-gate.md", "P1", "Data-type gate", "What kind of object is this?",
  "Three routing questions (value type, sampling, cross-sectional structure) send the series down the standard path or into one of seven branches, and set flags that later phases read.", []),
 ("p03-exploratory-diagnostics.md", "P3", "Exploratory diagnostics", "What structure is present?",
  "Distribution, variance stability, trend-stationary versus difference-stationary behaviour, unit roots and seasonal unit roots, explosive roots, structural breaks, seasonality, autocorrelation, long-memory indicators, nonlinearity tests, nonparametric trend tests, and the multivariate checks (cross-correlation, lead-lag, cointegration pre-check).",
  ["Descriptive statistics", "Distributional analysis", "Stationarity testing", "Autocorrelation analysis", "Seasonality detection"]),
 ("p04-transformations.md", "P4", "Transformations", "What must change before modelling?",
  "Variance-stabilising transforms, regular, seasonal and fractional differencing, detrending, seasonal adjustment, multiple seasonality, filter-based and model-based decomposition, break handling, and the retest loop.", []),
 ("p06-mean-model-class.md", "P6", "Conditional-mean model class", "Which family describes the mean?",
  "Routing on the multivariate, global and exogenous-variable flags, then the model families: univariate linear, periodic and intermittent, long memory, nonlinear, time-varying parameter, multivariate, structural state-space, system identification, count and categorical, machine learning and deep learning, and global models.",
  ["ARIMA models", "Seasonal models (SARIMA)", "Multivariate models (VAR, VECM)", "Volatility models (GARCH): now specified in P7", "State-space models", "Machine learning approaches"]),
 ("p07-error-process.md", "P7", "Error-process specification", "What process do the innovations follow?",
  "Given the residuals of the P6 mean model, decide the innovation process: remaining mean dependence, conditional heteroskedasticity, distribution, variance regimes, cross-series dependence, and the count and event-time variants. The output is a joint model handed to P8 for joint estimation, which is where Cochrane-Orcutt two-step estimation is replaced by joint maximum likelihood.", []),
 ("p08-estimation.md", "P8", "Estimation", "How are parameters obtained?",
  "Least squares and its generalisations, moment methods, exact and conditional likelihood, quasi-likelihood, GMM, Whittle, cointegrating-regression estimators, robust estimators, Bayesian computation, EM and filtering, simulation-based inference, empirical-loss minimisation with time-aware tuning, and convergence checks.", []),
 ("p09-diagnostics-selection.md", "P9", "Diagnostics and model selection", "Does the fitted model hold up?",
  "Residual tests on the complete model, volatility and count diagnostics, information criteria, bootstrap inference, and forecast-comparison tests; failures loop back to P6 or P7.", []),
 ("p10-inference.md", "P10", "Inference and interpretation", "What does the model say, for this purpose?",
  "Coefficient and restriction tests, HAC inference, cointegration and causality inference, structural identification and impulse responses, counterfactuals, forecasting outputs, nowcasting, risk measures and their backtests, scenario simulation, and interpretability.", []),
 ("p11-validation-deployment.md", "P11", "Validation and deployment", "Does it work out of sample and keep working?",
  "Rolling-origin validation and backtesting, purpose-specific metrics, documentation, drift monitoring, statistical process control, online updating, and the retraining policy.",
  ["Model validation", "Out-of-sample testing", "Cross-validation for time series", "Deployment strategies", "Monitoring and drift detection", "Retraining policies"]),
]

TEMPLATE = """# {pid}: {title}

**Question this phase answers:** {question}

{intro}

## Sub-diagram

!!! note "Diagram pending"
    The {pid} sub-diagram is drawn in Plan B. Leaf nodes of this phase are listed in `docs/flowcharts/inventory.yml`.

## Phase guide

!!! note "Section pending"
    Procedural guide to this phase: which tests to run, in which order, and where each outcome leads.
{topics}"""

for fname, pid, title, question, intro, topics in PHASES:
    topics_md = ""
    if topics:
        topics_md = "\n### Topics carried over from the previous outline\n\n" + "\n".join(f"- {t}" for t in topics) + "\n"
    (W / fname).write_text(TEMPLATE.format(pid=pid, title=title, question=question, intro=intro, topics=topics_md), encoding="utf-8")

(W / "index.md").write_text("""# General Flowchart

The general flowchart is the spine of this book. The master diagram below shows the twelve phases of the workflow; each phase box opens the chapter that holds that phase's sub-diagram, and every leaf node in a sub-diagram opens the section that teaches it.

## Master diagram

!!! note "Diagram pending"
    Drawn in Task 8 of the skeleton plan.

## How to read the diagrams

Shapes follow the decision-flowchart notation in the design system: stadiums start and end a chart, diamonds ask a question, rectangles are steps or outcomes, dashed subroutine boxes point to another chapter, and dotted edges are feedback or optional flow. Every rectangle is a section of this book; click it.
""", encoding="utf-8")

P2 = Path("docs/01-workflow/p02-purpose"); P2.mkdir(exist_ok=True)
PURPOSES = [
 ("01-forecasting.md", 1, "Forecasting", "Predict future values with quantified uncertainty.", "Point and interval forecasts, multi-step strategies, combination, reconciliation", "Rolling-origin cross-validation, RMSE / MAE / MASE, interval coverage, CRPS"),
 ("02-causal-inference.md", 2, "Causal and structural inference", "Determine whether and how one series drives another, and quantify the effect.", "Identification, impulse responses and variance decompositions, local projections, counterfactuals, placebo tests", "Robustness across specifications, pre-trend checks"),
 ("03-signal-extraction.md", 3, "Signal extraction and denoising", "Separate the signal of interest from noise.", "Filters and Kalman smoothing", "Signal-to-noise ratio, spectral comparison, phase distortion"),
 ("04-change-point-detection.md", 4, "Change-point detection", "Locate the times at which the statistical properties change.", "Change locations with confidence intervals", "Detection delay, false-alarm rate"),
 ("05-anomaly-regime-detection.md", 5, "Anomaly and regime detection", "Flag unusual observations or periods and identify state switches.", "Thresholds and regime probabilities", "Event-level precision and recall, NAB score"),
 ("06-decomposition.md", 6, "Decomposition", "Split the series into interpretable components.", "Component interpretation", "Residual white-noise check, revision stability"),
 ("07-feature-extraction-classification.md", 7, "Feature extraction, classification and clustering", "Turn series into feature vectors and learn labels or groups.", "Feature importance, prototypes", "Downstream cross-validation, F1, silhouette"),
 ("08-spectral-analysis.md", 8, "Spectral analysis", "Describe the distribution of variance across frequencies.", "Peak significance, coherence, phase", "Fisher's g test, confidence bands"),
 ("09-system-identification.md", 9, "System identification", "Identify a dynamic input-output model of a system.", "Transfer function, poles and zeros, stability", "Prediction error, cross-validated fit"),
 ("10-simulation.md", 10, "Simulation and scenario generation", "Generate paths from a fitted model for stress tests, scenarios or synthetic data.", "Path simulation, stress testing, synthetic data", "Distribution matching, bootstrap coverage"),
]
for fname, n, title, goal, inference, metrics in PURPOSES:
    (P2 / fname).write_text(f"""# Purpose {n}: {title}

**Goal:** {goal}

## Sub-chart

!!! note "Diagram pending"
    Drawn in Plan B. Structure: purpose-specific preliminary questions, then the spine phases with this purpose's emphasis, then purpose-specific leaves, then the P10 inference and P11 metrics below.

## P10 inference for this purpose

{inference}.

## P11 metrics for this purpose

{metrics}.
""", encoding="utf-8")
(P2 / "index.md").write_text("""# P2: Purpose

**Question this phase answers:** What is the question?

The purpose decides which later phases matter most and which inference and metrics apply at the end. Ten purposes are distinguished. Methods that belong to a purpose rather than to the standard pipeline (change-point algorithms, anomaly methods, decomposition methods, feature extraction, classification, clustering, simulation) are leaves of this phase.

## Purpose selector

!!! note "Diagram pending"
    Drawn in Task 8 of the skeleton plan.

## Quick navigation

| Purpose | Emphasised phases | Key leaves |
|---|---|---|
| Pending | Pending | Filled in Plan B |
""", encoding="utf-8")

P5 = Path("docs/01-workflow/p05-representation"); P5.mkdir(exist_ok=True)
REPS = [
 ("01-time-domain.md", 1, "Time domain", "Prediction, causal inference and sequential dependence."),
 ("02-frequency-domain.md", 2, "Frequency domain", "Periodicity, cycles, filtering and spectral content."),
 ("03-time-frequency.md", 3, "Time-frequency", "Non-stationary signals, transients and evolving spectra."),
 ("04-state-space.md", 4, "State space", "Latent states, irregular sampling, missing observations and online updating."),
 ("05-functional.md", 5, "Functional", "Series that are curves, shape analysis and derivative information."),
 ("06-hilbert-phase.md", 6, "Hilbert and phase", "Instantaneous frequency, amplitude envelopes and phase synchronisation."),
]
for fname, n, title, best in REPS:
    (P5 / fname).write_text(f"""# Representation {n}: {title}

**Best for:** {best}

## Sub-chart

!!! note "Diagram pending"
    Drawn in Plan B. Structure: when to choose this representation, representation-specific transforms and estimators, available P6 model families as references, back to P6.
""", encoding="utf-8")
(P5 / "index.md").write_text("""# P5: Representation selection

**Question this phase answers:** Which mathematical object is modelled?

Six representations are distinguished. Transforms and estimators that belong to a representation (spectral estimators, filters, wavelets, the analytic signal, embeddings, functional bases) are leaves of this phase; model families remain in P6.

## Representation selector

!!! note "Diagram pending"
    Drawn in Task 8 of the skeleton plan.

## Quick navigation

| Representation | Choose when | Key leaves |
|---|---|---|
| Pending | Pending | Filled in Plan B |

### Topics carried over from the previous outline

- Fourier theory
- Power spectral density
- Periodicity detection
- Spectral analysis
- Filtering techniques
""", encoding="utf-8")
print("written", len(list(W.rglob("*.md"))), "pages")
PY
```
Expected: `written 30 pages`.

- [ ] **Step 3: Replace the Flowcharts nav block**

In `mkdocs.yml`, replace the `- Flowcharts:` block with:
```yaml
  - Workflow:
      - 01-workflow/index.md
      - 01-workflow/p00-data.md
      - 01-workflow/p01-data-type-gate.md
      - Purpose:
          - 01-workflow/p02-purpose/index.md
          - 01-workflow/p02-purpose/01-forecasting.md
          - 01-workflow/p02-purpose/02-causal-inference.md
          - 01-workflow/p02-purpose/03-signal-extraction.md
          - 01-workflow/p02-purpose/04-change-point-detection.md
          - 01-workflow/p02-purpose/05-anomaly-regime-detection.md
          - 01-workflow/p02-purpose/06-decomposition.md
          - 01-workflow/p02-purpose/07-feature-extraction-classification.md
          - 01-workflow/p02-purpose/08-spectral-analysis.md
          - 01-workflow/p02-purpose/09-system-identification.md
          - 01-workflow/p02-purpose/10-simulation.md
      - 01-workflow/p03-exploratory-diagnostics.md
      - 01-workflow/p04-transformations.md
      - Representation:
          - 01-workflow/p05-representation/index.md
          - 01-workflow/p05-representation/01-time-domain.md
          - 01-workflow/p05-representation/02-frequency-domain.md
          - 01-workflow/p05-representation/03-time-frequency.md
          - 01-workflow/p05-representation/04-state-space.md
          - 01-workflow/p05-representation/05-functional.md
          - 01-workflow/p05-representation/06-hilbert-phase.md
      - 01-workflow/p06-mean-model-class.md
      - 01-workflow/p07-error-process.md
      - 01-workflow/p08-estimation.md
      - 01-workflow/p09-diagnostics-selection.md
      - 01-workflow/p10-inference.md
      - 01-workflow/p11-validation-deployment.md
```

- [ ] **Step 4: Fix the links that pointed at the old flowchart pages**

```bash
grep -rn '01-master-flowchart' docs mkdocs.yml README.md DESIGN-SYSTEM.md CLAUDE.md
```
For each hit, replace: `01-master-flowchart/01-general-flowchart.md` → `01-workflow/index.md`; `01-master-flowchart/02-purpose-workflow.md` → `01-workflow/p02-purpose/index.md`; `01-master-flowchart/03-representation-workflow.md` → `01-workflow/p05-representation/index.md`. Anchored links such as `02-purpose-workflow.md#1-forecasting-workflow` become the purpose page: `01-workflow/p02-purpose/01-forecasting.md`. In `ols-assumptions.md` the footer link text becomes `**[Next: General Flowchart →](../01-workflow/index.md)**`.

```bash
sed -i '' 's#01-master-flowchart/01-general-flowchart\.md#01-workflow/index.md#g; s#01-master-flowchart/02-purpose-workflow\.md\#1-forecasting-workflow#01-workflow/p02-purpose/01-forecasting.md#g; s#01-master-flowchart/02-purpose-workflow\.md\#2-causal-analysis-structural-inference#01-workflow/p02-purpose/02-causal-inference.md#g; s#01-master-flowchart/02-purpose-workflow\.md\#5-anomaly-regime-detection#01-workflow/p02-purpose/05-anomaly-regime-detection.md#g; s#01-master-flowchart/02-purpose-workflow\.md\#7-feature-extraction-for-ml#01-workflow/p02-purpose/07-feature-extraction-classification.md#g; s#01-master-flowchart/03-representation-workflow\.md\#1-time-domain-representation#01-workflow/p05-representation/01-time-domain.md#g; s#01-master-flowchart/03-representation-workflow\.md\#2-frequency-domain-representation#01-workflow/p05-representation/02-frequency-domain.md#g; s#01-master-flowchart/02-purpose-workflow\.md#01-workflow/p02-purpose/index.md#g; s#01-master-flowchart/03-representation-workflow\.md#01-workflow/p05-representation/index.md#g' docs/index.md docs/00-foundations/ols-assumptions.md README.md
grep -rn '01-master-flowchart' docs mkdocs.yml README.md DESIGN-SYSTEM.md CLAUDE.md
```
Expected: the final grep prints nothing.

- [ ] **Step 5: Build**

Run: `venv/bin/mkdocs build 2>&1 | grep WARNING | grep -v "audit error"; echo "---"`
Expected: no non-audit warnings. If MkDocs reports a page "not included in nav", add it to the block in Step 3.

- [ ] **Step 6: Commit**

```bash
git add -A docs/01-workflow planning/legacy-flowcharts docs/index.md docs/00-foundations/ols-assumptions.md mkdocs.yml README.md
git commit -m "feat: workflow skeleton with phase, purpose and representation pages; park legacy flowcharts"
```

---

### Task 7c: Reference skeleton — 34 area landing pages

**Files:**
- Create: `docs/reference/NN-slug/index.md` × 34
- Modify: `mkdocs.yml` nav

- [ ] **Step 1: Generate the 34 landing pages**

One-off generator; run from the repo root, do not commit the script:

```bash
venv/bin/python - <<'PY'
from pathlib import Path
AREAS = [
 (1, "math-foundations", "Math Foundations", "Probability, stochastic processes, linear algebra and asymptotics. The content of this area lives in Part 0; this page indexes it.", "Theory & Inference"),
 (2, "fundamentals", "Fundamentals", "Trend, seasonality, cycles and noise; stationarity and its tests; ACF and PACF.", "Core Models"),
 (3, "classical", "Classical Models", "ARIMA family, exponential smoothing, dynamic regression, classical decomposition and the periodogram.", "Core Models"),
 (4, "estimation", "Estimation", "Least squares, moments, likelihood, GMM, Whittle, Bayesian and empirical-loss estimators.", "Theory & Inference"),
 (5, "hypothesis-testing", "Hypothesis Testing", "Unit-root, cointegration, causality, break, serial-correlation and normality tests; bootstrap.", "Theory & Inference"),
 (6, "model-selection", "Model Selection", "Information criteria, time-series cross-validation, residual diagnostics and forecast comparison.", "Theory & Inference"),
 (7, "long-memory", "Long Memory", "ARFIMA, fractional Brownian motion, Hurst exponent, GPH and local Whittle estimation.", "Core Models"),
 (8, "nonlinear", "Nonlinear Models", "Threshold, smooth-transition, regime-switching, bilinear and nonparametric models; chaos indicators.", "Core Models"),
 (9, "multivariate", "Multivariate Models", "VAR, SVAR, VECM, factor models, regularised VAR, graphical and tensor models.", "Core Models"),
 (10, "volatility", "Volatility", "ARCH and GARCH families, stochastic volatility, realised measures, risk measures, copulas and extreme values.", "Core Models"),
 (11, "state-space", "State Space", "Linear Gaussian state-space models, Kalman filtering and smoothing, nonlinear filters and structural models.", "Specialized Models"),
 (12, "bayesian", "Bayesian Time Series", "Bayesian VAR, Bayesian ARIMA, posterior predictive inference, model comparison and time-varying parameters.", "Specialized Models"),
 (13, "spectral-analysis", "Spectral Analysis", "Discrete Fourier transform, spectral density estimation, cross-spectra, wavelets and band-pass filters.", "Representations & Signals"),
 (14, "functional-high-frequency", "Functional and High-Frequency", "Functional time series, durations, ultra-high-frequency data and survival models.", "Representations & Signals"),
 (15, "continuous-time", "Continuous-Time Models", "Diffusions, CARMA, Levy processes, jump diffusions and numerical methods for SDEs.", "Specialized Models"),
 (16, "count-categorical", "Count and Categorical", "Integer-valued, categorical and compositional time series.", "Specialized Models"),
 (17, "point-processes", "Point Processes", "Poisson, renewal, Cox and Hawkes processes; marked and neural point processes.", "Specialized Models"),
 (18, "machine-learning", "Machine Learning and Deep Learning", "Tree ensembles, Gaussian processes, recurrent and convolutional networks, transformers, state-space sequence models and foundation models.", "ML, Forecasting & Practice"),
 (19, "classification-anomaly", "Classification, Clustering and Anomaly Detection", "Distance-based and kernel methods, shapelets, symbolic representations, change-point and anomaly algorithms.", "Representations & Signals"),
 (20, "spatio-temporal", "Spatio-Temporal Models", "Spatial econometrics with time, geostatistics, graph-based and network time series.", "Representations & Signals"),
 (21, "causal-inference", "Causal Inference", "Granger-type causality, structural identification, counterfactual designs and nonlinear causal discovery.", "ML, Forecasting & Practice"),
 (22, "forecasting-practice", "Forecasting Theory and Practice", "Forecast combination, reconciliation, mixed-frequency methods and judgmental forecasting.", "ML, Forecasting & Practice"),
 (23, "online-adaptive", "Online Learning and Adaptive Methods", "Recursive estimation, forgetting factors, drift detection and streaming methods.", "ML, Forecasting & Practice"),
 (24, "robust-nonparametric", "Robust and Nonparametric Methods", "Robust filtering and estimation, quantile autoregression, nonparametric trend tests.", "ML, Forecasting & Practice"),
 (25, "simulation", "Simulation and Computational Methods", "Monte Carlo, bootstrap variants, simulation-based inference, EM, ABC and variational methods.", "Theory & Inference"),
 (26, "applied-domains", "Applied Domains", "Finance, macroeconomics, condition monitoring and reliability, environmental trends, epidemiology, biomedical signals and IoT.", "ML, Forecasting & Practice"),
 (27, "regression-time-series", "Regression with Time-Series Data", "OLS under temporal dependence, HAC inference, feasible GLS, dynamic regression, distributed lags and spurious regression.", "Theory & Inference"),
 (28, "nonstationarity-theory", "Nonstationarity Theory", "Unit-root asymptotics, cointegration theory, near-unit roots, fractional cointegration and bubble tests.", "Theory & Inference"),
 (29, "seasonality-calendar", "Seasonality and Calendar", "Seasonal unit roots, seasonal adjustment, periodic autoregression, multiple seasonality and calendar effects.", "Core Models"),
 (30, "structural-change", "Structural Change and Time-Varying Parameters", "Break tests, time-varying parameter models, forecasting under breaks and statistical process control.", "Core Models"),
 (31, "data-preparation", "Data Preparation and Missing Data", "Imputation, irregular sampling, outlier taxonomy, temporal disaggregation and real-time data. The procedural content lives in P0 and P1; this page indexes it.", "ML, Forecasting & Practice"),
 (32, "panel-time-series", "Panel Time Series", "Panel unit roots and cointegration, dynamic panel GMM, heterogeneous panels and cross-sectional dependence.", "Core Models"),
 (33, "system-identification", "System Identification and Dynamical Systems", "ARX, ARMAX and transfer-function models, subspace methods, Takens embedding, dynamic mode decomposition and sparse identification.", "Specialized Models"),
 (34, "probabilistic-forecasting", "Probabilistic Forecasting and Evaluation", "Density and quantile forecasts, scoring rules, calibration, multi-step strategies and intermittent demand.", "ML, Forecasting & Practice"),
]
for n, slug, title, blurb, tab in AREAS:
    d = Path(f"docs/reference/{n:02d}-{slug}"); d.mkdir(parents=True, exist_ok=True)
    (d / "index.md").write_text(f"""# {n}. {title}

{blurb}

Landing-page tab: *{tab}*. Sections below are created from the flowchart inventory; each is a leaf node of some sub-diagram and is written following the content rules in `DESIGN-SYSTEM.md`.
""", encoding="utf-8")
print("areas", len(AREAS))
PY
```
Expected: `areas 34`.

- [ ] **Step 2: Add the Reference nav block**

In `mkdocs.yml`, insert after the Workflow block and before `- Appendices:`:
```yaml
  - Reference:
      - Theory & Inference:
          - reference/01-math-foundations/index.md
          - reference/04-estimation/index.md
          - reference/05-hypothesis-testing/index.md
          - reference/06-model-selection/index.md
          - reference/25-simulation/index.md
          - reference/27-regression-time-series/index.md
          - reference/28-nonstationarity-theory/index.md
      - Core Models:
          - reference/02-fundamentals/index.md
          - reference/03-classical/index.md
          - reference/07-long-memory/index.md
          - reference/08-nonlinear/index.md
          - reference/09-multivariate/index.md
          - reference/10-volatility/index.md
          - reference/29-seasonality-calendar/index.md
          - reference/30-structural-change/index.md
          - reference/32-panel-time-series/index.md
      - Specialized Models:
          - reference/11-state-space/index.md
          - reference/12-bayesian/index.md
          - reference/15-continuous-time/index.md
          - reference/16-count-categorical/index.md
          - reference/17-point-processes/index.md
          - reference/33-system-identification/index.md
      - Representations & Signals:
          - reference/13-spectral-analysis/index.md
          - reference/14-functional-high-frequency/index.md
          - reference/19-classification-anomaly/index.md
          - reference/20-spatio-temporal/index.md
      - ML, Forecasting & Practice:
          - reference/18-machine-learning/index.md
          - reference/21-causal-inference/index.md
          - reference/22-forecasting-practice/index.md
          - reference/23-online-adaptive/index.md
          - reference/24-robust-nonparametric/index.md
          - reference/26-applied-domains/index.md
          - reference/31-data-preparation/index.md
          - reference/34-probabilistic-forecasting/index.md
```

- [ ] **Step 3: Build**

Run: `venv/bin/mkdocs build 2>&1 | grep WARNING | grep -v "audit error"; echo "---"`
Expected: no non-audit warnings.

- [ ] **Step 4: Commit**

```bash
git add docs/reference mkdocs.yml
git commit -m "feat: reference-axis landing pages for the 34 areas"
```

---

### Task 7d: Remove the old chapter directories and repoint the landing page and appendices

**Files:**
- Delete: `docs/02-data-preparation/`, `docs/03-exploratory-analysis/`, `docs/04-frequency-domain/`, `docs/05-modelling/`, `docs/06-feature-extraction/`, `docs/07-validation-deployment/`
- Modify: `mkdocs.yml` nav; `docs/index.md`; `docs/appendices/index.md`; `docs/00-foundations/do-you-need-time-series-analysis.md`; `docs/appendices/C-python-environment-setup.md`

- [ ] **Step 1: Delete the directories and their nav entries**

```bash
git rm -r docs/02-data-preparation docs/03-exploratory-analysis docs/04-frequency-domain docs/05-modelling docs/06-feature-extraction docs/07-validation-deployment
```
In `mkdocs.yml` delete the six nav blocks `- Data Preparation:` … `- Validation & Deployment:`.

- [ ] **Step 2: Repoint links**

```bash
grep -rn '0[2-7]-[a-z-]*/index\.md\|0[2-7]-[a-z-]*/' docs README.md DESIGN-SYSTEM.md CLAUDE.md | grep -v '^docs/reference/' | grep -v 'p0[0-9]-' 
```
Apply:
- `docs/00-foundations/do-you-need-time-series-analysis.md`: `../02-data-preparation/index.md` → `../01-workflow/p00-data.md`.
- `docs/appendices/C-python-environment-setup.md`: any `../0N-…/` link → the matching workflow page (`02-data-preparation` → `../01-workflow/p00-data.md`, `03-exploratory-analysis` → `../01-workflow/p03-exploratory-diagnostics.md`, `04-frequency-domain` → `../01-workflow/p05-representation/index.md`, `05-modelling` → `../01-workflow/p06-mean-model-class.md`, `06-feature-extraction` → `../01-workflow/p02-purpose/07-feature-extraction-classification.md`, `07-validation-deployment` → `../01-workflow/p11-validation-deployment.md`).
- `docs/index.md`: replace the whole `## Book Structure` section (from the heading to the line before `## Quick Start`) with:

```markdown
## Book Structure

The manual has three axes. Read Foundations first; follow the Workflow when you have data in hand; open Reference chapters when the workflow sends you there.

### Foundations

- **[The logic of statistical analysis](00-foundations/logic-of-statistical-analysis.md)**: model class, estimator, test
- **[Do you need time series analysis?](00-foundations/do-you-need-time-series-analysis.md)**: the gateway flowchart from OLS to richer models
- **[OLS assumptions and how time series violates them](00-foundations/ols-assumptions.md)**
- **[Stochastic processes](00-foundations/stochastic-processes.md)**: the roots of every error-process choice
- **[Asymptotics for dependent data](00-foundations/asymptotics.md)**

### Workflow

The [general flowchart](01-workflow/index.md) runs through twelve phases, P0 to P11, from raw data to a deployed model. Two of its phases are decision indexes: [Purpose](01-workflow/p02-purpose/index.md) (ten analytical goals) and [Representation](01-workflow/p05-representation/index.md) (six mathematical representations). The [error-process phase](01-workflow/p07-error-process.md) is where stochastic-process theory meets residual modelling.

### Reference

Thirty-four areas, listed under *Techniques This Book Covers* below, each with its own chapter group under Reference. Every leaf node of a workflow sub-diagram opens one reference section.

### Reference Materials

- **[Appendices](appendices/index.md)**: link indexes for tests, datasets, software, and the Python environment
```

- `docs/index.md` Quick Start: in the "New to Time Series" tab replace the four numbered steps with:
```markdown
    1. Read [Foundations](00-foundations/logic-of-statistical-analysis.md) to understand the model / estimator / test framework
    2. Open the [General Flowchart](01-workflow/index.md) and follow the phases with your own data
    3. Click any node to reach the section that teaches it
    4. Return to [Stochastic processes](00-foundations/stochastic-processes.md) whenever a residual-modelling choice needs its why
```
In the "Want Examples" tab, change `Code directory (WIP)` to `Code examples accompany each reference section as they are written`.

- `docs/appendices/index.md`: replace the `## Contents` list with:
```markdown
## Contents

Appendix pages are link indexes. They point at the section where each item is developed and carry no explanations of their own.

- [Appendix A: OLS Estimation, Derivation and Properties](A-ols-derivation.md)
- [Python Environment Setup](C-python-environment-setup.md)
- Statistical tests index: pending, generated from the inventory in Plan B
- Datasets and resources: pending
- Software ecosystem: pending
```

- [ ] **Step 3: Build**

Run: `venv/bin/mkdocs build 2>&1 | grep WARNING | grep -v "audit error"; echo "---"; grep -rn '0[2-7]-[a-z-]*/' docs/index.md docs/00-foundations docs/appendices | grep -v reference/`
Expected: no non-audit warnings; the grep prints nothing.

- [ ] **Step 4: Commit**

```bash
git add -A docs mkdocs.yml
git commit -m "refactor: fold the six topic directories into the workflow and repoint the landing page"
```

---

### Task 8: Master diagram, P1 / P2 / P5 / P7 sub-diagrams, branch stubs, inventory

**Files:**
- Modify: `docs/01-workflow/index.md`, `p01-data-type-gate.md`, `p02-purpose/index.md`, `p05-representation/index.md`, `p07-error-process.md`
- Modify: `docs/reference/16-count-categorical/index.md`, `17-point-processes/index.md`, `15-continuous-time/index.md`, `14-functional-high-frequency/index.md`, `20-spatio-temporal/index.md`, `32-panel-time-series/index.md` (B1–B6 entry stubs)
- Create: `docs/flowcharts/inventory.yml`
- Run: `scripts/scaffold_stubs.py`

**Interfaces:**
- Produces: node IDs `P0`–`P11`, `B1`–`B7`, `P1_*`, `P2_*`, `P5_*`, `P7_*`, `F_*` used by the inventory and by Plan B.

Paste the brand `classDef` block (from `DESIGN-SYSTEM.md`, "The `classDef` blocks", brand-default set) verbatim at the foot of every diagram below where `<<CLASSDEFS>>` appears:

```text
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

- [ ] **Step 1: Master diagram**

In `docs/01-workflow/index.md` replace the "Diagram pending" admonition under `## Master diagram` with:

````markdown
```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    MASTER_START(["Raw time-stamped data"]) --> P0["P0 Data acquisition and cleaning"]
    P0 --> P1["P1 Data-type gate"]
    P1 --> P2["P2 Purpose"]
    P2 --> P3["P3 Exploratory diagnostics"]
    P3 --> P4["P4 Transformations"]
    P4 --> P5["P5 Representation selection"]
    P5 --> P6["P6 Conditional-mean model class"]
    P6 --> P7["P7 Error-process specification"]
    P7 --> P8["P8 Estimation"]
    P8 --> P9["P9 Diagnostics and model selection"]
    P9 --> P10["P10 Inference and interpretation"]
    P10 --> P11["P11 Validation and deployment"]
    P9 -.->|"Mean misspecified"| P6
    P9 -.->|"Innovations misspecified"| P7
    P11 -.->|"Drift detected"| P8
    P11 --> MASTER_END(["Validated model deployed"])
    class MASTER_START,MASTER_END terminator
    class P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11 process
<<CLASSDEFS>>
```
````

- [ ] **Step 2: P1 sub-diagram**

In `docs/01-workflow/p01-data-type-gate.md` replace the "Diagram pending" admonition with:

````markdown
```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P1_IN(["Prepared series from P0"]) --> P1_VALUE_TYPE{"Value type?"}
    P1_VALUE_TYPE -->|"Continuous"| P1_SAMPLING{"Sampling?"}
    P1_VALUE_TYPE -->|"Counts, categorical, compositional"| B1[["B1 Counts and categorical"]]
    P1_VALUE_TYPE -->|"Curves"| B4[["B4 Functional"]]
    P1_VALUE_TYPE -->|"Event times"| B2[["B2 Event times"]]
    P1_SAMPLING -->|"Regular"| P1_STRUCTURE{"Cross-section?"}
    P1_SAMPLING -->|"Irregular"| B3[["B3 Irregular sampling and continuous time"]]
    P1_SAMPLING -->|"Mixed frequency"| P1_MIXED_FREQ_FLAG["Set flag: mixed frequency"]
    P1_MIXED_FREQ_FLAG --> P1_STRUCTURE
    P1_STRUCTURE -->|"Single"| P1_OUT
    P1_STRUCTURE -->|"Few related"| P1_MULTIVARIATE_FLAG["Set flag: multivariate"]
    P1_STRUCTURE -->|"Many similar"| B7["B7 Many similar series"]
    P1_STRUCTURE -->|"Wide panel"| B6[["B6 Wide panel"]]
    P1_STRUCTURE -->|"Spatial or network"| B5[["B5 Spatial and network"]]
    P1_MULTIVARIATE_FLAG --> P1_OUT
    B7 --> P1_GLOBAL_FLAG["Set flag: global model"]
    P1_GLOBAL_FLAG --> P1_OUT
    B3 -.->|"Resample"| P0[["P0 Data acquisition and cleaning"]]
    B3 --> P5[["P5 Representation selection"]]
    B4 --> P5
    B1 --> P8[["P8 Estimation"]]
    B2 --> P8
    B5 --> P8
    B6 --> P8
    P1_OUT(["To P2 Purpose"])
    class P1_IN,P1_OUT terminator
    class P1_VALUE_TYPE,P1_SAMPLING,P1_STRUCTURE decision
    class P1_MIXED_FREQ_FLAG,P1_MULTIVARIATE_FLAG,P1_GLOBAL_FLAG,B7 process
    class B1,B2,B3,B4,B5,B6,P0,P5,P8 ref
<<CLASSDEFS>>
```

## Routing variables

| Variable | Values | Effect |
|---|---|---|
| Value type | continuous / counts / categorical or ordinal / compositional / curves / event times | Continuous stays on the spine; counts, categorical and compositional enter B1; curves enter B4; event times enter B2 |
| Sampling | regular / irregular / mixed frequency | Irregular enters B3; mixed frequency sets a flag read by P6 and P10 |
| Cross-sectional structure | single / few related / many similar / wide panel / spatial or network | Few related sets the multivariate flag; many similar enters B7; wide panel enters B6; spatial enters B5 |

## Branches

| Branch | Chapter | Rejoins |
|---|---|---|
| B1 Counts and categorical | [Count and Categorical](../reference/16-count-categorical/index.md) | P8 |
| B2 Event times | [Point Processes](../reference/17-point-processes/index.md) | P8 |
| B3 Irregular sampling and continuous time | [Continuous-Time Models](../reference/15-continuous-time/index.md) | P5 or P8; may resample back to P0 |
| B4 Functional | [Functional and High-Frequency](../reference/14-functional-high-frequency/index.md) | P5 |
| B5 Spatial and network | [Spatio-Temporal Models](../reference/20-spatio-temporal/index.md) | P8 |
| B6 Wide panel | [Panel Time Series](../reference/32-panel-time-series/index.md) | P8, P10 |
| B7 Many similar series | this page | Stays on the spine with the global flag set |
````

- [ ] **Step 3: P2 and P5 selector diagrams**

In `docs/01-workflow/p02-purpose/index.md` replace the "Diagram pending" admonition under `## Purpose selector` with:

````markdown
```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_IN(["Series and flags from P1"]) --> P2_PURPOSE{"Purpose?"}
    P2_PURPOSE -->|"Predict"| P2_FORECASTING["1 Forecasting"]
    P2_PURPOSE -->|"Explain"| P2_CAUSAL["2 Causal and structural inference"]
    P2_PURPOSE -->|"Clean"| P2_SIGNAL["3 Signal extraction and denoising"]
    P2_PURPOSE -->|"Locate changes"| P2_CHANGE_POINT["4 Change-point detection"]
    P2_PURPOSE -->|"Flag unusual"| P2_ANOMALY["5 Anomaly and regime detection"]
    P2_PURPOSE -->|"Split"| P2_DECOMPOSITION["6 Decomposition"]
    P2_PURPOSE -->|"Label or group"| P2_FEATURES["7 Feature extraction, classification and clustering"]
    P2_PURPOSE -->|"Describe cycles"| P2_SPECTRAL["8 Spectral analysis"]
    P2_PURPOSE -->|"Identify a system"| P2_SYSTEM_ID["9 System identification"]
    P2_PURPOSE -->|"Generate paths"| P2_SIMULATION["10 Simulation and scenario generation"]
    P2_FORECASTING & P2_CAUSAL & P2_SIGNAL & P2_CHANGE_POINT & P2_ANOMALY --> P3[["P3 Exploratory diagnostics"]]
    P2_DECOMPOSITION & P2_FEATURES & P2_SPECTRAL & P2_SYSTEM_ID & P2_SIMULATION --> P3
    class P2_IN terminator
    class P2_PURPOSE decision
    class P2_FORECASTING,P2_CAUSAL,P2_SIGNAL,P2_CHANGE_POINT,P2_ANOMALY,P2_DECOMPOSITION,P2_FEATURES,P2_SPECTRAL,P2_SYSTEM_ID,P2_SIMULATION process
    class P3 ref
<<CLASSDEFS>>
```
````

In `docs/01-workflow/p05-representation/index.md` replace the "Diagram pending" admonition under `## Representation selector` with:

````markdown
```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_IN(["Transformed series from P4"]) --> P5_CHARACTER{"Dominant character?"}
    P5_CHARACTER -->|"Sequential dependence"| P5_TIME_DOMAIN["1 Time domain"]
    P5_CHARACTER -->|"Periodic"| P5_FREQUENCY_DOMAIN["2 Frequency domain"]
    P5_CHARACTER -->|"Spectrum changes over time"| P5_TIME_FREQUENCY["3 Time-frequency"]
    P5_CHARACTER -->|"Latent states, gaps"| P5_STATE_SPACE["4 State space"]
    P5_CHARACTER -->|"Curves"| P5_FUNCTIONAL["5 Functional"]
    P5_CHARACTER -->|"Instantaneous frequency"| P5_HILBERT["6 Hilbert and phase"]
    P5_TIME_DOMAIN & P5_FREQUENCY_DOMAIN & P5_TIME_FREQUENCY & P5_STATE_SPACE & P5_FUNCTIONAL & P5_HILBERT --> P6[["P6 Conditional-mean model class"]]
    class P5_IN terminator
    class P5_CHARACTER decision
    class P5_TIME_DOMAIN,P5_FREQUENCY_DOMAIN,P5_TIME_FREQUENCY,P5_STATE_SPACE,P5_FUNCTIONAL,P5_HILBERT process
    class P6 ref
<<CLASSDEFS>>
```
````

- [ ] **Step 4: P7 sub-diagram and question-order table**

In `docs/01-workflow/p07-error-process.md` replace the "Diagram pending" admonition with:

````markdown
The order of the questions is itself a derivation chain: each step's test assumes the previous step's structure has been removed. ARCH-LM assumes no serial correlation; distribution tests run on standardised residuals and assume the variance model is fixed; correlation tests run on each series' standardised residuals.

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_IN(["Residuals of the P6 mean model"]) --> P7_TYPE{"Innovation type?"}
    P7_TYPE -->|"Continuous"| P7_MEAN_TESTS["Test residual autocorrelation<br/>Ljung-Box, Breusch-Godfrey, ACF"]
    P7_TYPE -->|"Counts"| P7_COUNT_TESTS["Test overdispersion of count innovations"]
    P7_TYPE -->|"Event times"| P7_RESCALING["Time-rescaling check of event-time residuals"]
    P7_COUNT_TESTS --> P7_INGARCH["INGARCH and negative-binomial innovations"]
    P7_RESCALING --> P7_INTENSITY["Intensity misspecification"]
    P7_INGARCH & P7_INTENSITY --> P7_OUT
    P7_MEAN_TESTS --> P7_MEAN_DEP{"Mean dependence?"}
    P7_MEAN_DEP -->|"None"| P7_VAR_TESTS
    P7_MEAN_DEP -->|"Short memory"| P7_ARMA_ERRORS["Regression with ARMA errors"]
    P7_MEAN_DEP -->|"Slow decay"| P7_ARFIMA_ERRORS["ARFIMA errors"]
    P7_MEAN_DEP -.->|"Already ARMA: raise the order"| P6[["P6 Conditional-mean model class"]]
    P7_ARMA_ERRORS & P7_ARFIMA_ERRORS --> P7_VAR_TESTS["Test conditional heteroskedasticity<br/>ARCH-LM, McLeod-Li"]
    P7_VAR_TESTS --> P7_VAR_DEP{"Variance dependence?"}
    P7_VAR_DEP -->|"None"| P7_DIST_TESTS
    P7_VAR_DEP -->|"Present"| P7_VAR_TYPE{"Variance process?"}
    P7_VAR_TYPE -->|"Symmetric"| P7_GARCH["GARCH"]
    P7_VAR_TYPE -->|"Asymmetric"| P7_ASYM_GARCH["Asymmetric GARCH: EGARCH, GJR, TGARCH"]
    P7_VAR_TYPE -->|"Long memory"| P7_FIGARCH["FIGARCH"]
    P7_VAR_TYPE -->|"Persistence near one"| P7_IGARCH["IGARCH"]
    P7_VAR_TYPE -->|"Risk premium"| P7_GARCH_M["GARCH-in-mean"]
    P7_VAR_TYPE -->|"Latent variance"| P7_SV["Stochastic volatility"]
    P7_VAR_TYPE -->|"Realised measures"| P7_REALIZED["Realised measures: HAR-RV and Realized GARCH"]
    P7_GARCH & P7_ASYM_GARCH & P7_FIGARCH & P7_IGARCH --> P7_DIST_TESTS
    P7_GARCH_M & P7_SV & P7_REALIZED --> P7_DIST_TESTS["Test the distribution of standardised innovations<br/>Jarque-Bera, QQ, Hill, BNS"]
    P7_DIST_TESTS --> P7_DIST{"Distribution?"}
    P7_DIST -->|"Gaussian"| P7_GAUSSIAN["Gaussian innovations"]
    P7_DIST -->|"Heavy tails"| P7_HEAVY_TAILS["Heavy-tailed innovations: Student-t, GED, QMLE"]
    P7_DIST -->|"Skew"| P7_SKEWED["Skewed innovations"]
    P7_DIST -->|"Extreme tails"| P7_EVT["Extreme value theory for tails"]
    P7_DIST -->|"Jumps"| P7_JUMPS["Jump diffusion"]
    P7_GAUSSIAN & P7_HEAVY_TAILS & P7_SKEWED & P7_EVT & P7_JUMPS --> P7_REGIME_TESTS["Test for variance regimes<br/>ICSS, Markov-switching LR"]
    P7_REGIME_TESTS --> P7_REGIME{"Regimes?"}
    P7_REGIME -->|"None"| P7_MULTI
    P7_REGIME -->|"Present"| P7_MS_GARCH["Markov-switching GARCH and segmented variance"]
    P7_MS_GARCH --> P7_MULTI{"Several series?"}
    P7_MULTI -->|"No"| P7_OUT
    P7_MULTI -->|"Yes"| P7_CORR_TESTS["Test innovation correlation structure<br/>Engle-Sheppard, tail dependence"]
    P7_CORR_TESTS --> P7_CORR{"Correlation structure?"}
    P7_CORR -->|"Constant"| P7_CCC["Constant conditional correlation"]
    P7_CORR -->|"Time-varying"| P7_DCC["Dynamic conditional correlation and BEKK"]
    P7_CORR -->|"Non-Gaussian dependence"| P7_COPULA["Copula dependence"]
    P7_CCC & P7_DCC & P7_COPULA --> P7_OUT["Assemble the joint model<br/>mean + innovations"]
    P7_OUT --> P8[["P8 Estimation"]]
    F_WHITE_NOISE[["White noise, martingale difference, independence"]] -.- P7_MEAN_DEP
    F_WOLD[["Wold decomposition"]] -.- P7_ARMA_ERRORS
    F_LONG_MEMORY[["Long memory and hyperbolic decay"]] -.- P7_ARFIMA_ERRORS
    F_GARCH_STATIONARITY[["Stationarity conditions of GARCH"]] -.- P7_GARCH
    F_LATENT_FILTERING[["Latent processes and filtering"]] -.- P7_SV
    F_LEVY[["Brownian motion, Poisson jumps, Levy processes"]] -.- P7_JUMPS
    F_HMM[["Hidden Markov chains"]] -.- P7_MS_GARCH
    F_SKLAR[["Sklar's theorem"]] -.- P7_COPULA
    F_TIME_RESCALING[["Time-rescaling theorem"]] -.- P7_RESCALING
    class P7_IN terminator
    class P7_TYPE,P7_MEAN_DEP,P7_VAR_DEP,P7_VAR_TYPE,P7_DIST,P7_REGIME,P7_MULTI,P7_CORR decision
    class P7_MEAN_TESTS,P7_VAR_TESTS,P7_DIST_TESTS,P7_REGIME_TESTS,P7_CORR_TESTS,P7_COUNT_TESTS,P7_RESCALING,P7_OUT process
    class P7_ARMA_ERRORS,P7_ARFIMA_ERRORS,P7_GARCH,P7_ASYM_GARCH,P7_FIGARCH,P7_IGARCH,P7_GARCH_M,P7_SV,P7_REALIZED escalate
    class P7_GAUSSIAN good
    class P7_HEAVY_TAILS,P7_SKEWED,P7_EVT,P7_JUMPS,P7_MS_GARCH,P7_CCC,P7_DCC,P7_COPULA,P7_INGARCH,P7_INTENSITY escalate
    class P6,P8,F_WHITE_NOISE,F_WOLD,F_LONG_MEMORY,F_GARCH_STATIONARITY,F_LATENT_FILTERING,F_LEVY,F_HMM,F_SKLAR,F_TIME_RESCALING ref
<<CLASSDEFS>>
```

## Question order

| Step | Question | Tests | Branches |
|---|---|---|---|
| 1 | Mean dependence left? | Ljung-Box, Breusch-Godfrey, residual ACF | None: step 2. Short memory: ARMA errors. Slow decay: ARFIMA errors. Already ARMA and still dependent: back to P6 |
| 2 | Second-moment dependence? | ARCH-LM, McLeod-Li, squared-residual ACF | None: step 3. Present: step 2a |
| 2a | Which variance process? | Sign-bias test, squared-residual ACF decay, availability of high-frequency data | GARCH; EGARCH / GJR / TGARCH; FIGARCH; IGARCH; GARCH-in-mean; stochastic volatility; HAR-RV / Realized GARCH |
| 3 | Distribution of standardised innovations? | Jarque-Bera, QQ, Hill tail index, BNS jump test | Gaussian; Student-t / GED or QMLE; skewed-t; EVT; jump diffusion |
| 4 | Regimes in variance? | ICSS, Markov-switching LR | None: step 5. Present: MS-GARCH or segmented variance |
| 5 | Several series? | Engle-Sheppard constant-correlation test, tail dependence | CCC; DCC / BEKK; copula |
| 6 | Branch data types | Overdispersion tests; time-rescaling KS test | Counts: INGARCH / negative binomial. Event times: intensity misspecification |

Terminals name **model → estimator → inference**; for example, regression + ARMA errors + GARCH-t → joint MLE → asymptotic-normal standard errors.

## Part 0 hooks

| Branch | Stochastic-process concept | Chain link |
|---|---|---|
| White noise terminal | White noise, martingale difference, independence | Ljung-Box tests only uncorrelatedness and cannot detect ARCH, because ARCH is a martingale difference but not independent |
| ARMA errors | Wold decomposition | Any covariance-stationary process is MA(∞); ARMA is its rational approximation |
| ARFIMA errors | Long memory, hyperbolic decay | Why no finite-order ARMA reproduces it |
| GARCH | Weak stationarity α + β < 1; strict stationarity E[log(α z² + β)] < 0 | IGARCH is strictly stationary with infinite unconditional variance |
| Stochastic volatility | Latent process, filtering | Why the likelihood has no closed form |
| Jump diffusion | Brownian motion, Poisson jumps, Levy processes | Quadratic variation splits into continuous and jump parts |
| Markov switching | Hidden Markov chain | Hamilton filter |
| Event times | Conditional intensity, time-rescaling theorem | Under the true intensity, rescaled event times form a unit Poisson process |
| Copula | Sklar's theorem | Marginals and dependence separate |

## Relation to P9

P7 is specified once. After joint estimation in P8, P9 re-runs steps 1 to 5 on the complete model and loops back to P6 or P7 on failure.
````

- [ ] **Step 5: Branch entry stubs**

Append to each listed reference landing page, after its intro paragraph (replace `Bn`, the label and the dir as given):

| File | Diagram |
|---|---|
| `docs/reference/16-count-categorical/index.md` | `B1["B1 Counts and categorical"]` |
| `docs/reference/17-point-processes/index.md` | `B2["B2 Event times"]` |
| `docs/reference/15-continuous-time/index.md` | `B3["B3 Irregular sampling and continuous time"]` |
| `docs/reference/14-functional-high-frequency/index.md` | `B4["B4 Functional"]` |
| `docs/reference/20-spatio-temporal/index.md` | `B5["B5 Spatial and network"]` |
| `docs/reference/32-panel-time-series/index.md` | `B6["B6 Wide panel"]` |

Template (shown for B1):

````markdown
## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1["B1 Counts and categorical"] --> B1_PENDING(["Sub-diagram drawn in Plan B"])
    class B1 process
    class B1_PENDING terminator
<<CLASSDEFS>>
```
````

- [ ] **Step 6: Write the inventory**

Create `docs/flowcharts/inventory.yml`:

```yaml
# Leaf-node inventory. One row per leaf (rectangle that is not a ref and not a *_FLAG).
# Rows with phase F are foundation sections: they have no diagram definition and must be
# referenced by at least one ref node. See planning/2026-10-06-flowchart-framework-design.md §10.4.
nodes:
  # ---- master phases
  - {id: P0,  label: "P0: Data acquisition and cleaning",  phase: MASTER, areas: [31],                 section: "01-workflow/p00-data.md#p0-data-acquisition-and-cleaning"}
  - {id: P1,  label: "P1: Data-type gate",                 phase: MASTER, areas: [31],                 section: "01-workflow/p01-data-type-gate.md#p1-data-type-gate"}
  - {id: P2,  label: "P2: Purpose",                        phase: MASTER, areas: [19, 25, 30],         section: "01-workflow/p02-purpose/index.md#p2-purpose"}
  - {id: P3,  label: "P3: Exploratory diagnostics",        phase: MASTER, areas: [2, 5, 28, 29, 30],   section: "01-workflow/p03-exploratory-diagnostics.md#p3-exploratory-diagnostics"}
  - {id: P4,  label: "P4: Transformations",                phase: MASTER, areas: [2, 3, 29, 30],       section: "01-workflow/p04-transformations.md#p4-transformations"}
  - {id: P5,  label: "P5: Representation selection",       phase: MASTER, areas: [13, 33],             section: "01-workflow/p05-representation/index.md#p5-representation-selection"}
  - {id: P6,  label: "P6: Conditional-mean model class",   phase: MASTER, areas: [3, 6, 8, 9, 11, 12, 18, 27, 33], section: "01-workflow/p06-mean-model-class.md#p6-conditional-mean-model-class"}
  - {id: P7,  label: "P7: Error-process specification",    phase: MASTER, areas: [10],                 section: "01-workflow/p07-error-process.md#p7-error-process-specification"}
  - {id: P8,  label: "P8: Estimation",                     phase: MASTER, areas: [4, 12],              section: "01-workflow/p08-estimation.md#p8-estimation"}
  - {id: P9,  label: "P9: Diagnostics and model selection", phase: MASTER, areas: [5, 6],              section: "01-workflow/p09-diagnostics-selection.md#p9-diagnostics-and-model-selection"}
  - {id: P10, label: "P10: Inference and interpretation",  phase: MASTER, areas: [21, 22, 34],         section: "01-workflow/p10-inference.md#p10-inference-and-interpretation"}
  - {id: P11, label: "P11: Validation and deployment",     phase: MASTER, areas: [6, 23, 34],          section: "01-workflow/p11-validation-deployment.md#p11-validation-and-deployment"}
  # ---- P1 gate and branch entries
  - {id: B1, label: "B1 Counts and categorical",                phase: B1, areas: [16],         section: "reference/16-count-categorical/index.md#b1-counts-and-categorical"}
  - {id: B2, label: "B2 Event times",                           phase: B2, areas: [17, 14, 26], section: "reference/17-point-processes/index.md#b2-event-times"}
  - {id: B3, label: "B3 Irregular sampling and continuous time", phase: B3, areas: [15, 11, 13], section: "reference/15-continuous-time/index.md#b3-irregular-sampling-and-continuous-time"}
  - {id: B4, label: "B4 Functional",                            phase: B4, areas: [14],         section: "reference/14-functional-high-frequency/index.md#b4-functional"}
  - {id: B5, label: "B5 Spatial and network",                   phase: B5, areas: [20],         section: "reference/20-spatio-temporal/index.md#b5-spatial-and-network"}
  - {id: B6, label: "B6 Wide panel",                            phase: B6, areas: [32],         section: "reference/32-panel-time-series/index.md#b6-wide-panel"}
  - {id: B7, label: "B7 Many similar series",                   phase: P1, areas: [22, 18, 34, 19], section: "01-workflow/p01-data-type-gate.md#b7-many-similar-series"}
  # ---- P2 purposes
  - {id: P2_FORECASTING,   label: "Purpose 1: Forecasting",                                     phase: P2, areas: [22], section: "01-workflow/p02-purpose/01-forecasting.md#purpose-1-forecasting"}
  - {id: P2_CAUSAL,        label: "Purpose 2: Causal and structural inference",                 phase: P2, areas: [21], section: "01-workflow/p02-purpose/02-causal-inference.md#purpose-2-causal-and-structural-inference"}
  - {id: P2_SIGNAL,        label: "Purpose 3: Signal extraction and denoising",                 phase: P2, areas: [13], section: "01-workflow/p02-purpose/03-signal-extraction.md#purpose-3-signal-extraction-and-denoising"}
  - {id: P2_CHANGE_POINT,  label: "Purpose 4: Change-point detection",                          phase: P2, areas: [30, 19], section: "01-workflow/p02-purpose/04-change-point-detection.md#purpose-4-change-point-detection"}
  - {id: P2_ANOMALY,       label: "Purpose 5: Anomaly and regime detection",                    phase: P2, areas: [19], section: "01-workflow/p02-purpose/05-anomaly-regime-detection.md#purpose-5-anomaly-and-regime-detection"}
  - {id: P2_DECOMPOSITION, label: "Purpose 6: Decomposition",                                   phase: P2, areas: [3, 29], section: "01-workflow/p02-purpose/06-decomposition.md#purpose-6-decomposition"}
  - {id: P2_FEATURES,      label: "Purpose 7: Feature extraction, classification and clustering", phase: P2, areas: [19], section: "01-workflow/p02-purpose/07-feature-extraction-classification.md#purpose-7-feature-extraction-classification-and-clustering"}
  - {id: P2_SPECTRAL,      label: "Purpose 8: Spectral analysis",                               phase: P2, areas: [13], section: "01-workflow/p02-purpose/08-spectral-analysis.md#purpose-8-spectral-analysis"}
  - {id: P2_SYSTEM_ID,     label: "Purpose 9: System identification",                           phase: P2, areas: [33], section: "01-workflow/p02-purpose/09-system-identification.md#purpose-9-system-identification"}
  - {id: P2_SIMULATION,    label: "Purpose 10: Simulation and scenario generation",             phase: P2, areas: [25], section: "01-workflow/p02-purpose/10-simulation.md#purpose-10-simulation-and-scenario-generation"}
  # ---- P5 representations
  - {id: P5_TIME_DOMAIN,      label: "Representation 1: Time domain",        phase: P5, areas: [3, 9],  section: "01-workflow/p05-representation/01-time-domain.md#representation-1-time-domain"}
  - {id: P5_FREQUENCY_DOMAIN, label: "Representation 2: Frequency domain",   phase: P5, areas: [13],    section: "01-workflow/p05-representation/02-frequency-domain.md#representation-2-frequency-domain"}
  - {id: P5_TIME_FREQUENCY,   label: "Representation 3: Time-frequency",     phase: P5, areas: [13],    section: "01-workflow/p05-representation/03-time-frequency.md#representation-3-time-frequency"}
  - {id: P5_STATE_SPACE,      label: "Representation 4: State space",        phase: P5, areas: [11],    section: "01-workflow/p05-representation/04-state-space.md#representation-4-state-space"}
  - {id: P5_FUNCTIONAL,       label: "Representation 5: Functional",         phase: P5, areas: [14],    section: "01-workflow/p05-representation/05-functional.md#representation-5-functional"}
  - {id: P5_HILBERT,          label: "Representation 6: Hilbert and phase",  phase: P5, areas: [13],    section: "01-workflow/p05-representation/06-hilbert-phase.md#representation-6-hilbert-and-phase"}
  # ---- P7 procedural leaves (live in the phase page)
  - {id: P7_MEAN_TESTS,   label: "Test residual autocorrelation",                       phase: P7, areas: [5, 10], section: "01-workflow/p07-error-process.md#test-residual-autocorrelation"}
  - {id: P7_VAR_TESTS,    label: "Test conditional heteroskedasticity",                 phase: P7, areas: [5, 10], section: "01-workflow/p07-error-process.md#test-conditional-heteroskedasticity"}
  - {id: P7_DIST_TESTS,   label: "Test the distribution of standardised innovations",   phase: P7, areas: [5, 10], section: "01-workflow/p07-error-process.md#test-the-distribution-of-standardised-innovations"}
  - {id: P7_REGIME_TESTS, label: "Test for variance regimes",                           phase: P7, areas: [10, 30], section: "01-workflow/p07-error-process.md#test-for-variance-regimes"}
  - {id: P7_CORR_TESTS,   label: "Test innovation correlation structure",               phase: P7, areas: [10, 9],  section: "01-workflow/p07-error-process.md#test-innovation-correlation-structure"}
  - {id: P7_COUNT_TESTS,  label: "Test overdispersion of count innovations",            phase: P7, areas: [16],    section: "01-workflow/p07-error-process.md#test-overdispersion-of-count-innovations"}
  - {id: P7_RESCALING,    label: "Time-rescaling check of event-time residuals",        phase: P7, areas: [17],    section: "01-workflow/p07-error-process.md#time-rescaling-check-of-event-time-residuals"}
  - {id: P7_OUT,          label: "Assemble the joint model",                            phase: P7, areas: [10, 4], section: "01-workflow/p07-error-process.md#assemble-the-joint-model"}
  # ---- P7 model-family leaves (live in reference chapters)
  - {id: P7_ARMA_ERRORS,   label: "Regression with ARMA errors",                        phase: P7, areas: [27, 3],  section: "reference/27-regression-time-series/index.md#regression-with-arma-errors"}
  - {id: P7_ARFIMA_ERRORS, label: "ARFIMA errors",                                      phase: P7, areas: [7],      section: "reference/07-long-memory/index.md#arfima-errors"}
  - {id: P7_GARCH,         label: "GARCH",                                              phase: P7, areas: [10],     section: "reference/10-volatility/index.md#garch"}
  - {id: P7_ASYM_GARCH,    label: "Asymmetric GARCH: EGARCH, GJR, TGARCH",              phase: P7, areas: [10],     section: "reference/10-volatility/index.md#asymmetric-garch-egarch-gjr-tgarch"}
  - {id: P7_FIGARCH,       label: "FIGARCH",                                            phase: P7, areas: [10, 7],  section: "reference/10-volatility/index.md#figarch"}
  - {id: P7_IGARCH,        label: "IGARCH",                                             phase: P7, areas: [10],     section: "reference/10-volatility/index.md#igarch"}
  - {id: P7_GARCH_M,       label: "GARCH-in-mean",                                      phase: P7, areas: [10],     section: "reference/10-volatility/index.md#garch-in-mean"}
  - {id: P7_SV,            label: "Stochastic volatility",                              phase: P7, areas: [10, 11], section: "reference/10-volatility/index.md#stochastic-volatility"}
  - {id: P7_REALIZED,      label: "Realised measures: HAR-RV and Realized GARCH",       phase: P7, areas: [10, 14], section: "reference/10-volatility/index.md#realised-measures-har-rv-and-realized-garch"}
  - {id: P7_GAUSSIAN,      label: "Gaussian innovations",                               phase: P7, areas: [10, 4],  section: "reference/10-volatility/index.md#gaussian-innovations"}
  - {id: P7_HEAVY_TAILS,   label: "Heavy-tailed innovations: Student-t, GED, QMLE",     phase: P7, areas: [10, 4],  section: "reference/10-volatility/index.md#heavy-tailed-innovations-student-t-ged-qmle"}
  - {id: P7_SKEWED,        label: "Skewed innovations",                                 phase: P7, areas: [10],     section: "reference/10-volatility/index.md#skewed-innovations"}
  - {id: P7_EVT,           label: "Extreme value theory for tails",                     phase: P7, areas: [10],     section: "reference/10-volatility/index.md#extreme-value-theory-for-tails"}
  - {id: P7_JUMPS,         label: "Jump diffusion",                                     phase: P7, areas: [15, 10], section: "reference/15-continuous-time/index.md#jump-diffusion"}
  - {id: P7_MS_GARCH,      label: "Markov-switching GARCH and segmented variance",      phase: P7, areas: [10, 30], section: "reference/10-volatility/index.md#markov-switching-garch-and-segmented-variance"}
  - {id: P7_CCC,           label: "Constant conditional correlation",                   phase: P7, areas: [10, 9],  section: "reference/10-volatility/index.md#constant-conditional-correlation"}
  - {id: P7_DCC,           label: "Dynamic conditional correlation and BEKK",           phase: P7, areas: [10, 9],  section: "reference/10-volatility/index.md#dynamic-conditional-correlation-and-bekk"}
  - {id: P7_COPULA,        label: "Copula dependence",                                  phase: P7, areas: [10],     section: "reference/10-volatility/index.md#copula-dependence"}
  - {id: P7_INGARCH,       label: "INGARCH and negative-binomial innovations",          phase: P7, areas: [16],     section: "reference/16-count-categorical/index.md#ingarch-and-negative-binomial-innovations"}
  - {id: P7_INTENSITY,     label: "Intensity misspecification",                         phase: P7, areas: [17],     section: "reference/17-point-processes/index.md#intensity-misspecification"}
  # ---- foundation sections referenced from P7 (phase F: no diagram definition)
  - {id: F_WHITE_NOISE,        label: "White noise, martingale difference, independence", phase: F, areas: [1], section: "00-foundations/stochastic-processes.md#white-noise-martingale-difference-independence"}
  - {id: F_WOLD,               label: "Wold decomposition",                              phase: F, areas: [1], section: "00-foundations/stochastic-processes.md#wold-decomposition"}
  - {id: F_LONG_MEMORY,        label: "Long memory and hyperbolic decay",                phase: F, areas: [1, 7], section: "00-foundations/stochastic-processes.md#long-memory-and-hyperbolic-decay"}
  - {id: F_GARCH_STATIONARITY, label: "Stationarity conditions of GARCH",                phase: F, areas: [1, 10], section: "00-foundations/stochastic-processes.md#stationarity-conditions-of-garch"}
  - {id: F_LATENT_FILTERING,   label: "Latent processes and filtering",                  phase: F, areas: [1, 11], section: "00-foundations/stochastic-processes.md#latent-processes-and-filtering"}
  - {id: F_LEVY,               label: "Brownian motion, Poisson jumps, Levy processes",  phase: F, areas: [1, 15], section: "00-foundations/stochastic-processes.md#brownian-motion-poisson-jumps-levy-processes"}
  - {id: F_HMM,                label: "Hidden Markov chains",                            phase: F, areas: [1, 8],  section: "00-foundations/stochastic-processes.md#hidden-markov-chains"}
  - {id: F_SKLAR,              label: "Sklar's theorem",                                 phase: F, areas: [1, 10], section: "00-foundations/stochastic-processes.md#sklars-theorem"}
  - {id: F_TIME_RESCALING,     label: "Time-rescaling theorem",                          phase: F, areas: [1, 17], section: "00-foundations/stochastic-processes.md#time-rescaling-theorem"}
```

- [ ] **Step 7: Scaffold the pending sections and run the audit**

Run:
```bash
venv/bin/python scripts/scaffold_stubs.py
venv/bin/python scripts/audit_flowcharts.py; echo "exit $?"
```
Expected: the scaffold appends pending headings to the P7 page, the reference landing pages and `stochastic-processes.md` (no `create` actions: every target file exists). The audit reports only glossary findings (the glossary is migrated in Task 9) and `exit 1`. There must be no `leaf … has no inventory row`, `ref … has no definition`, `anchor … not found` or `already defined` lines. If a heading slug disagrees with an inventory anchor, fix the inventory anchor to the slug the scaffold produced.

- [ ] **Step 8: Build**

Run: `venv/bin/mkdocs build 2>&1 | grep WARNING | grep -v "audit error"; echo "---"`
Expected: no non-audit warnings.

- [ ] **Step 9: Commit**

```bash
git add docs/01-workflow docs/reference docs/00-foundations/stochastic-processes.md docs/flowcharts/inventory.yml
git commit -m "feat: master diagram, P1/P2/P5/P7 sub-diagrams, branch stubs and the leaf inventory"
```

---

### Task 9: Glossary — schema migration, drawer blocks, drawer-to-drawer navigation

**Files:**
- Move/modify: `docs/glossary/00-introduction.yml` → `00-foundations.yml`; `02-data-preparation.yml` → `p00-data.yml`; `03-exploratory-analysis.yml` → split into `00-foundations.yml`, `p03-exploratory-diagnostics.yml`, `p04-transformations.yml`, `p09-diagnostics-selection.yml`; `04-frequency-domain.yml` → `13-spectral-analysis.yml`; `05-modelling.yml` → `03-classical.yml`
- Modify: `docs/00-foundations/stochastic-processes.md`, `docs/reference/04-estimation/index.md` (manual root headings)
- Replace: `docs/javascripts/glossary.js`
- Modify: `docs/stylesheets/glossary.css` (append)

**Interfaces:**
- Consumes: `glossary/index.yml` written by the hook (Task 6); `reference` values as `path.md#anchor`.
- Produces: term fields `derivation`, `depends_on`, `foundation`; drawer blocks "Why it holds", "Rests on", "First developed in"; CSS classes `.glossary-chip`, `.glossary-back`, `.glossary-crumbs`.

- [ ] **Step 1: Rename and re-home the YAML files**

```bash
git mv docs/glossary/00-introduction.yml docs/glossary/00-foundations.yml
git mv docs/glossary/02-data-preparation.yml docs/glossary/p00-data.yml
git mv docs/glossary/04-frequency-domain.yml docs/glossary/13-spectral-analysis.yml
git mv docs/glossary/05-modelling.yml docs/glossary/03-classical.yml
```
Then split `docs/glossary/03-exploratory-analysis.yml` by hand: move the term blocks whose `reference` contains `01-stationarity-concept` or `06-white-noise` into `00-foundations.yml`; the blocks whose `reference` contains `03-unit-root-tests` or `05-acf-pacf` into a new `p03-exploratory-diagnostics.yml`; the block whose `reference` contains `04-differencing` into a new `p04-transformations.yml`; the block whose `reference` contains `06-ljung-box-test` into a new `p09-diagnostics-selection.yml`. Each new file starts with `# Glossary: <page title>\n\nterms:\n`. Delete the emptied `03-exploratory-analysis.yml` with `git rm`.

- [ ] **Step 2: Convert every `reference` to a source path that exists**

Apply these substitutions to the `reference:` lines (the Task 7a `sed` already turned `00-introduction` into `00-foundations` and `overview.html` into `ols-assumptions.html`):

| Old `reference` contains | New `reference` |
|---|---|
| `00-foundations/ols-assumptions.html#the-5-classical-…` | `00-foundations/ols-assumptions.md#the-5-classical-ols-assumptions-and-how-time-series-violates-them` |
| `00-foundations/do-you-need-time-series-analysis.html#feature-engineering-vs-time-series-modelling` | `00-foundations/do-you-need-time-series-analysis.md#feature-engineering-vs-time-series-modelling` |
| `00-foundations/logic-of-statistical-analysis.html#ordinary-least-squares-ols` | `00-foundations/logic-of-statistical-analysis.md#ordinary-least-squares-ols` |
| `02-data-preparation/…` (all four) | `01-workflow/p00-data.md#p0-data-acquisition-and-cleaning` |
| `03-exploratory-analysis/01-stationarity-concept.html` | `00-foundations/stochastic-processes.md#stochastic-processes` |
| `03-exploratory-analysis/06-white-noise.html` | `00-foundations/stochastic-processes.md#white-noise-martingale-difference-independence` |
| `03-exploratory-analysis/03-unit-root-tests.html#…`, `05-acf-pacf.html#…` | `01-workflow/p03-exploratory-diagnostics.md#p3-exploratory-diagnostics` |
| `03-exploratory-analysis/04-differencing.html` | `01-workflow/p04-transformations.md#p4-transformations` |
| `03-exploratory-analysis/06-ljung-box-test.html` | `01-workflow/p09-diagnostics-selection.md#p9-diagnostics-and-model-selection` |
| `04-frequency-domain/…` (all three) | `reference/13-spectral-analysis/index.md#13-spectral-analysis` |
| `05-modelling/01-arima.html` | `reference/03-classical/index.md#3-classical-models` |

These phase-page anchors are temporary homes; Plan B re-points each term to its own section when the section exists.

Add `foundation: true` to the terms `i.i.d`, `Stationarity` and `White Noise` (match the exact `term:` strings in the files).

- [ ] **Step 3: Add the root headings that are not inventory leaves**

Append to `docs/00-foundations/stochastic-processes.md` (after the scaffolded sections):

```markdown

## Probability density

!!! note "Section pending"
    Root of the joint-density chain: probability per unit volume; why continuous variables need densities.

## Independence

!!! note "Section pending"
    Root: the joint distribution factorises into marginals; relation to uncorrelatedness and martingale differences.

## Kolmogorov extension theorem

!!! note "Section pending"
    Root: a consistent family of finite-dimensional distributions determines the law of a process.

## KL divergence

!!! note "Section pending"
    Root: maximising average log-likelihood minimises Kullback-Leibler divergence to the truth.
```

Append to `docs/reference/04-estimation/index.md`:

```markdown

## Maximum likelihood

!!! note "Section pending"
    Home of the MLE chain: MLE, likelihood, joint density, chain rule, prediction-error decomposition, log and the law of large numbers, stationarity and ergodicity.

## Joint density

!!! note "Section pending"
    Home of the term *Joint density*; its derivation chain is in the glossary drawer.
```

- [ ] **Step 4: Add the root terms and the worked example to `00-foundations.yml`**

Append under `terms:`:

```yaml
  - term: "Probability density"
    definition: "Probability per unit volume. For a continuous variable the probability of any exact value is zero; the density is the limit of the probability of a small neighbourhood divided by its volume."
    foundation: true
    reference: "00-foundations/stochastic-processes.md#probability-density"

  - term: "Independence"
    definition: "Random variables are independent when their joint distribution equals the product of their marginal distributions. Independence implies uncorrelatedness; the converse fails."
    foundation: true
    reference: "00-foundations/stochastic-processes.md#independence"

  - term: "Kolmogorov extension theorem"
    definition: "A consistent family of finite-dimensional joint distributions determines a unique probability law for the whole stochastic process. This is what makes it legitimate to define a model class as a family of distributions for the entire sequence."
    foundation: true
    reference: "00-foundations/stochastic-processes.md#kolmogorov-extension-theorem"

  - term: "KL divergence"
    definition: "The Kullback-Leibler divergence from a true distribution to a model distribution is the expected log-ratio of their densities under the truth. It is non-negative and zero only when the two coincide."
    foundation: true
    reference: "00-foundations/stochastic-processes.md#kl-divergence"

  - term: "Law of large numbers"
    definition: "A sample average converges to the corresponding expectation as the sample grows. For dependent data the result needs stationarity and ergodicity (or mixing) in place of independence."
    foundation: true
    reference: "00-foundations/asymptotics.md#law-of-large-numbers"

  - term: "Joint density"
    definition: "The probability per unit volume of the whole sample (y_1, ..., y_T) regarded as one point in R^T."
    derivation: |
      1. The T observations form one point in $\mathbb{R}^T$. The joint density $p(y_1, \ldots, y_T; \theta)$ is the probability per unit volume near that point. A density is used because a continuous variable takes any exact value with probability zero; only "falls in a small neighbourhood" has positive probability, and dividing by the neighbourhood's volume gives the density. The volume factor does not depend on $\theta$, so it does not move the argmax.
      2. The object must be joint because the information about $\theta$ sits in the relations between observations. In AR(1), $\phi$ appears only in the conditional distribution of $y_t$ given $y_{t-1}$; the marginal $\mathcal{N}(0, \sigma^2/(1-\phi^2))$ confounds $\phi$ with $\sigma$. Using marginals alone discards the part being estimated.
      3. A process has a joint distribution to speak of because of the Kolmogorov extension theorem: a consistent family of finite-dimensional joint distributions determines the law of the whole process. This is also what makes the model-class definition "a family of distributions indexed by parameters" legitimate.
      4. Density and likelihood are one function read two ways. Fix $\theta$ and vary $y$: a density, integrating to one over $y$. Fix the observed $y$ and vary $\theta$: a likelihood, which does not integrate to one over $\theta$, so it is not a probability distribution of $\theta$. Adding a prior makes it one; that is the link to Bayesian estimation.
      5. "Highest data density" means "most reasonable $\theta$" because $\frac{1}{T}\log L(\theta) \to \mathbb{E}[\log p(y; \theta)]$, and maximising that minimises $\mathrm{KL}(\text{truth} \,\|\, p_\theta)$. MLE picks the model closest to the truth in KL divergence, even when the model class is wrong (the QMLE pseudo-true value).
    depends_on: ["Probability density", "Independence", "Kolmogorov extension theorem", "KL divergence", "Law of large numbers"]
    reference: "reference/04-estimation/index.md#joint-density"
```

- [ ] **Step 5: Run the audit and the strict build**

Run:
```bash
venv/bin/python scripts/audit_flowcharts.py; echo "exit $?"
venv/bin/mkdocs build --strict 2>&1 | tail -3
```
Expected: `0 error(s), N warning(s)` with `exit 0` (warnings are terms without chains and first-mention notices), and the strict build passes. If an anchor in the table above does not exist, open the target page and copy the heading's slug.

- [ ] **Step 6: Replace `docs/javascripts/glossary.js`**

```javascript
/**
 * Interactive Glossary System for Time Series Analysis Manual
 *
 * Recognises glossary terms in the page and makes them clickable. A click opens a
 * right-hand drawer with the term's definition, mathematical formulation, derivation
 * chain ("Why it holds"), upstream terms ("Rests on", clickable chips that open the
 * upstream drawer, with a back stack), historical context, and a link to the section
 * where the term is first developed.
 *
 * Term files are listed in glossary/index.yml, generated at build time by
 * scripts/mkdocs_hooks.py. Paths in `reference` are docs-relative source paths
 * (path/file.md#anchor); referenceUrl() converts them to site URLs.
 */

(function() {
  'use strict';

  // Pages where the glossary is switched off: the home page and the design showcase.
  const DISABLED_PATHS = ['/design-system-showcase/'];

  let allTerms = [];
  let drawerStack = [];

  function siteBase() {
    return window.__md_scope || '/';
  }

  function isGlossaryEnabled() {
    const path = window.location.pathname;
    const base = new URL(siteBase(), window.location.origin).pathname;
    if (path === base || path === base + 'index.html') return false;
    return !DISABLED_PATHS.some(disabled => path.includes(disabled));
  }

  // Convert "path/file.md#anchor" to a site URL under use_directory_urls.
  function referenceUrl(ref) {
    const [file, anchor] = ref.split('#');
    let path = file.replace(/\.md$/, '');
    path = path.endsWith('/index') ? path.slice(0, -'index'.length) : path + '/';
    return new URL(path, siteBase()).href + (anchor ? '#' + anchor : '');
  }

  async function loadGlossary() {
    let files = [];
    try {
      const response = await fetch(new URL('glossary/index.yml', siteBase()).href);
      files = ((jsyaml.load(await response.text()) || {}).files) || [];
    } catch (error) {
      console.warn('Could not load glossary/index.yml:', error);
      return [];
    }
    const fetches = files.map(async name => {
      try {
        const response = await fetch(new URL(`glossary/${name}`, siteBase()).href);
        const data = jsyaml.load(await response.text());
        return (data && data.terms) || [];
      } catch (error) {
        console.warn(`Could not load glossary/${name}:`, error);
        return [];
      }
    });
    return (await Promise.all(fetches)).flat();
  }

  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function escapeHtml(string) {
    return String(string)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // Find and mark glossary terms in content
  function highlightTerms(terms) {
    const content = document.querySelector('.md-content__inner');
    if (!content) return;

    const sortedTerms = [...terms].sort((a, b) => b.term.length - a.term.length);
    const regex = new RegExp(`\\b(${sortedTerms.map(t => escapeRegex(t.term)).join('|')})\\b`, 'gi');

    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {
      acceptNode: function(node) {
        if (node.parentElement.classList.contains('glossary-term')) return NodeFilter.FILTER_REJECT;
        if (node.parentElement.closest('code, pre, .highlight, .mermaid-container, .arithmatex')) return NodeFilter.FILTER_REJECT;
        if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    const nodesToProcess = [];
    let node;
    while ((node = walker.nextNode())) nodesToProcess.push(node);

    nodesToProcess.forEach(textNode => {
      const text = textNode.textContent;
      regex.lastIndex = 0;
      if (!regex.test(text)) return;
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = escapeHtml(text).replace(regex, match => {
        const matched = sortedTerms.find(t => t.term.toLowerCase() === match.toLowerCase());
        if (!matched) return match;
        return `<span class="glossary-term" data-term="${escapeHtml(matched.term)}">${match}</span>`;
      });
      const parent = textNode.parentNode;
      while (tempDiv.firstChild) parent.insertBefore(tempDiv.firstChild, textNode);
      parent.removeChild(textNode);
    });
  }

  function addClickHandlers() {
    document.querySelectorAll('.glossary-term').forEach(element => {
      if (element.dataset.bound) return;
      element.dataset.bound = 'true';
      element.addEventListener('click', function(e) {
        e.preventDefault();
        openTerm(this.dataset.term, { reset: true });
      });
    });
  }

  function findTerm(name) {
    return allTerms.find(t => t.term === name);
  }

  function openTerm(name, options) {
    const termData = findTerm(name);
    if (!termData) return;
    if (options && options.reset) drawerStack = [];
    drawerStack.push(termData);
    showDrawer(termData);
  }

  // Inline markdown: **bold**, *italic*
  function inlineMarkdownToHtml(text) {
    return text
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(?!\s)([^*\n]+?)(?<!\s)\*/g, '<em>$1</em>');
  }

  // Block markdown: paragraphs, "- " bullets, "1. " numbered steps. Math left for MathJax.
  function renderMarkdown(text) {
    if (!text) return '';
    const output = [];
    let open = null; // 'ul' | 'ol' | null
    const close = () => { if (open) { output.push(`</${open}>`); open = null; } };
    for (const raw of text.split('\n')) {
      const line = raw.trim();
      if (!line) { close(); continue; }
      const bullet = line.match(/^- (.*)$/);
      const numbered = line.match(/^\d+\.\s+(.*)$/);
      if (bullet) {
        if (open !== 'ul') { close(); output.push('<ul>'); open = 'ul'; }
        output.push(`<li class="arithmatex">${inlineMarkdownToHtml(bullet[1])}</li>`);
      } else if (numbered) {
        if (open !== 'ol') { close(); output.push('<ol>'); open = 'ol'; }
        output.push(`<li class="arithmatex">${inlineMarkdownToHtml(numbered[1])}</li>`);
      } else {
        close();
        output.push(`<p class="arithmatex">${inlineMarkdownToHtml(line)}</p>`);
      }
    }
    close();
    return output.join('');
  }

  function section(title, bodyHtml, extraClass) {
    if (!bodyHtml) return '';
    return `<section class="glossary-section ${extraClass || ''}"><h4>${title}</h4>${bodyHtml}</section>`;
  }

  function showDrawer(termData) {
    const existing = document.querySelector('.glossary-drawer');
    if (existing) existing.remove();

    const crumbs = drawerStack.map(t => escapeHtml(t.term)).join(' › ');
    const backButton = drawerStack.length > 1
      ? `<button class="glossary-back" aria-label="Back to ${escapeHtml(drawerStack[drawerStack.length - 2].term)}">‹ Back</button>`
      : '';
    const chips = (termData.depends_on || []).map(name => {
      const known = !!findTerm(name);
      return known
        ? `<button class="glossary-chip" data-term="${escapeHtml(name)}">${escapeHtml(name)}</button>`
        : `<span class="glossary-chip glossary-chip--missing" title="No glossary entry yet">${escapeHtml(name)}</span>`;
    }).join('');
    const reference = termData.reference
      ? `<p><a href="${referenceUrl(termData.reference)}">${escapeHtml(termData.reference.split('#')[0])}</a></p>`
      : '';

    const drawer = document.createElement('div');
    drawer.className = 'glossary-drawer';
    drawer.innerHTML = `
      <div class="glossary-drawer-content">
        <div class="glossary-drawer-header">
          <div>
            ${backButton}
            <h3>${escapeHtml(termData.term)}${termData.foundation ? ' <span class="glossary-root" title="Foundation: root of derivation chains">root</span>' : ''}</h3>
            ${drawerStack.length > 1 ? `<div class="glossary-crumbs">${crumbs}</div>` : ''}
          </div>
          <button class="close-drawer" aria-label="Close">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            </svg>
          </button>
        </div>
        <div class="glossary-drawer-body">
          ${section('Definition', `<p>${escapeHtml(termData.definition || '')}</p>`)}
          ${section('Mathematical Formulation', termData.mathematical ? `<div class="math-block">${renderMarkdown(termData.mathematical)}</div>` : '')}
          ${section('Why it holds', termData.derivation ? `<div class="derivation">${renderMarkdown(termData.derivation)}</div>` : '')}
          ${section('Rests on', chips ? `<div class="glossary-chips">${chips}</div>` : '')}
          ${section('Historical Context', termData.historical ? `<div class="historical-note">${renderMarkdown(termData.historical)}</div>` : '')}
          ${section('First developed in', reference)}
        </div>
      </div>
      <div class="glossary-drawer-overlay"></div>
    `;
    document.body.appendChild(drawer);
    drawer.offsetHeight;
    setTimeout(() => drawer.classList.add('open'), 10);

    if (window.MathJax) {
      const mathBlocks = Array.from(drawer.querySelectorAll('.arithmatex'));
      if (mathBlocks.length > 0) {
        MathJax.typesetPromise(mathBlocks).catch(err => console.warn('MathJax rendering in drawer failed:', err));
      }
    }

    function closeDrawer() {
      drawer.classList.remove('open');
      drawerStack = [];
      setTimeout(() => drawer.remove(), 300);
      document.removeEventListener('keydown', handleEscape);
    }
    function handleEscape(e) {
      if (e.key === 'Escape') closeDrawer();
    }

    drawer.querySelector('.close-drawer').addEventListener('click', closeDrawer);
    drawer.querySelector('.glossary-drawer-overlay').addEventListener('click', closeDrawer);
    document.addEventListener('keydown', handleEscape);

    drawer.querySelectorAll('.glossary-chip[data-term]').forEach(chip => {
      chip.addEventListener('click', () => {
        document.removeEventListener('keydown', handleEscape);
        openTerm(chip.dataset.term);
      });
    });
    const back = drawer.querySelector('.glossary-back');
    if (back) {
      back.addEventListener('click', () => {
        document.removeEventListener('keydown', handleEscape);
        drawerStack.pop();
        showDrawer(drawerStack[drawerStack.length - 1]);
      });
    }
  }

  async function initGlossary() {
    if (!isGlossaryEnabled()) return;
    if (allTerms.length === 0) {
      allTerms = await loadGlossary();
      if (allTerms.length === 0) { console.warn('No glossary terms loaded'); return; }
    }
    highlightTerms(allTerms);
    addClickHandlers();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlossary);
  } else {
    initGlossary();
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(() => setTimeout(initGlossary, 100));
  }
})();
```

- [ ] **Step 7: Append drawer styles to `docs/stylesheets/glossary.css`**

```css

/* ---- Derivation chain: chips, back button, breadcrumbs, root badge ---- */
.glossary-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.glossary-chip {
  font: inherit;
  font-size: 0.85em;
  padding: 0.2rem 0.6rem;
  border: 1px solid var(--md-primary-fg-color);
  border-radius: 999px;
  background: transparent;
  color: var(--md-primary-fg-color);
  cursor: pointer;
  transition: background-color 0.15s, color 0.15s;
}

.glossary-chip:hover,
.glossary-chip:focus {
  background: var(--md-primary-fg-color);
  color: var(--md-primary-bg-color);
  outline: none;
}

.glossary-chip--missing {
  border-style: dashed;
  color: var(--md-default-fg-color--light);
  cursor: default;
}

.glossary-back {
  font: inherit;
  font-size: 0.85em;
  margin-bottom: 0.25rem;
  padding: 0;
  border: none;
  background: none;
  color: var(--md-accent-fg-color);
  cursor: pointer;
}

.glossary-crumbs {
  font-size: 0.75em;
  color: var(--md-default-fg-color--light);
  margin-top: 0.25rem;
}

.glossary-root {
  font-size: 0.6em;
  vertical-align: middle;
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  background: var(--md-accent-fg-color);
  color: var(--md-accent-bg-color);
}

.glossary-section .derivation ol {
  padding-left: 1.25rem;
}

.glossary-section .derivation li {
  margin-bottom: 0.6rem;
}
```

- [ ] **Step 8: Verify in the browser**

Run: `venv/bin/mkdocs serve` and open the served site.

1. Open *Reference → Theory & Inference → Estimation*. The heading text "Joint density" is highlighted. Click it. Expected: drawer shows Definition, "Why it holds" with five numbered steps and rendered math, "Rests on" with five chips, "First developed in" linking to `reference/04-estimation/#joint-density`.
2. Click the chip "Independence". Expected: drawer swaps to *Independence* with a `root` badge, a "‹ Back" button and the breadcrumb `Joint density › Independence`. Click Back. Expected: *Joint density* again.
3. Open *Foundations → OLS assumptions*; click "i.i.d". Expected: drawer with `root` badge, no "Rests on" block, "First developed in" pointing at the *Do you need time series analysis?* page.
4. Open the home page. Expected: no highlighted terms. Open *Design System Showcase*. Expected: no highlighted terms.
5. Browser console shows no errors.

- [ ] **Step 9: Commit**

```bash
git add -A docs/glossary docs/javascripts/glossary.js docs/stylesheets/glossary.css docs/00-foundations/stochastic-processes.md docs/reference/04-estimation/index.md
git commit -m "feat(glossary): derivation chains, depends_on chips with back stack, source-path references"
```

---

### Task 10: Runtime node linking from the inventory

**Files:**
- Create: `docs/javascripts/flowchart-links.js`
- Modify: `docs/javascripts/mermaid-init.js` (dispatch an event after insertion)
- Modify: `docs/stylesheets/extra.css` (append), `mkdocs.yml` (`extra_javascript`)

**Interfaces:**
- Consumes: `docs/flowcharts/inventory.yml` rows (`id`, `label`, `areas`, `section`); CustomEvent `mermaid:rendered` with `detail.container`.
- Produces: SVG node groups gain class `flowchart-link`, `role="link"`, `tabindex="0"`, a `<title>`, and click / Enter navigation.

- [ ] **Step 1: Dispatch the event in `mermaid-init.js`**

Replace
```javascript
                container.innerHTML = result.svg;
                element.replaceWith(container);
```
with
```javascript
                container.innerHTML = result.svg;
                element.replaceWith(container);
                container.dispatchEvent(new CustomEvent('mermaid:rendered', {
                  bubbles: true,
                  detail: { container: container }
                }));
```

- [ ] **Step 2: Write `flowchart-links.js`**

```javascript
/**
 * Flowchart node linking.
 *
 * Mermaid diagrams carry no URLs. After mermaid-init.js inserts a rendered diagram it
 * dispatches `mermaid:rendered`; this script loads docs/flowcharts/inventory.yml once and,
 * for every SVG node whose id matches an inventory row, attaches navigation to the row's
 * section and a hover title with the label and area numbers. The inventory is the single
 * source of link targets (see planning/2026-10-06-flowchart-framework-design.md, section 10.5).
 */

(function() {
  'use strict';

  const NODE_ID_RE = /^flowchart-(.+)-\d+$/;
  let inventoryPromise = null;

  function siteBase() {
    return window.__md_scope || '/';
  }

  function sectionUrl(section) {
    const [file, anchor] = section.split('#');
    let path = file.replace(/\.md$/, '');
    path = path.endsWith('/index') ? path.slice(0, -'index'.length) : path + '/';
    return new URL(path, siteBase()).href + (anchor ? '#' + anchor : '');
  }

  function loadInventory() {
    if (!inventoryPromise) {
      inventoryPromise = fetch(new URL('flowcharts/inventory.yml', siteBase()).href)
        .then(response => response.text())
        .then(text => {
          const rows = ((jsyaml.load(text) || {}).nodes) || [];
          const byId = new Map();
          rows.forEach(row => byId.set(row.id, row));
          return byId;
        })
        .catch(error => {
          console.warn('flowchart-links: inventory unavailable', error);
          return new Map();
        });
    }
    return inventoryPromise;
  }

  async function decorate(container) {
    const inventory = await loadInventory();
    container.querySelectorAll('g.node[id]').forEach(group => {
      const match = NODE_ID_RE.exec(group.id);
      if (!match) return;
      const row = inventory.get(match[1]);
      if (!row || group.classList.contains('flowchart-link')) return;

      group.classList.add('flowchart-link');
      group.setAttribute('role', 'link');
      group.setAttribute('tabindex', '0');
      const title = document.createElementNS('http://www.w3.org/2000/svg', 'title');
      const areas = (row.areas || []).length ? ` (areas ${row.areas.join(', ')})` : '';
      title.textContent = `${row.label}${areas}`;
      group.prepend(title);

      const go = () => { window.location.href = sectionUrl(row.section); };
      group.addEventListener('click', go);
      group.addEventListener('keydown', event => { if (event.key === 'Enter') go(); });
    });
  }

  document.addEventListener('mermaid:rendered', event => decorate(event.detail.container));
})();
```

- [ ] **Step 3: Register the script and the styles**

In `mkdocs.yml`, change `extra_javascript` to:
```yaml
extra_javascript:
  - javascripts/mathjax.js
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js
  - https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js
  - https://unpkg.com/mermaid@10/dist/mermaid.min.js
  - javascripts/flowchart-links.js
  - javascripts/mermaid-init.js
  - javascripts/glossary.js
```
(js-yaml now precedes both consumers; the listener in `flowchart-links.js` is registered before the first render.)

Append to `docs/stylesheets/extra.css`, in the Mermaid section:
```css

/* Flowchart nodes that resolve to a section via docs/flowcharts/inventory.yml */
.mermaid-container .flowchart-link {
  cursor: pointer;
}

.mermaid-container .flowchart-link:hover rect,
.mermaid-container .flowchart-link:hover polygon,
.mermaid-container .flowchart-link:focus rect,
.mermaid-container .flowchart-link:focus polygon {
  stroke-width: 2px;
  filter: brightness(0.96);
}

.mermaid-container .flowchart-link:focus {
  outline: none;
}
```

- [ ] **Step 4: Verify in the browser**

Run: `venv/bin/mkdocs serve`.

1. Open *Workflow → General Flowchart*. Hover the "P7 Error-process specification" box. Expected: pointer cursor and a tooltip `P7: Error-process specification (areas 10)`. Click it. Expected: the P7 page opens at its H1.
2. On the P7 page, click "GARCH". Expected: `reference/10-volatility/#garch`, landing on the pending *GARCH* heading.
3. Click the dashed box "Wold decomposition". Expected: `00-foundations/stochastic-processes/#wold-decomposition`.
4. Click a diamond. Expected: nothing happens (not in the inventory).
5. Navigate between pages with the sidebar (SPA navigation) and repeat step 2. Expected: links still work after re-render.

- [ ] **Step 5: Strict build and commit**

Run: `venv/bin/mkdocs build --strict 2>&1 | tail -2`
Expected: pass.

```bash
git add docs/javascripts/flowchart-links.js docs/javascripts/mermaid-init.js docs/stylesheets/extra.css mkdocs.yml
git commit -m "feat: make flowchart nodes clickable from the leaf inventory"
```

---

### Task 11: CI — strict build, tests and audit

**Files:**
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Replace the dependency and build steps in both jobs**

In the `build` job, replace
```yaml
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
```
with
```yaml
      - name: Install documentation toolchain
        run: |
          pip install --upgrade pip
          pip install -r requirements-docs.txt

      - name: Run tests
        run: pytest tests -q

      - name: Audit flowcharts, inventory and glossary
        run: python scripts/audit_flowcharts.py
```
and replace
```yaml
      - name: Build MkDocs site
        run: mkdocs build --verbose
```
with
```yaml
      - name: Build MkDocs site
        run: mkdocs build --strict
```
In the `pr-preview` job apply the same two replacements (its install step and its `Build MkDocs site (PR preview)` step, which becomes `mkdocs build --strict`). Also change `cache: 'pip'` to add `cache-dependency-path: requirements-docs.txt` under both `setup-python` steps.

- [ ] **Step 2: Validate the workflow file**

Run: `venv/bin/python -c "import yaml, sys; yaml.safe_load(open('.github/workflows/deploy.yml')); print('yaml ok')"`
Expected: `yaml ok`.

- [ ] **Step 3: Reproduce the CI sequence locally**

Run:
```bash
venv/bin/pytest tests -q && venv/bin/python scripts/audit_flowcharts.py && venv/bin/mkdocs build --strict 2>&1 | tail -1
```
Expected: tests pass, `0 error(s)`, `Documentation built`.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: run tests and the flowchart audit, build with --strict"
```

---

### Task 12: Governance — design system, CLAUDE.md, writing rules, README, landing page

**Files:**
- Modify: `DESIGN-SYSTEM.md`, `CLAUDE.md`, `README.md`, `book_plan.md`, `docs/index.md`, `.gitignore`
- Create: `.claude/rules/writing.md`

- [ ] **Step 1: Design system — notation rules**

In `DESIGN-SYSTEM.md`, under "Decision-flowchart notation" → "**Rules.**", replace the `- **Node IDs.** …` bullet with these bullets:

```markdown
- **Node IDs.** `SCREAMING_SNAKE_CASE`, prefixed by the owning sub-diagram: `P3_ADF`, `P7_GARCH`, `B2_HAWKES`, `P2_CPD_PELT`. Master phase boxes are `P0` … `P11`; branch entries are `B1` … `B7`. Decision and terminator nodes carry the prefix too, because every defined ID is unique across the whole book.
- **Leaf nodes.** A defined rectangle `[ ]` that is not a `ref` and whose ID does not end in `_FLAG` is a leaf: one section of the book. Every leaf has a row in `docs/flowcharts/inventory.yml` (`id`, `label`, `phase`, `areas`, `section`). Diamonds, terminators, parallelograms (data), subroutine boxes and flag nodes are not leaves.
- **References.** A node that belongs to another sub-diagram is drawn as a `[[ ]]` subroutine box with the `ref` class and the owner's exact ID. A `ref` resolves to that definition, or to an inventory row of phase `F` (a Part 0 section, which has no diagram of its own).
- **No URLs in diagrams.** `docs/javascripts/flowchart-links.js` makes nodes clickable from the inventory at render time. Never use Mermaid `click`.
- **Audit.** `scripts/audit_flowcharts.py` enforces the rules above and runs in CI. A purely illustrative diagram opts out with the comment line `%% audit: skip` inside its fence.
```

- [ ] **Step 2: Design system — content rules pattern**

Insert a new subsection after "### Hypothesis-test layout" and before "### Page-footer navigation":

```markdown
### Content rules: method sections, why-chains, single source

These rules decide what a section contains and where a concept lives. They come from the flowchart framework design (`planning/2026-10-06-flowchart-framework-design.md`, section 9).

**Method and theory sections.** A *method* section says what to do and when; it is a leaf node of a flowchart sub-diagram and has an inventory row. A *theory* section says why something holds; it carries `kind: theory` in its front matter and is linked from at least one method section or one glossary derivation. Every page under `docs/reference/` and `docs/01-workflow/` is one or the other.

**Body text.** State each claim in one sentence and name methods as glossary terms. Multi-step derivations never appear inline. Outcome terminals in diagrams name **model → estimator → inference** in that order.

**Why-chains live in the glossary drawer.** Each term may carry `derivation` (numbered "because" steps) and `depends_on` (upstream term names). Part 0 roots carry `foundation: true`. The drawer renders them as "Why it holds", "Rests on" (chips that open the upstream term, with a back stack) and "First developed in" (`reference`). Every noun that appears in a chain is itself a term with its own entry: "joint density" is a term, not a step inside the MLE chain. For time series the likelihood factorises by the chain rule of probability into conditional densities, with i.i.d. as the special case; chains are written that way.

**Single source.** Every concept has one home: the section where it is first developed in `nav:` order. `reference` points there. The first occurrence develops the concept in full; later occurrences write only the term, which the glossary highlights. Part 0 takes only concepts needed before any method can be stated, and concepts shared across several phases with no natural home. Appendix pages are link indexes and contain no explanations.
```

- [ ] **Step 3: Design system — naming, checklist, changelog**

- In "Naming conventions", replace the `- **Glossary terms.** …` bullet with: ``- **Glossary terms.** One file per content directory or workflow page under `docs/glossary/`, named after it (`00-foundations.yml`, `p03-exploratory-diagnostics.yml`, `10-volatility.yml`); a term lives in the file of the page where it is first developed. `glossary/index.yml` is generated at build time and git-ignored.``
- In "New-chapter checklist", change `- New glossary terms are added to the chapter's docs/glossary/NN-chapter.yml file.` to `- New glossary terms are added to the glossary file of the page where they are first developed, with reference as a docs-relative path.md#anchor.` and add two bullets: `- Every leaf node drawn in the chapter's diagrams has a row in docs/flowcharts/inventory.yml, and every method section is such a leaf.` and ``- `python scripts/audit_flowcharts.py` reports zero errors.``
- In "Known gaps and future items", delete the first bullet (ad-hoc `fill:` styling): the legacy diagrams have been removed from the site.
- Add under `## Changelog`, above `### 1.1 — 2026-06-29`:

```markdown
### 1.2 — 2026-10-06

Flowchart framework: owner-prefixed node IDs, leaf-node definition and the `docs/flowcharts/inventory.yml` registry, `ref` resolution rules, runtime node linking (`flowchart-links.js`), the `%% audit: skip` opt-out and `scripts/audit_flowcharts.py`. New pattern "Content rules: method sections, why-chains, single source". Glossary schema gains `derivation`, `depends_on`, `foundation`; `reference` becomes a docs-relative source path; glossary files are named per page; the drawer shows "Why it holds", "Rests on" and "First developed in".
```
Update any "currently `1.0`" / "`1.1`" version mention at the top of the document to `1.2`.

- [ ] **Step 4: Replace `CLAUDE.md`**

```markdown
# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

A MkDocs-based educational manual on time series analysis, bridging classical econometrics and modern machine learning. Deployed to GitHub Pages at https://shuxin-y.github.io/time-series-analysis-manual.

Two goals, in order: readers must understand *why* each method works (every method traces back to Part 0 through an explicit derivation chain), and coverage is as complete as possible (34 areas, listed on the landing page). The flowcharts are the organising framework: every content unit is a leaf node of a workflow sub-diagram. The design is in `planning/2026-10-06-flowchart-framework-design.md`.

## Build & Development Commands

```bash
# One-time setup (docs toolchain only; requirements.txt holds the code-example stack)
python3 -m venv venv && venv/bin/pip install -r requirements-docs.txt

# Local development (hot-reload). The pre-build hook regenerates glossary/index.yml and prints audit findings.
venv/bin/mkdocs serve

# Production build. Audit errors surface as warnings, which --strict turns into a failed build.
venv/bin/mkdocs build --strict

# Tests, audit, stub scaffolding
venv/bin/pytest tests -q
venv/bin/python scripts/audit_flowcharts.py        # exit 1 on any error
venv/bin/python scripts/scaffold_stubs.py --dry-run  # pending sections the inventory still needs

# Deploy happens automatically via GitHub Actions on push to main (tests, audit, strict build).
```

## Architecture

### Three axes of content

| Axis | Location | Role |
|---|---|---|
| Part 0 Foundations | `docs/00-foundations/` | Roots of every derivation chain: statistical-analysis logic, OLS assumptions, stochastic processes, asymptotics |
| Workflow | `docs/01-workflow/` | The general flowchart: master diagram plus one chapter per phase P0–P11; `p02-purpose/` (10 purposes) and `p05-representation/` (6 representations) are decision indexes |
| Reference | `docs/reference/NN-slug/` | One chapter group per area (34) |

### Node = content unit

Every leaf rectangle in a workflow sub-diagram has a row in `docs/flowcharts/inventory.yml` pointing at one section (`path.md#anchor`). `scripts/audit_flowcharts.py` checks: defined IDs unique, `ref` nodes resolve, leaves have rows and targets exist, every page under `reference/` and `01-workflow/` is a method page (in the inventory) or a linked `kind: theory` page, glossary chains resolve and terminate at `foundation: true` terms. `scripts/scaffold_stubs.py` appends pending sections for rows whose target is missing.

### Browser-side systems

All four hook into Material's `document$.subscribe()` for SPA navigation:

1. **MathJax** (`docs/javascripts/mathjax.js`): `\( \)` inline, `\[ \]` display, AMS numbering.
2. **Mermaid** (`docs/javascripts/mermaid-init.js`): renders superfences blocks, `startOnLoad: false`, dispatches `mermaid:rendered` after each diagram.
3. **Flowchart links** (`docs/javascripts/flowchart-links.js`): reads the inventory once and makes matching SVG nodes navigate to their section. Diagrams contain no URLs.
4. **Glossary** (`docs/javascripts/glossary.js`): loads the per-page YAML files listed in `glossary/index.yml` (generated by `scripts/mkdocs_hooks.py`), highlights terms, and shows a drawer with definition, formulation, derivation chain, upstream chips and the home-section link.

### Custom CSS

`docs/stylesheets/extra.css` (admonitions, hypothesis-test boxes, Mermaid, clickable nodes) and `docs/stylesheets/glossary.css` (drawer, chips). `DESIGN-SYSTEM.md` is the catalog; the CSS/JS is the runtime truth.

## Content Conventions

- **No emojis** in content or diagrams.
- **Node = content unit.** Add or locate the leaf node first, then write the section. Node IDs are owner-prefixed `SCREAMING_SNAKE_CASE`; never label nodes "Ch N".
- **Why-chains in the drawer, not the body.** Body text: one sentence per claim, methods named as glossary terms. Derivations go in the term's `derivation` with `depends_on` back to Part 0 roots. Every noun in a chain is itself a term.
- **Single source.** First occurrence in `nav:` order develops a concept; later occurrences only name it. Appendices are link indexes.
- **Primary notation:** conditional-expectation form.
- **Design system:** `DESIGN-SYSTEM.md` governs appearance, flowchart notation, tables and figures. Content rules are in its "Content rules" pattern and in `.claude/rules/writing.md`.

## CI/CD

GitHub Actions (`.github/workflows/deploy.yml`): on push to main, installs `requirements-docs.txt`, runs `pytest`, runs the audit, builds with `mkdocs build --strict`, deploys to GitHub Pages.

## Basic

请使用第一性原理思考。你不能总假设我非常清楚自己想要什么和该怎么得到。请保持审慎，从原始需求和问题出发，如果动机和目标不清晰，停下来和我讨论。如果目标清晰但是路径不是最短，告诉我，并建议更好的办法。

Do not commit or push without permission.
```

- [ ] **Step 5: Track `.claude/rules/` and write `writing.md`**

In `.gitignore`, replace the line `.claude/` with:
```text
.claude/*
!.claude/rules/
```
Create `.claude/rules/writing.md`:

```markdown
# Writing rules

Source of truth for prose and structure decisions. Appearance is governed by `DESIGN-SYSTEM.md`; the framework design is `planning/2026-10-06-flowchart-framework-design.md`.

## Before writing a section

1. Locate its leaf node in a workflow sub-diagram, or add one. Add the inventory row (`docs/flowcharts/inventory.yml`): `id`, `label`, `phase`, `areas`, `section`.
2. Decide: method section (what to do, when) or theory section (`kind: theory` front matter, linked from a method section or a glossary derivation).
3. Check the concept is not already developed elsewhere (`grep` the glossary `reference` fields). If it is, link; do not re-explain.

## While writing

- One claim per sentence. Name methods as glossary terms; the glossary highlights them.
- No multi-step derivation in the body. Put it in the term's `derivation` as numbered "because" steps, each naming the assumption it uses, with `depends_on` listing the upstream terms. Every noun in the chain gets its own term entry.
- For time series, factorise likelihoods by the chain rule into conditional densities; i.i.d. is the special case. Never derive time-series MLE from an i.i.d. product.
- Follow the canonical chapter template and the equation → `(Read: …)` pairing from the design system.
- Outcome terminals name model → estimator → inference.

## After writing

- `python scripts/audit_flowcharts.py` reports zero errors.
- `mkdocs build --strict` passes.
```

- [ ] **Step 6: README and book_plan pointers**

In `README.md`:
- Delete the line `Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.` and replace with `Issues and pull requests are welcome. Pull requests must pass the tests, the flowchart audit and the strict build (see CLAUDE.md).`
- Replace the License section body with `Documentation: CC BY-SA 4.0. Code: MIT.` (no file links until the licence files exist) and change the License badge target to `https://creativecommons.org/licenses/by-sa/4.0/`.
- Replace `Or build locally and explore the \`code/\` directory for standalone examples.` with `Or build locally with \`mkdocs serve\`.`
- In "What Makes This Manual Different?", replace the first bullet with `- **Flowcharts as the framework**: every section of the book is a leaf node of a workflow sub-diagram; follow the arrows, run the named test, land on the method` and add `- **Derivation chains**: every method traces back to first principles through the glossary drawer`.
- Replace the "Core Chapters" list with the three-axis description used on the landing page (Foundations, Workflow P0–P11 with Purpose and Representation indexes, Reference 34 areas).

Prepend to `book_plan.md`:
```markdown
> Superseded for structure and flowcharts by `planning/2026-10-06-flowchart-framework-design.md` (approved 2026-10-06). The functional requirements below remain valid.

```

- [ ] **Step 7: Landing page — 34 areas and the PAR fix**

In `docs/index.md`, under *Techniques This Book Covers*:
- In the `=== "Theory & Inference"` tab, after the `=== "25. Simulation"` block add:
```markdown
    === "27. Regression with TS Data"

        OLS under temporal dependence, HAC inference (Newey-West, bandwidth choice), feasible GLS (Cochrane-Orcutt, Prais-Winsten), dynamic regression, distributed lags, trending regressors, spurious regression.

    === "28. Nonstationarity Theory"

        Unit-root asymptotics (functional CLT, Brownian limits), cointegration theory, near-unit roots and local-to-unity, fractional cointegration, explosive roots and bubble tests (PSY, GSADF).
```
- In `=== "Core Models"` after `=== "10. Volatility"` add:
```markdown
    === "29. Seasonality & Calendar"

        Seasonal unit roots (HEGY, Canova-Hansen, OCSB), seasonal adjustment (X-13, SEATS, STL as methodology), periodic autoregression (PAR), multiple seasonality (MSTL, TBATS, Fourier terms), calendar and holiday effects, cyclostationary processes.

    === "30. Structural Change & TVP"

        Break tests, time-varying parameter models, rolling and recursive estimation, forecasting under breaks (Pesaran-Timmermann), statistical process control (Shewhart, EWMA, CUSUM charts).

    === "32. Panel Time Series"

        Panel unit roots and cointegration, dynamic panel GMM (Arellano-Bond), heterogeneous panels (mean group, pooled mean group), cross-sectional dependence (CD test, CCE), large-N large-T asymptotics.
```
- In `=== "Specialized Models"` after `=== "17. Point Processes"` add:
```markdown
    === "33. System ID & Dynamical Systems"

        ARX, ARMAX and Box-Jenkins transfer functions from the control perspective, subspace methods (N4SID), Hammerstein-Wiener, Takens embedding and phase-space reconstruction, dynamic mode decomposition, Koopman operators, SINDy.
```
- In `=== "ML, Forecasting & Practice"` after `=== "26. Applied Domains"` add:
```markdown
    === "31. Data Preparation"

        Imputation (interpolation, Kalman-smoother and multiple imputation), irregular sampling, the outlier taxonomy (AO, IO, LS, TC), temporal disaggregation and benchmarking (Chow-Lin, Denton), data revisions and real-time vintages, calendar alignment.

    === "34. Probabilistic Forecasting"

        Density and quantile forecasts, scoring rules (CRPS, pinball, log score), calibration and PIT histograms, CAViaR, multi-step strategies (recursive, direct, MIMO), intermittent demand (Croston, TSB), MinT reconciliation, judgmental forecasting.
```
- In the `26. Applied Domains` block append the sentence: `Explicit sub-domains: condition monitoring and reliability (vibration analysis, degradation processes, remaining useful life), environmental trend methods (Mann-Kendall, Sen slope), epidemiology (Rt estimation, SIR fitting).`
- Abbreviations: change `*[PAR]: Poisson Autoregression` to `*[PAR]: Periodic Autoregression`, and add `*[INGARCH]` if absent (`*[INGARCH]: Integer-valued Generalized ARCH (Poisson autoregression is its INGARCH(p, 0) case)`). Add `*[HAC]: Heteroskedasticity-and-Autocorrelation-Consistent`, `*[PSY]: Phillips-Shi-Yu bubble test`, `*[HEGY]: Hylleberg-Engle-Granger-Yoo seasonal unit root test`, `*[CCE]: Common Correlated Effects`, `*[MinT]: Minimum Trace reconciliation`, `*[PIT]: Probability Integral Transform`, `*[SINDy]: Sparse Identification of Nonlinear Dynamics`, `*[DMD]: Dynamic Mode Decomposition`.
- Change any remaining "26 sections" wording to "34 areas".

- [ ] **Step 8: Verify and commit**

Run:
```bash
venv/bin/python scripts/audit_flowcharts.py | tail -1
venv/bin/mkdocs build --strict 2>&1 | tail -1
git status --short | head -30
git diff --cached --name-only >/dev/null; git diff | grep -nE '[/]Users[/]|[/]private[/]tmp[/]|[/]var[/]folders[/]|localhos[t]|127[.]0[.]0[.]1|[.]local\b' ; echo "local-ref scan done (expect no matches)"
```
Expected: `0 error(s)`, `Documentation built`, no local references.

```bash
git add DESIGN-SYSTEM.md CLAUDE.md README.md book_plan.md docs/index.md .gitignore .claude/rules/writing.md
git commit -m "docs: governance for the flowchart framework; 34 areas on the landing page"
```

---

## Plan Self-Review

**Spec coverage.** §3 architecture → Tasks 7b, 8. §4 phases → 7b (pages), 8 (master); phase sub-diagrams other than P1/P7 → Plan B (stated in scope). §5 gate and branches → Task 8 Steps 2, 5. §6 P7 → Task 8 Step 4. §7 purposes and representations → 7b pages, 8 Step 3 selectors; sub-charts → Plan B. §8 areas → 7c, 12 Step 7. §9 content rules → 9 (schema, drawer), 12 Steps 2, 4, 5. §10 conventions → 1–4 (audit rules), 8 (IDs), 7 (layout), 9 (paths), 10 (runtime links). §11 audit → 1–4, 6, 11. §12 migration → 7a–7d, 9, 12. §13 open items → unchanged, not blocking. §14 criteria 1, 2, 4, 5, 6 → Tasks 9–11 verify; criterion 3 → Plan B.

**Placeholder scan.** Pending admonitions in generated pages are intended content (the spec defines a node without content as a visible to-do), not plan placeholders. No placeholder markers, no "similar to Task N" shortcuts, and no undefined function references remain; every function referenced in a later task is defined in Tasks 1–6.

**Type consistency.** `Row(id, label, phase, areas, section)` with `.file`/`.anchor`; `Finding(level, where, message)`; `Diagram.is_ref/is_leaf`; `load_inventory(path) -> (rows, findings)`; `load_glossary(dir) -> (terms, findings)`; `run_all(root)`; `scaffold(root, dry_run)`; `write_glossary_index(docs_dir) -> bool` are used with the same names and shapes in Tasks 1–6 and their tests. The hook passes `docs_dir.parent` as `root` to `run_all`, matching Task 4.

**Review Focus coverage.** 1 → `test_unquoted_label_is_not_a_definition` (Task 1). 2 → `test_check_diagrams_flags_duplicate_definition_with_first_location` (Task 3). 3 → `test_heading_anchors_match_mkdocs_slugify_and_unique_suffixes` (Task 2). 4 → `test_write_glossary_index_does_not_rewrite_identical_content` (Task 6). 5 → `test_check_glossary_levels` (Task 4).
