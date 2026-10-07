import textwrap

import audit_flowcharts as audit
import sitekit


def render(text):
    return audit.render_page(audit.site_markdown(audit.load_site_config(sitekit.REPO / "mkdocs.yml")), text)


def test_anchors_are_the_rendered_heading_ids():
    page = render(textwrap.dedent('''
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

        ~~~python
        # not a heading either
        ~~~
    ''').lstrip())
    assert page.anchors == {"p7-error-process-specification", "garch", "garch_1",
                            "hypothesis-test-and-decision-rule-boxes", "my-anchor"}
    assert page.meta == {"kind": "theory"}


def test_anchors_follow_toc_for_nested_raw_html_and_attr_ids():
    page = render(textwrap.dedent('''
        # Page

        !!! note "Nested"

            ### Estimation

        ## Estimation

        ## What is <em>x</em>?

        ## Dup

        ## Dup

        ## Bar {#dup}
    '''))
    by_text = {}
    for h in page.headings:
        by_text.setdefault(h.text, []).append(h.id)
    assert by_text["Estimation"] == ["estimation", "estimation_1"]
    assert by_text["What is x?"] == ["what-is-x"]
    assert by_text["Bar"] == ["dup"]
    assert by_text["Dup"] == ["dup_1", "dup_2"]


def test_front_matter_is_parsed_and_absent_is_empty():
    assert render("---\nkind: theory\n---\n# T\n").meta == {"kind": "theory"}
    assert render("# T\n").meta == {}


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
    sitekit.write_project(tmp_path, {"reference/10-volatility/index.md": "# Volatility\n\n## GARCH\n"})
    rows = [
        audit.Row("P7_GARCH", "GARCH", "P7", (10,), "reference/10-volatility/index.md#garch"),
        audit.Row("P7_SV", "SV", "P7", (10,), "reference/10-volatility/index.md#stochastic-volatility"),
        audit.Row("P7_X", "X", "P7", (10,), "reference/99-nope/index.md#x"),
    ]
    findings = audit.check_inventory_targets(rows, sitekit.site(tmp_path))
    where = {f.where: f.message for f in findings}
    assert "P7_GARCH" not in where
    assert "anchor #stochastic-volatility not found" in where["P7_SV"]
    assert "does not exist" in where["P7_X"]


def inventory_findings(tmp_path, body):
    inv = tmp_path / "inventory.yml"
    inv.write_text(textwrap.dedent(body), encoding="utf-8")
    return audit.load_inventory(inv)


ROW = 'id: P7_GARCH\n    label: "GARCH"\n    phase: P7\n    section: "reference/10-volatility/index.md#garch"\n'


def test_areas_must_be_a_list_of_area_numbers(tmp_path):
    for areas in ('"31"', "31", "[0]", "[35]", "[true]", '["10"]'):
        rows, findings = inventory_findings(tmp_path, f"nodes:\n  - {ROW}    areas: {areas}\n")
        assert rows == [] and "must be a list of area numbers 1-34" in findings[0].message, areas


def test_rows_are_validated_structurally(tmp_path):
    cases = {
        "nodes:\n  - just a string\n": "row must be a mapping",
        f"nodes:\n  - {ROW.replace('P7_GARCH', 'p7_garch')}    areas: [10]\n": "SCREAMING_SNAKE_CASE string",
        f"nodes:\n  - {ROW.replace('id: P7_GARCH', 'id: NO')}    areas: [10]\n": "must be a SCREAMING_SNAKE_CASE string",
        f"nodes:\n  - {ROW.replace('phase: P7', 'phase: P12')}    areas: [10]\n": "phase 'P12' must be one of",
        f"nodes:\n  - {ROW.replace('phase: P7', 'phase: P11')}    areas: [10]\n": "owner prefix P11_",
        f"nodes:\n  - {ROW.replace('id: P7_GARCH', 'id: P7')}    areas: [10]\n": "master boxes P0-P11",
        f"nodes:\n  - {ROW.replace('phase: P7', 'phase: MASTER')}    areas: [10]\n": "master boxes P0-P11",
    }
    for body, expected in cases.items():
        rows, findings = inventory_findings(tmp_path, body)
        assert rows == [] and expected in findings[0].message, (body, findings)


def test_branch_entries_carry_their_own_id_as_phase(tmp_path):
    rows, findings = inventory_findings(tmp_path, f"nodes:\n  - {ROW.replace('id: P7_GARCH', 'id: B7').replace('phase: P7', 'phase: B7')}    areas: [22]\n")
    assert findings == [] and rows[0].id == "B7"
    rows, findings = inventory_findings(tmp_path, f"nodes:\n  - {ROW.replace('id: P7_GARCH', 'id: B1').replace('phase: P7', 'phase: P3')}    areas: [16]\n")
    assert rows == [] and "branch entry B1 must have phase B1" in findings[0].message


def test_invalid_yaml_and_duplicate_keys_are_findings_naming_the_file(tmp_path):
    rows, findings = inventory_findings(tmp_path, "nodes:\n  - id: [unclosed\n")
    assert rows == [] and findings[0].where == "inventory.yml" and "invalid YAML" in findings[0].message
    rows, findings = inventory_findings(tmp_path, f"nodes:\n  - {ROW}    areas: [10]\n    phase: P8\n")
    assert rows == [] and "duplicate key 'phase'" in findings[0].message
    rows, findings = inventory_findings(tmp_path, "- just\n- a list\n")
    assert "top level must be a mapping with a `nodes` list" in findings[0].message


def test_heading_text_keeps_inline_code_and_prose_text_drops_it():
    page = render("# A `code` head\n\nSome `x = 1` prose.\n")
    assert page.headings[0].text == "A code head"
    assert "x = 1" not in page.text and "Some" in page.text
