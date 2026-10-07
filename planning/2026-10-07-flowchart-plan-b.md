# Flowchart Framework Plan B: Remaining Sub-Diagrams

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Draw every sub-diagram the skeleton left pending (P0, P3, P4, P6, P8, P9, P10, P11; the ten purpose sub-charts; the six representation sub-charts; branches B1 to B7), register every leaf in the inventory, scaffold its pending section, and make the audit prove that all 34 areas have at least one leaf (spec acceptance criterion 3).

**Architecture:** Each diagram follows the P1 and P7 exemplars already in the repo: a decision chart in the design-system notation, leaves as rectangles with owner-prefixed IDs, `ref` boxes for nodes owned elsewhere, flags as `*_FLAG` process nodes, and no URLs. Leaf labels are short (the inventory label equals the first label line); method lists go on a second `<br/>` line. P0, P3, P4, P9 and P11 leaves (procedures, tests and the P4 transforms, which spec §10.2 lists as procedural) live in the phase page; model and estimator leaves (P5, P6, P7, P8 and the branches) live in the reference landing pages, where the scaffold appends pending sections.

**Tech Stack:** Mermaid 10 (as pinned), the existing `scripts/audit_flowcharts.py`, `scripts/scaffold_stubs.py`, pytest, MkDocs strict build. No new tooling beyond one coverage test and one audit helper.

**Spec:** `planning/2026-10-06-flowchart-framework-design.md` (§4 leaf candidates, §5 branches, §7 purposes and representations, §8 areas, §10 conventions, §11 audit). Content rules: `.claude/rules/writing.md`.

**Base:** branch `Shuxin-Y/flowchart-skeleton` (PR #7). Work on a new branch `Shuxin-Y/flowchart-plan-b` in a new worktree; open the PR against `Shuxin-Y/flowchart-skeleton` and retarget to `main` once PR #7 merges.

## Global Constraints

- All constraints of the skeleton plan apply (no emojis; quoted labels; `class` statements; brand `classDef` block at the foot of every diagram; owner-prefixed `SCREAMING_SNAKE_CASE` IDs; no URLs in diagrams; no local references in anything pushed; commits allowed, `Co-Authored-By` trailer per the repo's attribution rule).
- **Leaf label = inventory label = section heading.** The first line of a node label (before `<br/>`) is the inventory `label`; the inventory `section` anchor is the toc slug of that label (compute it with the audit's `slugify`, the scaffold writes a `{#anchor}` attribute when they differ). A second label line carries method names and is free text.
- **Where sections live.** P0, P3, P4, P9, P11 procedural leaves: the phase page. P6, P8 and branch leaves: the reference landing page of the first area in the row's `areas` list unless the table names a file. Purpose-specific and representation-specific leaves: the reference landing page named in the table. Foundation rows (phase `F`): `00-foundations/stochastic-processes.md` or `asymptotics.md` as named.
- **Audit stays green after every task:** `venv/bin/python scripts/audit_flowcharts.py` prints `0 error(s)`; `venv/bin/mkdocs build --strict` passes; `TSAM_REQUIRE_E2E=1 venv/bin/pytest tests -q -rs` passes with no skips.
- Diagram shape: `graph TD`, `curve: linear`; one decision question per diamond, at most about three words; edge labels quoted; `-.->` for loops back to earlier phases; terminators `<PHASE>_IN` and `<PHASE>_OUT` where a chart needs them.
- Nodes owned by another phase are drawn as `[["…"]]` with the owner's exact ID and label, and the `ref` class.

## Review Focus

1. A leaf drawn on a page outside its phase's owner page (or directory for P2/P5) must fail the audit; the owner table in the audit already enforces it, so each task ends with the audit run, not a visual check.
2. A label whose first line differs from the inventory label by a single character (hyphen vs en dash, trailing period) fails the label check; copy labels from the tables verbatim.
3. Area coverage must be asserted by a test that reads the real inventory, not by eye; Task 1 adds it and it fails until the last diagram lands.
4. Purpose and representation pages have the structural H2s `Sub-chart`, `P10 inference for this purpose`, `P11 metrics for this purpose`; a leaf heading must never be added to those pages (their leaves' sections live in reference chapters), or the heading-level check fails.
5. `ref` nodes to foundation rows must have a matching `F_*` inventory row whose section exists after the scaffold runs; a typo in an `F_*` ID is an "unresolved ref" error.

## File Structure

| Path | Responsibility |
|---|---|
| `docs/01-workflow/p00-data.md`, `p03-…`, `p04-…`, `p06-…`, `p08-…`, `p09-…`, `p10-…`, `p11-…` | Phase sub-diagram replaces the "Diagram pending" note; procedural leaf sections scaffolded below |
| `docs/01-workflow/p07-error-process.md` | P7 split into two stacked diagrams (layout fix) |
| `docs/01-workflow/p02-purpose/01-…10-*.md` | Purpose sub-charts replace the pending note; quick-navigation table on `index.md` |
| `docs/01-workflow/p05-representation/01-…06-*.md` | Representation sub-charts; quick-navigation table on `index.md` |
| `docs/01-workflow/p01-data-type-gate.md` | B7 sub-chart appended under its leaf heading |
| `docs/reference/16-…`, `17-…`, `15-…`, `14-…`, `20-…`, `32-…/index.md` | Branch stubs replaced by full B1–B6 diagrams |
| `docs/reference/*/index.md` | Pending sections appended by the scaffold |
| `docs/00-foundations/stochastic-processes.md`, `asymptotics.md` | New foundation sections appended by the scaffold |
| `docs/flowcharts/inventory.yml` | All new rows |
| `tests/test_area_coverage.py` | Every area 1–34 has at least one leaf row |

### Diagram conventions used in the node tables below

Each diagram is given as (a) a **flow** list: decisions (diamonds) with their edge labels and what each edge leads to, and (b) a **leaves** table: `ID | label | second line (optional) | areas | section file`. Refs and flags are named in the flow. The implementer writes the Mermaid from these, in the notation of the P1 and P7 diagrams in the repo, adds one inventory row per leaf (`phase` = owner, `section` = file + `#` + slug of the label), runs the scaffold, and runs the audit.

---

### Task 0: Branch and worktree

**Files:** none in the repo yet.

- [ ] **Step 1: Create the branch**

```bash
git fetch origin
git switch -c Shuxin-Y/flowchart-plan-b origin/Shuxin-Y/flowchart-skeleton
python3 -m venv venv && venv/bin/pip install -r requirements-docs.txt && venv/bin/playwright install chromium
TSAM_REQUIRE_E2E=1 venv/bin/pytest tests -q -rs && venv/bin/python scripts/audit_flowcharts.py && venv/bin/mkdocs build --strict
```
Expected: `84 passed`, `0 error(s)`, build passes.

- [ ] **Step 2: Commit nothing yet; push the branch**

```bash
git push -u origin Shuxin-Y/flowchart-plan-b
```

---

### Task 1: Area-coverage test and the P7 layout split

**Files:**
- Create: `tests/test_area_coverage.py`
- Modify: `docs/01-workflow/p07-error-process.md`, `docs/flowcharts/inventory.yml` (no row changes; node definitions move between two diagrams on the same page)

- [ ] **Step 1: Write the coverage test**

```python
# tests/test_area_coverage.py
"""Spec acceptance criterion 3: every one of the 34 areas has at least one leaf in the inventory."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
AREAS = range(1, 35)


def test_every_area_has_a_leaf():
    rows = yaml.safe_load((ROOT / "docs" / "flowcharts" / "inventory.yml").read_text(encoding="utf-8"))["nodes"]
    covered = {a for r in rows for a in (r.get("areas") or [])}
    missing = sorted(set(AREAS) - covered)
    assert not missing, f"areas without a leaf: {missing}"
```

- [ ] **Step 2: Run it to see it fail**

Run: `venv/bin/pytest tests/test_area_coverage.py -q`
Expected: FAIL listing the uncovered areas (at least 2, 6, 20, 23, 24, 25, 29, 32, 33, 34 at the start).

- [ ] **Step 3: Split the P7 diagram**

In `docs/01-workflow/p07-error-process.md` replace the single P7 diagram with two stacked diagrams under `## Sub-diagram`:
- **P7, part 1 (innovation type, mean, variance):** `P7_IN`, `P7_TYPE`, the count and event-time branch (`P7_COUNT_TESTS`, `P7_INGARCH`, `P7_RESCALING`, `P7_INTENSITY`), `P7_MEAN_TESTS`, `P7_MEAN_DEP`, `P7_ARMA_ERRORS`, `P7_ARFIMA_ERRORS`, the `-.->` to `P6`, `P7_VAR_TESTS`, `P7_VAR_DEP`, `P7_VAR_TYPE` and the seven variance leaves; the count/event path and the variance path both end in a terminator `P7_TO_PART_2(["Continue in part 2"])`. Foundation refs `F_WHITE_NOISE`, `F_WOLD`, `F_LONG_MEMORY`, `F_GARCH_STATIONARITY`, `F_LATENT_FILTERING`, `F_TIME_RESCALING` stay here.
- **P7, part 2 (distribution, regimes, correlation, assembly):** `P7_FROM_PART_1(["From part 1"])`, `P7_DIST_TESTS` … `P7_OUT`, the ref `P8`, and refs `F_LEVY`, `F_HMM`, `F_SKLAR`.
Every node keeps its ID, label and class; no inventory change. Two-line labels stay as they are; the split halves the width so the second lines are no longer clipped.

- [ ] **Step 4: Verify**

Run: `venv/bin/python scripts/audit_flowcharts.py | tail -1 && venv/bin/mkdocs build --strict 2>&1 | tail -1`
Expected: `0 error(s)`; build passes. Open the P7 page in `mkdocs serve` and confirm both second lines of the test nodes are readable.

- [ ] **Step 5: Commit**

```bash
git add tests/test_area_coverage.py docs/01-workflow/p07-error-process.md
git commit -m "test: assert every area has a leaf; split the P7 diagram into two parts"
```

---

### Task 2: P0 sub-diagram — data acquisition and cleaning

**Files:** `docs/01-workflow/p00-data.md`, `docs/flowcharts/inventory.yml`. Owner page: `01-workflow/p00-data.md`. Sections: the phase page.

**Flow.** `P0_IN(["Raw time-stamped data"])` → `P0_INSPECT_SAMPLING` → `P0_REGULAR{"Regular sampling?"}` →|"No"| `P0_ALIGN_TIMESTAMPS` → `P0_DEDUPLICATE` → `P0_RESAMPLE` → `P0_HAS_MISSING`; →|"Yes"| `P0_DEDUPLICATE`. `P0_HAS_MISSING{"Missing values?"}` →|"Short gaps"| `P0_MISSING_IMPUTE`; →|"Long gaps"| `P0_MISSING_SEGMENT`; →|"None"| `P0_HAS_OUTLIERS`. Both missing leaves → `P0_HAS_OUTLIERS{"Outliers?"}` →|"Yes"| `P0_OUTLIER_TAXONOMY` → `P0_ROBUST_FILTER` → `P0_UNITS_METADATA`; →|"No"| `P0_UNITS_METADATA`. `P0_UNITS_METADATA` → `P0_CUMULATIVE{"Cumulative measure?"}` →|"Yes"| `P0_CUMULATIVE_TO_FLOW` → `P0_CALENDAR_EFFECTS`; →|"No"| `P0_CALENDAR_EFFECTS`. `P0_CALENDAR_EFFECTS` → `P0_FREQUENCY{"Frequency conversion?"}` →|"Yes"| `P0_DISAGGREGATION` → `P0_VINTAGES`; →|"No"| `P0_VINTAGES`. `P0_VINTAGES` → `P1[["P1: Data-type gate"]]`. Classes: decisions `decision`; leaves `process`; `P0_IN` `terminator`; `P1` `ref`.

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P0_INSPECT_SAMPLING | Inspect sampling rate and resolution | | [31] | 01-workflow/p00-data.md |
| P0_ALIGN_TIMESTAMPS | Align timestamps | time zones, daylight-saving transitions | [31] | 01-workflow/p00-data.md |
| P0_DEDUPLICATE | Remove duplicate and out-of-order stamps | | [31] | 01-workflow/p00-data.md |
| P0_RESAMPLE | Resample and anti-alias | | [31, 13] | 01-workflow/p00-data.md |
| P0_MISSING_IMPUTE | Impute missing values | interpolation, Kalman smoother, multiple imputation | [31, 11] | 01-workflow/p00-data.md |
| P0_MISSING_SEGMENT | Segment around long gaps | | [31] | 01-workflow/p00-data.md |
| P0_OUTLIER_TAXONOMY | Classify outliers | additive, innovation, level shift, temporary change | [31, 24] | 01-workflow/p00-data.md |
| P0_ROBUST_FILTER | Robust filtering | median and Hampel filters | [24, 31] | 01-workflow/p00-data.md |
| P0_UNITS_METADATA | Check units and metadata | | [31] | 01-workflow/p00-data.md |
| P0_CUMULATIVE_TO_FLOW | Convert cumulative series to flows | | [31] | 01-workflow/p00-data.md |
| P0_CALENDAR_EFFECTS | Mark calendar effects | trading days, holidays, leap years | [29, 31] | 01-workflow/p00-data.md |
| P0_DISAGGREGATION | Temporal disaggregation and benchmarking | Chow-Lin, Denton | [31] | 01-workflow/p00-data.md |
| P0_VINTAGES | Track revisions and real-time vintages | | [31] | 01-workflow/p00-data.md |

- [ ] **Step 1:** Replace the "Diagram pending" note under `## Sub-diagram` with the diagram. Delete the bold "Topics carried over" lead-in and its list on this page (the leaves now carry that content).
- [ ] **Step 2:** Add the 13 inventory rows (`phase: P0`).
- [ ] **Step 3:** `venv/bin/python scripts/scaffold_stubs.py` (appends 13 pending sections), then `venv/bin/python scripts/audit_flowcharts.py | tail -1` → `0 error(s)`; `venv/bin/mkdocs build --strict`.
- [ ] **Step 4:** Commit `feat(flowchart): P0 data acquisition and cleaning sub-diagram`.

---

### Task 3: P3 sub-diagram — exploratory diagnostics

**Files:** `docs/01-workflow/p03-exploratory-diagnostics.md`, `docs/flowcharts/inventory.yml`, `docs/00-foundations/stochastic-processes.md` (scaffolded foundation sections). Owner page: `01-workflow/p03-exploratory-diagnostics.md`. Sections: the phase page; foundation rows in `00-foundations/stochastic-processes.md`.

**Flow.** `P3_IN(["Series and flags from P2"])` → `P3_PLOT` → `P3_DISTRIBUTION` → `P3_VARIANCE_STABILITY` → `P3_HETERO{"Variance stable?"}` →|"No"| `P3_GARCH_FLAG["Set flag: GARCH effects"]` → `P3_TREND_TYPE`; →|"Yes"| `P3_TREND_TYPE`. `P3_TREND_TYPE` → `P3_UNIT_ROOT` → `P3_BREAK_SUSPECTED{"Break suspected?"}` →|"Yes"| `P3_UNIT_ROOT_BREAKS` → `P3_STRUCTURAL_BREAKS` → `P3_BREAK_FLAG["Set flag: break handling"]` → `P3_UR_VERDICT`; →|"No"| `P3_UR_VERDICT{"Unit root?"}` →|"Yes"| `P3_DIFF_FLAG["Set flag: difference"]` → `P3_SEASONALITY`; →|"No"| `P3_SEASONALITY`; →|"Explosive"| `P3_EXPLOSIVE` → `P3_SEASONALITY`. `P3_VARIANCE_RATIO` hangs off `P3_UNIT_ROOT` as a parallel check: `P3_UNIT_ROOT --> P3_VARIANCE_RATIO --> P3_BREAK_SUSPECTED` (draw `P3_UNIT_ROOT --> P3_BREAK_SUSPECTED` as well). `P3_SEASONALITY` → `P3_SEASONAL{"Seasonal?"}` →|"Yes"| `P3_SEASONAL_UNIT_ROOT` → `P3_SDIFF_FLAG["Set flag: seasonal difference"]` → `P3_ACF_PACF`; →|"No"| `P3_ACF_PACF`. `P3_ACF_PACF` → `P3_DECAY{"ACF decay?"}` →|"Hyperbolic"| `P3_LONG_MEMORY` → `P3_LONG_MEMORY_FLAG["Set flag: long memory"]` → `P3_NONLINEARITY`; →|"Geometric or cut-off"| `P3_NONLINEARITY`. `P3_NONLINEARITY` → `P3_NONLINEAR{"Nonlinear?"}` →|"Yes"| `P3_NONLINEAR_FLAG["Set flag: nonlinear"]` → `P3_TREND_TEST`; →|"No"| `P3_TREND_TEST`. `P3_TREND_TEST` is `P3_NONPARAMETRIC_TREND`. Then `P3_MULTI{"Multivariate flag?"}` →|"Yes"| `P3_CROSS_CORRELATION` → `P3_COINTEGRATION_PRECHECK` → `P3_OUT`; →|"No"| `P3_OUT(["To P4 Transformations"])`. Foundation refs with `-.-`: `F_STATIONARITY -.- P3_TREND_TYPE`, `F_UNIT_ROOT_ASYMPTOTICS -.- P3_UNIT_ROOT`, `F_ERGODICITY -.- P3_PLOT`. Also `P4[["P4: Transformations"]]` is not needed (terminator suffices).

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P3_PLOT | Plot the series |  | [2] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_DISTRIBUTION | Test the distribution | Shapiro-Wilk, Jarque-Bera, skewness, tail index | [5, 2] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_VARIANCE_STABILITY | Check variance stability | rolling variance, ARCH-LM on levels | [10, 5] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_TREND_TYPE | Trend-stationary or difference-stationary |  | [28, 2] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_UNIT_ROOT | Unit-root tests | ADF, KPSS, PP, DF-GLS | [5, 28] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_UNIT_ROOT_BREAKS | Unit-root tests with breaks | Zivot-Andrews | [5, 30] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_VARIANCE_RATIO | Variance-ratio test | Lo-MacKinlay | [5, 28] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_EXPLOSIVE | Explosive-root and bubble tests | PSY, GSADF | [28] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_STRUCTURAL_BREAKS | Structural-break tests | Chow, CUSUM, Bai-Perron | [30, 5] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_SEASONALITY | Detect seasonality | seasonal subseries, periodogram peaks | [29, 2] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_SEASONAL_UNIT_ROOT | Seasonal unit-root tests | HEGY, Canova-Hansen, OCSB | [29, 5] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_ACF_PACF | Read the ACF and PACF |  | [2] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_LONG_MEMORY | Long-memory indicators | Hurst exponent, GPH | [7] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_NONLINEARITY | Nonlinearity tests | BDS, Terasvirta, Tsay, Keenan | [8, 5] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_NONPARAMETRIC_TREND | Nonparametric trend tests | Mann-Kendall, Sen slope, prewhitening | [24] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_CROSS_CORRELATION | Cross-correlation and lead-lag |  | [9] | 01-workflow/p03-exploratory-diagnostics.md |
| P3_COINTEGRATION_PRECHECK | Cointegration pre-check | spurious-regression warning | [28, 9] | 01-workflow/p03-exploratory-diagnostics.md |

**Foundation rows (phase F).**

| ID | label | section |
|---|---|---|
| F_STATIONARITY | Strict and weak stationarity | 00-foundations/stochastic-processes.md#strict-and-weak-stationarity |
| F_ERGODICITY | Ergodicity and mixing | 00-foundations/stochastic-processes.md#ergodicity-and-mixing |
| F_UNIT_ROOT_ASYMPTOTICS | Random walks and unit-root asymptotics | 00-foundations/stochastic-processes.md#random-walks-and-unit-root-asymptotics |

- [ ] **Step 1:** Replace the pending note with the diagram; delete the "Topics carried over" lead-in and list.
- [ ] **Step 2:** Add 17 leaf rows (`phase: P3`, areas as listed) and 3 foundation rows (`phase: F`, `areas: [1]`).
- [ ] **Step 3:** Scaffold; audit `0 error(s)`; strict build.
- [ ] **Step 4:** Commit `feat(flowchart): P3 exploratory diagnostics sub-diagram and foundation hooks`.

---

### Task 4: P4 sub-diagram — transformations

**Files:** `docs/01-workflow/p04-transformations.md`, inventory. Owner page: the phase page. Sections: the phase page.

**Flow.** `P4_IN(["Flags from P3"])` → `P4_VARIANCE{"Variance grows with level?"}` →|"Yes"| `P4_LOG_BOXCOX` → `P4_TREND`; →|"No"| `P4_TREND{"Trend type?"}` →|"Deterministic"| `P4_DETREND` → `P4_SEASON`; →|"Stochastic"| `P4_DIFFERENCE` → `P4_OVERDIFFERENCING` → `P4_SEASON`; →|"Long memory flag"| `P4_FRACTIONAL_DIFFERENCE` → `P4_SEASON`; →|"None"| `P4_SEASON`. `P4_SEASON{"Seasonal flag?"}` →|"Single period"| `P4_SEASONAL_CHOICE{"Difference or adjust?"}` →|"Difference"| `P4_SEASONAL_DIFFERENCE` → `P4_BREAKS`; →|"Adjust"| `P4_SEASONAL_ADJUSTMENT` → `P4_BREAKS`; `P4_SEASON` →|"Multiple periods"| `P4_MULTIPLE_SEASONALITY` → `P4_BREAKS`; →|"No"| `P4_BREAKS`. `P4_BREAKS{"Break flag?"}` →|"Yes"| `P4_BREAK_HANDLING` → `P4_DECOMP`; →|"No"| `P4_DECOMP{"Decomposition wanted?"}` →|"Filter-based"| `P4_FILTER_DECOMPOSITION` → `P4_RETEST`; →|"Model-based"| `P4_MODEL_DECOMPOSITION` → `P4_RETEST`; →|"Nonparametric"| `P4_SSA` → `P4_RETEST`; →|"No"| `P4_RETEST`. `P4_RETEST` → `P4_STATIONARY{"Stationary now?"}` →|"Yes"| `P4_OUT(["To P5 Representation"])`; →|"No"| `-.->` `P3[["P3: Exploratory diagnostics"]]`.

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P4_LOG_BOXCOX | Variance-stabilising transforms | log, Box-Cox | [2] | 01-workflow/p04-transformations.md |
| P4_DIFFERENCE | Regular differencing |  | [2] | 01-workflow/p04-transformations.md |
| P4_OVERDIFFERENCING | Check for over-differencing |  | [2] | 01-workflow/p04-transformations.md |
| P4_FRACTIONAL_DIFFERENCE | Fractional differencing |  | [7] | 01-workflow/p04-transformations.md |
| P4_DETREND | Detrending by regression on time |  | [2, 28] | 01-workflow/p04-transformations.md |
| P4_SEASONAL_DIFFERENCE | Seasonal differencing |  | [29] | 01-workflow/p04-transformations.md |
| P4_SEASONAL_ADJUSTMENT | Seasonal adjustment | classical decomposition, STL, X-13 and SEATS | [29, 3] | 01-workflow/p04-transformations.md |
| P4_MULTIPLE_SEASONALITY | Multiple seasonality | MSTL, TBATS, Fourier terms | [29] | 01-workflow/p04-transformations.md |
| P4_BREAK_HANDLING | Handle structural breaks | segmenting, regime dummies, time-varying parameters | [30] | 01-workflow/p04-transformations.md |
| P4_FILTER_DECOMPOSITION | Filter-based decomposition | HP, Baxter-King, Christiano-Fitzgerald, Hamilton | [13, 3] | 01-workflow/p04-transformations.md |
| P4_MODEL_DECOMPOSITION | Model-based decomposition | Beveridge-Nelson, unobserved components | [11, 3] | 01-workflow/p04-transformations.md |
| P4_SSA | Singular spectrum analysis |  | [13] | 01-workflow/p04-transformations.md |
| P4_RETEST | Retest stationarity after transforming |  | [5] | 01-workflow/p04-transformations.md |

- [ ] **Steps:** as Task 2 (replace the note, 13 rows with `phase: P4`, scaffold, audit, build). Commit `feat(flowchart): P4 transformations sub-diagram`.

---

### Task 5: P6 sub-diagram — conditional-mean model class

**Files:** `docs/01-workflow/p06-mean-model-class.md`, inventory, reference landing pages (scaffolded). Owner page: the phase page. Sections: reference landing pages as listed.

**Flow.** `P6_IN(["Transformed series, representation, flags"])` → `P6_EXOGENOUS{"Exogenous variables?"}` →|"Future known"| `P6_EXOG_FLAG["Set flag: exogenous regressors"]` → `P6_SCALE`; →|"Co-forecast"| `P6_MULTI_FLAG["Set flag: multivariate"]` → `P6_SCALE`; →|"None"| `P6_SCALE{"Series structure?"}` →|"Global flag"| `P6_GLOBAL_MODELS` → `P6_OUT`; →|"Multivariate"| `P6_COINTEGRATED{"Cointegrated?"}` →|"Yes"| `P6_VECM`; →|"No"| `P6_VAR`; →|"Many variables"| `P6_DIMENSION{"Dimension reduction?"}` →|"Factors"| `P6_FACTOR_MODELS`; →|"Shrinkage"| `P6_REGULARISED_VAR`; →|"Graph"| `P6_GRAPHICAL_MODELS`; →|"Tensor"| `P6_TENSOR_AR`; `P6_VAR` →|"Structural question"| `P6_SVAR`; `P6_FACTOR_MODELS` → `P6_FAVAR`; `P6_SCALE` →|"Mixed-frequency flag"| `P6_MIXED_FREQUENCY`; all multivariate leaves → `P6_OUT`. `P6_SCALE` →|"Univariate"| `P6_DEPENDENCE{"Dependence type?"}` →|"Linear"| `P6_LINEAR{"Long memory flag?"}` →|"Yes"| `P6_ARFIMA` → `P6_OUT`; →|"No"| `P6_LINEAR_FAMILY{"Family?"}` →|"Autoregressive"| `P6_AR_MA_ARMA` → `P6_ARIMA_SARIMA` → `P6_OUT`; →|"Exogenous flag"| `P6_ARIMAX` → `P6_DYNAMIC_REGRESSION` → `P6_TRANSFER_FUNCTION` → `P6_OUT`; →|"Smoothing"| `P6_ETS` → `P6_THETA` → `P6_OUT`; →|"Periodic"| `P6_PERIODIC_AR` → `P6_OUT`; →|"Intermittent"| `P6_INTERMITTENT` → `P6_OUT`. `P6_DEPENDENCE` →|"Nonlinear flag"| `P6_NONLINEAR_FAMILY{"Regime mechanism?"}` →|"Threshold"| `P6_THRESHOLD`; →|"Smooth"| `P6_SMOOTH_TRANSITION`; →|"Hidden state"| `P6_MARKOV_SWITCHING`; →|"Bilinear"| `P6_BILINEAR`; →|"Unknown form"| `P6_NONPARAMETRIC`; all → `P6_OUT`. `P6_DEPENDENCE` →|"Time-varying coefficients"| `P6_TVP_REGRESSION` → `P6_OUT`; →|"Latent components"| `P6_STRUCTURAL_TS` → `P6_DLM` → `P6_BSTS` → `P6_OUT`; →|"Bayesian priors"| `P6_BVAR` → `P6_TVP_VAR` → `P6_OUT`; →|"Input-output system"| `P6_ARX_ARMAX` → `P6_SUBSPACE` → `P6_HAMMERSTEIN_WIENER` → `P6_SINDY` → `P6_OUT`; →|"Learn from data"| `P6_ML_FAMILY{"Model class?"}` →|"Trees"| `P6_TREE_ENSEMBLES`; →|"Kernel"| `P6_GAUSSIAN_PROCESS`; →|"Reservoir"| `P6_RESERVOIR`; →|"Recurrent"| `P6_RNN`; →|"Convolutional"| `P6_TCN`; →|"Attention"| `P6_TRANSFORMERS`; →|"State-space sequence"| `P6_SSM_SEQUENCE`; →|"MLP forecasters"| `P6_NEURAL_FORECASTERS`; →|"Pretrained"| `P6_FOUNDATION_MODELS`; →|"Generative"| `P6_GENERATIVE`; →|"Hybrid"| `P6_HYBRID`; all → `P6_OUT`. `P6_OUT(["To P7 Error process"])`. Foundation ref: `F_LAG_OPERATOR -.- P6_AR_MA_ARMA`. Refs: `B1[["B1 Counts and categorical"]]` reached from `P6_DEPENDENCE` →|"Count-valued"| (the count GLM families are B1 leaves).

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P6_AR_MA_ARMA | AR, MA and ARMA | | [3] | reference/03-classical/index.md |
| P6_ARIMA_SARIMA | ARIMA and SARIMA | | [3] | reference/03-classical/index.md |
| P6_ARIMAX | ARIMAX and SARIMAX |  | [3, 27] | reference/03-classical/index.md |
| P6_ETS | Exponential smoothing and ETS | | [3] | reference/03-classical/index.md |
| P6_THETA | Theta method | | [22, 3] | reference/22-forecasting-practice/index.md |
| P6_DYNAMIC_REGRESSION | Distributed-lag and ADL models | | [27, 3] | reference/27-regression-time-series/index.md |
| P6_TRANSFER_FUNCTION | Transfer-function and intervention models | | [3, 33] | reference/03-classical/index.md |
| P6_PERIODIC_AR | Periodic autoregression | | [29] | reference/29-seasonality-calendar/index.md |
| P6_INTERMITTENT | Intermittent demand | Croston, TSB | [34, 22] | reference/34-probabilistic-forecasting/index.md |
| P6_ARFIMA | ARFIMA | | [7] | reference/07-long-memory/index.md |
| P6_THRESHOLD | Threshold models | TAR, SETAR, MTAR | [8] | reference/08-nonlinear/index.md |
| P6_SMOOTH_TRANSITION | Smooth-transition models | STAR, LSTAR, ESTAR | [8] | reference/08-nonlinear/index.md |
| P6_MARKOV_SWITCHING | Markov-switching models | | [8, 30] | reference/08-nonlinear/index.md |
| P6_BILINEAR | Bilinear models | | [8] | reference/08-nonlinear/index.md |
| P6_NONPARAMETRIC | Nonparametric and additive regression | kernels, local polynomials, GAM | [8, 24] | reference/08-nonlinear/index.md |
| P6_TVP_REGRESSION | Time-varying parameter regression | | [30, 11] | reference/30-structural-change/index.md |
| P6_VAR | VAR | | [9] | reference/09-multivariate/index.md |
| P6_VECM | VECM | | [9, 28] | reference/09-multivariate/index.md |
| P6_SVAR | SVAR | identification schemes in P10 | [9, 21] | reference/09-multivariate/index.md |
| P6_FACTOR_MODELS | Static and dynamic factor models | | [9] | reference/09-multivariate/index.md |
| P6_REGULARISED_VAR | Regularised VAR | LASSO, ridge, elastic net | [9] | reference/09-multivariate/index.md |
| P6_GRAPHICAL_MODELS | Graphical models and sparse precision matrices | | [9] | reference/09-multivariate/index.md |
| P6_TENSOR_AR | Matrix and tensor autoregression | | [9] | reference/09-multivariate/index.md |
| P6_FAVAR | FAVAR and global VAR | | [9] | reference/09-multivariate/index.md |
| P6_MIXED_FREQUENCY | Mixed-frequency models | MIDAS, mixed-frequency VAR | [22, 9] | reference/22-forecasting-practice/index.md |
| P6_STRUCTURAL_TS | Structural time-series models | local level, local linear trend, seasonal, cycle | [11] | reference/11-state-space/index.md |
| P6_DLM | Dynamic linear models | | [11, 12] | reference/11-state-space/index.md |
| P6_BSTS | Bayesian structural time series | | [11, 12] | reference/11-state-space/index.md |
| P6_BVAR | Bayesian VAR | Minnesota and conjugate priors | [12] | reference/12-bayesian/index.md |
| P6_TVP_VAR | Time-varying parameter VAR | | [12, 30] | reference/12-bayesian/index.md |
| P6_ARX_ARMAX | ARX and ARMAX input-output models |  | [33] | reference/33-system-identification/index.md |
| P6_SUBSPACE | Subspace identification | N4SID | [33] | reference/33-system-identification/index.md |
| P6_HAMMERSTEIN_WIENER | Hammerstein-Wiener models | | [33] | reference/33-system-identification/index.md |
| P6_SINDY | Sparse identification of nonlinear dynamics | | [33] | reference/33-system-identification/index.md |
| P6_TREE_ENSEMBLES | Tree ensembles on lag features | random forests, XGBoost, LightGBM | [18] | reference/18-machine-learning/index.md |
| P6_GAUSSIAN_PROCESS | Gaussian-process regression | | [18] | reference/18-machine-learning/index.md |
| P6_RESERVOIR | Reservoir computing | echo state networks | [18] | reference/18-machine-learning/index.md |
| P6_RNN | Recurrent networks | RNN, LSTM, GRU | [18] | reference/18-machine-learning/index.md |
| P6_TCN | Temporal convolutional networks | | [18] | reference/18-machine-learning/index.md |
| P6_TRANSFORMERS | Transformers for time series | Informer, Autoformer, PatchTST | [18] | reference/18-machine-learning/index.md |
| P6_SSM_SEQUENCE | State-space sequence models | S4, S5, Mamba | [18] | reference/18-machine-learning/index.md |
| P6_NEURAL_FORECASTERS | Neural forecasters | N-BEATS, N-HiTS, TiDE | [18] | reference/18-machine-learning/index.md |
| P6_FOUNDATION_MODELS | Foundation models | Chronos, Lag-Llama, Moirai, TimesFM, MOMENT | [18] | reference/18-machine-learning/index.md |
| P6_GENERATIVE | Generative models for time series | diffusion models | [18] | reference/18-machine-learning/index.md |
| P6_HYBRID | Hybrid models | ARIMA with neural residuals | [18] | reference/18-machine-learning/index.md |
| P6_GLOBAL_MODELS | Global models across many series | | [18, 22] | reference/18-machine-learning/index.md |

**Foundation row.** `F_LAG_OPERATOR` | Lag operator, difference equations and characteristic roots | `00-foundations/stochastic-processes.md#lag-operator-difference-equations-and-characteristic-roots`.

- [ ] **Steps:** replace the note (and delete the "Topics carried over" lead-in), 46 rows `phase: P6` plus the F row, scaffold, audit, build. If the diagram is too wide, split it into part 1 (routing, univariate, multivariate) and part 2 (nonlinear, state-space, Bayesian, system identification, ML) as P7 was, with `P6_TO_PART_2` / `P6_FROM_PART_1` terminators. Commit `feat(flowchart): P6 conditional-mean model class sub-diagram`.

---

### Task 6: P8 sub-diagram — estimation

**Files:** `docs/01-workflow/p08-estimation.md`, inventory, reference landing pages. Owner page: the phase page. Sections: as listed.

**Flow.** `P8_IN(["Joint model from P7"])` → `P8_OBSERVABLE{"All components observable?"}` →|"Yes"| `P8_LINEAR{"Linear in parameters?"}` →|"Yes"| `P8_OLS_GLS` → `P8_CONVERGENCE`; →|"Moments only"| `P8_YULE_WALKER` → `P8_DURBIN_LEVINSON` → `P8_HANNAN_RISSANEN` → `P8_CONVERGENCE`; →|"Cointegrating regression"| `P8_FMOLS_DOLS` → `P8_CONVERGENCE`; →|"Outlier-prone"| `P8_ROBUST` → `P8_CONVERGENCE`. `P8_OBSERVABLE` →|"No"| `P8_LIKELIHOOD{"Likelihood tractable?"}` →|"Gaussian state space"| `P8_PREDICTION_ERROR` → `P8_KALMAN` → `P8_MLE` → `P8_CONVERGENCE`; →|"Closed form"| `P8_MLE` ; →|"Misspecified distribution"| `P8_QMLE` → `P8_CONVERGENCE`; →|"Nonlinear state"| `P8_NONLINEAR_FILTERS` → `P8_PARTICLE_FILTERS` → `P8_CONVERGENCE`; →|"Latent variables"| `P8_EM` → `P8_CONVERGENCE`; →|"Intractable"| `P8_INTRACTABLE{"Approach?"}` →|"Moment conditions"| `P8_GMM`; →|"Frequency domain"| `P8_WHITTLE`; →|"Priors"| `P8_MCMC` → `P8_VARIATIONAL`; →|"Simulate"| `P8_SIMULATION_INFERENCE`; →|"Loss minimisation"| `P8_EMPIRICAL_LOSS` → `P8_HYPERPARAMETERS`; all → `P8_CONVERGENCE`. `P8_CONVERGENCE` → `P8_CONVERGED{"Converged?"}` →|"Yes"| `P8_OUT(["To P9 Diagnostics"])`; →|"No"| `-.->` `P6[["P6: Conditional-mean model class"]]` labelled "Simplify or re-initialise". Foundation refs: `F_LLN -.- P8_MLE`, `F_CLT -.- P8_QMLE`.

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P8_OLS_GLS | OLS, GLS and feasible GLS | Cochrane-Orcutt, Prais-Winsten | [4, 27] | reference/04-estimation/index.md |
| P8_YULE_WALKER | Yule-Walker and the method of moments | | [4] | reference/04-estimation/index.md |
| P8_DURBIN_LEVINSON | Durbin-Levinson and the innovations algorithm | | [4] | reference/04-estimation/index.md |
| P8_HANNAN_RISSANEN | Hannan-Rissanen and Burg estimation | | [4] | reference/04-estimation/index.md |
| P8_FMOLS_DOLS | Cointegrating regression | FMOLS, DOLS | [4, 28] | reference/04-estimation/index.md |
| P8_ROBUST | Robust estimation | M-estimators, LAD | [24, 4] | reference/24-robust-nonparametric/index.md |
| P8_PREDICTION_ERROR | Prediction-error decomposition | | [4, 11] | reference/04-estimation/index.md |
| P8_KALMAN | Kalman filter and smoother | | [11] | reference/11-state-space/index.md |
| P8_MLE | Maximum likelihood, exact and conditional | | [4] | reference/04-estimation/index.md |
| P8_QMLE | Quasi-maximum likelihood and sandwich standard errors | | [4] | reference/04-estimation/index.md |
| P8_NONLINEAR_FILTERS | Extended and unscented Kalman filters | | [11] | reference/11-state-space/index.md |
| P8_PARTICLE_FILTERS | Particle filters | | [11] | reference/11-state-space/index.md |
| P8_EM | EM for state-space models | | [4, 11] | reference/04-estimation/index.md |
| P8_GMM | Generalised method of moments | | [4] | reference/04-estimation/index.md |
| P8_WHITTLE | Whittle and local Whittle estimation | | [4, 7] | reference/04-estimation/index.md |
| P8_MCMC | Bayesian computation | MCMC, Gibbs, Metropolis-Hastings | [12] | reference/12-bayesian/index.md |
| P8_VARIATIONAL | Variational inference | | [12] | reference/12-bayesian/index.md |
| P8_SIMULATION_INFERENCE | Simulation-based inference | ABC, indirect inference | [25, 4] | reference/25-simulation/index.md |
| P8_EMPIRICAL_LOSS | Empirical-loss minimisation | gradient descent, boosting | [18, 4] | reference/18-machine-learning/index.md |
| P8_HYPERPARAMETERS | Time-aware hyperparameter tuning | leakage-safe splits | [18, 6] | reference/18-machine-learning/index.md |
| P8_CONVERGENCE | Convergence and numerical checks | | [4] | 01-workflow/p08-estimation.md |

**Foundation rows.** `F_LLN` | Law of large numbers | `00-foundations/asymptotics.md#law-of-large-numbers` (heading exists). `F_CLT` | Central limit theorem | `00-foundations/asymptotics.md#central-limit-theorem` (heading exists).

- [ ] **Steps:** replace the note, 21 rows `phase: P8` plus 2 F rows (`areas: [1]`), scaffold, audit, build. Commit `feat(flowchart): P8 estimation sub-diagram`.

---

### Task 7: P9 sub-diagram — diagnostics and model selection

**Files:** `docs/01-workflow/p09-diagnostics-selection.md`, inventory, `reference/06-model-selection/index.md`. Owner page: the phase page.

**Flow.** `P9_IN(["Estimated joint model"])` → `P9_RESIDUAL_AUTOCORRELATION` → `P9_AC{"Autocorrelation left?"}` →|"Yes"| `-.->` `P6[["P6: Conditional-mean model class"]]`; →|"No"| `P9_RESIDUAL_ARCH` → `P9_ARCH{"ARCH left?"}` →|"Yes"| `-.->` `P7[["P7: Error-process specification"]]`; →|"No"| `P9_RESIDUAL_NORMALITY` → `P9_RESIDUAL_NONLINEARITY` → `P9_MODEL_KIND{"Model kind?"}` →|"Volatility"| `P9_VOLATILITY_DIAGNOSTICS` → `P9_SELECT`; →|"Counts"| `P9_COUNT_DIAGNOSTICS` → `P9_SELECT`; →|"Other"| `P9_SELECT`. `P9_SELECT` is `P9_INFORMATION_CRITERIA` → `P9_INFERENCE_NEEDED{"Finite-sample inference?"}` →|"Yes"| `P9_BOOTSTRAP` → `P9_COMPARE`; →|"No"| `P9_COMPARE`. `P9_COMPARE` is `P9_FORECAST_COMPARISON` → `P9_ENCOMPASSING` → `P9_PASS{"All diagnostics pass?"}` →|"Yes"| `P9_OUT(["To P10 Inference"])`; →|"No"| `-.->` `P6`.

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P9_RESIDUAL_NONLINEARITY | Remaining nonlinearity | BDS on residuals | [8, 5] | 01-workflow/p09-diagnostics-selection.md |
| P9_VOLATILITY_DIAGNOSTICS | Volatility model diagnostics | standardised residuals, sign-bias test, news impact curve | [10] | 01-workflow/p09-diagnostics-selection.md |
| P9_INFORMATION_CRITERIA | Information criteria | AIC, BIC, HQIC, WAIC, LOO | [6, 12] | reference/06-model-selection/index.md |
| P9_BOOTSTRAP | Bootstrap inference | block, stationary, sieve | [5, 25] | reference/06-model-selection/index.md |
| P9_FORECAST_COMPARISON | Forecast comparison tests | Diebold-Mariano, Clark-West, reality check, model confidence set | [6] | reference/06-model-selection/index.md |
| P9_ENCOMPASSING | Forecast encompassing | | [6] | reference/06-model-selection/index.md |

- [ ] **Steps:** replace the note, 10 rows `phase: P9`, scaffold, audit, build. Commit `feat(flowchart): P9 diagnostics and model selection sub-diagram`.

---

### Task 8: P10 sub-diagram — inference and interpretation

**Files:** `docs/01-workflow/p10-inference.md`, inventory, reference landing pages. Owner page: the phase page.

**Flow.** `P10_IN(["Validated model and purpose flag"])` → `P10_PURPOSE{"Purpose?"}` →|"Forecasting"| `P10_POINT_FORECASTS` → `P10_INTERVALS` → `P10_DENSITY_QUANTILE` → `P10_MULTISTEP` → `P10_HIERARCHY{"Hierarchy or many series?"}` →|"Yes"| `P10_RECONCILIATION` → `P10_COMBINATION`; →|"No"| `P10_COMBINATION` → `P10_JUDGMENTAL` → `P10_MIXED{"Mixed-frequency flag?"}` →|"Yes"| `P10_NOWCASTING` → `P10_OUT`; →|"No"| `P10_OUT`. `P10_PURPOSE` →|"Causal or structural"| `P10_COEFFICIENT_TESTS` → `P10_HAC` → `P10_SYSTEM{"Multivariate?"}` →|"Yes"| `P10_COINTEGRATION` → `P10_GRANGER` → `P10_NONLINEAR_CAUSALITY` → `P10_SVAR_IDENTIFICATION` → `P10_IRF_FEVD` → `P10_LOCAL_PROJECTIONS` → `P10_OUT`; →|"No"| `P10_COUNTERFACTUALS` → `P10_OUT`. `P10_PURPOSE` →|"Risk"| `P10_RISK_MEASURES` → `P10_SCENARIOS` → `P10_OUT`. `P10_PURPOSE` →|"Black-box model"| `P10_INTERPRETABILITY` → `P10_OUT`. `P10_OUT(["To P11 Validation"])`. Foundation refs: `F_CONDITIONAL_EXPECTATION -.- P10_POINT_FORECASTS`, `F_PROJECTION -.- P10_INTERVALS`.

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P10_COEFFICIENT_TESTS | Coefficient and restriction tests | t, F, likelihood ratio, Wald, Lagrange multiplier | [5] | reference/05-hypothesis-testing/index.md |
| P10_HAC | HAC inference | Newey-West, bandwidth choice | [27, 5] | reference/27-regression-time-series/index.md |
| P10_COINTEGRATION | Cointegration inference | Engle-Granger, Johansen, ARDL bounds | [28, 5] | reference/28-nonstationarity-theory/index.md |
| P10_GRANGER | Granger, Sims and Toda-Yamamoto causality | | [21] | reference/21-causal-inference/index.md |
| P10_NONLINEAR_CAUSALITY | Nonlinear causal discovery | transfer entropy, convergent cross mapping, PCMCI | [21] | reference/21-causal-inference/index.md |
| P10_SVAR_IDENTIFICATION | SVAR identification | Cholesky, sign restrictions, long-run, external instruments | [21, 9] | reference/21-causal-inference/index.md |
| P10_IRF_FEVD | Impulse responses and variance decompositions | | [9, 21] | reference/09-multivariate/index.md |
| P10_LOCAL_PROJECTIONS | Local projections | | [21] | reference/21-causal-inference/index.md |
| P10_COUNTERFACTUALS | Counterfactual designs | intervention analysis, interrupted time series, difference-in-differences, synthetic control, CausalImpact | [21] | reference/21-causal-inference/index.md |
| P10_POINT_FORECASTS | Point forecasts and horizons | | [22] | reference/22-forecasting-practice/index.md |
| P10_INTERVALS | Prediction intervals | analytical, bootstrap, conformal | [34, 22] | reference/34-probabilistic-forecasting/index.md |
| P10_DENSITY_QUANTILE | Density and quantile forecasts | | [34] | reference/34-probabilistic-forecasting/index.md |
| P10_MULTISTEP | Multi-step strategies | recursive, direct, MIMO | [34, 22] | reference/34-probabilistic-forecasting/index.md |
| P10_RECONCILIATION | Hierarchical and temporal reconciliation | bottom-up, top-down, MinT | [22, 34] | reference/22-forecasting-practice/index.md |
| P10_COMBINATION | Forecast combination and model averaging | | [22, 12] | reference/22-forecasting-practice/index.md |
| P10_JUDGMENTAL | Judgmental adjustment | | [22] | reference/22-forecasting-practice/index.md |
| P10_NOWCASTING | Nowcasting | bridge equations, factor models | [22, 9] | reference/22-forecasting-practice/index.md |
| P10_RISK_MEASURES | Risk measures and their backtests | VaR, expected shortfall, Kupiec, Christoffersen | [10] | reference/10-volatility/index.md |
| P10_SCENARIOS | Scenario simulation and stress testing | | [25, 10] | reference/25-simulation/index.md |
| P10_INTERPRETABILITY | Interpretability | SHAP, attention | [18] | reference/18-machine-learning/index.md |

**Foundation rows.** `F_CONDITIONAL_EXPECTATION` | Conditional expectation as the optimal forecast | `00-foundations/stochastic-processes.md#conditional-expectation-as-the-optimal-forecast`. `F_PROJECTION` | Projection theorem and best linear prediction | `00-foundations/stochastic-processes.md#projection-theorem-and-best-linear-prediction`.

- [ ] **Steps:** replace the note, 20 rows `phase: P10`, 2 F rows, scaffold, audit, build. Commit `feat(flowchart): P10 inference and interpretation sub-diagram`.

---

### Task 9: P11 sub-diagram — validation and deployment

**Files:** `docs/01-workflow/p11-validation-deployment.md`, inventory, reference landing pages. Owner page: the phase page.

**Flow.** `P11_IN(["Model and forecasts from P10"])` → `P11_ROLLING_ORIGIN` → `P11_BACKTESTING` → `P11_METRIC_KIND{"Output type?"}` →|"Point"| `P11_POINT_METRICS`; →|"Probabilistic"| `P11_PROBABILISTIC_METRICS`; →|"Labels or anomalies"| `P11_CLASSIFICATION_METRICS`; →|"Change points"| `P11_CHANGE_POINT_METRICS`; all → `P11_ACCEPTABLE{"Performance acceptable?"}` →|"No"| `-.->` `P6[["P6: Conditional-mean model class"]]`; →|"Yes"| `P11_DOCUMENTATION` → `P11_DRIFT_MONITORING` → `P11_SPC` → `P11_DRIFT{"Drift detected?"}` →|"Yes"| `P11_ONLINE_UPDATING` → `-.->` `P8[["P8: Estimation"]]`; →|"No"| `P11_RETRAINING` → `P11_OUT(["Validated model deployed"])`.

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P11_ROLLING_ORIGIN | Rolling-origin backtesting | look-ahead bias, backtest overfitting | [6] | 01-workflow/p11-validation-deployment.md |
| P11_POINT_METRICS | Point-forecast metrics | RMSE, MAE, MAPE, MASE | [6] | reference/06-model-selection/index.md |
| P11_PROBABILISTIC_METRICS | Probabilistic metrics | coverage, CRPS, pinball loss, log score, PIT | [34] | reference/34-probabilistic-forecasting/index.md |
| P11_CLASSIFICATION_METRICS | Classification and anomaly metrics | F1, event-level precision and recall, NAB score | [19] | reference/19-classification-anomaly/index.md |
| P11_CHANGE_POINT_METRICS | Change-point metrics | detection delay, false-alarm rate | [19, 30] | reference/19-classification-anomaly/index.md |
| P11_DOCUMENTATION | Document the model specification |  | [6] | 01-workflow/p11-validation-deployment.md |
| P11_DRIFT_MONITORING | Drift monitoring | KL divergence, spectral shift, ADWIN, DDM | [23, 30] | reference/23-online-adaptive/index.md |
| P11_SPC | Statistical process control | Shewhart and EWMA charts | [30, 23] | reference/30-structural-change/index.md |
| P11_ONLINE_UPDATING | Online updating | recursive least squares, forgetting factors, online Kalman, online gradient | [23] | reference/23-online-adaptive/index.md |
| P11_RETRAINING | Retraining policy | | [23] | 01-workflow/p11-validation-deployment.md |

- [ ] **Steps:** replace the note (and delete the "Topics carried over" lead-in), 11 rows `phase: P11`, scaffold, audit, build. Commit `feat(flowchart): P11 validation and deployment sub-diagram`.

---

### Task 10: The ten purpose sub-charts (P2)

**Files:** `docs/01-workflow/p02-purpose/01-forecasting.md` … `10-simulation.md`, inventory, reference landing pages. Owner: the directory `01-workflow/p02-purpose/`. Each page keeps its structural H2s (`Sub-chart`, `P10 inference for this purpose`, `P11 metrics for this purpose`); the diagram replaces the pending note under `Sub-chart`. Purpose-specific leaves' sections live in the reference pages named below; no leaf heading is added to a purpose page.

Fixed structure of every purpose sub-chart (spec §7.1): `P2_<XX>_IN` terminator → purpose-specific preliminary decisions → `ref` boxes to the spine phases emphasised, in order → purpose-specific leaves → `ref` boxes to this purpose's P10 and P11 leaves → `P2_<XX>_OUT` terminator. `<XX>` is the two-letter purpose code in the tables.

**10.1 Forecasting (`01-forecasting.md`, code FC).** Decisions: `P2_FC_HORIZON_Q{"Horizon?"}` (short / medium / long, all → `P2_FC_HORIZON`), `P2_FC_MANY{"Many similar series?"}` (Yes → `B7[["B7 Many similar series"]]`; No → continue), `P2_FC_EXOG{"Future covariates known?"}` (Yes → `P6_ARIMAX` ref; No → continue). Refs in order: `P3`, `P4`, `P6_ARIMA_SARIMA`, `P6_ETS`, `P6_GLOBAL_MODELS`, `P7`, `P8`, `P9_FORECAST_COMPARISON`, `P10_POINT_FORECASTS`, `P10_INTERVALS`, `P10_MULTISTEP`, `P10_RECONCILIATION`, `P10_COMBINATION`, `P11_ROLLING_ORIGIN`, `P11_POINT_METRICS`, `P11_PROBABILISTIC_METRICS`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_FC_BASELINES | Naive and seasonal-naive baselines | | [22] | reference/22-forecasting-practice/index.md |
| P2_FC_EPIDEMIC | Epidemic nowcasting | reproduction-number estimation, SIR fitting | [26, 22] | reference/26-applied-domains/index.md |

(`P2_FC_EPIDEMIC` hangs off a decision `P2_FC_DOMAIN{"Epidemic counts?"}` →|"Yes"| after the baselines.)

**10.2 Causal and structural inference (`02-causal-inference.md`, code CA).** Decisions: `P2_CA_DESIGN{"Experimental data?"}` →|"Randomised or natural experiment"| `P2_CA_IDENTIFICATION` → `P10_COUNTERFACTUALS`; →|"Observational"| `P2_CA_IDENTIFICATION` → `P2_CA_SYSTEM{"Several series?"}` →|"Yes"| `P6_VAR`, `P6_VECM`, `P10_COINTEGRATION`, `P10_GRANGER`, `P10_NONLINEAR_CAUSALITY`, `P10_SVAR_IDENTIFICATION`, `P10_IRF_FEVD`, `P10_LOCAL_PROJECTIONS`; →|"One series"| `P10_COUNTERFACTUALS`. Then `P2_CA_PLACEBO` → `P2_CA_SENSITIVITY` → `P2_CA_VERDICT{"Identification holds?"}` →|"Yes"| `P2_CA_OUT(["Report a causal effect"])`; →|"No"| `P2_CA_ASSOC(["Report an association only"])`. Refs also `P10_HAC`, `P10_COEFFICIENT_TESTS`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_CA_IDENTIFICATION | Identification strategy and exogeneity | | [21] | reference/21-causal-inference/index.md |
| P2_CA_PLACEBO | Placebo and falsification tests | | [21] | reference/21-causal-inference/index.md |
| P2_CA_SENSITIVITY | Sensitivity analysis across specifications | | [21] | reference/21-causal-inference/index.md |

**10.3 Signal extraction and denoising (`03-signal-extraction.md`, code SE).** Decisions: `P2_SE_NOISE_Q{"Noise character?"}` →|"White"| `P2_SE_FILTER_DESIGN`; →|"Coloured"| `P2_SE_WIENER`; →|"Impulsive"| `P0_ROBUST_FILTER` ref → `P2_SE_FILTER_DESIGN`; →|"Non-stationary"| `P8_KALMAN` ref; →|"1/f"| `P2_SE_WAVELET_DENOISING`. All → `P2_SE_SNR` → `P2_SE_OK{"Signal preserved?"}` →|"No"| `-.->` `P2_SE_FILTER_DESIGN`; →|"Yes"| `P2_SE_OUT`. Preliminary leaf `P2_SE_NOISE_TYPE` before the decision. Refs: `P5_FD_FILTERS`, `P5_TF_DWT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SE_NOISE_TYPE | Characterise the noise | white, coloured, impulsive, non-stationary, 1/f | [13] | reference/13-spectral-analysis/index.md |
| P2_SE_WIENER | Wiener filtering | | [13] | reference/13-spectral-analysis/index.md |
| P2_SE_WAVELET_DENOISING | Wavelet denoising | | [13] | reference/13-spectral-analysis/index.md |
| P2_SE_SNR | Evaluate the signal-to-noise ratio |  | [13] | reference/13-spectral-analysis/index.md |

**10.4 Change-point detection (`04-change-point-detection.md`, code CP).** `P2_CP_MODE{"Online or offline?"}` →|"Online"| `P2_CP_CUSUM` → `P2_CP_BOCPD`; →|"Offline"| `P2_CP_PELT` → `P2_CP_PENALTY`; →|"Multivariate"| `P2_CP_MULTIVARIATE`. All → `P2_CP_TYPE` → `P2_CP_KIND{"Change kind?"}` →|"Mean"| `P4_BREAK_HANDLING` ref; →|"Variance"| `P7_MS_GARCH` ref; →|"Regime"| `P6_MARKOV_SWITCHING` ref. Then `P11_CHANGE_POINT_METRICS` ref → `P2_CP_OUT`. Also ref `P3_STRUCTURAL_BREAKS` at the start.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_CP_CUSUM | Sequential detection | CUSUM, Page-Hinkley | [30, 23] | reference/30-structural-change/index.md |
| P2_CP_BOCPD | Bayesian online change-point detection | | [30, 12] | reference/30-structural-change/index.md |
| P2_CP_PELT | Offline segmentation | PELT, binary segmentation | [30, 19] | reference/30-structural-change/index.md |
| P2_CP_PENALTY | Choose the number of change points | penalty, BIC | [30, 6] | reference/30-structural-change/index.md |
| P2_CP_MULTIVARIATE | Multivariate change points | E-divisive | [30] | reference/30-structural-change/index.md |
| P2_CP_TYPE | Classify the change | mean, variance, regime | [30] | reference/30-structural-change/index.md |

**10.5 Anomaly and regime detection (`05-anomaly-regime-detection.md`, code AN).** `P2_AN_TYPE` → `P2_AN_KIND{"Anomaly kind?"}` →|"Point"| `P2_AN_STATISTICAL`; →|"Contextual"| `P2_AN_RESIDUAL` → `P2_AN_AUTOENCODER`; →|"Collective"| `P2_AN_MATRIX_PROFILE` → `P2_AN_ISOLATION_FOREST`; →|"Regime"| `P2_AN_REGIME`. All → `P2_AN_THRESHOLD` → `P2_AN_LABELS{"Labels available?"}` →|"Yes"| `P8_HYPERPARAMETERS` ref; →|"No"| `P11_DRIFT_MONITORING` ref. → `P11_CLASSIFICATION_METRICS` ref → `P2_AN_OUT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_AN_STATISTICAL | Statistical outlier scores | modified z-score, robust statistics | [19, 24] | reference/19-classification-anomaly/index.md |
| P2_AN_RESIDUAL | Residual-based detection from a fitted model | | [19] | reference/19-classification-anomaly/index.md |
| P2_AN_MATRIX_PROFILE | Matrix profile and discord discovery | | [19] | reference/19-classification-anomaly/index.md |
| P2_AN_ISOLATION_FOREST | Isolation forests for time series | | [19] | reference/19-classification-anomaly/index.md |
| P2_AN_AUTOENCODER | Autoencoders and variational autoencoders | | [19, 18] | reference/19-classification-anomaly/index.md |
| P2_AN_THRESHOLD | Set thresholds by the cost of errors | | [19] | reference/19-classification-anomaly/index.md |

**10.6 Decomposition (`06-decomposition.md`, code DC).** `P2_DC_SEASONAL{"Seasonal?"}` →|"Yes"| `P2_DC_PERIOD` → `P2_DC_ADDITIVE_MULTIPLICATIVE` → `P2_DC_METHOD{"Method?"}` →|"STL or X-13"| `P4_SEASONAL_ADJUSTMENT`; →|"Several periods"| `P4_MULTIPLE_SEASONALITY`; →|"Model-based"| `P4_MODEL_DECOMPOSITION`; →|"Nonparametric"| `P4_SSA`; `P2_DC_SEASONAL` →|"No"| `P4_FILTER_DECOMPOSITION`. All → `P2_DC_COMPONENT_ANALYSIS` → `P9_RESIDUAL_AUTOCORRELATION` ref → `P2_DC_RESIDUAL{"Residual white?"}` →|"No"| `-.->` `P2_DC_METHOD`; →|"Yes"| `P2_DC_REVISION` → `P2_DC_OUT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_DC_ADDITIVE_MULTIPLICATIVE | Additive or multiplicative decomposition | | [3] | reference/03-classical/index.md |
| P2_DC_COMPONENT_ANALYSIS | Analyse and interpret the components | | [3] | reference/03-classical/index.md |
| P2_DC_REVISION | Revision stability of real-time decompositions | | [29] | reference/29-seasonality-calendar/index.md |

**10.7 Feature extraction, classification and clustering (`07-feature-extraction-classification.md`, code FE).** `P2_FE_TASK` → `P2_FE_FEATURE_Q{"Feature family?"}` →|"Time"| `P2_FE_TIME_FEATURES`; →|"Frequency"| `P2_FE_FREQ_FEATURES`; →|"Time-frequency"| `P2_FE_TF_FEATURES`; →|"Nonlinear dynamics"| `P2_FE_NONLINEAR_FEATURES`; →|"Automated"| `P2_FE_AUTOMATED`; →|"Symbolic"| `P2_FE_SYMBOLIC`; →|"Learned"| `P2_FE_REPRESENTATION_LEARNING`; →|"Topological"| `P2_FE_TDA`. All → `P2_FE_LEARNER{"Task?"}` →|"Classification"| `P2_FE_DISTANCES` → `P2_FE_SHAPELETS` → `P2_FE_DEEP_CLASSIFIERS`; →|"Clustering"| `P2_FE_CLUSTERING`; →|"Regression"| `P6_TREE_ENSEMBLES` ref. → `P2_FE_AUGMENTATION` → `P8_HYPERPARAMETERS` ref → `P11_CLASSIFICATION_METRICS` ref → `P2_FE_OUT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_FE_TIME_FEATURES | Time-domain features | moments, autocorrelation, rolling statistics | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_FREQ_FEATURES | Frequency-domain features | band power, spectral entropy, spectral centroid | [19, 13] | reference/19-classification-anomaly/index.md |
| P2_FE_TF_FEATURES | Time-frequency features | STFT and wavelet coefficients | [19, 13] | reference/19-classification-anomaly/index.md |
| P2_FE_NONLINEAR_FEATURES | Nonlinear dynamics features | entropy, Lyapunov exponents, recurrence quantification | [19, 8] | reference/19-classification-anomaly/index.md |
| P2_FE_AUTOMATED | Automated feature extraction | tsfresh, catch22 | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_SYMBOLIC | Symbolic representations | SAX, SFA | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_REPRESENTATION_LEARNING | Self-supervised representation learning | | [19, 18] | reference/19-classification-anomaly/index.md |
| P2_FE_TDA | Topological data analysis | | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_DISTANCES | Distance measures | dynamic time warping, edit distances, kernels | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_SHAPELETS | Shapelets and ROCKET | | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_DEEP_CLASSIFIERS | Deep classifiers | InceptionTime | [19, 18] | reference/19-classification-anomaly/index.md |
| P2_FE_CLUSTERING | Clustering | k-means with DTW, spectral clustering | [19] | reference/19-classification-anomaly/index.md |
| P2_FE_AUGMENTATION | Data augmentation | slicing, warping, synthetic oversampling | [19] | reference/19-classification-anomaly/index.md |

**10.8 Spectral analysis (`08-spectral-analysis.md`, code SP).** `P2_SP_SERIES{"One or two series?"}` →|"One"| `P5_FD_DFT` ref → `P5_FD_SMOOTHED` ref → `P2_SP_SPECTRAL_SHAPE` → `P2_SP_PEAKS{"Peaks?"}` →|"Yes"| `P2_SP_PEAK_SIGNIFICANCE` → `P2_SP_HARMONIC_REGRESSION`; →|"No"| `P2_SP_OUT`; `P2_SP_SERIES` →|"Two"| `P2_SP_CROSS_SPECTRUM` → `P2_SP_FREQ_GRANGER`. All → `P2_SP_OUT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SP_SPECTRAL_SHAPE | Interpret the spectral shape | white, 1/f, peaks, band-limited | [13] | reference/13-spectral-analysis/index.md |
| P2_SP_PEAK_SIGNIFICANCE | Peak significance | Fisher's g-test | [13, 5] | reference/13-spectral-analysis/index.md |
| P2_SP_HARMONIC_REGRESSION | Harmonic regression from detected frequencies | | [13, 3] | reference/13-spectral-analysis/index.md |
| P2_SP_CROSS_SPECTRUM | Cross-spectrum, coherence and phase | | [13] | reference/13-spectral-analysis/index.md |
| P2_SP_FREQ_GRANGER | Frequency-domain Granger causality | | [13, 21] | reference/13-spectral-analysis/index.md |

**10.9 System identification (`09-system-identification.md`, code SI).** `P2_SI_EXPERIMENT_DESIGN` → `P2_SI_MODEL_STRUCTURE` → `P2_SI_STRUCTURE_Q{"Structure?"}` →|"Polynomial"| `P6_ARX_ARMAX` ref; →|"State space"| `P6_SUBSPACE` ref; →|"Block-oriented"| `P6_HAMMERSTEIN_WIENER` ref. All → `P2_SI_ORDER_SELECTION` → `P2_SI_TRANSFER_FUNCTION` → `P2_SI_STABILITY` → `P2_SI_VALIDATION` → `P2_SI_OUT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SI_EXPERIMENT_DESIGN | Input design and persistent excitation | | [33] | reference/33-system-identification/index.md |
| P2_SI_MODEL_STRUCTURE | Choose the model structure | polynomial ARX and ARMAX, state space, block-oriented | [33] | reference/33-system-identification/index.md |
| P2_SI_ORDER_SELECTION | Order selection | Hankel singular values | [33] | reference/33-system-identification/index.md |
| P2_SI_TRANSFER_FUNCTION | Estimate the frequency response | empirical transfer-function estimate | [33] | reference/33-system-identification/index.md |
| P2_SI_STABILITY | Poles, zeros and stability | | [33] | reference/33-system-identification/index.md |
| P2_SI_VALIDATION | Validate on held-out input-output data | | [33] | reference/33-system-identification/index.md |

**10.10 Simulation and scenario generation (`10-simulation.md`, code SM).** `P2_SM_SOURCE{"Generator?"}` →|"Fitted model"| `P2_SM_MONTE_CARLO`; →|"Resampling"| `P2_SM_BOOTSTRAP_PATHS`; →|"Learned"| `P2_SM_SYNTHETIC`. All → `P2_SM_STRESS` → `P2_SM_DISTRIBUTION_MATCH` → `P10_SCENARIOS` ref → `P10_RISK_MEASURES` ref → `P2_SM_OUT`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SM_MONTE_CARLO | Monte Carlo simulation from a fitted model | | [25] | reference/25-simulation/index.md |
| P2_SM_BOOTSTRAP_PATHS | Simulating paths by resampling |  | [25] | reference/25-simulation/index.md |
| P2_SM_SYNTHETIC | Synthetic data generation | TimeGAN | [25, 18] | reference/25-simulation/index.md |
| P2_SM_DISTRIBUTION_MATCH | Check distribution and dependence matching | | [25] | reference/25-simulation/index.md |

- [ ] **Steps:** one commit per purpose page is fine, or one for all ten: replace each pending note with its diagram, add the rows (`phase: P2`), scaffold, audit, build after each page. Commit `feat(flowchart): ten purpose sub-charts`.

---

### Task 11: The six representation sub-charts (P5)

**Files:** `docs/01-workflow/p05-representation/01-time-domain.md` … `06-hilbert-phase.md`, inventory, reference landing pages. Owner: the directory `01-workflow/p05-representation/`. Structure (spec §7.2): `P5_<XX>_IN` → three discriminating decisions (each "Yes" leads on, "No" leads to `P5[["P5: Representation selection"]]` as a ref back to the selector) → representation-specific leaves → `ref` boxes to the available P6 families → `P6[["P6: Conditional-mean model class"]]`.

**11.1 Time domain (TD).** Decisions: "Predict next values?", "Causal question?", "Sequential dependence matters?". Leaves then refs `P6_AR_MA_ARMA`, `P6_ARIMA_SARIMA`, `P6_VAR`, `P6_THRESHOLD`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_TD_AUTOCOVARIANCE | Autocovariance and the ACF as the time-domain object | | [2] | reference/02-fundamentals/index.md |
| P5_TD_LAG_STRUCTURE | Lag structure and memory | | [2, 3] | reference/02-fundamentals/index.md |

**11.2 Frequency domain (FD).** Decisions: "Periodic patterns?", "Separate frequency bands?", "Spectral content is the question?". Leaves then refs `P2_SP_SPECTRAL_SHAPE`, `P2_SP_HARMONIC_REGRESSION`, `P6_ARFIMA` (1/f spectra).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_FD_DFT | Discrete Fourier transform and the periodogram | | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_SMOOTHED | Smoothed spectral estimates | Welch, Bartlett | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_MULTITAPER | Multitaper spectral estimation | | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_PARAMETRIC | Parametric spectra | AR and ARMA spectral estimates | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_LOMB_SCARGLE | Lomb-Scargle periodogram | irregular sampling | [13, 15] | reference/13-spectral-analysis/index.md |
| P5_FD_LEAKAGE | Leakage, tapering and the Nyquist frequency | | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_FILTERS | FIR and IIR filter design | low-pass, high-pass, band-pass, notch; FIR and IIR; zero-phase | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_ENVELOPE | Machine-vibration analysis | envelope analysis, cepstrum, order tracking, spectral kurtosis | [26, 13] | reference/26-applied-domains/index.md |

**11.3 Time-frequency (TF).** Decisions: "Frequency content changes over time?", "Transients or bursts?", "Need both localisations?". Leaves then refs `P2_FE_TF_FEATURES`, `P2_SE_WAVELET_DENOISING`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_TF_STFT | Short-time Fourier transform and the spectrogram | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_CWT | Continuous wavelet transform and the scalogram | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_DWT | Discrete and maximal-overlap wavelet transforms | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_SYNCHROSQUEEZING | Reassignment and synchrosqueezing | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_EMD | Empirical mode decomposition and the Hilbert-Huang transform | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_VMD | Variational mode decomposition | | [13] | reference/13-spectral-analysis/index.md |

**11.4 State space (SS).** Decisions: "Latent states?", "Irregular sampling or gaps?", "Online updating needed?". Leaves then refs `P6_STRUCTURAL_TS`, `P6_DLM`, `P6_BSTS`, `P8_KALMAN`, `P8_NONLINEAR_FILTERS`, `P8_PARTICLE_FILTERS`, `B3`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_SS_FORM | State-space form and the ARIMA rewriting | | [11] | reference/11-state-space/index.md |
| P5_SS_LATENT | Latent states and missing observations |  | [11] | reference/11-state-space/index.md |
| P5_SS_TAKENS | Takens embedding and phase-space reconstruction | | [33, 8] | reference/33-system-identification/index.md |
| P5_SS_DMD | Dynamic mode decomposition and Koopman operators | | [33] | reference/33-system-identification/index.md |

**11.5 Functional (FN).** Decisions: "Observations are curves?", "Shape or derivatives matter?", "Dense sampling per curve?". Leaves then refs `B4`, `P6_GAUSSIAN_PROCESS`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_FN_BASIS | Basis representation and smoothing of curves | | [14] | reference/14-functional-high-frequency/index.md |
| P5_FN_FPCA | Functional principal components | | [14] | reference/14-functional-high-frequency/index.md |
| P5_FN_REGRESSION | Functional regression and functional autoregression | | [14] | reference/14-functional-high-frequency/index.md |

**11.6 Hilbert and phase (HP).** Decisions: "Instantaneous frequency?", "Amplitude envelope?", "Phase relations between signals?". Leaves then refs `P5_TF_EMD`, `P2_FE_NONLINEAR_FEATURES`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_HP_ANALYTIC_SIGNAL | Analytic signal and instantaneous frequency | | [13] | reference/13-spectral-analysis/index.md |
| P5_HP_PHASE_SYNC | Phase synchronisation and the phase-locking value | | [13, 33] | reference/13-spectral-analysis/index.md |

- [ ] **Steps:** replace each pending note, 25 rows `phase: P5`, scaffold, audit, build. Delete the bold "Topics carried over" lead-in and list on `p05-representation/index.md`. Commit `feat(flowchart): six representation sub-charts`.

---

### Task 12: Branch sub-diagrams B1 to B7

**Files:** `docs/reference/16-count-categorical/index.md` (B1), `17-point-processes/index.md` (B2), `15-continuous-time/index.md` (B3), `14-functional-high-frequency/index.md` (B4), `20-spatio-temporal/index.md` (B5), `32-panel-time-series/index.md` (B6), `docs/01-workflow/p01-data-type-gate.md` (B7), inventory. Owner pages: the pages that already define `B1` … `B7`. Each branch diagram replaces the one-node stub under `## Branch sub-diagram` (B7: a new diagram under the existing `B7 Many similar series` leaf section on the P1 page). Structure (spec §5.2): entry box `Bn["Bn …"]` (already defined, keep it) → compressed diagnose → transform → model class → error process → `ref` to the rejoin phase. Sections: the same landing page unless listed.

**B1 (counts and categorical, phase B1):** `B1` → `B1_COUNT_EDA` → `B1_VALUE{"Value type?"}` →|"Counts"| `B1_DISPERSION{"Overdispersed?"}` →|"No"| `B1_INAR` → `B1_POISSON_AR`; →|"Yes"| `B1_NEGATIVE_BINOMIAL` → `B1_GLARMA`; `B1_VALUE` →|"Categorical"| `B1_MARKOV_CHAIN` → `B1_AR_LOGIT`; →|"Compositional"| `B1_COMPOSITIONAL`. All → `P7_COUNT_TESTS[["Test overdispersion of count innovations"]]` → `P8[["P8: Estimation"]]`. Foundation ref `F_MARKOV -.- B1_MARKOV_CHAIN`.

| ID | label | second line | areas |
|---|---|---|---|
| B1_COUNT_EDA | Count-data diagnostics | zero counts, autocorrelation of counts | [16] |
| B1_INAR | INAR models | | [16] |
| B1_POISSON_AR | Poisson and negative-binomial autoregression | INGARCH | [16] |
| B1_GLARMA | GLARMA and dynamic generalised linear models | | [16] |
| B1_MARKOV_CHAIN | Markov chains for categorical series | | [16] |
| B1_AR_LOGIT | Autoregressive logit, probit and multinomial series | | [16] |
| B1_COMPOSITIONAL | Compositional series | log-ratio transforms, Dirichlet regression | [16] |

Foundation row: `F_MARKOV` | Markov chains | `00-foundations/stochastic-processes.md#markov-chains`.

**B2 (event times, phase B2):** `B2` → `B2_EVENT_EDA` → `B2_QUESTION{"Object of interest?"}` →|"Event intensity"| `B2_CLUSTERING{"Self-exciting?"}` →|"No"| `B2_POISSON` → `B2_COX`; →|"Yes"| `B2_HAWKES` → `B2_MARKED` → `B2_NEURAL_PP`; `B2_QUESTION` →|"Durations"| `B2_ACD`; →|"Time to failure"| `B2_SURVIVAL` → `B2_DEGRADATION`. All → `P7_RESCALING[["Time-rescaling check of event-time residuals"]]` → `P8`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| B2_EVENT_EDA | Event-time diagnostics | intensity, inter-event distributions | [17] | reference/17-point-processes/index.md |
| B2_POISSON | Poisson and renewal processes |  | [17] | reference/17-point-processes/index.md |
| B2_COX | Cox processes |  | [17] | reference/17-point-processes/index.md |
| B2_HAWKES | Hawkes self-exciting processes |  | [17] | reference/17-point-processes/index.md |
| B2_MARKED | Marked and multivariate point processes |  | [17] | reference/17-point-processes/index.md |
| B2_NEURAL_PP | Neural point processes |  | [17, 18] | reference/17-point-processes/index.md |
| B2_ACD | Autoregressive conditional duration | | [14] | reference/14-functional-high-frequency/index.md |
| B2_SURVIVAL | Survival and hazard models | Cox proportional hazards | [14, 26] | reference/17-point-processes/index.md |
| B2_DEGRADATION | Degradation processes and remaining useful life | Wiener and gamma processes | [26, 15] | reference/26-applied-domains/index.md |

**B3 (irregular sampling and continuous time, phase B3):** `B3` → `B3_CHOICE` → `B3_ROUTE{"Route?"}` →|"Resample"| `-.->` `P0_RESAMPLE[["Resample and anti-alias"]]`; →|"Keep the grid"| `B3_IRREGULAR_KALMAN` → `P5_FD_LOMB_SCARGLE[["Lomb-Scargle periodogram"]]` → `P5[["P5: Representation selection"]]`; →|"Continuous time"| `B3_OU` → `B3_CARMA` → `B3_SDE` → `B3_JUMPS{"Jumps?"}` →|"Yes"| `B3_JUMP_LEVY`; →|"No"| `B3_SDE_INFERENCE`; `B3_JUMP_LEVY` → `B3_SDE_INFERENCE` → `P8`.

| ID | label | second line | areas |
|---|---|---|---|
| B3_IRREGULAR_KALMAN | Kalman filtering on an irregular grid | | [11, 15] |
| B3_OU | Ornstein-Uhlenbeck process and exact discretisation | | [15] |
| B3_CARMA | CARMA processes | | [15] |
| B3_SDE | Diffusions and SDE discretisation | Euler-Maruyama, Milstein | [15] |
| B3_SDE_INFERENCE | Likelihood inference for diffusions | signature methods | [15] |

**B4 (functional, phase B4):** `B4` → `B4_CURVES` → `B4_INTRADAY` → `P5_FN_BASIS[["Basis representation and smoothing of curves"]]` → `P5` ref.

| ID | label | second line | areas |
|---|---|---|---|
| B4_CURVES | Series as curves | when functional data analysis applies | [14] |
| B4_INTRADAY | Intraday seasonality and curve alignment | | [14] |

**B5 (spatial and network, phase B5):** `B5` → `B5_SPATIAL_AUTOCORRELATION` → `B5_INDEX{"Index?"}` →|"Regions or panels"| `B5_SPATIAL_PANEL_VAR`; →|"Continuous space"| `B5_KRIGING`; →|"Graph"| `B5_GRAPH_SIGNAL` → `B5_STGNN` → `B5_NETWORK_AR`; →|"Events in space"| `B5_ST_POINT_PROCESS`. All → `P8`.

| ID | label | second line | areas |
|---|---|---|---|
| B5_SPATIAL_AUTOCORRELATION | Spatial autocorrelation | Moran's I | [20] |
| B5_SPATIAL_PANEL_VAR | Spatial panel VAR and spatial error and lag models | | [20] |
| B5_KRIGING | Spatio-temporal kriging and Gaussian processes | | [20] |
| B5_GRAPH_SIGNAL | Graph signal processing | | [20] |
| B5_STGNN | Spatio-temporal graph neural networks | | [20, 18] |
| B5_NETWORK_AR | Network autoregression | | [20] |
| B5_ST_POINT_PROCESS | Spatio-temporal point processes | | [20, 17] |

**B6 (wide panel, phase B6):** `B6` → `B6_PANEL_UNIT_ROOT` → `B6_DYNAMIC{"Lagged dependent variable?"}` →|"No"| `B6_STATIC_PANEL`; →|"Yes"| `B6_DYNAMIC_PANEL`; both → `B6_HETERO{"Heterogeneous slopes?"}` →|"Yes"| `B6_HETEROGENEOUS`; →|"No"| `B6_CROSS_SECTION_DEPENDENCE`; `B6_HETEROGENEOUS` → `B6_CROSS_SECTION_DEPENDENCE` → `P8` and `P10[["P10: Inference and interpretation"]]`.

| ID | label | second line | areas |
|---|---|---|---|
| B6_PANEL_UNIT_ROOT | Panel unit-root and cointegration tests | | [32, 28] |
| B6_STATIC_PANEL | Fixed and random effects | | [32] |
| B6_DYNAMIC_PANEL | Dynamic panel GMM | Arellano-Bond | [32, 4] |
| B6_HETEROGENEOUS | Heterogeneous panels | mean group, pooled mean group | [32] |
| B6_CROSS_SECTION_DEPENDENCE | Cross-sectional dependence | CD test, common correlated effects | [32] |

**B7 (many similar series, phase P1, drawn on `p01-data-type-gate.md` as a second diagram under the `B7 Many similar series` heading; sections in reference pages):** `B7` → `B7_GLOBAL_VS_LOCAL` → `B7_STRATEGY{"Strategy?"}` →|"Global"| `P6_GLOBAL_MODELS` ref → `P6_FOUNDATION_MODELS` ref; →|"Cluster first"| `B7_CLUSTER_THEN_LOCAL`; →|"Hierarchy"| `B7_HIERARCHY` → `P10_RECONCILIATION` ref. All → `P2[["P2: Purpose"]]`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| B7_GLOBAL_VS_LOCAL | Global or local models | | [22, 18] | reference/22-forecasting-practice/index.md |
| B7_HIERARCHY | Detect hierarchical and grouped structure | | [22] | reference/22-forecasting-practice/index.md |
| B7_CLUSTER_THEN_LOCAL | Cluster series, then fit local models | | [19, 22] | reference/19-classification-anomaly/index.md |

Note on B7 rows: phase `P1` (the owner page is the P1 page); the row ids keep the `B7_` prefix, which the audit accepts because `B7` is a branch entry defined on that page — if the owner-prefix check rejects `B7_*` on a P1 page, extend `owner_pages` so a `B7_*` id is owned by the page that defines `B7`, with a test, rather than renaming the leaves.

- [ ] **Steps:** one commit per branch or one for all seven: replace each stub, add rows (`phase` = B1…B6, `P1` for B7), the `F_MARKOV` row, scaffold, audit, build. Commit `feat(flowchart): branch sub-diagrams B1 to B7`.

---

### Task 13: Quick-navigation tables and the landing page

**Files:** `docs/01-workflow/p02-purpose/index.md`, `docs/01-workflow/p05-representation/index.md`, `docs/index.md`.

- [ ] **Step 1:** Replace the "Pending" row of the Quick navigation table on `p02-purpose/index.md` with ten rows: purpose → emphasised phases → key leaves (three leaf labels each, taken from Task 10). Same on `p05-representation/index.md` with six rows (representation → choose when → key leaves from Task 11).
- [ ] **Step 2:** On `docs/index.md`, in the Quick Start "Have Specific Goals" tab, point each goal at its purpose page (forecasting → `01-workflow/p02-purpose/01-forecasting.md`, causal → `02-causal-inference.md`, anomaly → `05-anomaly-regime-detection.md`, feature engineering → `07-feature-extraction-classification.md`); in "Know Your Domain", point finance at `01-workflow/p05-representation/01-time-domain.md` and signal processing at `02-frequency-domain.md` (these may already be so; verify).
- [ ] **Step 3:** `venv/bin/mkdocs build --strict`; commit `docs: quick-navigation tables for purposes and representations`.

---

### Task 14: Coverage, final verification, PR

- [ ] **Step 1:** `venv/bin/pytest tests/test_area_coverage.py -q` → PASS (every area 1–34 has a leaf). If an area is missing, the missing area's leaf from the tables above was not added; add it rather than widening a row's `areas`.
- [ ] **Step 2:** `TSAM_REQUIRE_E2E=1 venv/bin/pytest tests -q -rs` (no skips), `venv/bin/python scripts/audit_flowcharts.py` → `0 error(s)`, `venv/bin/mkdocs build --strict`.
- [ ] **Step 3:** Open every phase, purpose, representation and branch page in `mkdocs serve`; confirm every diagram renders and no node's second line is clipped; where a diagram is too wide, split it in two stacked parts as P7 was.
- [ ] **Step 4:** Cleanup grep over added lines (local references) and over the PR body; push; open the PR with the `create-pr` skill against `Shuxin-Y/flowchart-skeleton`, title `Flowchart framework Plan B: remaining sub-diagrams and full area coverage`, body: what Plan B adds (one paragraph), the diagram list with commits, leaf and row counts, the area-coverage test result, the verification lines, and the note that the PR retargets to `main` after PR #7 merges. Do not merge.

## Plan Self-Review

- **Spec coverage.** §4 phases P0, P3, P4, P6, P8–P11 → Tasks 2–9; §5 branches → Task 12; §7.1 ten purposes and §7.2 six representations → Tasks 10–11; §7.3 quick navigation → Task 13; §8 area coverage (criterion 3) → Tasks 1 and 14; Part 0 roots referenced from phases → F rows in Tasks 3, 5, 6, 8, 12.
- **Area check (every area has at least one leaf in the tables):** 1 (F rows), 2 (P3, P4, P5_TD), 3 (P6), 4 (P8), 5 (P3, P9, P10), 6 (P9, P11), 7 (P6_ARFIMA), 8 (P6 nonlinear), 9 (P6 multivariate), 10 (P7, P9, P10), 11 (P6, P8), 12 (P6, P8), 13 (P5_FD, P5_TF, P2_SP), 14 (P5_FN, B2, B4), 15 (B3), 16 (B1), 17 (B2), 18 (P6 ML), 19 (P2_FE, P2_AN), 20 (B5), 21 (P10, P2_CA), 22 (P2_FC, P10), 23 (P11), 24 (P3, P0, P8_ROBUST), 25 (P2_SM, P8), 26 (P2_FC_EPIDEMIC, P5_FD_ENVELOPE, B2_DEGRADATION), 27 (P6, P8, P10_HAC), 28 (P3, P10), 29 (P3, P4, P6), 30 (P3, P4, P2_CP, P11_SPC), 31 (P0), 32 (B6), 33 (P6, P2_SI, P5_SS), 34 (P6_INTERMITTENT, P10, P11).
- **Placeholders.** None: every leaf has an ID, label, areas and a section file or the stated default; every diagram has its flow.
- **Owner rule.** P2 and P5 leaves sit on pages under their directories; branch leaves on their entry pages; B7 on the P1 page (handled in Task 12's note).
- **Label rule.** Labels avoid characters that slugify differently from how they read (no slashes or ampersands; "and" spelled out; hyphens only).
