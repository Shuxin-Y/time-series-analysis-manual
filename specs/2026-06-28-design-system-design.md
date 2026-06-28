# Design System — Design Spec

- **Date:** 2026-06-28
- **Status:** Draft (pending review)
- **Author:** Shuxin-Y (with Claude)
- **Topic:** Extract the established visual/structural design into a single, versioned design-system document so future chapters share the same appearance.

> Spec location note: this spec lives in repo-root `specs/`, **not** under `docs/`, because `docs/` is the published MkDocs site and internal specs should not be published.

---

## 1. Problem & Goal

The introduction layer (chapters `00-introduction/*`) and the supporting CSS/JS have
established a consistent visual and structural identity: an academic brand palette,
typed admonitions, hypothesis-test and decision-rule boxes, an interactive glossary
drawer, pronunciation guides, decision flowcharts, and styled tables. These conventions
are currently **implicit** — encoded partly in `docs/stylesheets/extra.css`, partly in
the `.claude/rules/` agent-instruction files (which are git-ignored), and partly only as
patterns visible in the intro chapters.

**Goal.** Produce one authoritative, version-controlled **design system** document
(`DESIGN-SYSTEM.md`, repo root) that is the single source of truth for the book's
*appearance*, readable by both human contributors and Claude, so that every future
chapter is a fill-in-the-blanks exercise against a known standard.

This is a **design system**, not merely a style guide: it is organized into the standard
tiers — principles → foundations (design tokens) → components & patterns → governance —
and is treated as a living, versioned, single source of truth.

## 2. Scope

**In scope (appearance):** visual identity (brand tokens, typography, spacing), the
component catalog (admonitions, custom boxes, interactive components), composition
patterns (chapter template, decision-flowchart notation, table standard, data-viz
standard), layout/responsive/print behavior, accessibility target, and governance.

**Out of scope (referenced, not absorbed):** prose voice (`writing.md`), mathematical
notation conventions (`notation.md`), Python code style (`code.md`), and glossary data
standards (`glossary.md`) remain in their own `.claude/rules/` files. The design system
**links to** them rather than restating them.

**Non-goals:** no redesign of the current look (the maintainer is satisfied with it); no
creation of new brand artwork (logo/favicon) now — only a reserved spec for them; no
change to published content beyond what governance later requires.

## 3. Decisions

| # | Decision | Resolution |
|---|---|---|
| Audience & home | Who reads it, where it lives | Single version-controlled doc for **both human and Claude**; `.claude/rules` appearance files deduplicated to **pointers** at it |
| Scope | How much it absorbs | **Appearance only** (visual + structure + figures); notation/writing/code stay separate |
| Filename/location | — | `DESIGN-SYSTEM.md` at **repo root** (not under `docs/`, so unpublished); may graduate to a `design-system/` directory if it grows |
| Data-viz palette | Chart/diagram colours | **Brand-derived palette as default**, plus a **colorblind-safe alternative** that authors can switch to |
| Matplotlib | Reusable figure defaults | Ship a **`.mplstyle`** (or rc snippet) so every static figure is generated consistently |
| Brand assets | Logo/favicon/social card | Option (b): **document current icon usage + specify the asset spec now** (sizes, social-card template, files under `docs/assets/`) as a ready-to-fill placeholder |
| Accessibility | Target standard | **WCAG 2.1 AA**; audit palette pairs and flag any that need care; figure alt-text required; colour never the sole signal |
| Governance | Versioning & change process | **Version + `## Changelog`**; deprecation noted in the changelog; changes go via **PR + passing `mkdocs build --strict`** |
| Components 5–7 | Interactive / layout / naming | All folded in (extracted from existing CSS/JS) |
| Flowchart notation | Decision-flowchart grammar | Full notation (see §5.4) — diamond decisions with **terse labels** (Option A), type-based shapes & colours, equal-weight sizing, edge curve-by-scenario, edge-type semantics |
| Tables | Predetermined table standard | Full table standard (see §5.5) — patterns, structural rules, semantic cell colour, accessibility |

The document is **living**: further refinements are expected during writing.

## 4. Artifacts produced

1. **`DESIGN-SYSTEM.md`** (repo root) — the design system document (structure in §5).
2. **`docs/stylesheets/`** additions/edits — table semantic-cell classes; optional
   `min-width` floor for Mermaid nodes; any small CSS needed to support documented
   components. (Existing tokens/components are documented, not rewritten.)
3. **`docs/assets/brand.mplstyle`** — the matplotlib style file (tracked) encoding the
   brand-derived default palette and figure defaults, plus the colorblind-safe variant. Its
   **full contents are also embedded verbatim in `DESIGN-SYSTEM.md`** (a fenced code block
   in §5.6) so the doc is the readable source of truth; the shipped file is the runnable
   copy. (Only the reference mechanism is deferred — see §7.)
4. **`brand.py`** (repo root) — helper exposing `use_brand_style(palette="brand" | "cb")`,
   resolving `docs/assets/brand.mplstyle` via `__file__` so figure code is CWD-independent.
5. **Mermaid `classDef` snippets** — the canonical node-type class set (two palettes:
   brand + colorblind-safe), to be copy-pasted into diagrams.
6. **`.claude/rules/chapters.md` and `.claude/rules/figures.md`** — **hybrid refactor** on
   the principle *design system = how the book looks; `.claude/rules` = how Claude works*.
   Appearance content (admonition colours, chapter structure, Mermaid styling) moves into
   `DESIGN-SYSTEM.md` and is replaced by a one-line pointer. **Genuinely operational notes
   stay** because they are workflow, not appearance — e.g., "validate Mermaid with the
   `validate-mermaid` skill," "update `mkdocs.yml` `nav:` when adding a page," and the
   "applies when editing `docs/*`" scoping.
7. **`CLAUDE.md`** — add a reference directing readers to `DESIGN-SYSTEM.md`.

> **Tracked vs. ignored.** `.claude/` is git-ignored, so a pointer left in
> `chapters.md`/`figures.md` is visible only to Claude in this working tree, not to anyone
> cloning the repo. Therefore the **human-facing** single-source-of-truth pointer lives in
> tracked files: `CLAUDE.md` and `DESIGN-SYSTEM.md` itself (both tracked). Editing the
> `.claude/rules` files to pointers is a courtesy for Claude's context only; the plan must
> not rely on them for human discoverability.

## 5. `DESIGN-SYSTEM.md` structure

### Tier 0 — Principles
What the design optimizes for, in a few sentences: academic gravitas (serif display
headings), readability (1.75 prose line-height, body-size floor), accessibility
(pronunciation guides, dark mode, print, WCAG AA), and consistency. States the three-tier
model and how to read the document.

**Catalog vs. implementation (read this first).** "Single source of truth" here has a
deliberate asymmetry: this document is the authoritative **catalog/specification** of the
design (what exists, when to use it, the intended values); `extra.css`/`*.js` are the
authoritative **implementation** (what the browser renders). When they diverge, the CSS/JS
is the runtime truth and the doc is corrected to match. The doc is the map, not the
territory.

### Tier 1 — Foundations (design tokens)
- **Colour tokens.** The `:root` custom properties from `extra.css` (Cerulean, Burgundy,
  Thistle, Navajo, Sunset and their light/dark/deep variants) with hex, **semantic role**,
  and light (`default`) / dark (`slate`) mapping.
- **Typography scale.** Source Serif 4 (H1–H3) vs Inter (H4–H6 + chrome); the size/weight
  ladder; H2 underrule; prose line-height; OpenType features.
- **Spacing & utilities.** `mt-*`/`mb-*`, `text-center`/`text-right`, `highlight-text`.
- **Layout, responsive & print.** Content width, the 768px mobile breakpoint, scrollable
  tables/diagrams, and the print stylesheet — documented from `extra.css`.

### Tier 2a — Components

Each documented as: **purpose · when to use · markup (copy-paste) · rendered appearance ·
do/don't**.
- **Admonitions:** `theorem` (Burgundy), `definition` (Thistle), `note`/remark (Cerulean),
  `abstract` (Navajo) — mapped to their CSS and semantic use.
- **`.hypothesis-test` box** (auto H₀/H₁ labels) and **`.decision-rule` box**.
- **Annotations + "common alternative forms"** (`<div class="annotate">` + numbered
  footnotes) — the alternative-notation pattern from the intro.
- **`(Read: …)` pronunciation guide** — required after display equations (accessibility).
- **`## References` block** — Chicago author-date, `id="references"` for the smaller
  styling.
- **Interactive components:** the **glossary drawer** (`glossary.css` + `glossary.js`),
  **tabbed sets**, **`abbr` tooltips**, **Material annotations** — including hover/focus
  and motion states.

### Tier 2b — Patterns (composition)

- **Canonical chapter template** + the content flow (conceptual intro → definition → time-
  series context → consequences → diagnostics → code → summary table → cross-references).
- **Equation → pronunciation-guide pairing.**
- **Hypothesis-test layout** (H₀ / H₁ / statistic / decision rule / interpretation).
- **Page-footer navigation** convention.
- **Decision-Flowchart Notation** (§5.4).
- **Table Standard** (§5.5).
- **Data-Visualization Standard** (§5.6).

### 5.4 Decision-Flowchart Notation
Controlled vocabulary mapping node **shape** and **colour** to **meaning**, applied via
reusable Mermaid `classDef`s.

**Shapes by role** (ANSI/ISO flowchart semantics):

| Role | Shape | Mermaid | `classDef` |
|---|---|---|---|
| Start / end | stadium | `([ ])` | `terminator` |
| Process / action | rectangle | `[ ]` | `process` |
| Decision / test | diamond | `{ }` | `decision` |
| Data (I/O) | parallelogram | `[/ /]` | `data` |
| Outcome — sufficient | rectangle | `[ ]` | `good` |
| Outcome — escalate | rectangle | `[ ]` | `escalate` |
| Outcome — problem/replace | rectangle | `[ ]` | `problem` |
| Reference to another chapter | subroutine | `[[ ]]` | `ref` |

**Colours by type** (brand-default set; structural nodes muted, outcomes saturated):

| `classDef` | Fill | Stroke |
|---|---|---|
| `terminator` | #E6F2F7 | #007BA7 |
| `process` | #FFFFFF/#F7F7F7 | #5A6B73 |
| `decision` | #EFE7F0 | #9B7FA7 |
| `data` | #FFF4E0 | #C9A55E |
| `good` | #DCEFD8 | #4A7A3F |
| `escalate` | #FFE9C2 | #C9A55E |
| `problem` | #F2D9DE | #800020 |
| `ref` | #F7F7F7 (dashed) | #5A6B73 |

A **colorblind-safe** `classDef` set is provided alongside, drawn from the Okabe–Ito
palette (the canonical 8-colour CVD-safe set) and mapped to the same roles:

| `classDef` | Fill (Okabe–Ito) | Role colour name |
|---|---|---|
| `terminator` | #56B4E9 | sky blue |
| `process` | #FFFFFF | white (neutral) |
| `decision` | #0072B2 | blue |
| `data` | #F0E442 | yellow |
| `good` | #009E73 | bluish green |
| `escalate` | #E69F00 | orange |
| `problem` | #D55E00 | vermillion |
| `ref` | #999999 (dashed) | grey |

(Reddish-purple #CC79A7 and black #000000 complete the Okabe–Ito set and are held in
reserve for additional categorical series in figures.) Authors select the brand or
colorblind-safe set per diagram by applying the corresponding `classDef` block.

**Rules.**
- **Decision labels are terse** (≤ ~3 words, a single question). Method names (e.g.,
  "ADF + KPSS") move onto the incoming process node or an attached note; branch logic
  goes on edge labels. This keeps diamonds compact (Option A — root-cause fix for the
  diamond-size problem; the parallelogram is *not* repurposed as a decision shape because
  it conventionally means I/O).
- **Equal visual weight per rank:** labels on the same rank kept to similar length, plus a
  CSS `min-width`/padding floor on Mermaid node shapes. Exact equality is not guaranteed
  by Mermaid; the rule is "equal visual weight."
- **Edge curve by scenario:** decision flowcharts (`TD`) use `linear`/`step` (crisp);
  sequential pipelines (`LR`) use `basis` (smooth). Set per-diagram via
  `%%{init: {"flowchart": {"curve": "…"}}}%%`.
- **Edge-type semantics:** `-->` primary flow; `-.->` optional/secondary/feedback; `==>`
  highlighted main route. Decision branches **always labeled** (`-->|Yes|`).
- **Direction:** `TD` for decision workflows, `LR` for sequences.
- **Node IDs:** `SCREAMING_SNAKE_CASE`, semantic (not `A`/`B`).
- **Text:** no emojis; `<br/>` for line breaks; outcome terminals name *model → estimator
  → inference* in order.
- **Accessibility:** type is encoded by **shape first**; colour reinforces; outcome
  category also stated in node text, so colour is never the sole signal (WCAG 1.4.1).

### 5.5 Table Standard
Tables receive the same predetermined treatment as figures.

**Patterns:** (1) notation table (symbol · meaning · first-use), (2) comparison table,
(3) decision matrix (combined test outcomes → verdict; cells may carry semantic colour),
(4) summary table, (5) results table (estimates · SE · p-values).

**Structural rules:**
- Header row mandatory; text left-aligned, **numerics decimal/right-aligned** with
  `tabular-nums`.
- **Consistent decimal places per column**; uniform p-value formatting; `—` for N/A,
  never a blank cell.
- **Units in the header**, not per row.
- **Self-contained caption**, numbered `Table N.M` (cross-reference labels per
  `writing.md`).
- Soft cap ~5–6 columns before transpose/split; wide tables scroll on mobile.

**Semantic cell colour** (decision matrices) reuses the chart/flowchart semantic palette:
sufficient `#DCEFD8`, escalate `#FFE9C2`, problem `#F2D9DE`. **Mechanism:** the
enabled extension stack (`tables`, `attr_list`, `md_in_html`) offers no Markdown-native
per-cell colouring — `attr_list` cannot target an individual `<td>`, and no `pymdownx.*`
extension styles table cells. Therefore colour-coded decision matrices are written as an
HTML `<table markdown>` (via the already-enabled `md_in_html`) using **CSS classes**
(`.decision-matrix td.good` / `.escalate` / `.problem` defined in `extra.css`), **not**
inline `style=` — so the semantic hex values stay tokenized in one place. Ordinary tables
remain Markdown pipe tables; only matrices needing cell colour use the HTML mechanism.

**Accessibility:** `<th>` scope; AA contrast on tinted cells; category stated in cell
text so colour is not the sole signal. The worked decision-matrix example in the doc
demonstrates this — each coloured cell carries its verdict as text (e.g., a green cell
reads "Sufficient", not green alone).

### 5.6 Data-Visualization Standard
- **Default palette** derived from the brand: categorical = Cerulean `#007BA7`, Burgundy
  `#800020`, Thistle-dark `#9B7FA7`, Navajo-dark `#C9A55E`, Sunset `#B87D6C`; sequential =
  single-hue Cerulean ramp; semantic = sage/amber/Burgundy as above.
- **Colorblind-safe alternative** — the Okabe–Ito categorical cycle, selectable per
  figure: #E69F00, #56B4E9, #009E73, #F0E442, #0072B2, #D55E00, #CC79A7, #000000.
- **Matplotlib style** encoding figure size, DPI, fonts, grid, and both palettes, so every
  static figure is consistent. The full `.mplstyle` contents are **embedded in this section
  as a fenced code block** (readable source of truth) and shipped as a runnable file at
  **`docs/assets/brand.mplstyle`** (tracked).
- **Reference mechanism.** A small helper module `brand.py` (repo root) resolves the style
  path via `__file__` and exposes `use_brand_style(palette="brand" | "cb")`; figure code
  calls it with one import, no path arithmetic and CWD-independent. (Rejected: a relative
  `plt.style.use("…/brand.mplstyle")` — fragile CWD; a registered style name — needs an
  install step; a `pymdownx.snippets` include — that is a build-time doc include, not a
  runtime loader.) The helper is for the **book's own figure-generation pipeline** that
  produces the committed PNG/SVGs; copy-pasted reader code is illustrative and cannot be
  made self-contained regardless of mechanism.
- **Mermaid** uses the `classDef` sets from §5.4 (replacing today's ad-hoc fills).

### Tier 3 — Governance
- **Single source of truth:** tokens/components are *defined* in `extra.css`/`*.js`; this
  doc is the authoritative *catalog*; the two must stay in sync. Where they diverge, the
  CSS is the runtime truth and the doc is updated.
- **Naming conventions:** chapter dirs (`NN-kebab-case/`), section anchors, CSS class
  names, component IDs, glossary term placement.
- **Brand-asset spec (reserved):** favicon sizes, social-card template, files under
  `docs/assets/` — placeholder until artwork exists; current Material icon usage
  documented.
- **How to add/modify a component:** add/adjust CSS → document here with a copy-paste
  example → verify build.
- **Versioning:** semantic-ish version at the top; a `## Changelog` at the bottom with
  dated entries. Deprecations are noted in the changelog.
- **Change process:** changes land via PR; `mkdocs build --strict` must pass.
- **New-chapter checklist:** a short list ("to match the house style, every chapter
  has: …") so authoring is fill-in-the-blanks.
- **Relationship to `.claude/rules`:** `notation`/`writing`/`code`/`glossary` referenced,
  not absorbed; `chapters.md` + `figures.md` appearance content moved here, those files
  reduced to pointers. Because `.claude/` is git-ignored, the **human-facing** pointer to
  this design system lives in tracked files (`CLAUDE.md` and `DESIGN-SYSTEM.md` itself); the
  `.claude/rules` pointers serve only Claude's in-tree context and are never relied on for
  human discoverability.

### Known gaps / future items (documented, not fixed now)
- Existing Mermaid diagrams use ad-hoc fills; migrating them to the `classDef` sets is a
  follow-up governance task.
- Logo/favicon/social-card artwork not yet created (spec reserved).
- A published "kitchen-sink" showcase page is intentionally omitted (the doc is
  unpublished); revisit if a living demo is wanted later.

## 6. Verification

- `mkdocs build --strict` passes after the rules-file refactor and any CSS additions.
- The two load-bearing anchors remain intact:
  `overview.html#the-5-classical-ols-assumptions-and-how-time-series-violates-them` and
  `do-you-need-time-series-analysis.html#feature-engineering-vs-time-series-modelling`.
- Spot-check: an **ephemeral** sample chapter built purely from the new-chapter checklist +
  component snippets renders correctly (admonitions, flowchart classDefs, a semantic-
  coloured decision matrix, a brand-palette matplotlib figure). This is a throwaway
  verification artifact, deleted after the check — **not** a shipped chapter.
- Palette pairs audited against WCAG AA; any failing pair flagged in the doc.
- Documented hex values are diffed against `extra.css` so token drift cannot recur.
