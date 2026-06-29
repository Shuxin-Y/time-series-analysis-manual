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
