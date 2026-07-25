# Time Series Analysis Manual — design system

The visual identity of an academic monograph on time-series analysis: a restrained
scholarly palette, a serif display face for headings, and a signature set of
"branded box" components (theorems, definitions, hypothesis tests). Build screens
that read like a well-typeset textbook or a quantitative research tool, not a
generic SaaS app.

## Wrapping and setup

Wrap the app (or any screen) in `Root`. It establishes the brand body font,
foreground/background, and the colour scheme:

```jsx
import { Root, Heading, Admonition, Button } from '@tsam/design-system'

<Root theme="light">      {/* omit `theme` to follow the OS; "dark" for the dark scheme */}
  <Heading level={1}>Stationarity and Unit Roots</Heading>
  <Admonition type="definition" title="Stationarity">
    Mean, variance, and autocovariances are constant over time.
  </Admonition>
  <Button variant="primary">Run ADF test</Button>
</Root>
```

The design tokens (below) are defined globally by the shipped `styles.css`, so
components are styled even outside `Root` — but `Root` is what paints the page
background/text and sets the theme, so always wrap with it. Dark mode also works
via `prefers-color-scheme`; `theme="dark"` forces it. Do not hand-write the
internal `tsam-*` class names — compose the exported components instead.

## Styling idiom — CSS custom-property tokens

This is a **token system**, not a utility-class system. Style your own layout glue
with the CSS variables below (via `style={{ … }}` or your own classes); never
invent Tailwind-style class names — they will not resolve.

| Token family | Real names |
|---|---|
| Brand hues | `--color-cerulean` `--color-burgundy` `--color-thistle-dark` `--color-navajo-dark` `--color-sunset` `--color-sage-dark` `--color-amber-dark` |
| Semantic outcomes | `--color-good` `--color-escalate` `--color-problem` |
| Surface / text | `--tsam-bg` `--tsam-surface` `--tsam-surface-sunken` `--tsam-fg` `--tsam-fg-muted` `--tsam-border` |
| Interactive | `--tsam-link` `--tsam-accent` `--tsam-primary` |
| Type | `--font-display` (Source Serif 4, headings) `--font-body` (Inter) |
| Space / shape | `--space-xs…--space-xl` `--radius-box` `--radius-control` |

Surface/text/interactive tokens are theme-aware — they flip automatically in the
dark scheme, so prefer them over the raw `--color-*` hues for anything that must
read in both schemes. Headings 1–3 use `--font-display`; everything else uses
`--font-body`.

## Components

Primitives: `Button` (variant: primary/secondary/outline/ghost), `Card`, `Input`,
`Badge` (tone: neutral/primary/good/escalate/problem), `Heading` (level 1–4),
`Table`. Signature book components: `Admonition` (type selects the accent colour —
note/theorem/definition/tip/warning/question/etc.), `TheoremBox`, `DefinitionBox`,
`HypothesisTest` (auto-labels H₀/H₁), `DecisionMatrix` (colour-coded verdict
cells). Choose an `Admonition`/`Badge` type by *meaning*, not by preferred colour.

## Where the truth lives

Read `styles.css` (and its `@import`ed `_ds_bundle.css`) for the exact token values
and component styles. Each component's API is in its `<Name>.d.ts`; usage guidance
and examples are in `<Name>.prompt.md`.
