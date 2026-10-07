# Writing rules

Single home of the content rules: what a section contains and where a concept lives. Appearance is governed by `DESIGN-SYSTEM.md`; the framework design is `planning/2026-10-06-flowchart-framework-design.md` (section 9).

## Section kinds

- A **method** section says what to do and when. It is a leaf node of a flowchart sub-diagram and has an inventory row in `docs/flowcharts/inventory.yml` (`id`, `label`, `phase`, `areas`, `section`).
- A **theory** section says why something holds. Its page carries `kind: theory` in the front matter and is reachable: start from every method page and every area landing page (`reference/NN-*/index.md`), then repeatedly add every page a reachable page links to and every page linked from the derivation (exact `path.md#anchor` form) of a term homed on a reachable page; pages that only reach each other are not reachable, because none of them is a seed.
- Every non-index page under `docs/reference/` and `docs/01-workflow/` is a method page or a theory page. On every page there, index pages included, every H2 is an inventory anchor (a leaf's section) or a structural heading (`STRUCTURAL_H2`). Headings H3 and deeper under a leaf's H2 belong to that leaf and need no node of their own. An H3 or deeper heading inherits its H2's status: under a leaf's H2 it belongs to that leaf; under a structural H2, or before the first H2, it is not allowed unless it is itself a leaf's heading or the page is `kind: theory`. A glossary `reference` anchor is valid as a leaf's own heading, as an H3 or deeper under a leaf's H2, or as any heading, H2 included, on a `kind: theory` page. The structural headings are the `STRUCTURAL_H2` constant in `scripts/audit_flowcharts.py`.

## Single source

- Every concept has one home: the section where it is first developed in `nav:` order. The glossary `reference` points there, and the drawer shows it as "First developed in".
- The first occurrence develops the concept in full; later occurrences write only the term, which the glossary highlights. Do not re-explain.
- Sections on a page appear in the order the page's diagram reaches them; a re-scaffolded section is moved to that position.
- Part 0 takes only concepts needed before any method can be stated, and concepts shared across several phases with no natural home.
- Appendix pages are link indexes and contain no explanations.

## Why-chains live in the glossary drawer

- A term may carry `derivation` (numbered "because" steps, each naming the assumption it uses) and `depends_on` (upstream term names). Part 0 roots carry `foundation: true`, are homed under `docs/00-foundations/` and depend on nothing. Any other term is homed under `docs/reference/`, `docs/01-workflow/` or `docs/00-foundations/`; a home anywhere else (appendices, the home page, the showcase) is an error.
- The drawer renders them as "Why it holds", "Rests on" (chips that open the upstream term, with a back stack) and "First developed in".
- Every noun that appears in a chain is itself a term with its own entry: "joint density" is a term, not a step inside the MLE chain.
- For time series, factorise likelihoods by the chain rule into conditional densities; i.i.d. is the special case. Never derive time-series MLE from an i.i.d. product.

## Before writing a section

1. Locate its leaf node in a workflow sub-diagram, or add one, and add its inventory row. Its `section` (and any glossary `reference`) points at a heading anchor; ids on paragraphs, `<a id>` tags and footnotes are not targets.
2. Decide: method section or theory section.
3. Check the concept is not already developed elsewhere (`grep` the glossary `reference` fields). If it is, link; do not re-explain.

## While writing

- One claim per sentence. Name methods as glossary terms; the glossary highlights them.
- No multi-step derivation in the body; it goes in the term's `derivation`.
- Follow the canonical chapter template and the equation → `(Read: …)` pairing from the design system.
- Outcome terminals in diagrams name **model → estimator → inference**, in that order.
- Purpose sub-charts index the spine (spec §7.1). The reader's route is the spine; a chart indexes it and may omit phases but never reorders them. The spine's purpose-flag diamonds (P6 entry, P10, P11) make every purpose's route total. A chart that refs a phase's leaves also draws that phase's box, before those leaves.

## After writing

- `python scripts/audit_flowcharts.py`, run from the repository root, reports zero errors.
- `mkdocs build --strict` passes.
