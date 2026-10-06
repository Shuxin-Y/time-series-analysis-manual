import textwrap

import audit_flowcharts as audit
import sitekit


def make_docs(tmp_path):
    docs = tmp_path / "docs"
    (docs / "glossary").mkdir(parents=True)
    (docs / "00-foundations").mkdir()
    (docs / "reference" / "04-estimation").mkdir(parents=True)
    (docs / "01-workflow").mkdir()
    (docs / "00-foundations" / "stochastic-processes.md").write_text("# Stochastic processes\n\n## Independence\n\n## Law of large numbers\n", encoding="utf-8")
    (docs / "reference" / "04-estimation" / "index.md").write_text("# Estimation\n\n## Joint density\n\nThe joint density is defined here. See [theory](theory.md).\n", encoding="utf-8")
    (docs / "reference" / "04-estimation" / "theory.md").write_text("---\nkind: theory\n---\n# Why MLE\n", encoding="utf-8")
    (docs / "reference" / "04-estimation" / "stray.md").write_text("# Stray\n", encoding="utf-8")
    (docs / "01-workflow" / "index.md").write_text("# Workflow\n", encoding="utf-8")
    sitekit.write_project(tmp_path, {})
    return docs


ROOTS = textwrap.dedent('''
    terms:
      - term: "Independence"
        definition: "d"
        foundation: true
        reference: "00-foundations/stochastic-processes.md#independence"
      - term: "Law of large numbers"
        definition: "d"
        foundation: true
        reference: "00-foundations/stochastic-processes.md#law-of-large-numbers"
''')


GLOSSARY = textwrap.dedent('''
    terms:
      - term: "Joint density"
        definition: "d"
        derivation: "1. because of [Why MLE](theory.md)"
        depends_on: ["Independence", "Law of large numbers"]
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Dead end"
        definition: "d"
        depends_on: []
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Not yet"
        definition: "d"
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Cycle A"
        definition: "d"
        depends_on: ["Cycle B"]
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Cycle B"
        definition: "d"
        depends_on: ["Cycle A"]
        reference: "reference/04-estimation/index.md#joint-density"
      - term: "Bad ref"
        definition: "d"
        foundation: true
        reference: "reference/04-estimation/index.md#nope"
      - term: "Unknown dep"
        definition: "d"
        depends_on: ["Ghost"]
        reference: "reference/04-estimation/index.md#joint-density"
''')


def test_load_glossary_merges_files_and_flags_duplicates(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "glossary" / "a.yml").write_text('terms:\n  - term: "X"\n    definition: "d"\n', encoding="utf-8")
    (docs / "glossary" / "b.yml").write_text('terms:\n  - term: "X"\n    definition: "d"\n  - term: "Y"\n    definition: "d"\n', encoding="utf-8")
    (docs / "glossary" / "index.yml").write_text("files: [a.yml, b.yml]\n", encoding="utf-8")
    terms, findings = audit.load_glossary(docs / "glossary")
    assert [t["term"] for t in terms] == ["X", "Y"]
    assert terms[0]["_file"] == "a.yml"
    assert any("also defined in a.yml" in f.message for f in findings)


def test_check_glossary_levels(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "glossary" / "stochastic-processes.yml").write_text(ROOTS, encoding="utf-8")
    (docs / "glossary" / "04-estimation.yml").write_text(GLOSSARY, encoding="utf-8")
    terms, _ = audit.load_glossary(docs / "glossary")
    findings = audit.check_glossary(terms, sitekit.site(tmp_path))
    by_term = {}
    for f in findings:
        by_term.setdefault(f.where.split(":", 1)[-1], []).append(f)
    assert "Joint density" not in by_term
    assert "Independence" not in by_term
    assert by_term["Not yet"][0].level == "warning"
    assert "depends_on absent" in by_term["Not yet"][0].message
    assert any(f.level == "error" and "non-foundation" in f.message for f in by_term["Dead end"])
    assert any("cycle" in f.message for f in findings)
    assert any("anchor #nope not found" in f.message for f in by_term["Bad ref"])
    assert any("'Ghost' is not a glossary term" in f.message for f in by_term["Unknown dep"])


def test_check_sections_method_theory_and_stray(tmp_path):
    docs = make_docs(tmp_path)
    rows = [audit.Row("P8_JOINT", "Joint density", "P8", (4,), "reference/04-estimation/index.md#joint-density")]
    terms = [{"term": "x", "derivation": ""}]
    findings = audit.check_sections(sitekit.site(tmp_path), rows, terms)
    wheres = {f.where: f.message for f in findings}
    assert "reference/04-estimation/theory.md" not in wheres            # linked from index.md
    assert "neither in the inventory" in wheres["reference/04-estimation/stray.md"]
    assert "01-workflow/index.md" not in wheres                         # index pages exempt


def test_check_sections_unlinked_theory_is_an_error(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "reference" / "04-estimation" / "index.md").write_text("# Estimation\n\n## Joint density\n", encoding="utf-8")
    rows = [audit.Row("P8_JOINT", "Joint density", "P8", (4,), "reference/04-estimation/index.md#joint-density")]
    findings = audit.check_sections(sitekit.site(tmp_path), rows, [])
    assert any(f.where == "reference/04-estimation/theory.md" and "not linked" in f.message for f in findings)


def test_nav_pages_flattens_the_loaded_config(tmp_path):
    sitekit.write_project(tmp_path, {}, nav=[{"Home": "index.md"},
                                             {"Foundations": ["00-foundations/a.md", {"Sub": ["00-foundations/b.md"]}]},
                                             "reference/04-estimation/index.md",
                                             {"External": "https://example.org/"}])
    assert sitekit.site(tmp_path).nav_pages() == ["index.md", "00-foundations/a.md", "00-foundations/b.md", "reference/04-estimation/index.md"]


def test_first_mention_warning_only_when_pages_differ(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "00-foundations" / "early.md").write_text("# Early\n\nThe joint density appears here first.\n", encoding="utf-8")
    terms = [{"term": "Joint density", "_file": "g.yml", "reference": "reference/04-estimation/index.md#joint-density"},
             {"term": "Independence", "_file": "g.yml", "reference": "00-foundations/stochastic-processes.md#independence"}]
    sitekit.write_project(tmp_path, {}, nav=["00-foundations/early.md", "00-foundations/stochastic-processes.md", "reference/04-estimation/index.md"])
    findings = audit.first_mention_warnings(sitekit.site(tmp_path), terms)
    assert len(findings) == 1
    assert findings[0].level == "warning"
    assert "first mentioned on 00-foundations/early.md" in findings[0].message


def test_theory_page_cleared_only_by_an_exact_glossary_derivation_link(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "reference" / "04-estimation" / "index.md").write_text("# Estimation\n\n## Joint density\n", encoding="utf-8")
    rows = [audit.Row("P8_JOINT", "Joint density", "P8", (4,), "reference/04-estimation/index.md#joint-density")]
    linked = [{"term": "x", "derivation": "1. because [why](reference/04-estimation/theory.md#why-mle)"}]
    loose = [{"term": "x", "derivation": "1. because [why](theory.md) and reference/04-estimation/theory.md"}]
    site = sitekit.site(tmp_path)
    assert not any(f.where == "reference/04-estimation/theory.md" for f in audit.check_sections(site, rows, linked))
    assert any(f.where == "reference/04-estimation/theory.md" and "not linked" in f.message
               for f in audit.check_sections(site, rows, loose))


def test_theory_page_is_not_cleared_by_a_link_to_another_page_with_the_same_name(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "reference" / "10-volatility").mkdir()
    (docs / "reference" / "10-volatility" / "theory.md").write_text("---\nkind: theory\n---\n# Why GARCH\n", encoding="utf-8")
    rows = [audit.Row("P8_JOINT", "Joint density", "P8", (4,), "reference/04-estimation/index.md#joint-density")]
    findings = audit.check_sections(sitekit.site(tmp_path), rows, [])
    wheres = {f.where for f in findings if "not linked" in f.message}
    assert wheres == {"reference/10-volatility/theory.md"}


def glossary_findings(tmp_path, files):
    docs = make_docs(tmp_path)
    for name, body in files.items():
        (docs / "glossary" / name).write_text(textwrap.dedent(body), encoding="utf-8")
    terms, findings = audit.load_glossary(docs / "glossary")
    return findings + audit.check_glossary(terms, sitekit.site(tmp_path))


def test_glossary_yaml_errors_and_duplicate_keys_are_findings(tmp_path):
    findings = glossary_findings(tmp_path, {
        "stochastic-processes.yml": 'terms:\n  - term: "Independence"\n    reference: "00-foundations/stochastic-processes.md#independence"\n    reference: "00-foundations/stochastic-processes.md#law-of-large-numbers"\n',
        "04-estimation.yml": "terms: [unclosed\n",
    })
    messages = {f.where: f.message for f in findings}
    assert "duplicate key 'reference'" in messages["stochastic-processes.yml"]
    assert "invalid YAML" in messages["04-estimation.yml"]


def test_depends_on_must_be_a_list_of_names(tmp_path):
    findings = glossary_findings(tmp_path, {"04-estimation.yml": '''
        terms:
          - term: "Joint density"
            depends_on: "Independence"
            reference: "reference/04-estimation/index.md#joint-density"
    '''})
    assert [f.message for f in findings if f.level == "error"] == ["depends_on must be a list of term names"]


def test_foundation_terms_live_in_part_0_and_have_no_dependencies(tmp_path):
    findings = glossary_findings(tmp_path, {
        "04-estimation.yml": '''
            terms:
              - term: "Joint density"
                foundation: true
                reference: "reference/04-estimation/index.md#joint-density"
        ''',
        "stochastic-processes.yml": '''
            terms:
              - term: "Independence"
                foundation: true
                depends_on: ["Joint density"]
                reference: "00-foundations/stochastic-processes.md#independence"
        ''',
    })
    messages = {f.where: f.message for f in findings}
    assert "must be homed under 00-foundations/" in messages["04-estimation.yml:Joint density"]
    assert "cannot depend on other terms" in messages["stochastic-processes.yml:Independence"]


def test_term_must_live_in_the_file_named_after_its_reference_page(tmp_path):
    findings = glossary_findings(tmp_path, {"misc.yml": '''
        terms:
          - term: "Independence"
            foundation: true
            reference: "00-foundations/stochastic-processes.md#independence"
          - term: "Joint density"
            depends_on: ["Independence"]
            reference: "reference/04-estimation/index.md#joint-density"
    '''})
    messages = sorted(f.message for f in findings)
    assert messages == ["term belongs in glossary/04-estimation.yml, the file named after its reference page",
                        "term belongs in glossary/stochastic-processes.yml, the file named after its reference page"]


def test_each_cycle_is_reported_once(tmp_path):
    make_docs(tmp_path)
    terms = [{"term": n, "_file": "04-estimation.yml", "depends_on": [d], "reference": "reference/04-estimation/index.md#joint-density"}
             for n, d in (("B", "C"), ("C", "A"), ("A", "B"))]
    cycles = [f.message for f in audit.check_glossary(terms, sitekit.site(tmp_path)) if "cycle" in f.message]
    assert cycles == ["cycle: A -> B -> C -> A"]


def test_chain_walk_is_linear_on_shared_upstream_terms(tmp_path):
    import time
    layers = 40
    terms = [{"term": "ROOT", "foundation": True, "reference": "00-foundations/stochastic-processes.md#independence", "_file": "stochastic-processes.yml"}]
    for layer in range(layers):
        below = ["ROOT"] if layer == 0 else [f"L{layer - 1}A", f"L{layer - 1}B"]
        for side in "AB":
            terms.append({"term": f"L{layer}{side}", "depends_on": below, "_file": "04-estimation.yml",
                          "reference": "reference/04-estimation/index.md#joint-density"})
    make_docs(tmp_path)
    start = time.perf_counter()
    findings = audit.check_glossary(terms, sitekit.site(tmp_path))
    assert time.perf_counter() - start < 2
    assert [f for f in findings if f.level == "error"] == []


def test_every_h2_under_reference_and_workflow_is_a_content_unit_or_structural(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "reference" / "04-estimation" / "index.md").write_text(
        "# Estimation\n\n## Joint density\n\n## Maximum likelihood\n\n## References\n\n### Detail\n", encoding="utf-8")
    (docs / "01-workflow" / "index.md").write_text("# Workflow\n\n## Master diagram\n\n## EGARCH\n", encoding="utf-8")
    terms = [{"term": "Joint density", "reference": "reference/04-estimation/index.md#joint-density"}]
    findings = audit.check_headings(sitekit.site(tmp_path), [], terms)
    assert sorted(f.where for f in findings) == ["01-workflow/index.md#egarch", "reference/04-estimation/index.md#maximum-likelihood"]


def test_first_mention_scan_covers_workflow_pages(tmp_path):
    docs = make_docs(tmp_path)
    (docs / "01-workflow" / "p00-data.md").write_text("# P0\n\nImputation fills gaps.\n", encoding="utf-8")
    (docs / "reference" / "31-data").mkdir(parents=True)
    (docs / "reference" / "31-data" / "index.md").write_text("# Data\n\nImputation again.\n", encoding="utf-8")
    sitekit.write_project(tmp_path, {}, nav=["01-workflow/p00-data.md", "reference/31-data/index.md"])
    terms = [{"term": "Imputation", "_file": "p00-data.yml", "reference": "01-workflow/p00-data.md#p0"}]
    assert audit.first_mention_warnings(sitekit.site(tmp_path), terms) == []
