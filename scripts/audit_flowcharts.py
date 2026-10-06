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
