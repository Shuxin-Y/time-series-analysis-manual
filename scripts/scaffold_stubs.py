"""Create pending stub sections for inventory rows whose target file or heading is missing.

Run: python scripts/scaffold_stubs.py [--root PATH] [--dry-run]
Idempotent: a second run reports no actions. Never deletes or rewrites existing text.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from markdown.extensions.toc import slugify  # noqa: E402

from audit_flowcharts import ERROR, INVENTORY_PATH, Finding, Row, load_inventory, load_site_config, render_page, site_markdown  # noqa: E402

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


def scaffold(root: Path, dry_run: bool) -> tuple[list[str], list[Finding]]:
    """Actions taken (or planned, with dry_run) and the inventory findings; rejected rows are not scaffolded."""
    cfg = load_site_config(root / "mkdocs.yml")
    docs = Path(cfg["docs_dir"])
    md = site_markdown(cfg)
    rows, findings = load_inventory(docs.joinpath(*INVENTORY_PATH))
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
        if row.anchor in render_page(md, text).anchors:
            continue
        actions.append(f"append #{row.anchor} to {row.file}")
        if not dry_run:
            with target.open("a", encoding="utf-8") as fh:
                fh.write(f"\n{heading_for(row)}\n\n{PENDING.format(id=row.id)}")
    return actions, findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    actions, findings = scaffold(args.root, args.dry_run)
    for f in findings:
        print(f, file=sys.stderr)
    for action in actions:
        print(action)
    return 1 if any(f.level == ERROR for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
