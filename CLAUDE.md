# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A MkDocs-based educational documentation site covering time series analysis, bridging classical econometrics and modern machine learning. Deployed to GitHub Pages at https://shuxin-y.github.io/time-series-analysis-manual.

## Build & Development Commands

```bash
# Local development (hot-reload)
source venv/bin/activate && mkdocs serve

# Production build (use --strict to catch warnings as errors)
source venv/bin/activate && mkdocs build --strict

# Deploy happens automatically via GitHub Actions on push to main
```

## Architecture

### Three-Layer Enhancement System

All three systems are SPA-aware, hooking into Material theme's `document$.subscribe()` for re-rendering on navigation:

1. **MathJax** (`docs/javascripts/mathjax.js`) — Renders LaTeX equations. Uses `\( \)` for inline, `\[ \]` for display. Defines custom macros: `\RR`, `\EE`, `\Var`, `\Cov`, `\Corr`, `\argmin`, `\argmax`, `\plim`, `\convd`, `\convp`, `\convas`, `\Prob`, `\iid`, `\bm`. Equation numbering is AMS style.

2. **Mermaid** (`docs/javascripts/mermaid-init.js`) — Renders diagrams. Initialized with `startOnLoad: false` for manual control. Uses `securityLevel: 'loose'`. Handles multiple selectors (`code.mermaid`, `div.mermaid`, `pre.mermaid`). Tracks processed elements via `data-processed` attribute with 100ms debounce.

3. **Interactive Glossary** (`docs/javascripts/glossary.js`) — Loads terms from `docs/glossary.yml`, highlights them in content (chapters 02+), shows a right-slide drawer with definition, LaTeX formula, historical context, and reference link. Uses longest-match-first regex, skips code blocks and headers.

### Mermaid Diagrams

Diagrams use triple-backtick fenced blocks via `pymdownx.superfences` with `fence_code_format` — NOT `<div class="mermaid">` tags. This is configured in `mkdocs.yml` under `custom_fences`.

### Custom CSS

- `docs/stylesheets/extra.css` — Custom admonition types: `theorem` (purple), `definition` (teal). Hypothesis test boxes with H₀/H₁ styling. Mermaid container centering.
- `docs/stylesheets/glossary.css` — Drawer panel (550px desktop, 100% mobile), overlay, animations.

Both use Material theme CSS variables (`--md-primary-fg-color`, `--md-code-bg-color`, etc.).

### Glossary Entry Format

```yaml
- term: "Term Name"
  definition: "Clear, concise definition"
  mathematical: |
    LaTeX formulation using $inline$ and $$display$$ math.
  historical: |
    - YYYY: Key milestone
  reference: "NN-chapter/page.html#section-anchor"
```

## Content Conventions

- **No emojis** in content or diagrams
- Chapter directories: `NN-kebab-case/` (e.g., `03-exploratory-analysis/`)
- Files within chapters: `NN-kebab-case.md` with `index.md` as landing page
- Navigation structure is defined explicitly in `mkdocs.yml` under `nav:`
- Hypothesis tests always state H₀ and interpretation rules with explicit thresholds
- Decision rules state p-value thresholds (e.g., p < 0.05)

## CI/CD

GitHub Actions (`.github/workflows/deploy.yml`): triggers on push to main, builds with Python 3.11, deploys to GitHub Pages. Includes optional PR preview comments.


## Basic

请使用第一性原理思考。你不能总假设我非常清楚自己想要什么和该怎么得到。请保持审慎，从原始需求和问题出发，如果动机和目标不清晰，停下来和我讨论。如果目标清晰但是路径不是最短，告诉我，并建议更好的办法。
