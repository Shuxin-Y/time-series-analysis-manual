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
