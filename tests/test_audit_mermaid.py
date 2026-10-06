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
