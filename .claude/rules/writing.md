# Writing rules

Source of truth for prose and structure decisions. Appearance is governed by `DESIGN-SYSTEM.md`; the framework design is `planning/2026-10-06-flowchart-framework-design.md`.

## Before writing a section

1. Locate its leaf node in a workflow sub-diagram, or add one. Add the inventory row (`docs/flowcharts/inventory.yml`): `id`, `label`, `phase`, `areas`, `section`.
2. Decide: method section (what to do, when) or theory section (`kind: theory` front matter, linked from a method section or a glossary derivation).
3. Check the concept is not already developed elsewhere (`grep` the glossary `reference` fields). If it is, link; do not re-explain.

## While writing

- One claim per sentence. Name methods as glossary terms; the glossary highlights them.
- No multi-step derivation in the body. Put it in the term's `derivation` as numbered "because" steps, each naming the assumption it uses, with `depends_on` listing the upstream terms. Every noun in the chain gets its own term entry.
- For time series, factorise likelihoods by the chain rule into conditional densities; i.i.d. is the special case. Never derive time-series MLE from an i.i.d. product.
- Follow the canonical chapter template and the equation → `(Read: …)` pairing from the design system.
- Outcome terminals name model → estimator → inference.

## After writing

- `python scripts/audit_flowcharts.py` reports zero errors.
- `mkdocs build --strict` passes.
