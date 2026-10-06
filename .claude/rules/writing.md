# Writing rules

Single home of the content rules: what a section contains and where a concept lives. Appearance is governed by `DESIGN-SYSTEM.md`; the framework design is `planning/2026-10-06-flowchart-framework-design.md` (section 9).

## Section kinds

- A **method** section says what to do and when. It is a leaf node of a flowchart sub-diagram and has an inventory row in `docs/flowcharts/inventory.yml` (`id`, `label`, `phase`, `areas`, `section`).
- A **theory** section says why something holds. Its page carries `kind: theory` in the front matter and is linked from at least one method section, or from a glossary derivation in the exact `path.md#anchor` form.
- Every non-index page under `docs/reference/` and `docs/01-workflow/` is a method page or a theory page. On every page there, index pages included, every H2 is an inventory anchor (a leaf's section) or a structural heading (`STRUCTURAL_H2`). Headings H3 and deeper under a leaf's H2 belong to that leaf and need no node of their own. A glossary `reference` anchor is valid as a leaf's own heading, as an H3 or deeper under a leaf's H2, or as any heading, H2 included, on a `kind: theory` page. The structural headings are listed in `DESIGN-SYSTEM.md` (notation rules, "Content units").

## Single source

- Every concept has one home: the section where it is first developed in `nav:` order. The glossary `reference` points there, and the drawer shows it as "First developed in".
- The first occurrence develops the concept in full; later occurrences write only the term, which the glossary highlights. Do not re-explain.
- Part 0 takes only concepts needed before any method can be stated, and concepts shared across several phases with no natural home.
- Appendix pages are link indexes and contain no explanations.

## Why-chains live in the glossary drawer

- A term may carry `derivation` (numbered "because" steps, each naming the assumption it uses) and `depends_on` (upstream term names). Part 0 roots carry `foundation: true`, are homed under `docs/00-foundations/` and depend on nothing.
- The drawer renders them as "Why it holds", "Rests on" (chips that open the upstream term, with a back stack) and "First developed in".
- Every noun that appears in a chain is itself a term with its own entry: "joint density" is a term, not a step inside the MLE chain.
- For time series, factorise likelihoods by the chain rule into conditional densities; i.i.d. is the special case. Never derive time-series MLE from an i.i.d. product.

## Before writing a section

1. Locate its leaf node in a workflow sub-diagram, or add one, and add its inventory row.
2. Decide: method section or theory section.
3. Check the concept is not already developed elsewhere (`grep` the glossary `reference` fields). If it is, link; do not re-explain.

## While writing

- One claim per sentence. Name methods as glossary terms; the glossary highlights them.
- No multi-step derivation in the body; it goes in the term's `derivation`.
- Follow the canonical chapter template and the equation → `(Read: …)` pairing from the design system.
- Outcome terminals in diagrams name **model → estimator → inference**, in that order.

## After writing

- `python scripts/audit_flowcharts.py`, run from the repository root, reports zero errors.
- `mkdocs build --strict` passes.
