import textwrap

import audit_flowcharts as audit
import scaffold_stubs as scaffold
import sitekit


def write_inventory(root, body):
    sitekit.write_project(root, {})
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
    actions, findings = scaffold.scaffold(root, dry_run=False)
    assert findings == []
    assert "append #garch to reference/10-volatility/index.md" in actions
    assert "create reference/15-continuous-time/index.md" in actions
    vol = (root / "docs" / "reference" / "10-volatility" / "index.md").read_text(encoding="utf-8")
    assert "\n## GARCH\n" in vol and scaffold.pending_note("P7_GARCH") in vol
    ct = (root / "docs" / "reference" / "15-continuous-time" / "index.md").read_text(encoding="utf-8")
    assert ct.startswith("# Continuous Time\n")
    assert "## Jump diffusion" in ct
    assert scaffold.scaffold(root, dry_run=False) == ([], [])          # second run: nothing to do
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
    actions, _ = scaffold.scaffold(root, dry_run=True)
    assert actions == ["create reference/10-volatility/index.md", "append #garch to reference/10-volatility/index.md"]
    assert not (root / "docs" / "reference").exists()


def test_main_reports_a_malformed_row_and_exits_1(tmp_path, capsys):
    write_inventory(tmp_path, '''
        nodes:
          - id: P7_GARCH
            label: "GARCH"
            phase: P7
            section: "reference/10-volatility/index.md#garch"
    ''')
    assert scaffold.main(["--root", str(tmp_path), "--dry-run"]) == 1
    err = capsys.readouterr().err
    assert "inventory.yml#nodes[0]: missing keys ['areas']" in err


def test_every_pending_note_in_the_book_uses_the_one_template():
    import re

    template = re.escape(scaffold.PENDING).replace(r"\{source\}", "(flowchart inventory|glossary)").replace(
        r"\{kind\}", "(node|term)").replace(r"\{key\}", "[^`]+")
    for page in sorted((sitekit.REPO / "docs").rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        for m in re.finditer(r'^!!! note "[^"]*[Pp]ending"\n.*\n', text, re.M):
            assert re.fullmatch(template, m.group(0)), (page, m.group(0))
