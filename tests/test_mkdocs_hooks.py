import logging

import pytest
from mkdocs.config import load_config

import audit_flowcharts as audit
import mkdocs_hooks as hooks
import sitekit


def test_write_glossary_index_lists_yml_files_and_skips_itself(tmp_path):
    g = tmp_path / "glossary"
    g.mkdir()
    (g / "b.yml").write_text("terms: []\n", encoding="utf-8")
    (g / "a.yml").write_text("terms: []\n", encoding="utf-8")
    (g / "index.yml").write_text("stale\n", encoding="utf-8")
    assert hooks.write_glossary_index(tmp_path) is True
    assert (g / "index.yml").read_text(encoding="utf-8") == "files:\n- a.yml\n- b.yml\ndisabled_pages:\n- index.md\n- design-system-showcase.md\n"


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
    (docs / "flowcharts" / "inventory.yml").write_text("nodes:\n  - id: P0_X\n    label: x\n    phase: P0\n    areas: []\n    section: 'a/b.md#c'\n", encoding="utf-8")
    with caplog.at_level(logging.INFO, logger="mkdocs.plugins.tsam_hooks"):
        hooks.on_pre_build(audit.load_site_config(sitekit.write_project(tmp_path, {})))
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert any("inventory row has no leaf definition" in r.getMessage() for r in warnings)
    assert (docs / "glossary" / "index.yml").exists()


def strict_build(tmp_path, anchor):
    from mkdocs.commands.build import build

    config = sitekit.write_project(tmp_path, {
        "01-workflow/index.md": '# P0: Data\n\n```mermaid\ngraph TD\n    P0["P0: Data"]\n```\n',
        "glossary/.keep": "",
        "flowcharts/inventory.yml": f'nodes:\n  - {{id: P0, label: "P0: Data", phase: MASTER, areas: [31], section: "01-workflow/index.md#{anchor}"}}\n',
    })
    with config.open("a", encoding="utf-8") as fh:
        fh.write(f"\nhooks:\n  - {sitekit.REPO / 'scripts' / 'mkdocs_hooks.py'}\n")
    cfg = load_config(config_file=str(config), strict=True, site_dir=str(tmp_path / "site"))
    build(cfg)


def test_strict_build_aborts_on_an_audit_error(tmp_path):
    from mkdocs.exceptions import Abort

    strict_build(tmp_path / "ok", "p0-data")
    with pytest.raises(Abort):
        strict_build(tmp_path / "broken", "no-such-anchor")
