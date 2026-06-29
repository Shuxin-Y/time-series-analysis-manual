# Design System — Time Series Analysis Manual

**Version:** 1.0

This document is the single source of truth for the book's *appearance*: the brand tokens, typography, components, and composition patterns that every chapter shares.

## How to read this document

The design system is organized into four tiers, from the most abstract to the most operational:

- **Tier 0 — Principles.** What the design optimizes for.
- **Tier 1 — Foundations.** The design tokens: colour, typography, spacing, layout.
- **Tier 2 — Components & Patterns.** Reusable building blocks and how to compose them.
- **Tier 3 — Governance.** Versioning, naming, and the change process.

Read the tiers in order on a first pass. Later, use Tier 1 and Tier 2 as a reference catalog while authoring a chapter.

## Tier 0 — Principles

The design optimizes for four properties, in priority order.

**Academic gravitas.** Content-area headings use a serif display face (Source Serif 4) to evoke the typographic register of a printed monograph. The palette is a restrained academic set rather than a saturated web palette.

**Readability.** Prose uses a generous 1.75 line-height, and the body font-size has a floor (`max(0.8rem, 14px)`) so text never shrinks below a legible size under browser zoom. Tables and admonitions are sized to match the surrounding prose rather than the smaller Material defaults.

**Accessibility.** The design targets WCAG 2.1 AA. Every display equation is followed by a `(Read: …)` pronunciation guide. The site supports a dark mode (Material's `slate` scheme) and a print stylesheet. Colour is never the sole signal: semantic categories also carry text labels.

**Consistency.** Every chapter is a fill-in-the-blanks exercise against this catalog. The same concept is always expressed with the same token, component, and pattern.

### Catalog vs. implementation (read this first)

"Single source of truth" here has a deliberate asymmetry. This document is the authoritative **catalog/specification** of the design: what exists, when to use it, and the intended values. The files `docs/stylesheets/extra.css` and `docs/javascripts/*.js` are the authoritative **implementation**: what the browser actually renders. When the two diverge, the CSS/JS is the runtime truth and this document is corrected to match it, never the reverse. The doc is the map, not the territory.

## Tier 1 — Foundations (design tokens)

The foundations are the lowest-level design decisions. All values below are read verbatim from `docs/stylesheets/extra.css`; that file is the implementation, and this catalog mirrors it.

### Colour tokens

The brand palette is defined as custom properties in the `:root` block of `extra.css`. Five hue families — Cerulean (cool primary), Burgundy (accent), Thistle (soft violet tint), Navajo White (warm tint), and Sunset (warm rose-coral) — each carry light/dark/deep variants.

| Token | Hex | Semantic role | Light (`default`) / dark (`slate`) usage |
|---|---|---|---|
| `--color-cerulean` | `#007BA7` | Primary cool hue; body links | Link colour in light mode; note/remark admonition |
| `--color-cerulean-light` | `#4DA8C9` | Lighter cerulean | Link colour in dark mode |
| `--color-cerulean-dark` | `#005A7A` | Footer background | Footer background in light mode |
| `--color-cerulean-deep` | `#003D5C` | Deepest cerulean | Footer background in dark mode (and `--dark` footer in light) |
| `--color-burgundy` | `#800020` | Accent; theorem | Accent (light), theorem admonition, link hover (light) |
| `--color-burgundy-light` | `#A33548` | Lighter burgundy | Reserved variant |
| `--color-burgundy-dark` | `#5A0017` | Darker burgundy | Reserved variant |
| `--color-thistle` | `#D8BFD8` | Soft violet tint | Accent in dark mode; link hover (dark) |
| `--color-thistle-dark` | `#9B7FA7` | Definition; blockquote | Definition admonition border, blockquote accent (both schemes) |
| `--color-navajo` | `#FFDEAD` | Warm tint; selection | Text-selection highlight, abstract admonition fill |
| `--color-navajo-dark` | `#C9A55E` | Abstract accent | Abstract/summary admonition border (both schemes) |
| `--color-sunset` | `#B87D6C` | Header | Site header (Material primary) in both schemes |
| `--color-sunset-dark` | `#9E6657` | Darker sunset | Primary `--dark` variant |
| `--color-sunset-light` | `#D5A496` | Lighter sunset | Primary `--light` variant |

Semantic role summary: header = Sunset; footer = Cerulean-dark (light) / Cerulean-deep (dark); body links = Cerulean; accent and theorem = Burgundy; definition and blockquote = Thistle-dark; abstract and text selection = Navajo.

The dark (`slate`) scheme keeps the same Sunset header and Cerulean footer but brightens interactive colours: links shift to Cerulean-light and the accent shifts from Burgundy to Thistle for sufficient contrast on a dark background.

!!! note "WCAG note on tinted component fills"
    The tinted component fills introduced in Tier 2 (the flowchart `terminator`, `decision`, `data`, `good`, `escalate`, and `problem` node fills, and the matching decision-matrix cells) all pass WCAG 2.1 AA body-text contrast when paired with dark text (verified ratios in the range 13–16:1). Dark text on those tints is therefore safe.

### Typography scale

Content-area headings H1–H3 use Source Serif 4 for academic gravitas; H4–H6 and all chrome (navigation, admonition titles, drawer) stay in Inter, the Material default, for navigability. The serif rule is scoped to `.md-typeset` so only body content is affected.

| Element | Font | Size | Weight | Notes |
|---|---|---|---|---|
| H1 | Source Serif 4 | `2.25em` | 700 | Chapter opener; `line-height: 1.2`, `letter-spacing: -0.015em` |
| H2 | Source Serif 4 | `1.625em` | 700 | Major section; `line-height: 1.3`; bottom underrule (`1px` border) |
| H3 | Source Serif 4 | `1.25em` | 600 | Subsection; `line-height: 1.35` |
| H4 | Inter | `1.05em` | 600 | Deepest labelled heading |
| H5–H6 | Inter | (Material default) | — | Chrome-register headings |
| Body prose (`p`, `li`) | Inter | `max(0.8rem, 14px)` | — | `line-height: 1.75` |

The H1–H3 serif rules apply the OpenType feature settings `"kern", "liga", "onum"` (kerning, standard ligatures, old-style figures). Body text and `.md-typeset` apply `"kern", "liga", "calt", "ss01"` (kerning, ligatures, contextual alternates, stylistic set 1) together with antialiased font smoothing and `text-rendering: optimizeLegibility`. Numeric table cells use `font-variant-numeric: tabular-nums` so columns of figures align.

### Spacing & utilities

A small set of utility classes is available for one-off spacing and alignment. They are applied via `attr_list` (`{ .class }`).

| Class | Effect |
|---|---|
| `.mt-1` | `margin-top: 0.5rem` |
| `.mt-2` | `margin-top: 1rem` |
| `.mt-3` | `margin-top: 1.5rem` |
| `.mb-1` | `margin-bottom: 0.5rem` |
| `.mb-2` | `margin-bottom: 1rem` |
| `.mb-3` | `margin-bottom: 1.5rem` |
| `.text-center` | `text-align: center` |
| `.text-right` | `text-align: right` |
| `.highlight-text` | Highlighter-pen background (a linear-gradient using the transparent accent colour) |

### Layout, responsive & print

Content uses Material's default centred column width; the responsive and print rules below adjust it for small screens and for paper.

**Mobile (`@media screen and (max-width: 768px)`).** Content padding is reduced to `1rem`. Unclassed tables become `display: block` with `overflow-x: auto` so wide tables scroll horizontally instead of overflowing. Mermaid diagrams also gain `overflow-x: auto` for the same reason.

**Print (`@media print`).** The header, sidebar, and footer are hidden (`display: none`). Content expands to full width (`max-width: none`). Page-break rules keep headings with their following content (`h1, h2, h3 { page-break-after: avoid }`) and keep code blocks, blockquotes, and tables from splitting across pages (`page-break-inside: avoid`). External link URLs are printed inline after the link text via `a[href^="http"]::after`, so a paper copy retains its references.

## Tier 2a — Components

Components are the reusable building blocks an author drops into a chapter. Each entry below records its purpose, when to use it, the copy-paste markup, a note on what renders, and a do/don't. All markup and class names are read from `docs/00-introduction/*.md`, `docs/stylesheets/extra.css`, and `docs/javascripts/glossary.js`; those files are the implementation, and this catalog mirrors them.

### Admonitions

The book uses four typed admonitions, each with a fixed colour and a fixed semantic role. The type word in the `!!! type "Title"` fence selects the styling.

| Type | Colour token | Semantic use |
|---|---|---|
| `theorem` | Burgundy (`--color-burgundy`, `#800020`) | Theorems, assumptions, propositions |
| `definition` | Thistle (`--color-thistle-dark`, `#9B7FA7`) | Key concept definitions |
| `note` | Cerulean (`--color-cerulean`, `#007BA7`) | Remarks and informational asides |
| `abstract` | Navajo (`--color-navajo-dark`, `#C9A55E`) | Chapter and section summaries |

**Purpose.** Mark a block as a theorem, definition, remark, or summary, and signal its kind by colour and a labelled title bar.

**When to use.** Choose the type by semantic role from the table, not by colour preference. Use `theorem` for any formal statement to be proved or assumed; `definition` for the first formal statement of a term; `note` for a remark; `abstract` for an overview block. Standard Material types (`warning`, `tip`, `example`) remain available for other purposes.

**Markup.**

```markdown
!!! theorem "Assumption 1: Zero Mean"
    $$\EE[\epsilon_t \mid \mathbf{X}] = 0$$

    (Read: the expected value of epsilon-sub-t given X equals zero.)

!!! definition "Estimator"
    An **estimator** is a procedure that maps observed data to parameter
    values within a chosen model class.
```

**Rendered note.** The title bar carries a tinted background (the colour at 8–32% opacity) and the left border takes the full token colour. The `theorem` type reuses the Material `note` icon mask; `definition` reuses the `abstract` icon mask. Body text is set to `0.8rem` to match surrounding prose rather than the smaller Material default.

**Do/don't.** Do select the type by meaning. Don't use `theorem` styling for a plain note because the colour is preferred, and don't omit the quoted title — the title bar is where the type reads.

### `.hypothesis-test` and `.decision-rule` boxes

These two boxes format the components of a hypothesis test. They are raw HTML, not admonition fences, because the labels are generated by CSS pseudo-elements that require a specific element structure.

**Purpose.** The `.hypothesis-test` box presents a null and an alternative hypothesis with automatic `H₀:` and `H₁:` labels. The `.decision-rule` box presents the reject/retain rule with an accent-coloured left border.

**When to use.** Use the pair when laying out a diagnostic or coefficient test (see the hypothesis-test pattern in Tier 2b). The auto-labels free the author from typing `H₀:`/`H₁:` and keep them consistent across chapters.

**Markup.** The container must be `<div class="hypothesis-test">` with an `<h4>` title and child `<div class="null-hypothesis">` / `<div class="alternative-hypothesis">` blocks. The `::before` pseudo-elements inject the labels, so the class names and nesting are load-bearing.

```html
<div class="hypothesis-test" markdown>
<h4>Augmented Dickey–Fuller Test</h4>

<div class="null-hypothesis" markdown>
The series has a unit root (non-stationary): \( \gamma = 0 \).
</div>

<div class="alternative-hypothesis" markdown>
The series is stationary: \( \gamma < 0 \).
</div>

<div class="decision-rule" markdown>
**Decision rule:** reject \( H_0 \) when the p-value falls below \( \alpha = 0.05 \).
</div>
</div>
```

**Rendered note.** The `.hypothesis-test` container has a `2px` solid border in the primary colour and rounded corners; its `<h4>` is primary-coloured with an underrule. The `.null-hypothesis::before` pseudo-element prints `H₀:` in the primary colour, and `.alternative-hypothesis::before` prints `H₁:` in the accent colour, both positioned in the left padding gutter. The `.decision-rule` box renders with the transparent accent fill and a `4px` accent left border; `<strong>` text inside it takes the accent colour.

**Do/don't.** Do keep the exact class names and the `<div>` nesting — the `H₀:`/`H₁:` labels exist only because of the `.null-hypothesis`/`.alternative-hypothesis` selectors. Don't type the `H₀:`/`H₁:` text yourself inside these blocks; it would duplicate the generated label.

### Annotations and "common alternative forms"

This pattern shows a primary notation in an admonition while parking equivalent forms in a numbered footnote, so the main statement stays uncluttered.

**Purpose.** Present one canonical form of an equation or assumption in the body, with alternative formulations available on demand below.

**When to use.** Use it whenever a definition or assumption has several standard expressions and the chapter commits to one (per `notation.md`, the conditional-expectation form). The intro uses it for the Gauss–Markov assumptions.

**Markup.** Wrap an admonition in `<div class="annotate" markdown>`, place a `(1)` marker at the point the note attaches, then write the numbered list item below the closing `</div>`.

```markdown
<div class="annotate" markdown>

!!! theorem "Assumption 0: No Perfect Multicollinearity (Rank Condition)"
    $$\text{rank}(\mathbf{X}) = K$$

    (Read: the rank of X equals K, the number of regressors.)

The design matrix \( \mathbf{X} \) has full column rank. (1)

</div>

1.  **Common alternative forms:**
    - \( \det(\mathbf{X}^T\mathbf{X}) \neq 0 \) — the determinant form
    - \( \mathbf{X}^T\mathbf{X} \) is positive definite — the spectral form
```

**Rendered note.** Material renders the `(1)` as an inline annotation marker; clicking or focusing it reveals the numbered content in a tooltip. The list item supplies the alternative forms.

**Do/don't.** Do label the note "Common alternative forms:" and list the equivalents. Don't restate the alternatives in the body; the annotation exists to keep them out of the main flow.

### `(Read: …)` pronunciation guide

**Purpose.** Give every display equation a plain-language reading so the notation is accessible to readers less fluent in it (a WCAG-supporting practice).

**When to use.** After every display equation, without exception. The guide is placed on the line immediately following the equation and is exempt from the sentence-completeness rule.

**Markup.**

```markdown
$$\hat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta}} \sum_{t=1}^T \left( y_t - \mathbf{x}_t^T \boldsymbol{\beta} \right)^2.$$

(Read: beta-hat is the argmin over beta of the sum over $t$ of the squared residual.)
```

**Rendered note.** The guide renders as ordinary prose directly beneath the equation. Inside an admonition, indent it to the admonition body as shown in the admonition example above.

**Do/don't.** Do read the symbols aloud in order, naming each one. Don't merely restate the equation in symbols, and don't skip the guide on "obvious" equations.

### `## References` block

**Purpose.** List the chapter's sources in Chicago author-date style, set smaller than body prose because they are supporting material.

**When to use.** At the end of any chapter that cites work. The smaller styling is triggered by the heading's `id`, which MkDocs derives as `references` from the literal text "References".

**Markup.** Write the H2 as `## References` and follow it directly with a bulleted list; the CSS targets the list immediately after `h2#references`.

```markdown
## References

- Dickey, D. A., and W. A. Fuller. 1979. "Distribution of the Estimators for
  Autoregressive Time Series with a Unit Root." *Journal of the American
  Statistical Association* 74 (366): 427–431.
- Engle, R. F. 1982. "Autoregressive Conditional Heteroscedasticity with
  Estimates of the Variance of United Kingdom Inflation." *Econometrica*
  50 (4): 987–1007.
```

**Rendered note.** The list following `h2#references` renders at `0.7rem` with `line-height: 1.55`, distinguishing it from body prose. Both `ul` and `ol` are matched.

**Do/don't.** Do keep the heading text exactly "References" so the `id` resolves and the styling applies. Don't intersperse prose between the heading and the list; the selector targets the adjacent list.

### Interactive components

These components add behaviour at runtime. Each is described with its trigger and its motion or focus states.

**Glossary drawer.** A custom component (`docs/javascripts/glossary.js` plus `docs/stylesheets/glossary.css`) that highlights known glossary terms across all chapters (00–07) and appendices, and opens a right-slide drawer on click. The script wraps matched terms in `<span class="glossary-term">`; the span shows a `cursor: help` and a hover state. The `.glossary-drawer` slides in from the right via `transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1)` when the `.open` class is added, and the drawer body shows the term's definition, mathematical form, and historical context. Use it by authoring terms in `docs/glossary/NN-chapter.yml`; highlighting is automatic and requires no per-page markup.

**Tabbed sets.** Provided by `pymdownx.tabbed`. Use `=== "Tab Title"` blocks to group parallel content such as alternative approaches or reader tracks. Outer-level tab labels are enlarged (`0.8rem`, weight 700) so nested tab sets read hierarchically.

```markdown
=== "OLS"
    Closed-form, i.i.d. errors.

=== "MLE"
    Required for unobservable error components.
```

**`abbr` tooltips.** Material's abbreviation syntax produces `<abbr title="…">`. The CSS overrides the slow native tooltip: `abbr[title]` shows a dotted underline and `cursor: help`, and `abbr[title]:hover::after` renders an instant tooltip above the term using the default foreground colour as the background. Use it for first-mention acronym expansions.

**Material annotations.** The numbered-marker mechanism underlying the "common alternative forms" pattern above. Beyond alternative notation, use it for any short aside that would interrupt the sentence if inlined. A `(N)` marker in the text reveals the matching numbered list item on click or focus.

A shared motion note: body links transition colour on hover over `0.15s` (to Burgundy in light mode, Thistle in dark), and the glossary drawer and its close button animate rather than snap, so interactive state changes read as deliberate.
