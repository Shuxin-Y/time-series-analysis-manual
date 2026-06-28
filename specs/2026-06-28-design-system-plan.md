# Design System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract the book's established appearance into one version-controlled `DESIGN-SYSTEM.md` (repo root), backed by supporting CSS, a matplotlib style + helper, and a hybrid refactor of the appearance `.claude/rules` files into pointers.

**Architecture:** A documentation deliverable. The design system doc is the authoritative *catalog*; `extra.css`/`*.js` remain the runtime *implementation*. New artifacts (`brand.mplstyle`, `brand.py`, decision-matrix CSS) are small and additive. "Tests" are `mkdocs build --strict`, targeted `grep` checks on built HTML, a Python contrast/hex-audit script, and a throwaway sample-chapter render check.

**Tech Stack:** MkDocs + Material, `pymdownx` extensions (`md_in_html`, `attr_list`, `tabbed`, `snippets`, `superfences`/Mermaid), MathJax, matplotlib.

**Spec:** `specs/2026-06-28-design-system-design.md`

**Pre-work (one-time, not a task):** branch off `main` (e.g. `feat/design-system`) before starting — the current `cleanup/00-introduction` branch is unrelated. No git worktree needed for a docs change.

**Conventions for every task:** after the change, run `source venv/bin/activate && mkdocs build --strict` and confirm it still passes (only the known non-fatal `code-examples/notebooks/` INFO is acceptable). Commit messages end with the project's `Co-Authored-By` trailer. Do not push without the maintainer's say-so.

---

## File Structure

| File | Responsibility | Tracked? |
|---|---|---|
| `DESIGN-SYSTEM.md` (repo root) | The design system catalog (all tiers) | yes |
| `docs/stylesheets/extra.css` | + decision-matrix semantic cell classes (append only) | yes |
| `docs/assets/brand.mplstyle` | matplotlib figure defaults + brand cycle | yes |
| `brand.py` (repo root) | `use_brand_style(palette=...)` helper, CWD-independent | yes |
| `scripts/audit_palette.py` | one-shot WCAG-AA contrast + hex-drift audit (dev tool) | yes |
| `.claude/rules/chapters.md` | reduced to pointer + operational notes | no (git-ignored) |
| `.claude/rules/figures.md` | reduced to pointer + operational notes | no (git-ignored) |
| `CLAUDE.md` | add human-facing pointer to `DESIGN-SYSTEM.md` | yes |

---

## Task 1: Decision-matrix semantic-cell CSS

**Files:**
- Modify: `docs/stylesheets/extra.css` (append a new section at end)

- [ ] **Step 1: Append the CSS**

```css
/* ===== Decision-matrix semantic cells (md_in_html tables) ===== */
.md-typeset table.decision-matrix td.good     { background: #DCEFD8; }
.md-typeset table.decision-matrix td.escalate { background: #FFE9C2; }
.md-typeset table.decision-matrix td.problem  { background: #F2D9DE; }

[data-md-color-scheme="slate"] .md-typeset table.decision-matrix td.good     { background: rgba(76, 122, 63, 0.30); }
[data-md-color-scheme="slate"] .md-typeset table.decision-matrix td.escalate { background: rgba(201, 165, 94, 0.30); }
[data-md-color-scheme="slate"] .md-typeset table.decision-matrix td.problem  { background: rgba(128, 0, 32, 0.28); }
```

- [ ] **Step 2: Verify build**

Run: `source venv/bin/activate && mkdocs build --strict 2>&1 | tail -3`
Expected: build succeeds (only the known `code-examples/notebooks/` INFO).

- [ ] **Step 3: Commit**

```bash
git add docs/stylesheets/extra.css
git commit -m "feat(design): add decision-matrix semantic cell classes"
```

> Note on Mermaid equal-node-width: a CSS `min-width` floor does **not** reliably apply to SVG `<rect>` nodes, so it is intentionally NOT added here. Equal visual weight is achieved by the label-length-parity rule documented in §5.4; this is recorded as a known limitation, not a CSS fix.

---

## Task 2: `brand.mplstyle`

**Files:**
- Create: `docs/assets/brand.mplstyle`

- [ ] **Step 1: Create the style file**

```
# Time Series Analysis Manual — brand matplotlib style
# Default colour cycle = brand-derived palette. Switch to colorblind-safe via brand.use_brand_style("cb").

figure.figsize: 7.0, 4.0
figure.dpi: 150
savefig.dpi: 150
savefig.bbox: tight
savefig.transparent: False

font.family: sans-serif
font.size: 11
axes.titlesize: 13
axes.titleweight: bold
axes.labelsize: 11

axes.spines.top: False
axes.spines.right: False
axes.grid: True
axes.axisbelow: True
grid.color: E0E0E0
grid.linewidth: 0.8

lines.linewidth: 1.8
legend.frameon: False

axes.prop_cycle: cycler('color', ['007BA7', '800020', '9B7FA7', 'C9A55E', 'B87D6C'])
```

- [ ] **Step 2: Verify it loads**

Run: `source venv/bin/activate && python -c "import matplotlib.pyplot as plt; plt.style.use('docs/assets/brand.mplstyle'); print('ok')"`
Expected: prints `ok` with no parse error.

- [ ] **Step 3: Commit**

```bash
git add docs/assets/brand.mplstyle
git commit -m "feat(design): add brand matplotlib style"
```

---

## Task 3: `brand.py` helper

**Files:**
- Create: `brand.py` (repo root)

- [ ] **Step 1: Create the helper**

```python
"""Brand matplotlib styling for the Time Series Analysis Manual.

Apply the house figure style and colour cycle in one call, from any working
directory (the style path resolves relative to this file):

    import brand
    brand.use_brand_style()        # default brand palette
    brand.use_brand_style("cb")    # colorblind-safe (Okabe-Ito) palette

This helper drives the book's own figure-generation pipeline. Code shown to
readers is illustrative and is not expected to import this module.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

_STYLE = Path(__file__).resolve().parent / "docs" / "assets" / "brand.mplstyle"

_BRAND_CYCLE = ["#007BA7", "#800020", "#9B7FA7", "#C9A55E", "#B87D6C"]
_CB_CYCLE = [
    "#E69F00", "#56B4E9", "#009E73", "#F0E442",
    "#0072B2", "#D55E00", "#CC79A7", "#000000",
]


def use_brand_style(palette: str = "brand") -> None:
    """Apply the manual's matplotlib style and colour cycle.

    Args:
        palette: "brand" (default) or "cb" (colorblind-safe Okabe-Ito).
    """
    if palette not in ("brand", "cb"):
        raise ValueError(f"palette must be 'brand' or 'cb', got {palette!r}")
    plt.style.use(str(_STYLE))
    cycle = _CB_CYCLE if palette == "cb" else _BRAND_CYCLE
    mpl.rcParams["axes.prop_cycle"] = cycler(color=cycle)
```

- [ ] **Step 2: Verify it works from a different CWD**

Run: `source venv/bin/activate && (cd docs && python -c "import sys; sys.path.insert(0, '..'); import brand; brand.use_brand_style('cb'); import matplotlib as mpl; print(mpl.rcParams['axes.prop_cycle'].by_key()['color'][0])")`
Expected: prints `#E69F00` (CB cycle applied) — proves `__file__` path resolution is CWD-independent.

- [ ] **Step 3: Commit**

```bash
git add brand.py
git commit -m "feat(design): add brand.py matplotlib style helper"
```

---

## Task 4: Palette audit tool (WCAG AA + hex drift)

**Files:**
- Create: `scripts/audit_palette.py`

This produces (a) the AA contrast table for tinted backgrounds that the doc must cite, and (b) a drift check that documented hexes match `extra.css`.

- [ ] **Step 1: Create the audit script**

```python
"""Audit design-system colour tokens: WCAG AA contrast + hex drift.

Run: python scripts/audit_palette.py
Exits non-zero if any documented token is missing from extra.css.
"""
import re
import sys
from pathlib import Path

CSS = Path(__file__).resolve().parent.parent / "docs" / "stylesheets" / "extra.css"

# Semantic / structural fills that carry body text (must pass AA against text).
FILLS = {
    "terminator": "#E6F2F7", "decision": "#EFE7F0", "data": "#FFF4E0",
    "good": "#DCEFD8", "escalate": "#FFE9C2", "problem": "#F2D9DE",
}
TEXT_DARK = "#1A1A1A"  # default body text in light mode (approx)


def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def main():
    print("WCAG contrast of body text on tinted fills (AA body >= 4.5):")
    for name, fill in FILLS.items():
        ratio = contrast(TEXT_DARK, fill)
        flag = "PASS" if ratio >= 4.5 else "FLAG (large-text/bold only)"
        print(f"  {name:11s} {fill}  {ratio:5.2f}:1  {flag}")

    css = CSS.read_text()
    missing = [h for h in FILLS.values() if h.lower() not in css.lower()]
    # FILLS are flowchart classDef values; not all live in CSS — only check
    # the decision-matrix cell colours, which must exist in extra.css.
    cell = {"#DCEFD8", "#FFE9C2", "#F2D9DE"}
    drift = [h for h in cell if h.lower() not in css.lower()]
    if drift:
        print(f"\nDRIFT: decision-matrix colours missing from extra.css: {drift}")
        sys.exit(1)
    print("\nDecision-matrix cell colours present in extra.css: OK")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the audit**

Run: `source venv/bin/activate && python scripts/audit_palette.py`
Expected: prints a contrast table and `Decision-matrix cell colours present in extra.css: OK` (Task 1 must be done first). Record any `FLAG` rows — they become the WCAG notes in §5.4/§5.5 of the doc (use bold/dark text on those fills).

- [ ] **Step 3: Commit**

```bash
git add scripts/audit_palette.py
git commit -m "chore(design): add palette WCAG/drift audit script"
```

---

## Task 5: `DESIGN-SYSTEM.md` — scaffold + Tier 0 + Tier 1

**Files:**
- Create: `DESIGN-SYSTEM.md` (repo root)

Source all prose/values from spec §5 (Tier 0, Tier 1). Read `docs/stylesheets/extra.css` for the exact token hexes, typography ladder, and spacing utilities; document them verbatim.

- [ ] **Step 1: Write the document header + Tier 0**

Header: title, `**Version:** 1.0`, one-line purpose, and the three-tier reading guide. Then the **Principles** section including the "Catalog vs. implementation" asymmetry paragraph from the spec (doc = authoritative catalog; CSS/JS = runtime implementation).

- [ ] **Step 2: Write Tier 1 — Foundations**

Four subsections, values pulled from `extra.css`:
- Colour tokens table: token name · hex · semantic role · light/dark mapping. Include the WCAG-AA notes produced by Task 4 (flag any fill needing bold/dark text).
- Typography scale (Source Serif 4 H1–H3, Inter H4–H6, the size/weight ladder, H2 underrule, 1.75 prose line-height).
- Spacing & utilities (`mt-*`/`mb-*`, `text-center`/`text-right`, `highlight-text`).
- Layout, responsive & print (content width, 768px breakpoint, scrollable tables/diagrams, print stylesheet).

- [ ] **Step 3: Verify hexes match CSS**

Run: `source venv/bin/activate && python scripts/audit_palette.py` and manually confirm the colour-token table in `DESIGN-SYSTEM.md` lists the same hexes as `:root` in `extra.css` (diff by eye against `grep -E '\-\-color' docs/stylesheets/extra.css`).
Expected: no mismatches.

- [ ] **Step 4: Commit**

```bash
git add DESIGN-SYSTEM.md
git commit -m "docs(design): scaffold DESIGN-SYSTEM.md with principles and foundations"
```

---

## Task 6: `DESIGN-SYSTEM.md` — Tier 2a Components

**Files:**
- Modify: `DESIGN-SYSTEM.md`

Each component documented as: **purpose · when to use · copy-paste markup · rendered note · do/don't**. Pull live markup from the intro chapters and CSS class names from `extra.css`/`glossary.css`.

- [ ] **Step 1: Write the component catalog**

Cover: the four admonitions (`theorem`/`definition`/`note`/`abstract`) with their colours and a fenced `!!! theorem "…"` example each; `.hypothesis-test` and `.decision-rule` boxes (with the exact HTML structure that triggers the `H₀:`/`H₁:` pseudo-elements); the `annotate` + numbered "common alternative forms" pattern; the `(Read: …)` pronunciation-guide rule; the `## References` block (Chicago author-date, `id="references"`); interactive components (glossary drawer, tabbed sets, `abbr` tooltips, Material annotations) with their hover/focus/motion notes.

- [ ] **Step 2: Verify build**

Run: `source venv/bin/activate && mkdocs build --strict 2>&1 | tail -3`
Expected: passes. (Any fenced examples in the doc are not built — the doc is unpublished — but confirm no accidental site change broke the build.)

- [ ] **Step 3: Commit**

```bash
git add DESIGN-SYSTEM.md
git commit -m "docs(design): add component catalog (Tier 2a)"
```

---

## Task 7: `DESIGN-SYSTEM.md` — Tier 2b Patterns (flowchart, table, data-viz)

**Files:**
- Modify: `DESIGN-SYSTEM.md`

- [ ] **Step 1: Write the composition patterns**

Canonical chapter template + content flow; equation→pronunciation pairing; hypothesis-test layout; page-footer nav.

- [ ] **Step 2: Write the Decision-Flowchart Notation (§5.4)**

Include both tables (shapes-by-role, colours-by-type) and the **two ready-to-paste `classDef` blocks**. Brand set:

```
classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

Colorblind-safe set (Okabe–Ito):

```
classDef terminator fill:#56B4E9,stroke:#005A7A,color:#000000;
classDef process fill:#FFFFFF,stroke:#000000,color:#000000;
classDef decision fill:#0072B2,stroke:#003D5C,color:#FFFFFF;
classDef data fill:#F0E442,stroke:#7A6E00,color:#000000;
classDef good fill:#009E73,stroke:#005A41,color:#FFFFFF;
classDef escalate fill:#E69F00,stroke:#8A5F00,color:#000000;
classDef problem fill:#D55E00,stroke:#7A3500,color:#FFFFFF;
classDef ref fill:#FFFFFF,stroke:#999999,color:#000000,stroke-dasharray:4 3;
```

Plus a **worked example diagram** (adapt the existing `do-you-need` flowchart) demonstrating terse decision labels, `:::class` application, `%%{init: {"flowchart": {"curve": "linear"}}}%%`, labeled edges, and `SCREAMING_SNAKE_CASE` IDs. Then the rules list (terse labels, equal-weight via label parity, edge curve-by-scenario, edge-type semantics, direction, IDs, text, accessibility).

- [ ] **Step 3: Write the Table Standard (§5.5)**

Five patterns; structural rules; then a **worked colour-coded decision matrix** using the `md_in_html` mechanism, showing verdict-as-text in each coloured cell:

```html
<table class="decision-matrix" markdown>
<tr><th>ADF</th><th>KPSS</th><th>Verdict</th></tr>
<tr><td>Reject</td><td>Fail to reject</td><td class="good">Stationary</td></tr>
<tr><td>Fail to reject</td><td>Reject</td><td class="problem">Unit root — difference</td></tr>
<tr><td>Reject</td><td>Reject</td><td class="escalate">Inconclusive — inspect</td></tr>
</table>
```

- [ ] **Step 4: Write the Data-Visualization Standard (§5.6)**

Default + CB palettes (hexes); the **embedded `brand.mplstyle` fenced block** (verbatim copy of Task 2's file); the `brand.py` usage snippet (`import brand; brand.use_brand_style()`); and the note that Mermaid uses the §5.4 `classDef` sets. State the figure-pipeline-vs-reader-copy caveat.

- [ ] **Step 5: Verify the decision-matrix renders (temporary check)**

Temporarily paste the decision-matrix HTML into an existing built page (e.g., the bottom of `docs/00-introduction/overview.md`), run `mkdocs build --strict`, then `grep -o 'class="decision-matrix"' site/00-introduction/overview/index.html` and confirm the `td.good`/`.problem`/`.escalate` cells appear coloured (open in preview if unsure). **Revert the temporary paste** before committing.

Run: `source venv/bin/activate && mkdocs build --strict && grep -c 'decision-matrix' site/00-introduction/overview/index.html`
Expected: `1` while the temp paste is in place; then revert and rebuild.

- [ ] **Step 6: Commit**

```bash
git add DESIGN-SYSTEM.md
git commit -m "docs(design): add flowchart notation, table and data-viz standards (Tier 2b)"
```

---

## Task 8: `DESIGN-SYSTEM.md` — Tier 3 Governance + Changelog

**Files:**
- Modify: `DESIGN-SYSTEM.md`

- [ ] **Step 1: Write governance**

Single-source-of-truth asymmetry restatement; naming conventions; reserved brand-asset spec (favicon sizes, social-card template, `docs/assets/` home, current Material icon usage); how to add/modify a component; versioning policy; change process (PR + `--strict`); **new-chapter checklist**; relationship to `.claude/rules` (incl. the git-ignored discoverability note). Then the **Known gaps** list and a `## Changelog` with a dated `v1.0` entry.

- [ ] **Step 2: Lint the doc**

Run: `source venv/bin/activate && mkdocs build --strict 2>&1 | tail -3`
Expected: passes. Confirm no stray markdownlint MD0xx warnings in the editor for `DESIGN-SYSTEM.md`.

- [ ] **Step 3: Commit**

```bash
git add DESIGN-SYSTEM.md
git commit -m "docs(design): add governance, new-chapter checklist, changelog (Tier 3)"
```

---

## Task 9: Refactor `.claude/rules/chapters.md` and `figures.md` to pointers

**Files:**
- Modify: `.claude/rules/chapters.md`
- Modify: `.claude/rules/figures.md`

Hybrid refactor: appearance content → pointer to `DESIGN-SYSTEM.md`; keep genuinely operational notes.

- [ ] **Step 1: Refactor `figures.md`**

Replace the Mermaid-styling / matplotlib / CSS-appearance content with a one-line pointer: "Visual conventions for diagrams and figures live in `DESIGN-SYSTEM.md` (§5.4 flowcharts, §5.6 data-viz)." **Retain** the operational notes: "applies when editing `docs/*`", and "after creating/editing Mermaid diagrams, validate with the `validate-mermaid` skill."

- [ ] **Step 2: Refactor `chapters.md`**

Move appearance/structure content (admonition types, hypothesis-test formatting, annotations, tabs, content flow) to a pointer: "Chapter structure, admonitions, and composition patterns live in `DESIGN-SYSTEM.md` (§5 Tier 2)." **Retain** operational notes: directory/naming rule, "update `mkdocs.yml` `nav:` when adding pages", citation hierarchy reference to `writing.md`.

- [ ] **Step 3: Verify nothing else referenced the moved content**

Run: `grep -rnE '9c27b0|00897b' .claude/`
Expected: no matches — the old purple/teal admonition hexes are gone after Steps 1–2.

- [ ] **Step 4: Commit**

```bash
git add -A .claude/rules/chapters.md .claude/rules/figures.md 2>/dev/null || true
git commit -m "refactor(rules): point chapters/figures rules at DESIGN-SYSTEM.md" || echo "(.claude is git-ignored — change is local only, no commit)"
```

> Reminder: `.claude/` is git-ignored, so this change is local-only and will NOT commit. That is expected (spec §4 "Tracked vs. ignored"). Skip the commit if git reports nothing to add.

---

## Task 10: Add human-facing pointer in `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add a reference**

Under "Content Conventions" (or a new "Design System" subsection), add: "Visual and structural standards (palette, typography, components, flowchart/table/figure conventions) are defined in `DESIGN-SYSTEM.md` at the repo root — the single source of truth for the book's appearance."

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: point CLAUDE.md at DESIGN-SYSTEM.md design system"
```

---

## Task 11: Final verification pass

**Files:** none (verification only)

- [ ] **Step 1: Strict build**

Run: `source venv/bin/activate && mkdocs build --strict 2>&1 | tail -5`
Expected: succeeds; only the known `code-examples/notebooks/` INFO.

- [ ] **Step 2: Load-bearing anchors intact**

Run:
```bash
grep -o 'id="the-5-classical-ols-assumptions-and-how-time-series-violates-them"' site/00-introduction/overview/index.html
grep -o 'id="feature-engineering-vs-time-series-modelling"' site/00-introduction/do-you-need-time-series-analysis/index.html
```
Expected: both ids print (unchanged by this work).

- [ ] **Step 3: Hex-drift audit**

Run: `source venv/bin/activate && python scripts/audit_palette.py`
Expected: `Decision-matrix cell colours present in extra.css: OK`.

- [ ] **Step 4: Ephemeral sample-chapter render check**

Create a throwaway `docs/_designcheck.md` that uses one of each: a `theorem` admonition, the brand-set flowchart `classDef` block with a 3-node diagram, the colour-coded decision matrix, and an `![](...)` reference to a figure produced by `brand.py`. Add it to `nav` temporarily, run `mkdocs build --strict`, preview the page, confirm everything renders (admonition colour, coloured matrix cells, flowchart node colours). Then **delete** `docs/_designcheck.md`, remove the temporary `nav` entry, and rebuild.

Run: `source venv/bin/activate && mkdocs build --strict 2>&1 | tail -3` (after cleanup)
Expected: passes; `docs/_designcheck.md` no longer exists (`ls docs/_designcheck.md` → not found).

- [ ] **Step 5: Confirm worktree is clean of throwaways**

Run: `git status --short`
Expected: no `_designcheck.md`, no stray temp edits; only the intended tracked files changed.

- [ ] **Step 6 (optional): WCAG note completeness**

Confirm every `FLAG` row from `scripts/audit_palette.py` has a corresponding "use bold/dark text" note in `DESIGN-SYSTEM.md` §5.4/§5.5.

---

## Done criteria

- `DESIGN-SYSTEM.md` exists at repo root with all tiers, version 1.0, and a changelog.
- `docs/assets/brand.mplstyle`, `brand.py`, and `scripts/audit_palette.py` exist and pass their checks.
- `extra.css` has the decision-matrix classes; `mkdocs build --strict` passes.
- `.claude/rules/chapters.md` + `figures.md` are pointers + operational notes (local-only); `CLAUDE.md` points to the design system (tracked).
- Both load-bearing anchors intact; no throwaway files left behind.
