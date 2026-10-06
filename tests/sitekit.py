"""Build throwaway MkDocs projects that use the repository's own Markdown extension stack."""
import re
from pathlib import Path

import yaml

import audit_flowcharts as audit

REPO = Path(__file__).resolve().parent.parent
_EXTENSIONS_BLOCK = re.search(r"^markdown_extensions:\n(?:(?:[ #].*)?\n)*", (REPO / "mkdocs.yml").read_text(encoding="utf-8"), re.M).group(0)


def write_project(root: Path, files: dict[str, str], nav: list | None = None) -> Path:
    """Write docs files and an mkdocs.yml with the real markdown_extensions; return the config path."""
    docs = root / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    for rel, text in files.items():
        path = docs / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    head = {"site_name": "t", "docs_dir": "docs"}
    if nav is not None:
        head["nav"] = nav
    config = root / "mkdocs.yml"
    config.write_text(yaml.safe_dump(head, sort_keys=False) + _EXTENSIONS_BLOCK, encoding="utf-8")
    return config


def site(root: Path) -> audit.Site:
    return audit.Site(root / "mkdocs.yml", root / "docs")
