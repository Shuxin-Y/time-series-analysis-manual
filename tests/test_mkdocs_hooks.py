import logging

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
    (docs / "flowcharts" / "inventory.yml").write_text("nodes:\n  - id: P0_X\n    label: x\n    phase: P0\n    areas: []\n    section: 'a/b.md#c'\n", encoding="utf-8")
    with caplog.at_level(logging.INFO, logger="mkdocs.plugins.tsam_hooks"):
        hooks.on_pre_build(audit.load_site_config(sitekit.write_project(tmp_path, {})))
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    assert any("inventory row has no leaf definition" in r.getMessage() for r in warnings)
    assert (docs / "glossary" / "index.yml").exists()
