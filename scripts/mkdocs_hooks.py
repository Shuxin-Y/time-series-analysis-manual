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
    files = sorted(p.name for p in gdir.glob("*.yml") if p.name != audit.GLOSSARY_INDEX_NAME)
    content = yaml.safe_dump({"files": files}, sort_keys=False)
    target = gdir / audit.GLOSSARY_INDEX_NAME
    if target.is_file() and target.read_text(encoding="utf-8") == content:
        return False
    target.write_text(content, encoding="utf-8")
    return True


def on_pre_build(config, **kwargs) -> None:
    docs_dir = Path(config["docs_dir"])
    if write_glossary_index(docs_dir):
        log.info("wrote glossary/%s", audit.GLOSSARY_INDEX_NAME)
    for f in audit.run_all(docs_dir.parent):
        logger = log.warning if f.level == "error" else log.info
        logger("audit %s %s: %s", f.level, f.where, f.message)
