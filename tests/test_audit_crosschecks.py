import audit_flowcharts as audit


def diagram(src, where):
    return audit.parse_diagram(src, where)


A = diagram('graph TD\n    P7_IN(["in"]) --> P7_MULTI{"Several?"}\n    P7_MULTI -->|"Yes"| P7_GARCH["GARCH"]\n    P7_GARCH --> P8[["P8 Estimation"]]\n    F_WOLD[["Wold"]] -.- P7_GARCH\n    class P8,F_WOLD ref\n', "p07.md:3")
B = diagram('graph TD\n    P8_IN(["in"]) --> P7_MULTI{"dup"}\n    P7_MULTI --> P8["P8 Estimation"]\n    P8 --> P8_GHOST\n', "p08.md:3")


def test_check_diagrams_flags_duplicate_definition_with_first_location():
    findings = audit.check_diagrams([A, B])
    dup = [f for f in findings if "P7_MULTI" in f.message]
    assert len(dup) == 1
    assert dup[0].where == "p08.md:3"
    assert "already defined in p07.md:3" in dup[0].message


def test_check_diagrams_flags_bare_edge_ids():
    findings = audit.check_diagrams([A, B])
    bare = [f for f in findings if "P8_GHOST" in f.message]
    assert bare and bare[0].level == "error"
    assert "no quoted, shaped definition" in bare[0].message


def test_check_refs_resolve_to_definitions_or_foundation_rows():
    rows = [audit.Row("F_WOLD", "Wold decomposition", audit.FOUNDATION_PHASE, (1,), "00-foundations/stochastic-processes.md#wold-decomposition")]
    assert audit.check_refs([A, B], rows) == []            # P8 defined in B, F_WOLD is a foundation row
    assert any("F_WOLD" in f.message for f in audit.check_refs([A], []))   # no definition, no row
    assert any("P8" in f.message for f in audit.check_refs([A], rows))     # P8 undefined without B


def test_check_nodes_vs_inventory_both_directions():
    rows = [
        audit.Row("P7_GARCH", "GARCH", "P7", (10,), "reference/10-volatility/index.md#garch"),
        audit.Row("P7_ORPHAN", "Orphan", "P7", (10,), "reference/10-volatility/index.md#orphan"),
        audit.Row("F_WOLD", "Wold decomposition", audit.FOUNDATION_PHASE, (1,), "00-foundations/stochastic-processes.md#wold-decomposition"),
        audit.Row("F_LONELY", "Lonely", audit.FOUNDATION_PHASE, (1,), "00-foundations/stochastic-processes.md#lonely"),
    ]
    findings = audit.check_nodes_vs_inventory([A, B], rows)
    messages = {f.where: f.message for f in findings}
    assert "no inventory row" in messages["p08.md:3"]        # P8 is a leaf rectangle in B
    assert "no leaf definition" in messages["P7_ORPHAN"]
    assert "not referenced by any ref node" in messages["F_LONELY"]
    assert "P7_GARCH" not in messages and "F_WOLD" not in messages


def test_diagram_label_first_line_must_equal_the_inventory_label():
    d = diagram('graph TD\n    P7_GARCH["Symmetric GARCH<br/>sigma"] --> P7_SV["Stochastic volatility<br/>latent"]\n', "p07.md#mermaid-1")
    rows = [audit.Row("P7_GARCH", "GARCH", "P7", (10,), "reference/10-volatility/index.md#garch"),
            audit.Row("P7_SV", "Stochastic volatility", "P7", (10,), "reference/10-volatility/index.md#stochastic-volatility")]
    messages = [f.message for f in audit.check_nodes_vs_inventory([d], rows) if "label" in f.message]
    assert messages == ["node P7_GARCH label 'Symmetric GARCH' differs from its inventory label 'GARCH'"]


def test_a_leaf_must_be_defined_on_its_phase_owner_page():
    p3 = diagram('graph TD\n    P3_FOREIGN["Foreign"]\n', "01-workflow/p07-error-process.md#mermaid-1")
    own = diagram('graph TD\n    P3_HOME["Home"]\n', "01-workflow/p03-exploratory-diagnostics.md#mermaid-1")
    rows = [audit.Row("P3", "P3: Exploratory diagnostics", "MASTER", (2,), "01-workflow/p03-exploratory-diagnostics.md#p3"),
            audit.Row("P3_FOREIGN", "Foreign", "P3", (2,), "01-workflow/p03-exploratory-diagnostics.md#foreign"),
            audit.Row("P3_HOME", "Home", "P3", (2,), "01-workflow/p03-exploratory-diagnostics.md#home"),
            audit.Row("P4_LOST", "Lost", "P4", (2,), "01-workflow/p04.md#lost")]
    lost = diagram('graph TD\n    P4_LOST["Lost"]\n', "01-workflow/p04.md#mermaid-1")
    messages = [f.message for f in audit.check_nodes_vs_inventory([p3, own, lost], rows) if "P3" in f.message or "P4" in f.message]
    assert "leaf P3_FOREIGN of phase P3 is defined on 01-workflow/p07-error-process.md, but P3 is owned by 01-workflow/p03-exploratory-diagnostics.md" in messages
    assert "leaf P4_LOST: phase P4 has no owner page (no inventory row P4)" in messages
    assert not any("P3_HOME" in m for m in messages)


def test_purpose_and_representation_leaves_may_sit_on_their_sub_chart_pages():
    rows = [audit.Row("P2", "P2: Purpose", "MASTER", (19,), "01-workflow/p02-purpose/index.md#p2-purpose"),
            audit.Row("P2_CPD_PELT", "PELT", "P2", (30,), "01-workflow/p02-purpose/04-change-point-detection.md#sub-chart"),
            audit.Row("P2_STRAY", "Stray", "P2", (30,), "01-workflow/p02-purpose/04-change-point-detection.md#sub-chart")]
    sub_chart = diagram('graph TD\n    P2_CPD_PELT["PELT"]\n', "01-workflow/p02-purpose/04-change-point-detection.md#mermaid-1")
    outside = diagram('graph TD\n    P2_STRAY["Stray"]\n', "01-workflow/p03-exploratory-diagnostics.md#mermaid-1")
    messages = [f.message for f in audit.check_nodes_vs_inventory([sub_chart, outside], rows)]
    assert not any("P2_CPD_PELT" in m for m in messages)
    assert "leaf P2_STRAY of phase P2 is defined on 01-workflow/p03-exploratory-diagnostics.md, but P2 is owned by 01-workflow/p02-purpose/" in messages
