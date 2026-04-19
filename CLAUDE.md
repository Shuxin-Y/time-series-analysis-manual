# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

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

1. **MathJax** (`docs/javascripts/mathjax.js`) — Renders LaTeX. Uses `\( \)` for inline, `\[ \]` for display. Custom macros defined in file. Equation numbering is AMS style.

2. **Mermaid** (`docs/javascripts/mermaid-init.js`) — Renders diagrams via superfences (NOT `<div>` tags). Initialized with `startOnLoad: false`.

3. **Interactive Glossary** (`docs/javascripts/glossary.js`) — Loads per-chapter YAML files from `docs/glossary/`, highlights terms in all chapters (00–07) and appendices, shows right-slide drawer.

### Custom CSS

- `docs/stylesheets/extra.css` — Custom admonitions: `theorem` (purple), `definition` (teal). Hypothesis test boxes. Mermaid centering.
- `docs/stylesheets/glossary.css` — Drawer panel, overlay, animations.

## Content Conventions

- **No emojis** in content or diagrams
- Chapter directories: `NN-kebab-case/` with `index.md` as landing page
- Navigation: defined explicitly in `mkdocs.yml` under `nav:`
- Primary notation: conditional expectation form (most general, modern standard)
- See `.claude/rules/` for detailed standards: chapters, notation, code, figures, writing

## CI/CD

GitHub Actions (`.github/workflows/deploy.yml`): triggers on push to main, builds with Python 3.11, deploys to GitHub Pages.

## Basic

请使用第一性原理思考。你不能总假设我非常清楚自己想要什么和该怎么得到。请保持审慎，从原始需求和问题出发，如果动机和目标不清晰，停下来和我讨论。如果目标清晰但是路径不是最短，告诉我，并建议更好的办法。

Do not commit or push without permission. 