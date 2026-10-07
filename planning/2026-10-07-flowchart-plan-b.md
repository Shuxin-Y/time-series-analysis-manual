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
| `docs/01-workflow/p07-error-process.md` | P7 split into three stacked diagrams (width rule) |
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
"""Spec acceptance criterion 3: every one of the 34 areas has at least one leaf in some sub-diagram.

Area 1 (math foundations) is Part 0 by design (spec section 8): it is satisfied by foundation sections, the
phase-F rows that sub-diagrams draw as refs. Areas 2-34 need a leaf, so they count only rows that are neither
foundation sections nor master phase boxes (which sit on the master diagram, not in a sub-diagram).
"""
from pathlib import Path

import audit_flowcharts as audit
import sitekit

FOUNDATION_AREA = 1


def test_every_area_has_a_leaf():
    docs = Path(audit.load_site_config(sitekit.REPO / "mkdocs.yml")["docs_dir"])
    rows, findings = audit.load_inventory(docs.joinpath(*audit.INVENTORY_PATH))
    assert not findings
    foundation = {a for r in rows if r.phase == audit.FOUNDATION_PHASE for a in r.areas}
    leaves = {a for r in rows if r.phase not in (audit.FOUNDATION_PHASE, audit.MASTER_PHASE) for a in r.areas}
    assert FOUNDATION_AREA in foundation, "area 1 has no foundation section"
    missing = sorted(set(audit.AREAS) - {FOUNDATION_AREA} - leaves)
    assert not missing, f"areas without a leaf: {missing}"
```

- [ ] **Step 2: Run it to see it fail**

Run: `venv/bin/pytest tests/test_area_coverage.py -q`
Expected: FAIL listing the uncovered areas (2, 6, 12, 23, 24, 28, 31 at the start; master boxes do not count, area 1 is satisfied by foundation rows).

- [ ] **Step 3: Split the P7 diagram**

In `docs/01-workflow/p07-error-process.md` replace the single P7 diagram with three stacked diagrams under `## Sub-diagram` (the width rule in DESIGN-SYSTEM.md; the plan's two-part split left part 1 at scale 0.36). The second-line clipping was a CSS line-height mismatch, fixed in `docs/stylesheets/extra.css` and checked by the rendering gate. Flow as drawn:

The order of the questions is itself a derivation chain: each step's test assumes the previous step's structure has been removed. ARCH-LM assumes no serial correlation; distribution tests run on standardised residuals and assume the variance model is fixed; correlation tests run on each series' standardised residuals: `P7_IN(["Residuals of the P6 mean model"])` → `P7_TYPE{"Innovation type?"}`; `P7_TYPE` →|"Continuous"| `P7_MEAN_TESTS`; `P7_TYPE` →|"Counts"| `P7_COUNT_TESTS`; `P7_TYPE` →|"Event times"| `P7_RESCALING`; `P7_COUNT_TESTS` → `P7_INGARCH`; `P7_RESCALING` → `P7_INTENSITY`; `P7_INGARCH` & `P7_INTENSITY` → `P7_COUNTS_TO_PART_3(["Continue in part 3"])`; `P7_MEAN_TESTS` → `P7_MEAN_DEP{"Mean dependence?"}`; `P7_MEAN_DEP` →|"None"| `P7_TO_PART_2`; `P7_MEAN_DEP` →|"Short memory"| `P7_ARMA_ERRORS`; `P7_MEAN_DEP` →|"Slow decay"| `P7_ARFIMA_ERRORS`; `P7_MEAN_DEP` -.->|"Already ARMA: raise the order"| `P6` (ref); `P7_ARMA_ERRORS` & `P7_ARFIMA_ERRORS` → `P7_TO_PART_2(["Continue in part 2"])`; `F_WHITE_NOISE` (ref) -.- `P7_MEAN_DEP`; `F_WOLD` (ref) -.- `P7_ARMA_ERRORS`; `F_LONG_MEMORY` (ref) -.- `P7_ARFIMA_ERRORS`; `F_TIME_RESCALING` (ref) -.- `P7_RESCALING`.

- **Part 2:** conditional variance: `P7_FROM_PART_1(["From part 1"])` → `P7_VAR_TESTS`; `P7_VAR_TESTS` → `P7_VAR_DEP{"Variance dependence?"}`; `P7_VAR_DEP` →|"None"| `P7_TO_PART_3`; `P7_VAR_DEP` →|"Present"| `P7_VAR_TYPE{"Variance process?"}`; `P7_VAR_TYPE` →|"GARCH family"| `P7_GARCH_TYPE{"GARCH variant?"}`; `P7_VAR_TYPE` →|"Latent variance"| `P7_SV`; `P7_VAR_TYPE` →|"Realised measures"| `P7_REALIZED`; `P7_GARCH_TYPE` →|"Symmetric"| `P7_GARCH`; `P7_GARCH_TYPE` →|"Asymmetric"| `P7_ASYM_GARCH`; `P7_GARCH_TYPE` →|"Long memory"| `P7_FIGARCH`; `P7_GARCH_TYPE` →|"Persistence near one"| `P7_IGARCH`; `P7_GARCH_TYPE` →|"Risk premium"| `P7_GARCH_M`; `P7_GARCH` & `P7_ASYM_GARCH` & `P7_FIGARCH` & `P7_IGARCH` & `P7_GARCH_M` → `P7_TO_PART_3`; `P7_SV` & `P7_REALIZED` → `P7_TO_PART_3(["Continue in part 3"])`; `F_GARCH_STATIONARITY` (ref) -.- `P7_GARCH`; `F_LATENT_FILTERING` (ref) -.- `P7_SV`.

- **Part 3:** distribution, regimes, correlation and assembly: `P7_PART_3_IN(["From parts 1 and 2"])` → `P7_TYPE_3{"Innovation type?"}`; `P7_TYPE_3` →|"Continuous"| `P7_DIST_TESTS`; `P7_TYPE_3` →|"Counts or event times"| `P7_OUT`; `P7_DIST_TESTS` → `P7_DIST{"Distribution?"}`; `P7_DIST` →|"Gaussian"| `P7_GAUSSIAN`; `P7_DIST` →|"Heavy tails"| `P7_HEAVY_TAILS`; `P7_DIST` →|"Skew"| `P7_SKEWED`; `P7_DIST` →|"Extreme tails"| `P7_EVT`; `P7_DIST` →|"Jumps"| `P7_JUMPS`; `P7_GAUSSIAN` & `P7_HEAVY_TAILS` & `P7_SKEWED` & `P7_EVT` & `P7_JUMPS` → `P7_REGIME_TESTS`; `P7_REGIME_TESTS` → `P7_REGIME{"Regimes?"}`; `P7_REGIME` →|"None"| `P7_MULTI`; `P7_REGIME` →|"Present"| `P7_MS_GARCH`; `P7_MS_GARCH` → `P7_MULTI{"Several series?"}`; `P7_MULTI` →|"No"| `P7_OUT`; `P7_MULTI` →|"Yes"| `P7_CORR_TESTS`; `P7_CORR_TESTS` → `P7_CORR{"Correlation structure?"}`; `P7_CORR` →|"Constant"| `P7_CCC`; `P7_CORR` →|"Time-varying"| `P7_DCC`; `P7_CORR` →|"Non-Gaussian dependence"| `P7_COPULA`; `P7_CCC` & `P7_DCC` & `P7_COPULA` → `P7_OUT`; `P7_OUT` → `P8` (ref); `F_LEVY` (ref) -.- `P7_JUMPS`; `F_HMM` (ref) -.- `P7_MS_GARCH`; `F_SKLAR` (ref) -.- `P7_COPULA`.

Every leaf keeps its ID, label and class; `P7_INGARCH` is relabelled in review round 1 (see Deviations).

- [ ] **Step 4: Verify**

Run: `venv/bin/python scripts/audit_flowcharts.py | tail -1 && venv/bin/mkdocs build --strict 2>&1 | tail -1`
Expected: `0 error(s)`; build passes. Open the P7 page in `mkdocs serve` and confirm both second lines of the test nodes are readable.

- [ ] **Step 5: Commit**

```bash
git add tests/test_area_coverage.py docs/01-workflow/p07-error-process.md
git commit -m "test: assert every area has a leaf; split the P7 diagram into two parts"
# (P7 later became three parts in commit f0ff054)
```

---

### Task 2: P0 sub-diagram — data acquisition and cleaning

**Files:** `docs/01-workflow/p00-data.md`, `docs/flowcharts/inventory.yml`. Owner page: `01-workflow/p00-data.md`. Sections: the phase page.

**Flow.** Flow as drawn (revised in review round 1, see Deviations): `P0_IN(["Raw time-stamped data"])` → `P0_INSPECT_SAMPLING`; `P0_INSPECT_SAMPLING` → `P0_REGULAR{"Regular sampling?"}`; `P0_REGULAR` →|"No"| `P0_ALIGN_TIMESTAMPS`; `P0_REGULAR` →|"Yes"| `P0_DEDUPLICATE`; `P0_ALIGN_TIMESTAMPS` → `P0_DEDUPLICATE`; `P0_DEDUPLICATE` → `P0_RESAMPLE_NOW{"Resample now?"}`; `P0_RESAMPLE_NOW` →|"Yes: downsample or regrid"| `P0_RESAMPLE`; `P0_RESAMPLE_NOW` →|"No: keep the sampling"| `P0_HAS_MISSING`; `P0_RESAMPLE` → `P0_HAS_MISSING{"Missing values?"}`; `P0_HAS_MISSING` →|"Short gaps"| `P0_MISSING_IMPUTE`; `P0_HAS_MISSING` →|"Long gaps"| `P0_MISSING_SEGMENT`; `P0_HAS_MISSING` →|"None"| `P0_HAS_OUTLIERS`; `P0_MISSING_IMPUTE` & `P0_MISSING_SEGMENT` → `P0_HAS_OUTLIERS{"Outliers?"}`; `P0_HAS_OUTLIERS` →|"Yes"| `P0_OUTLIER_TAXONOMY`; `P0_HAS_OUTLIERS` →|"No"| `P0_UNITS_METADATA`; `P0_OUTLIER_TAXONOMY` → `P0_ROBUST_FILTER`; `P0_ROBUST_FILTER` → `P0_UNITS_METADATA`; `P0_UNITS_METADATA` → `P0_CUMULATIVE{"Cumulative measure?"}`; `P0_CUMULATIVE` →|"Yes"| `P0_CUMULATIVE_TO_FLOW`; `P0_CUMULATIVE` →|"No"| `P0_CALENDAR_EFFECTS`; `P0_CUMULATIVE_TO_FLOW` → `P0_CALENDAR_EFFECTS`; `P0_CALENDAR_EFFECTS` → `P0_FREQUENCY{"Frequency conversion?"}`; `P0_FREQUENCY` →|"Yes"| `P0_DISAGGREGATION`; `P0_FREQUENCY` →|"No"| `P0_VINTAGES`; `P0_DISAGGREGATION` → `P0_VINTAGES`; `P0_VINTAGES` → `P1` (ref).

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

**Flow.** Flow as drawn (revised in review round 1, see Deviations): `P3_IN(["Series and flags from P2"])` → `P3_PLOT`; `P3_PLOT` → `P3_DISTRIBUTION`; `P3_DISTRIBUTION` → `P3_VARIANCE_STABILITY`; `P3_VARIANCE_STABILITY` → `P3_HETERO{"Variance stable?"}`; `P3_HETERO` →|"Level-dependent variance"| `P3_VARIANCE_FLAG["Set flag: transform variance"]`; `P3_HETERO` →|"Conditional heteroskedasticity: tested in P7"| `P3_TREND_TYPE`; `P3_HETERO` →|"Yes"| `P3_TREND_TYPE`; `P3_VARIANCE_FLAG` → `P3_TREND_TYPE`; `P3_TREND_TYPE` → `P3_UNIT_ROOT`; `P3_UNIT_ROOT` → `P3_BREAK_SUSPECTED`; `P3_UNIT_ROOT` → `P3_VARIANCE_RATIO`; `P3_VARIANCE_RATIO` → `P3_BREAK_SUSPECTED{"Break suspected?"}`; `P3_BREAK_SUSPECTED` →|"Yes"| `P3_UNIT_ROOT_BREAKS`; `P3_BREAK_SUSPECTED` →|"No"| `P3_UR_VERDICT`; `P3_UNIT_ROOT_BREAKS` → `P3_STRUCTURAL_BREAKS`; `P3_STRUCTURAL_BREAKS` → `P3_BREAK_VERDICT{"Breaks found?"}`; `P3_BREAK_VERDICT` →|"Yes"| `P3_BREAK_FLAG["Set flag: break handling"]`; `P3_BREAK_VERDICT` →|"No"| `P3_UR_VERDICT`; `P3_BREAK_FLAG` → `P3_UR_VERDICT{"Unit root?"}`; `P3_UR_VERDICT` →|"Yes"| `P3_DIFF_FLAG["Set flag: difference"]`; `P3_UR_VERDICT` →|"No"| `P3_TREND_TS{"Deterministic trend?"}`; `P3_UR_VERDICT` →|"Explosive"| `P3_EXPLOSIVE`; `P3_TREND_TS` →|"Yes: trend-stationary"| `P3_TREND_FLAG["Set flag: deterministic trend"]`; `P3_TREND_TS` →|"No"| `P3_SEASONALITY`; `P3_DIFF_FLAG` & `P3_EXPLOSIVE` & `P3_TREND_FLAG` → `P3_SEASONALITY`; `P3_SEASONALITY` → `P3_SEASONAL{"Seasonal?"}`; `P3_SEASONAL` →|"Single period"| `P3_SEASONAL_UNIT_ROOT`; `P3_SEASONAL` →|"Multiple periods"| `P3_MULTI_SEASON_FLAG["Set flag: multiple seasonality"]`; `P3_SEASONAL` →|"No"| `P3_ACF_PACF`; `P3_SEASONAL_UNIT_ROOT` → `P3_SUR_VERDICT{"Seasonal unit root?"}`; `P3_SUR_VERDICT` →|"Yes"| `P3_SDIFF_FLAG["Set flag: seasonal difference"]`; `P3_SUR_VERDICT` →|"No"| `P3_SADJ_FLAG["Set flag: seasonal adjustment"]`; `P3_SDIFF_FLAG` & `P3_SADJ_FLAG` & `P3_MULTI_SEASON_FLAG` → `P3_ACF_PACF`; `P3_ACF_PACF` → `P3_DECAY{"ACF decay?"}`; `P3_DECAY` →|"Hyperbolic"| `P3_LONG_MEMORY`; `P3_DECAY` →|"Geometric or cut-off"| `P3_NONLINEARITY`; `P3_LONG_MEMORY` → `P3_LM_VERDICT{"Long memory?"}`; `P3_LM_VERDICT` →|"Yes"| `P3_LONG_MEMORY_FLAG["Set flag: long memory"]`; `P3_LM_VERDICT` →|"No"| `P3_NONLINEARITY`; `P3_LONG_MEMORY_FLAG` → `P3_NONLINEARITY`; `P3_NONLINEARITY` → `P3_NONLINEAR{"Nonlinear?"}`; `P3_NONLINEAR` →|"Yes"| `P3_NONLINEAR_FLAG["Set flag: nonlinear"]`; `P3_NONLINEAR` →|"No"| `P3_NONPARAMETRIC_TREND`; `P3_NONLINEAR_FLAG` → `P3_NONPARAMETRIC_TREND`; `P3_NONPARAMETRIC_TREND` → `P3_MULTI{"Multivariate flag?"}`; `P3_MULTI` →|"Yes"| `P3_CROSS_CORRELATION`; `P3_MULTI` →|"No"| `P3_OUT`; `P3_CROSS_CORRELATION` → `P3_COINTEGRATION_PRECHECK`; `P3_COINTEGRATION_PRECHECK` → `P3_OUT(["To P4 Transformations"])`; `F_ERGODICITY` (ref) -.- `P3_PLOT`; `F_STATIONARITY` (ref) -.- `P3_TREND_TYPE`; `F_UNIT_ROOT_ASYMPTOTICS` (ref) -.- `P3_UNIT_ROOT`.

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
| P3_NONLINEARITY | Nonlinearity tests | BDS, Terasvirta, Tsay, Keenan; chaos indicators (Lyapunov exponents, correlation dimension) | [8, 5] | 01-workflow/p03-exploratory-diagnostics.md |
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

**Flow.** Flow as drawn (revised in review round 1, see Deviations): `P4_IN(["Flags from P3"])` → `P4_VARIANCE{"Variance flag?"}`; `P4_VARIANCE` →|"Transform variance"| `P4_LOG_BOXCOX`; `P4_VARIANCE` →|"None"| `P4_TREND`; `P4_LOG_BOXCOX` → `P4_TREND{"Trend flag?"}`; `P4_TREND` →|"Deterministic trend"| `P4_DETREND`; `P4_TREND` →|"Difference"| `P4_DIFFERENCE`; `P4_TREND` →|"Long memory"| `P4_FRACTIONAL_DIFFERENCE`; `P4_TREND` →|"None"| `P4_SEASON`; `P4_DIFFERENCE` → `P4_OVERDIFFERENCING`; `P4_DETREND` & `P4_OVERDIFFERENCING` & `P4_FRACTIONAL_DIFFERENCE` → `P4_SEASON{"Seasonal flag?"}`; `P4_SEASON` →|"Seasonal difference"| `P4_SEASONAL_DIFFERENCE`; `P4_SEASON` →|"Seasonal adjustment"| `P4_SEASONAL_ADJUSTMENT`; `P4_SEASON` →|"Multiple seasonality"| `P4_MULTIPLE_SEASONALITY`; `P4_SEASON` →|"None"| `P4_BREAKS`; `P4_SEASONAL_DIFFERENCE` & `P4_SEASONAL_ADJUSTMENT` & `P4_MULTIPLE_SEASONALITY` → `P4_BREAKS{"Break flag?"}`; `P4_BREAKS` →|"Yes"| `P4_BREAK_HANDLING`; `P4_BREAKS` →|"No"| `P4_DECOMP`; `P4_BREAK_HANDLING` → `P4_DECOMP{"Decomposition wanted?"}`; `P4_DECOMP` →|"Filter-based"| `P4_FILTER_DECOMPOSITION`; `P4_DECOMP` →|"Model-based"| `P4_MODEL_DECOMPOSITION`; `P4_DECOMP` →|"Nonparametric"| `P4_SSA`; `P4_DECOMP` →|"No"| `P4_RETEST`; `P4_FILTER_DECOMPOSITION` & `P4_MODEL_DECOMPOSITION` & `P4_SSA` → `P4_RETEST`; `P4_RETEST` → `P4_STATIONARY{"Stationary now?"}`; `P4_STATIONARY` →|"Yes"| `P4_OUT(["To P5 Representation"])`; `P4_STATIONARY` -.->|"No"| `P3` (ref).

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
| P4_BREAK_HANDLING | Handle structural breaks | segmenting, regime dummies, time-varying parameters, forecasting under breaks | [30] | 01-workflow/p04-transformations.md |
| P4_FILTER_DECOMPOSITION | Filter-based decomposition | HP, Baxter-King, Christiano-Fitzgerald, Hamilton | [13, 3] | 01-workflow/p04-transformations.md |
| P4_MODEL_DECOMPOSITION | Model-based decomposition | Beveridge-Nelson, unobserved components | [11, 3] | 01-workflow/p04-transformations.md |
| P4_SSA | Singular spectrum analysis |  | [13] | 01-workflow/p04-transformations.md |
| P4_RETEST | Retest stationarity after transforming |  | [5] | 01-workflow/p04-transformations.md |

- [ ] **Steps:** as Task 2 (replace the note, 13 rows with `phase: P4`, scaffold, audit, build). Commit `feat(flowchart): P4 transformations sub-diagram`.

---

### Task 5: P6 sub-diagram — conditional-mean model class

**Files:** `docs/01-workflow/p06-mean-model-class.md`, inventory, reference landing pages (scaffolded). Owner page: the phase page. Sections: reference landing pages as listed.

**Flow.** Flow as drawn (revised in review round 1, see Deviations): Part 1: routing on the flags: `P6_IN(["Transformed series, representation, flags"])` → `P6_EXOGENOUS{"Exogenous variables?"}`; `P6_EXOGENOUS` →|"Future known"| `P6_EXOG_FLAG["Set flag: exogenous regressors"]`; `P6_EXOGENOUS` →|"Co-forecast"| `P6_MULTI_FLAG["Set flag: multivariate"]`; `P6_EXOGENOUS` →|"None"| `P6_GLOBAL_Q`; `P6_EXOG_FLAG` & `P6_MULTI_FLAG` → `P6_GLOBAL_Q{"Global flag?"}`; `P6_GLOBAL_Q` →|"Yes"| `P6_GLOBAL_MODELS`; `P6_GLOBAL_Q` →|"No"| `P6_MIXED_Q{"Mixed-frequency flag?"}`; `P6_MIXED_Q` →|"Yes"| `P6_MIXED_FREQUENCY`; `P6_MIXED_Q` →|"No"| `P6_MULTI_Q{"Multivariate flag?"}`; `P6_MULTI_Q` →|"Yes"| `P6_MANY_Q{"Many variables?"}`; `P6_MULTI_Q` →|"No"| `P6_TO_PART_4(["Continue in part 4"])`; `P6_MANY_Q` →|"No"| `P6_TO_PART_2(["Continue in part 2"])`; `P6_MANY_Q` →|"Yes"| `P6_TO_PART_3(["Continue in part 3"])`; `P6_GLOBAL_MODELS` & `P6_MIXED_FREQUENCY` → `P7` (ref). Part 2: a few related series: `P6_PART_2_IN(["From part 1: a few related series"])` → `P6_COINTEGRATED{"Cointegrated?"}`; `P6_COINTEGRATED` →|"Yes"| `P6_VECM`; `P6_COINTEGRATED` →|"No"| `P6_VAR`; `P6_VAR` →|"Structural question"| `P6_SVAR`; `P6_VAR` →|"Time-varying"| `P6_TVP_VAR`; `P6_VAR` →|"Reduced form"| `P7`; `P6_VECM` & `P6_SVAR` & `P6_TVP_VAR` → `P7` (ref). Part 3: many variables: `P6_PART_3_IN(["From part 1: many variables"])` → `P6_DIMENSION{"Dimension reduction?"}`; `P6_DIMENSION` →|"Factors"| `P6_FACTOR_MODELS`; `P6_DIMENSION` →|"Shrinkage"| `P6_REGULARISED_VAR`; `P6_DIMENSION` →|"Bayesian shrinkage"| `P6_BVAR`; `P6_DIMENSION` →|"Graph"| `P6_GRAPHICAL_MODELS`; `P6_DIMENSION` →|"Tensor"| `P6_TENSOR_AR`; `P6_FACTOR_MODELS` →|"Factors in a VAR"| `P6_FAVAR`; `P6_FACTOR_MODELS` →|"Factors alone"| `P7`; `P6_FAVAR` & `P6_REGULARISED_VAR` & `P6_BVAR` & `P6_GRAPHICAL_MODELS` & `P6_TENSOR_AR` → `P7` (ref). Part 4: one series, and its linear families: `P6_PART_4_IN(["From part 1: one series"])` → `P6_DEPENDENCE{"Dependence type?"}`; `P6_DEPENDENCE` →|"Linear"| `P6_LINEAR{"Long memory flag?"}`; `P6_DEPENDENCE` →|"Nonlinear flag"| `P6_TO_PART_6(["Continue in part 6"])`; `P6_DEPENDENCE` →|"Time-varying, latent or Bayesian"| `P6_TO_PART_7(["Continue in part 7"])`; `P6_DEPENDENCE` →|"Input-output system"| `P6_TO_PART_8(["Continue in part 8"])`; `P6_DEPENDENCE` →|"Learn from data"| `P6_TO_PART_9(["Continue in part 9"])`; `P6_LINEAR` →|"Yes"| `P6_ARFIMA`; `P6_LINEAR` →|"No"| `P6_LINEAR_FAMILY{"Family?"}`; `P6_LINEAR_FAMILY` →|"Autoregressive"| `P6_AR_MA_ARMA`; `P6_LINEAR_FAMILY` →|"Exogenous flag"| `P6_TO_PART_5(["Continue in part 5"])`; `P6_LINEAR_FAMILY` →|"Smoothing"| `P6_SMOOTHING{"Smoothing method?"}`; `P6_LINEAR_FAMILY` →|"Periodic"| `P6_PERIODIC_AR`; `P6_LINEAR_FAMILY` →|"Intermittent"| `P6_INTERMITTENT`; `P6_SMOOTHING` →|"State-space ETS"| `P6_ETS`; `P6_SMOOTHING` →|"Theta decomposition"| `P6_THETA`; `P6_AR_MA_ARMA` → `P6_ARIMA_SARIMA`; `P6_ARFIMA` & `P6_ARIMA_SARIMA` & `P6_ETS` → `P7`; `P6_THETA` & `P6_PERIODIC_AR` & `P6_INTERMITTENT` → `P7` (ref); `F_LAG_OPERATOR` (ref) -.- `P6_AR_MA_ARMA`. Part 5: exogenous regressors: `P6_PART_5_IN(["From part 4: exogenous flag"])` → `P6_EXOG_FORM{"Exogenous form?"}`; `P6_EXOG_FORM` →|"Inputs in the ARMA recursion"| `P6_ARIMAX`; `P6_EXOG_FORM` →|"Distributed lags"| `P6_DYNAMIC_REGRESSION`; `P6_EXOG_FORM` →|"Transfer function or intervention"| `P6_TRANSFER_FUNCTION`; `P6_ARIMAX` & `P6_DYNAMIC_REGRESSION` & `P6_TRANSFER_FUNCTION` → `P7` (ref). Part 6: nonlinear families: `P6_PART_6_IN(["From part 4: nonlinear flag"])` → `P6_NONLINEAR_FAMILY{"Regime mechanism?"}`; `P6_NONLINEAR_FAMILY` →|"Threshold"| `P6_THRESHOLD`; `P6_NONLINEAR_FAMILY` →|"Smooth"| `P6_SMOOTH_TRANSITION`; `P6_NONLINEAR_FAMILY` →|"Hidden state"| `P6_MARKOV_SWITCHING`; `P6_NONLINEAR_FAMILY` →|"Bilinear"| `P6_BILINEAR`; `P6_NONLINEAR_FAMILY` →|"Unknown form"| `P6_NONPARAMETRIC`; `P6_THRESHOLD` & `P6_SMOOTH_TRANSITION` & `P6_MARKOV_SWITCHING` & `P6_BILINEAR` & `P6_NONPARAMETRIC` → `P7` (ref). Part 7: time-varying, latent-component and Bayesian families: `P6_PART_7_IN(["From part 4"])` → `P6_STRUCTURED{"Structure?"}`; `P6_STRUCTURED` →|"Time-varying coefficients"| `P6_TVP_REGRESSION`; `P6_STRUCTURED` →|"Latent components"| `P6_LATENT_MODEL{"Latent model?"}`; `P6_STRUCTURED` →|"Bayesian priors"| `P6_DLM` & `P6_BSTS`; `P6_LATENT_MODEL` →|"Components"| `P6_STRUCTURAL_TS`; `P6_LATENT_MODEL` →|"General linear Gaussian"| `P6_DLM`; `P6_LATENT_MODEL` →|"Bayesian with regressors"| `P6_BSTS`; `P6_TVP_REGRESSION` & `P6_STRUCTURAL_TS` & `P6_DLM` & `P6_BSTS` → `P7` (ref). Part 8: input-output systems: `P6_PART_8_IN(["From part 4: input-output system"])` → `P6_IO_STRUCTURE{"Structure?"}`; `P6_IO_STRUCTURE` →|"Polynomial"| `P6_ARX_ARMAX`; `P6_IO_STRUCTURE` →|"State space"| `P6_SUBSPACE`; `P6_IO_STRUCTURE` →|"Block-oriented"| `P6_HAMMERSTEIN_WIENER`; `P6_IO_STRUCTURE` →|"Sparse nonlinear"| `P6_SINDY`; `P6_ARX_ARMAX` & `P6_SUBSPACE` & `P6_HAMMERSTEIN_WIENER` & `P6_SINDY` → `P7` (ref). Part 9: machine-learning families: classical, pretrained or generative, and hybrid: `P6_PART_9_IN(["From part 4: learn from data"])` → `P6_ML_FAMILY{"Model family?"}`; `P6_ML_FAMILY` →|"Classical ML"| `P6_ML_CLASSICAL{"Learner?"}`; `P6_ML_FAMILY` →|"Neural sequence models"| `P6_TO_PART_10(["Continue in part 10"])`; `P6_ML_FAMILY` →|"Pretrained or generative"| `P6_ML_PRETRAINED{"Approach?"}`; `P6_ML_FAMILY` →|"Hybrid"| `P6_HYBRID`; `P6_ML_CLASSICAL` →|"Trees"| `P6_TREE_ENSEMBLES`; `P6_ML_CLASSICAL` →|"Kernel"| `P6_GAUSSIAN_PROCESS`; `P6_ML_CLASSICAL` →|"Reservoir"| `P6_RESERVOIR`; `P6_ML_PRETRAINED` →|"Pretrained"| `P6_FOUNDATION_MODELS`; `P6_ML_PRETRAINED` →|"Generative"| `P6_GENERATIVE`; `P6_TREE_ENSEMBLES` & `P6_GAUSSIAN_PROCESS` & `P6_RESERVOIR` → `P7`; `P6_FOUNDATION_MODELS` & `P6_GENERATIVE` & `P6_HYBRID` → `P7` (ref). Part 10: neural sequence models: `P6_PART_10_IN(["From part 9: neural sequence models"])` → `P6_ML_NEURAL{"Architecture?"}`; `P6_ML_NEURAL` →|"Recurrent"| `P6_RNN`; `P6_ML_NEURAL` →|"Convolutional"| `P6_TCN`; `P6_ML_NEURAL` →|"Attention"| `P6_TRANSFORMERS`; `P6_ML_NEURAL` →|"State-space sequence"| `P6_SSM_SEQUENCE`; `P6_ML_NEURAL` →|"MLP forecasters"| `P6_NEURAL_FORECASTERS`; `P6_RNN` & `P6_TCN` & `P6_TRANSFORMERS` & `P6_SSM_SEQUENCE` & `P6_NEURAL_FORECASTERS` → `P7` (ref).

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
| P6_VECM | VECM | fractional cointegration (FCVAR) | [9, 28] | reference/09-multivariate/index.md |
| P6_SVAR | SVAR | identification schemes in P10 | [9, 21] | reference/09-multivariate/index.md |
| P6_FACTOR_MODELS | Static and dynamic factor models | | [9] | reference/09-multivariate/index.md |
| P6_REGULARISED_VAR | Regularised VAR | LASSO, ridge, elastic net | [9] | reference/09-multivariate/index.md |
| P6_GRAPHICAL_MODELS | Graphical models and sparse precision matrices | | [9] | reference/09-multivariate/index.md |
| P6_TENSOR_AR | Matrix and tensor autoregression | | [9] | reference/09-multivariate/index.md |
| P6_FAVAR | FAVAR and GVAR |  | [9] | reference/09-multivariate/index.md |
| P6_MIXED_FREQUENCY | Mixed-frequency models | MIDAS, mixed-frequency VAR | [22, 9] | reference/22-forecasting-practice/index.md |
| P6_STRUCTURAL_TS | Structural time-series models | local level, local linear trend, seasonal, cycle | [11] | reference/11-state-space/index.md |
| P6_DLM | Dynamic linear models | Bayesian ARIMA | [11, 12] | reference/11-state-space/index.md |
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

**Flow.** Flow as drawn (revised in review round 1, see Deviations): Part 1: observable components, least squares and moments: `P8_IN(["Joint model from P7"])` → `P8_OBSERVABLE{"All components observable?"}`; `P8_OBSERVABLE` →|"Yes"| `P8_LINEAR{"Linear in parameters?"}`; `P8_OBSERVABLE` →|"No"| `P8_TO_PART_3(["Continue in part 3"])`; `P8_LINEAR` →|"Yes"| `P8_OLS_GLS`; `P8_LINEAR` →|"Moments only"| `P8_MOMENTS{"Algorithm?"}`; `P8_LINEAR` →|"Cointegration, outliers or quantiles"| `P8_TO_PART_2(["Continue in part 2"])`; `P8_LINEAR` →|"No"| `P8_TO_PART_3`; `P8_MOMENTS` →|"Moment equations"| `P8_YULE_WALKER`; `P8_MOMENTS` →|"Recursive"| `P8_DURBIN_LEVINSON`; `P8_MOMENTS` →|"Regression on innovations"| `P8_HANNAN_RISSANEN`; `P8_OLS_GLS` & `P8_YULE_WALKER` & `P8_DURBIN_LEVINSON` & `P8_HANNAN_RISSANEN` → `P8_LINEAR_TO_PART_4(["Continue in part 4"])`. Part 2: cointegrating, robust and quantile regression: `P8_PART_2_IN(["From part 1"])` → `P8_SPECIAL{"Which case?"}`; `P8_SPECIAL` →|"Cointegrating regression"| `P8_FMOLS_DOLS`; `P8_SPECIAL` →|"Outliers"| `P8_ROBUST`; `P8_SPECIAL` →|"Conditional quantiles"| `P8_QUANTILE_REGRESSION`; `P8_FMOLS_DOLS` & `P8_ROBUST` & `P8_QUANTILE_REGRESSION` → `P8_SPECIAL_TO_PART_4(["Continue in part 4"])`. Part 3: tractable likelihoods: `P8_PART_3_IN(["From part 1"])` → `P8_LIKELIHOOD{"Likelihood tractable?"}`; `P8_LIKELIHOOD` →|"Gaussian state space"| `P8_PREDICTION_ERROR`; `P8_LIKELIHOOD` →|"Closed form"| `P8_MLE`; `P8_LIKELIHOOD` →|"Misspecified distribution"| `P8_QMLE`; `P8_LIKELIHOOD` →|"Nonlinear state"| `P8_NONLINEAR_FILTERS`; `P8_LIKELIHOOD` →|"Latent variables"| `P8_EM`; `P8_LIKELIHOOD` →|"Intractable"| `P8_TO_PART_4`; `P8_PREDICTION_ERROR` → `P8_KALMAN`; `P8_KALMAN` → `P8_MLE`; `P8_NONLINEAR_FILTERS` → `P8_PARTICLE_FILTERS`; `P8_MLE` & `P8_QMLE` & `P8_PARTICLE_FILTERS` & `P8_EM` → `P8_TO_PART_4(["Continue in part 4"])`; `F_LLN` (ref) -.- `P8_MLE`; `F_CLT` (ref) -.- `P8_QMLE`. Part 4: intractable likelihoods and convergence: `P8_PART_4_IN(["From parts 1 to 3"])` → `P8_ESTIMATED{"Estimated already?"}`; `P8_ESTIMATED` →|"No: likelihood intractable"| `P8_INTRACTABLE{"Approach?"}`; `P8_ESTIMATED` →|"Yes"| `P8_CONVERGENCE`; `P8_INTRACTABLE` →|"Moment conditions"| `P8_GMM`; `P8_INTRACTABLE` →|"Frequency domain"| `P8_WHITTLE`; `P8_INTRACTABLE` →|"Priors"| `P8_MCMC`; `P8_INTRACTABLE` →|"Simulate"| `P8_SIMULATION_INFERENCE`; `P8_INTRACTABLE` →|"Loss minimisation"| `P8_EMPIRICAL_LOSS`; `P8_MCMC` → `P8_VARIATIONAL`; `P8_EMPIRICAL_LOSS` → `P8_HYPERPARAMETERS`; `P8_GMM` & `P8_WHITTLE` & `P8_VARIATIONAL` & `P8_SIMULATION_INFERENCE` & `P8_HYPERPARAMETERS` → `P8_CONVERGENCE`; `P8_CONVERGENCE` → `P8_CONVERGED{"Converged?"}`; `P8_CONVERGED` →|"Yes"| `P8_OUT(["To P9 Diagnostics"])`; `P8_CONVERGED` -.->|"No: simplify or re-initialise"| `P6` (ref).

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P8_OLS_GLS | OLS, GLS and feasible GLS | Cochrane-Orcutt, Prais-Winsten | [4, 27] | reference/04-estimation/index.md |
| P8_YULE_WALKER | Yule-Walker and the method of moments | | [4] | reference/04-estimation/index.md |
| P8_DURBIN_LEVINSON | Durbin-Levinson and the innovations algorithm | | [4] | reference/04-estimation/index.md |
| P8_HANNAN_RISSANEN | Hannan-Rissanen and Burg estimation | | [4] | reference/04-estimation/index.md |
| P8_FMOLS_DOLS | Cointegrating regression | FMOLS, DOLS | [4, 28] | reference/04-estimation/index.md |
| P8_ROBUST | Robust estimation | M-estimators, LAD | [24, 4] | reference/24-robust-nonparametric/index.md |
| P8_QUANTILE_REGRESSION | Quantile regression and quantile autoregression |  | [24, 34] | reference/24-robust-nonparametric/index.md |
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

**Flow.** Flow as drawn (revised in review round 1, see Deviations): Part 1: innovation tests re-run on the complete model: `P9_IN(["Estimated joint model"])` → `P9_TYPE{"Innovation type?"}`; `P9_TYPE` →|"Continuous"| `P7_MEAN_TESTS` (ref); `P9_TYPE` →|"Counts"| `P7_COUNT_TESTS` (ref); `P9_TYPE` →|"Event times"| `P7_RESCALING` (ref); `P7_MEAN_TESTS` → `P9_AC{"Autocorrelation left?"}`; `P9_AC` -.->|"Yes: mean misspecified"| `P6` (ref); `P9_AC` →|"No"| `P7_VAR_TESTS` (ref); `P7_VAR_TESTS` → `P9_ARCH{"ARCH left?"}`; `P9_ARCH` -.->|"Yes"| `P7` (ref); `P9_ARCH` →|"No"| `P7_DIST_TESTS` (ref); `P7_DIST_TESTS` → `P9_DIST{"Distribution rejected?"}`; `P9_DIST` -.->|"Yes"| `P7`; `P9_DIST` →|"No"| `P7_REGIME_TESTS` (ref); `P7_REGIME_TESTS` → `P9_REGIME{"Regimes left?"}`; `P9_REGIME` -.->|"Yes"| `P7`; `P9_REGIME` →|"No"| `P9_MULTI{"Multivariate flag?"}`; `P9_MULTI` →|"Yes"| `P7_CORR_TESTS` (ref); `P9_MULTI` →|"No"| `P9_RESIDUAL_NONLINEARITY`; `P7_CORR_TESTS` → `P9_CORR{"Correlation misspecified?"}`; `P9_CORR` -.->|"Yes"| `P7`; `P9_CORR` →|"No"| `P9_RESIDUAL_NONLINEARITY`; `P9_RESIDUAL_NONLINEARITY` → `P9_NONLINEAR{"Nonlinearity left?"}`; `P9_NONLINEAR` -.->|"Yes"| `P6`; `P9_NONLINEAR` →|"No"| `P9_TO_PART_2`; `P7_COUNT_TESTS` → `P9_COUNT{"Dispersion misspecified?"}`; `P9_COUNT` -.->|"Yes"| `P7`; `P9_COUNT` →|"No"| `P9_TO_PART_2`; `P7_RESCALING` → `P9_INTENSITY{"Intensity misspecified?"}`; `P9_INTENSITY` -.->|"Yes"| `P7`; `P9_INTENSITY` →|"No"| `P9_TO_PART_2(["Continue in part 2"])`. Part 2: model-specific checks, selection and comparison: `P9_PART_2_IN(["From part 1"])` → `P9_MODEL_KIND{"Model kind?"}`; `P9_MODEL_KIND` →|"Volatility"| `P9_VOLATILITY_DIAGNOSTICS`; `P9_MODEL_KIND` →|"Other"| `P9_INFORMATION_CRITERIA`; `P9_VOLATILITY_DIAGNOSTICS` → `P9_INFORMATION_CRITERIA`; `P9_INFORMATION_CRITERIA` → `P9_INFERENCE_NEEDED{"Finite-sample inference?"}`; `P9_INFERENCE_NEEDED` →|"Yes"| `P9_BOOTSTRAP`; `P9_INFERENCE_NEEDED` →|"No"| `P9_FORECAST_COMPARISON`; `P9_BOOTSTRAP` → `P9_FORECAST_COMPARISON`; `P9_FORECAST_COMPARISON` → `P9_ENCOMPASSING`; `P9_ENCOMPASSING` → `P9_PASS{"All diagnostics pass?"}`; `P9_PASS` →|"Yes"| `P9_OUT(["To P10 Inference"])`; `P9_PASS` -.->|"Mean misspecified"| `P6` (ref); `P9_PASS` -.->|"Innovations misspecified"| `P7` (ref).

**Leaves.**

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P9_RESIDUAL_NONLINEARITY | Remaining nonlinearity | BDS on residuals | [8, 5] | 01-workflow/p09-diagnostics-selection.md |
| P9_VOLATILITY_DIAGNOSTICS | Volatility model diagnostics | standardised residuals, sign-bias test, news impact curve | [10] | 01-workflow/p09-diagnostics-selection.md |
| P9_INFORMATION_CRITERIA | Information criteria | AIC, BIC, HQIC, WAIC, LOO; posterior predictive checks | [6, 12] | reference/06-model-selection/index.md |
| P9_BOOTSTRAP | Bootstrap inference | block, stationary, sieve | [5, 25] | reference/06-model-selection/index.md |
| P9_FORECAST_COMPARISON | Forecast comparison tests | Diebold-Mariano, Clark-West, reality check, model confidence set | [6] | reference/06-model-selection/index.md |
| P9_ENCOMPASSING | Forecast encompassing | | [6] | reference/06-model-selection/index.md |

- [ ] **Steps:** replace the note, 10 rows `phase: P9`, scaffold, audit, build. Commit `feat(flowchart): P9 diagnostics and model selection sub-diagram`.

---

### Task 8: P10 sub-diagram — inference and interpretation

**Files:** `docs/01-workflow/p10-inference.md`, inventory, reference landing pages. Owner page: the phase page.

**Flow.** Flow as drawn (revised in review round 1, see Deviations): Part 1: dispatch on the purpose flag, and forecasting: `P10_IN(["Validated model and purpose flag"])` → `P10_PURPOSE{"Purpose flag?"}`; `P10_PURPOSE` →|"The future"| `P10_POINT_FORECASTS`; `P10_PURPOSE` →|"Causes"| `P10_TO_PART_2(["Continue in part 2"])`; `P10_PURPOSE` →|"Structure in the series or events"| `P10_TO_PART_4(["Continue in part 4"])`; `P10_PURPOSE` →|"Other outputs"| `P10_TO_PART_5(["Continue in part 5"])`; `P10_POINT_FORECASTS` → `P10_INTERVALS`; `P10_INTERVALS` → `P10_DENSITY_QUANTILE`; `P10_DENSITY_QUANTILE` → `P10_RISK{"Risk measures needed?"}`; `P10_RISK` →|"Yes"| `P10_RISK_MEASURES` (ref); `P10_RISK` →|"No"| `P10_MULTISTEP`; `P10_RISK_MEASURES` → `P10_MULTISTEP`; `P10_MULTISTEP` → `P10_HIERARCHY{"Hierarchy flag?"}`; `P10_HIERARCHY` →|"Yes"| `P10_RECONCILIATION`; `P10_HIERARCHY` →|"No"| `P10_COMBINATION`; `P10_RECONCILIATION` → `P10_COMBINATION`; `P10_COMBINATION` → `P10_JUDGMENTAL`; `P10_JUDGMENTAL` → `P10_BLACK_BOX{"Black-box model?"}`; `P10_BLACK_BOX` →|"Yes"| `P10_INTERPRETABILITY` (ref); `P10_BLACK_BOX` →|"No"| `P10_MIXED`; `P10_INTERPRETABILITY` → `P10_MIXED{"Mixed-frequency flag?"}`; `P10_MIXED` →|"Yes"| `P10_NOWCASTING`; `P10_MIXED` →|"No"| `P11`; `P10_NOWCASTING` → `P11` (ref); `F_CONDITIONAL_EXPECTATION` (ref) -.- `P10_POINT_FORECASTS`; `F_PROJECTION` (ref) -.- `P10_INTERVALS`; `P6_MIXED_FREQUENCY` (ref) -.- `P10_NOWCASTING`. Part 2: causal and structural inference: `P10_PART_2_IN(["From part 1: causes"])` → `P10_COEFFICIENT_TESTS`; `P10_COEFFICIENT_TESTS` → `P10_HAC`; `P10_HAC` → `P10_SYSTEM{"Multivariate flag?"}`; `P10_SYSTEM` →|"Yes"| `P10_TO_PART_3(["Continue in part 3"])`; `P10_SYSTEM` →|"No"| `P10_COUNTERFACTUALS`; `P10_COUNTERFACTUALS` → `P11` (ref). Part 3: causal questions for several series: `P10_PART_3_IN(["From part 2: several series"])` → `P10_CAUSAL_Q{"Causal question?"}`; `P10_CAUSAL_Q` →|"Long-run relations"| `P10_COINTEGRATION`; `P10_CAUSAL_Q` →|"Predictive causality"| `P10_GRANGER`; `P10_CAUSAL_Q` →|"Nonlinear dependence"| `P10_NONLINEAR_CAUSALITY`; `P10_CAUSAL_Q` →|"Structural shocks"| `P10_SVAR_IDENTIFICATION`; `P10_CAUSAL_Q` →|"Dynamic effects"| `P10_LOCAL_PROJECTIONS`; `P10_SVAR_IDENTIFICATION` → `P10_IRF_FEVD`; `P10_COINTEGRATION` & `P10_GRANGER` & `P10_NONLINEAR_CAUSALITY` → `P11`; `P10_IRF_FEVD` & `P10_LOCAL_PROJECTIONS` → `P11` (ref). Part 4: structure in the series and events: `P10_PART_4_IN(["From part 1"])` → `P10_PURPOSE_4{"Purpose flag?"}`; `P10_PURPOSE_4` →|"Structure in the series"| `P10_STRUCTURE{"Which structure?"}`; `P10_PURPOSE_4` →|"Events"| `P10_EVENTS{"Which events?"}`; `P10_STRUCTURE` →|"Signal versus noise"| `P2_SE_SNR` (ref); `P10_STRUCTURE` →|"Components"| `P2_DC_COMPONENT_ANALYSIS` (ref); `P10_STRUCTURE` →|"Frequencies"| `P2_SP_PEAK_SIGNIFICANCE` (ref); `P10_EVENTS` →|"Changes"| `P2_CP_TYPE` (ref); `P10_EVENTS` →|"Anomalies or regimes"| `P2_AN_THRESHOLD` (ref); `P2_SE_SNR` & `P2_DC_COMPONENT_ANALYSIS` & `P2_SP_PEAK_SIGNIFICANCE` & `P2_CP_TYPE` & `P2_AN_THRESHOLD` → `P11` (ref). Part 5: other outputs: `P10_PART_5_IN(["From part 1: other outputs"])` → `P10_OUTPUTS{"Which output?"}`; `P10_OUTPUTS` →|"Features and labels"| `P10_INTERPRETABILITY`; `P10_OUTPUTS` →|"A system model"| `P2_SI_TRANSFER_FUNCTION` (ref); `P10_OUTPUTS` →|"Simulated paths"| `P10_SCENARIOS`; `P2_SI_TRANSFER_FUNCTION` → `P2_SI_STABILITY` (ref); `P10_SCENARIOS` → `P10_RISK_MEASURES`; `P10_INTERPRETABILITY` & `P2_SI_STABILITY` & `P10_RISK_MEASURES` → `P11` (ref).

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
| P10_COUNTERFACTUALS | Counterfactual designs | interrupted time series, difference-in-differences, synthetic control, CausalImpact | [21] | reference/21-causal-inference/index.md |
| P10_POINT_FORECASTS | Point forecasts and horizons | | [22] | reference/22-forecasting-practice/index.md |
| P10_INTERVALS | Prediction intervals | analytical, bootstrap, conformal | [34, 22] | reference/34-probabilistic-forecasting/index.md |
| P10_DENSITY_QUANTILE | Density and quantile forecasts | | [34] | reference/34-probabilistic-forecasting/index.md |
| P10_MULTISTEP | Multi-step strategies | recursive, direct, MIMO | [34, 22] | reference/34-probabilistic-forecasting/index.md |
| P10_RECONCILIATION | Hierarchical and temporal reconciliation | bottom-up, top-down, MinT | [22, 34] | reference/22-forecasting-practice/index.md |
| P10_COMBINATION | Forecast combination and model averaging | | [22, 12] | reference/22-forecasting-practice/index.md |
| P10_JUDGMENTAL | Judgmental adjustment | | [22] | reference/22-forecasting-practice/index.md |
| P10_NOWCASTING | Nowcasting | bridge equations, factor models | [22, 9] | reference/22-forecasting-practice/index.md |
| P10_RISK_MEASURES | Risk measures and their backtests | VaR, expected shortfall, Kupiec, Christoffersen | [10] | reference/10-volatility/index.md |
| P10_SCENARIOS | Stress testing and scenario design |  | [25, 10] | reference/25-simulation/index.md |
| P10_INTERPRETABILITY | Interpretability | SHAP, attention | [18] | reference/18-machine-learning/index.md |

**Foundation rows.** `F_CONDITIONAL_EXPECTATION` | Conditional expectation as the optimal forecast | `00-foundations/stochastic-processes.md#conditional-expectation-as-the-optimal-forecast`. `F_PROJECTION` | Projection theorem and best linear prediction | `00-foundations/stochastic-processes.md#projection-theorem-and-best-linear-prediction`.

- [ ] **Steps:** replace the note, 20 rows `phase: P10`, 2 F rows, scaffold, audit, build. Commit `feat(flowchart): P10 inference and interpretation sub-diagram`.

---

### Task 9: P11 sub-diagram — validation and deployment

**Files:** `docs/01-workflow/p11-validation-deployment.md`, inventory, reference landing pages. Owner page: the phase page.

**Flow.** Flow as drawn (revised in review round 1, see Deviations): Part 1: backtesting and metrics for the future, causes and structure: `P11_IN(["Model and outputs from P10"])` → `P11_ROLLING_ORIGIN`; `P11_ROLLING_ORIGIN` → `P11_METRIC_KIND{"Purpose flag?"}`; `P11_METRIC_KIND` →|"The future"| `P11_POINT_METRICS`; `P11_METRIC_KIND` →|"Causes"| `P2_CA_SENSITIVITY` (ref); `P11_METRIC_KIND` →|"Structure in the series"| `P11_STRUCTURE{"Which structure?"}`; `P11_METRIC_KIND` →|"Events or other outputs"| `P11_TO_PART_2(["Continue in part 2"])`; `P11_POINT_METRICS` → `P11_PROBABILISTIC_METRICS`; `P11_STRUCTURE` →|"Signal versus noise"| `P2_SE_SNR` (ref); `P11_STRUCTURE` →|"Components"| `P7_MEAN_TESTS` (ref); `P11_STRUCTURE` →|"Frequencies"| `P2_SP_PEAK_SIGNIFICANCE` (ref); `P11_PROBABILISTIC_METRICS` & `P2_CA_SENSITIVITY` & `P2_SE_SNR` & `P7_MEAN_TESTS` & `P2_SP_PEAK_SIGNIFICANCE` → `P11_METRICS_TO_PART_3(["Continue in part 3"])`. Part 2: metrics for events and other outputs: `P11_PART_2_IN(["From part 1"])` → `P11_METRIC_KIND_2{"Purpose flag?"}`; `P11_METRIC_KIND_2` →|"Events"| `P11_EVENTS{"Which events?"}`; `P11_METRIC_KIND_2` →|"Other outputs"| `P11_OUTPUTS{"Which output?"}`; `P11_EVENTS` →|"Changes"| `P11_CHANGE_POINT_METRICS`; `P11_EVENTS` →|"Anomalies or regimes"| `P11_CLASSIFICATION_METRICS`; `P11_OUTPUTS` →|"Features and labels"| `P11_CLASSIFICATION_METRICS`; `P11_OUTPUTS` →|"A system model"| `P2_SI_VALIDATION` (ref); `P11_OUTPUTS` →|"Simulated paths"| `P2_SM_DISTRIBUTION_MATCH` (ref); `P11_CHANGE_POINT_METRICS` & `P11_CLASSIFICATION_METRICS` & `P2_SI_VALIDATION` & `P2_SM_DISTRIBUTION_MATCH` → `P11_TO_PART_3(["Continue in part 3"])`. Part 3: acceptance and deployment: `P11_PART_3_IN(["From parts 1 and 2"])` → `P11_ACCEPTABLE{"Performance acceptable?"}`; `P11_ACCEPTABLE` -.->|"No"| `P6` (ref); `P11_ACCEPTABLE` →|"Yes"| `P11_DOCUMENTATION`; `P11_DOCUMENTATION` → `P11_RETRAINING`; `P11_RETRAINING` → `P11_DRIFT_MONITORING`; `P11_DRIFT_MONITORING` → `P11_SPC`; `P11_SPC` → `P11_DRIFT{"Drift detected?"}`; `P11_DRIFT` →|"Yes"| `P11_ONLINE_UPDATING`; `P11_DRIFT` →|"No"| `P11_OUT(["Validated model deployed"])`; `P11_ONLINE_UPDATING` -.-> `P8` (ref); `P2_CP_CUSUM` (ref) -.- `P11_SPC`; `P2_CP_CUSUM` -.- `P11_DRIFT_MONITORING`; `P2_CP_BOCPD` (ref) -.- `P11_DRIFT_MONITORING`.

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

**10.1 Forecasting (`01-forecasting.md`, code FC).** Flow as drawn (revised in review round 1, see Deviations): `P2_FC_IN(["Forecasting question"])` → `P2_FC_HORIZON_Q{"Horizon?"}`; `P2_FC_HORIZON_Q` →|"Short or medium"| `P2_FC_MANY`; `P2_FC_HORIZON_Q` →|"Long"| `P2_FC_LONG_FLAG["Set flag: multi-step horizon"]`; `P2_FC_LONG_FLAG` → `P2_FC_MANY{"Global or hierarchy flag?"}`; `P2_FC_MANY` →|"Yes"| `B7` (ref); `P2_FC_MANY` →|"No"| `P2_FC_EXOG`; `B7` → `P2_FC_EXOG{"Future covariates known?"}`; `P2_FC_EXOG` →|"Yes"| `P6_ARIMAX` (ref); `P2_FC_EXOG` →|"No"| `P3` (ref); `P6_ARIMAX` → `P3`; `P3` → `P4` (ref); `P4` → `P6_ARIMA_SARIMA` (ref); `P4` → `P6_ETS` (ref); `P4` → `P6_GLOBAL_MODELS` (ref); `P6_ARIMA_SARIMA` & `P6_ETS` & `P6_GLOBAL_MODELS` → `P7` (ref); `P7` → `P8` (ref); `P8` → `P9_FORECAST_COMPARISON` (ref); `P9_FORECAST_COMPARISON` → `P2_FC_BASELINES`; `P2_FC_BASELINES` → `P2_FC_DOMAIN{"Epidemic counts?"}`; `P2_FC_DOMAIN` →|"Yes"| `P2_FC_EPIDEMIC`; `P2_FC_DOMAIN` →|"No"| `P10_POINT_FORECASTS`; `P2_FC_EPIDEMIC` → `P10_POINT_FORECASTS` (ref); `P10_POINT_FORECASTS` → `P10_INTERVALS` (ref); `P10_INTERVALS` → `P2_FC_STEPS{"Multi-step flag?"}`; `P2_FC_STEPS` →|"Yes"| `P10_MULTISTEP` (ref); `P2_FC_STEPS` →|"No"| `P10_RECONCILIATION`; `P10_MULTISTEP` → `P10_RECONCILIATION` (ref); `P10_RECONCILIATION` → `P10_COMBINATION` (ref); `P10_COMBINATION` → `P11_ROLLING_ORIGIN` (ref); `P11_ROLLING_ORIGIN` → `P11_POINT_METRICS` (ref); `P11_POINT_METRICS` → `P11_PROBABILISTIC_METRICS` (ref); `P11_PROBABILISTIC_METRICS` → `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_FC_BASELINES | Naive and seasonal-naive baselines | | [22] | reference/22-forecasting-practice/index.md |
| P2_FC_EPIDEMIC | Epidemic nowcasting | reproduction-number estimation, SIR fitting | [26, 22] | reference/26-applied-domains/index.md |


**10.2 Causal and structural inference (`02-causal-inference.md`, code CA).** Flow as drawn (revised in review round 1, see Deviations): `P2_CA_IN(["Causal question"])` → `P2_CA_DESIGN{"Experimental data?"}`; `P2_CA_DESIGN` →|"Randomised or natural experiment"| `P10_COUNTERFACTUALS` (ref); `P2_CA_DESIGN` →|"Observational"| `P2_CA_IDENTIFICATION`; `P2_CA_IDENTIFICATION` → `P3` (ref); `P3` → `P4` (ref); `P4` → `P2_CA_SYSTEM{"Several series?"}`; `P2_CA_SYSTEM` →|"Yes"| `P3_COINTEGRATION_PRECHECK` (ref); `P2_CA_SYSTEM` →|"No"| `P6_TRANSFER_FUNCTION` (ref); `P3_COINTEGRATION_PRECHECK` → `P2_CA_COINT{"Cointegrated?"}`; `P2_CA_COINT` →|"Yes"| `P6_VECM` (ref); `P2_CA_COINT` →|"No"| `P6_VAR` (ref); `P6_VECM` & `P6_VAR` & `P6_TRANSFER_FUNCTION` → `P7` (ref); `P7` → `P8` (ref); `P8` → `P9` (ref); `P9` → `P2_CA_MULTI{"Multivariate flag?"}`; `P2_CA_MULTI` →|"Yes"| `P2_CA_QUESTION{"Causal question?"}`; `P2_CA_MULTI` →|"No"| `P10_COUNTERFACTUALS`; `P2_CA_QUESTION` →|"Long-run relations"| `P10_COINTEGRATION` (ref); `P2_CA_QUESTION` →|"Predictive causality"| `P10_GRANGER` (ref); `P2_CA_QUESTION` →|"Nonlinear dependence"| `P10_NONLINEAR_CAUSALITY` (ref); `P2_CA_QUESTION` →|"Structural shocks"| `P10_SVAR_IDENTIFICATION` (ref); `P2_CA_QUESTION` →|"Dynamic effects"| `P10_LOCAL_PROJECTIONS` (ref); `P10_SVAR_IDENTIFICATION` → `P10_IRF_FEVD` (ref); `P10_COINTEGRATION` & `P10_GRANGER` & `P10_NONLINEAR_CAUSALITY` & `P10_IRF_FEVD` → `P10_COEFFICIENT_TESTS` (ref); `P10_LOCAL_PROJECTIONS` & `P10_COUNTERFACTUALS` → `P10_COEFFICIENT_TESTS`; `P10_COEFFICIENT_TESTS` → `P10_HAC` (ref); `P10_HAC` → `P2_CA_PLACEBO`; `P2_CA_PLACEBO` → `P2_CA_SENSITIVITY`; `P2_CA_SENSITIVITY` → `P2_CA_VERDICT{"Identification holds?"}`; `P2_CA_VERDICT` →|"Yes: report a causal effect"| `P11` (ref); `P2_CA_VERDICT` →|"No: report an association only"| `P11`.

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_CA_IDENTIFICATION | Identification strategy and exogeneity | | [21] | reference/21-causal-inference/index.md |
| P2_CA_PLACEBO | Placebo and falsification tests | | [21] | reference/21-causal-inference/index.md |
| P2_CA_SENSITIVITY | Sensitivity analysis across specifications | | [21] | reference/21-causal-inference/index.md |

**10.3 Signal extraction and denoising (`03-signal-extraction.md`, code SE).** Flow as drawn (revised in review round 1, see Deviations): `P2_SE_IN(["Noisy signal"])` → `P2_SE_NOISE_TYPE`; `P2_SE_NOISE_TYPE` → `P2_SE_NOISE_Q{"Noise character?"}`; `P2_SE_NOISE_Q` →|"White"| `P2_SE_FILTER_Q`; `P2_SE_NOISE_Q` →|"Coloured"| `P2_SE_WIENER`; `P2_SE_NOISE_Q` →|"Impulsive"| `P0_ROBUST_FILTER` (ref); `P2_SE_NOISE_Q` →|"Non-stationary"| `P8_KALMAN` (ref); `P2_SE_NOISE_Q` →|"1/f"| `P5_TF_DWT` (ref); `P0_ROBUST_FILTER` → `P2_SE_FILTER_Q{"Filter type?"}`; `P2_SE_FILTER_Q` →|"Low-pass"| `P5_FD_FILTERS` (ref); `P2_SE_FILTER_Q` →|"High-pass"| `P5_FD_FILTERS`; `P2_SE_FILTER_Q` →|"Band-pass"| `P5_FD_FILTERS`; `P2_SE_FILTER_Q` →|"Notch"| `P5_FD_FILTERS`; `P5_TF_DWT` → `P2_SE_WAVELET_DENOISING`; `P5_FD_FILTERS` & `P2_SE_WIENER` & `P8_KALMAN` & `P2_SE_WAVELET_DENOISING` → `P2_SE_SNR`; `P2_SE_SNR` → `P2_SE_OK{"Signal preserved?"}`; `P2_SE_OK` -.->|"No"| `P2_SE_FILTER_Q`; `P2_SE_OK` →|"Yes"| `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SE_NOISE_TYPE | Characterise the noise | white, coloured, impulsive, non-stationary, 1/f | [13] | reference/13-spectral-analysis/index.md |
| P2_SE_WIENER | Wiener filtering | | [13] | reference/13-spectral-analysis/index.md |
| P2_SE_WAVELET_DENOISING | Wavelet denoising | | [13] | reference/13-spectral-analysis/index.md |
| P2_SE_SNR | Evaluate the signal-to-noise ratio |  | [13] | reference/13-spectral-analysis/index.md |

**10.4 Change-point detection (`04-change-point-detection.md`, code CP).** Flow as drawn (revised in review round 1, see Deviations): `P2_CP_IN(["Change-point question"])` → `P3_STRUCTURAL_BREAKS` (ref); `P3_STRUCTURAL_BREAKS` → `P2_CP_MODE{"Online or offline?"}`; `P2_CP_MODE` →|"Online"| `P2_CP_ONLINE{"Detector?"}`; `P2_CP_MODE` →|"Offline"| `P2_CP_PELT`; `P2_CP_MODE` →|"Multivariate"| `P2_CP_MULTIVARIATE`; `P2_CP_ONLINE` →|"Sequential statistic"| `P2_CP_CUSUM`; `P2_CP_ONLINE` →|"Bayesian"| `P2_CP_BOCPD`; `P2_CP_PELT` → `P2_CP_PENALTY`; `P2_CP_CUSUM` & `P2_CP_BOCPD` & `P2_CP_PENALTY` & `P2_CP_MULTIVARIATE` → `P2_CP_TYPE`; `P2_CP_TYPE` → `P2_CP_KIND{"Change kind?"}`; `P2_CP_KIND` →|"Mean"| `P4_BREAK_HANDLING` (ref); `P2_CP_KIND` →|"Regime"| `P6_MARKOV_SWITCHING` (ref); `P2_CP_KIND` →|"Variance"| `P7_MS_GARCH` (ref); `P4_BREAK_HANDLING` & `P6_MARKOV_SWITCHING` & `P7_MS_GARCH` → `P11_CHANGE_POINT_METRICS` (ref); `P11_CHANGE_POINT_METRICS` → `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_CP_CUSUM | Sequential detection | CUSUM, Page-Hinkley | [30, 23] | reference/30-structural-change/index.md |
| P2_CP_BOCPD | Bayesian online change-point detection | | [30, 12] | reference/30-structural-change/index.md |
| P2_CP_PELT | Offline segmentation | PELT, binary segmentation | [30, 19] | reference/30-structural-change/index.md |
| P2_CP_PENALTY | Choose the number of change points | penalty, BIC | [30, 6] | reference/30-structural-change/index.md |
| P2_CP_MULTIVARIATE | Multivariate change points | E-divisive | [30] | reference/30-structural-change/index.md |
| P2_CP_TYPE | Classify the change | mean, variance, regime | [30] | reference/30-structural-change/index.md |

**10.5 Anomaly and regime detection (`05-anomaly-regime-detection.md`, code AN).** Flow as drawn (revised in review round 1, see Deviations): `P2_AN_IN(["Anomaly or regime question"])` → `P3` (ref); `P3` → `P2_AN_KIND{"Anomaly kind?"}`; `P2_AN_KIND` →|"Point"| `P2_AN_STATISTICAL`; `P2_AN_KIND` →|"Contextual"| `P2_AN_CONTEXT{"Detector?"}`; `P2_AN_KIND` →|"Collective"| `P2_AN_COLLECTIVE{"Detector?"}`; `P2_AN_KIND` →|"Regime"| `P6_MARKOV_SWITCHING` (ref); `P2_AN_CONTEXT` →|"Model residuals"| `P2_AN_RESIDUAL`; `P2_AN_CONTEXT` →|"Reconstruction error"| `P2_AN_AUTOENCODER`; `P2_AN_COLLECTIVE` →|"Distance-based"| `P2_AN_MATRIX_PROFILE`; `P2_AN_COLLECTIVE` →|"Isolation-based"| `P2_AN_ISOLATION_FOREST`; `P2_AN_STATISTICAL` & `P2_AN_RESIDUAL` & `P2_AN_AUTOENCODER` → `P2_AN_LABELS`; `P2_AN_MATRIX_PROFILE` & `P2_AN_ISOLATION_FOREST` & `P6_MARKOV_SWITCHING` → `P2_AN_LABELS{"Labels available?"}`; `P2_AN_LABELS` →|"Yes"| `P8_HYPERPARAMETERS` (ref); `P2_AN_LABELS` →|"No"| `P2_AN_THRESHOLD`; `P8_HYPERPARAMETERS` → `P2_AN_THRESHOLD`; `P2_AN_THRESHOLD` → `P11_CLASSIFICATION_METRICS` (ref); `P11_CLASSIFICATION_METRICS` → `P11_DRIFT_MONITORING` (ref); `P11_DRIFT_MONITORING` → `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_AN_STATISTICAL | Statistical outlier scores | modified z-score, robust statistics | [19, 24] | reference/19-classification-anomaly/index.md |
| P2_AN_RESIDUAL | Residual-based detection from a fitted model | | [19] | reference/19-classification-anomaly/index.md |
| P2_AN_MATRIX_PROFILE | Matrix profile and discord discovery | | [19] | reference/19-classification-anomaly/index.md |
| P2_AN_ISOLATION_FOREST | Isolation forests for time series | | [19] | reference/19-classification-anomaly/index.md |
| P2_AN_AUTOENCODER | Autoencoders and variational autoencoders | | [19, 18] | reference/19-classification-anomaly/index.md |
| P2_AN_THRESHOLD | Set thresholds by the cost of errors | | [19] | reference/19-classification-anomaly/index.md |

**10.6 Decomposition (`06-decomposition.md`, code DC).** Flow as drawn (revised in review round 1, see Deviations): `P2_DC_IN(["Decomposition question"])` → `P2_DC_SEASONAL{"Seasonal?"}`; `P2_DC_SEASONAL` →|"Yes"| `P3_SEASONALITY` (ref); `P2_DC_SEASONAL` →|"No"| `P4_FILTER_DECOMPOSITION` (ref); `P3_SEASONALITY` → `P2_DC_ADDITIVE_MULTIPLICATIVE`; `P2_DC_ADDITIVE_MULTIPLICATIVE` → `P2_DC_METHOD{"Method?"}`; `P2_DC_METHOD` →|"STL or X-13"| `P4_SEASONAL_ADJUSTMENT` (ref); `P2_DC_METHOD` →|"Several periods"| `P4_MULTIPLE_SEASONALITY` (ref); `P2_DC_METHOD` →|"Model-based"| `P4_MODEL_DECOMPOSITION` (ref); `P2_DC_METHOD` →|"Nonparametric"| `P4_SSA` (ref); `P4_SEASONAL_ADJUSTMENT` & `P4_MULTIPLE_SEASONALITY` & `P4_MODEL_DECOMPOSITION` & `P4_SSA` & `P4_FILTER_DECOMPOSITION` → `P2_DC_COMPONENT_ANALYSIS`; `P2_DC_COMPONENT_ANALYSIS` → `P7_MEAN_TESTS` (ref); `P7_MEAN_TESTS` → `P2_DC_RESIDUAL{"Residual white?"}`; `P2_DC_RESIDUAL` -.->|"No"| `P2_DC_METHOD`; `P2_DC_RESIDUAL` →|"Yes"| `P2_DC_REVISION`; `P2_DC_REVISION` → `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_DC_ADDITIVE_MULTIPLICATIVE | Additive or multiplicative decomposition | | [3] | reference/03-classical/index.md |
| P2_DC_COMPONENT_ANALYSIS | Analyse and interpret the components | | [3] | reference/03-classical/index.md |
| P2_DC_REVISION | Revision stability of real-time decompositions | | [29] | reference/29-seasonality-calendar/index.md |

**10.7 Feature extraction, classification and clustering (`07-feature-extraction-classification.md`, code FE).** Flow as drawn (revised in review round 1, see Deviations): Part 1: hand-crafted features: `P2_FE_IN(["Labelling or grouping question"])` → `P2_FE_FEATURE_Q{"Feature family?"}`; `P2_FE_FEATURE_Q` →|"Hand-crafted features"| `P2_FE_HANDCRAFTED{"Domain?"}`; `P2_FE_FEATURE_Q` →|"Representations"| `P2_FE_TO_PART_2`; `P2_FE_HANDCRAFTED` →|"Time"| `P2_FE_TIME_FEATURES`; `P2_FE_HANDCRAFTED` →|"Frequency"| `P2_FE_FREQ_FEATURES`; `P2_FE_HANDCRAFTED` →|"Time-frequency"| `P2_FE_TF_FEATURES`; `P2_FE_HANDCRAFTED` →|"Nonlinear dynamics"| `P2_FE_NONLINEAR_FEATURES`; `P2_FE_HANDCRAFTED` →|"Automated"| `P2_FE_AUTOMATED`; `P2_FE_TIME_FEATURES` & `P2_FE_FREQ_FEATURES` & `P2_FE_TF_FEATURES` & `P2_FE_NONLINEAR_FEATURES` & `P2_FE_AUTOMATED` → `P2_FE_TO_PART_2(["Continue in part 2"])`. Part 2: representations, learners and evaluation: `P2_FE_FROM_PART_1(["From part 1"])` → `P2_FE_FEATURE_Q_2{"Feature family?"}`; `P2_FE_FEATURE_Q_2` →|"Representations"| `P2_FE_REPRESENTATION{"Representation?"}`; `P2_FE_FEATURE_Q_2` →|"Hand-crafted features"| `P2_FE_LEARNER`; `P2_FE_REPRESENTATION` →|"Symbolic"| `P2_FE_SYMBOLIC`; `P2_FE_REPRESENTATION` →|"Learned"| `P2_FE_REPRESENTATION_LEARNING`; `P2_FE_REPRESENTATION` →|"Topological"| `P2_FE_TDA`; `P2_FE_SYMBOLIC` & `P2_FE_REPRESENTATION_LEARNING` & `P2_FE_TDA` → `P2_FE_LEARNER{"Task?"}`; `P2_FE_LEARNER` →|"Classification"| `P2_FE_DISTANCES`; `P2_FE_LEARNER` →|"Clustering"| `P2_FE_CLUSTERING`; `P2_FE_LEARNER` →|"Regression"| `P6_TREE_ENSEMBLES` (ref); `P2_FE_DISTANCES` → `P2_FE_SHAPELETS`; `P2_FE_SHAPELETS` → `P2_FE_DEEP_CLASSIFIERS`; `P2_FE_DEEP_CLASSIFIERS` & `P2_FE_CLUSTERING` & `P6_TREE_ENSEMBLES` → `P2_FE_AUGMENTATION`; `P2_FE_AUGMENTATION` → `P8_HYPERPARAMETERS` (ref); `P8_HYPERPARAMETERS` → `P10_INTERPRETABILITY` (ref); `P10_INTERPRETABILITY` → `P11_CLASSIFICATION_METRICS` (ref); `P11_CLASSIFICATION_METRICS` → `P11` (ref).

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

**10.8 Spectral analysis (`08-spectral-analysis.md`, code SP).** Flow as drawn (revised in review round 1, see Deviations): `P2_SP_IN(["Spectral question"])` → `P3` (ref); `P3` → `P4` (ref); `P4` → `P2_SP_SERIES{"One or two series?"}`; `P2_SP_SERIES` →|"One"| `P5_FD_DFT` (ref); `P2_SP_SERIES` →|"Two"| `P2_SP_CROSS_SPECTRUM`; `P5_FD_DFT` → `P5_FD_SMOOTHED` (ref); `P5_FD_SMOOTHED` → `P2_SP_SPECTRAL_SHAPE`; `P2_SP_SPECTRAL_SHAPE` → `P2_SP_PEAKS{"Peaks?"}`; `P2_SP_PEAKS` →|"Yes"| `P2_SP_PEAK_SIGNIFICANCE`; `P2_SP_PEAKS` →|"No"| `P11`; `P2_SP_PEAK_SIGNIFICANCE` → `P2_SP_HARMONIC_REGRESSION`; `P2_SP_CROSS_SPECTRUM` → `P2_SP_FREQ_GRANGER`; `P2_SP_HARMONIC_REGRESSION` & `P2_SP_FREQ_GRANGER` → `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SP_SPECTRAL_SHAPE | Interpret the spectral shape | white, 1/f, peaks, band-limited | [13] | reference/13-spectral-analysis/index.md |
| P2_SP_PEAK_SIGNIFICANCE | Peak significance | Fisher's g-test | [13, 5] | reference/13-spectral-analysis/index.md |
| P2_SP_HARMONIC_REGRESSION | Harmonic regression from detected frequencies | | [13, 3] | reference/13-spectral-analysis/index.md |
| P2_SP_CROSS_SPECTRUM | Cross-spectrum, coherence and phase | | [13] | reference/13-spectral-analysis/index.md |
| P2_SP_FREQ_GRANGER | Frequency-domain Granger causality | | [13, 21] | reference/13-spectral-analysis/index.md |

**10.9 System identification (`09-system-identification.md`, code SI).** Flow as drawn (revised in review round 1, see Deviations): `P2_SI_IN(["Input-output data"])` → `P2_SI_EXPERIMENT_DESIGN`; `P2_SI_EXPERIMENT_DESIGN` → `P2_SI_MODEL_STRUCTURE`; `P2_SI_MODEL_STRUCTURE` → `P2_SI_STRUCTURE_Q{"Structure?"}`; `P2_SI_STRUCTURE_Q` →|"Polynomial"| `P6_ARX_ARMAX` (ref); `P2_SI_STRUCTURE_Q` →|"State space"| `P6_SUBSPACE` (ref); `P2_SI_STRUCTURE_Q` →|"Block-oriented"| `P6_HAMMERSTEIN_WIENER` (ref); `P6_ARX_ARMAX` & `P6_SUBSPACE` & `P6_HAMMERSTEIN_WIENER` → `P2_SI_ORDER_SELECTION`; `P2_SI_ORDER_SELECTION` → `P8` (ref); `P8` → `P2_SI_TRANSFER_FUNCTION`; `P2_SI_TRANSFER_FUNCTION` → `P2_SI_STABILITY`; `P2_SI_STABILITY` → `P2_SI_VALIDATION`; `P2_SI_VALIDATION` → `P11` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P2_SI_EXPERIMENT_DESIGN | Input design and persistent excitation | | [33] | reference/33-system-identification/index.md |
| P2_SI_MODEL_STRUCTURE | Choose the model structure | polynomial ARX, ARMAX and Box-Jenkins, state space, block-oriented | [33] | reference/33-system-identification/index.md |
| P2_SI_ORDER_SELECTION | Order selection | Hankel singular values | [33] | reference/33-system-identification/index.md |
| P2_SI_TRANSFER_FUNCTION | Estimate the frequency response | empirical transfer-function estimate | [33] | reference/33-system-identification/index.md |
| P2_SI_STABILITY | Poles, zeros and stability | | [33] | reference/33-system-identification/index.md |
| P2_SI_VALIDATION | Validate on held-out input-output data | | [33] | reference/33-system-identification/index.md |

**10.10 Simulation and scenario generation (`10-simulation.md`, code SM).** Flow as drawn (revised in review round 1, see Deviations): `P2_SM_IN(["Simulation question"])` → `P2_SM_SOURCE{"Generator?"}`; `P2_SM_SOURCE` →|"Fitted model"| `P9` (ref); `P2_SM_SOURCE` →|"Resampling"| `P2_SM_BOOTSTRAP_PATHS`; `P2_SM_SOURCE` →|"Learned"| `P2_SM_SYNTHETIC`; `P9` → `P2_SM_MONTE_CARLO`; `P2_SM_MONTE_CARLO` & `P2_SM_BOOTSTRAP_PATHS` & `P2_SM_SYNTHETIC` → `P2_SM_DISTRIBUTION_MATCH`; `P9_BOOTSTRAP` (ref) -.- `P2_SM_BOOTSTRAP_PATHS`; `P6_GENERATIVE` (ref) -.- `P2_SM_SYNTHETIC`; `P2_SM_DISTRIBUTION_MATCH` → `P10_SCENARIOS` (ref); `P10_SCENARIOS` → `P10_RISK_MEASURES` (ref); `P10_RISK_MEASURES` → `P11` (ref).

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

**11.1 Time domain (TD).** Flow as drawn (revised in review round 1, see Deviations): `P5_TD_IN(["Transformed series from P4"])` → `P5_TD_PREDICT{"Predict next values?"}`; `P5_TD_PREDICT` →|"Yes"| `P5_TD_AUTOCOVARIANCE`; `P5_TD_PREDICT` →|"No"| `P5_TD_CAUSAL{"Causal question?"}`; `P5_TD_CAUSAL` →|"Yes"| `P5_TD_AUTOCOVARIANCE`; `P5_TD_CAUSAL` →|"No"| `P5_TD_SEQUENTIAL{"Sequential dependence matters?"}`; `P5_TD_SEQUENTIAL` →|"Yes"| `P5_TD_AUTOCOVARIANCE`; `P5_TD_SEQUENTIAL` →|"No"| `P5` (ref); `P5_TD_AUTOCOVARIANCE` → `P5_TD_LAG_STRUCTURE`; `P5_TD_LAG_STRUCTURE` → `P6_AR_MA_ARMA` (ref); `P5_TD_LAG_STRUCTURE` → `P6_ARIMA_SARIMA` (ref); `P5_TD_LAG_STRUCTURE` → `P6_VAR` (ref); `P5_TD_LAG_STRUCTURE` → `P6_THRESHOLD` (ref); `P6_AR_MA_ARMA` & `P6_ARIMA_SARIMA` & `P6_VAR` & `P6_THRESHOLD` → `P6` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_TD_AUTOCOVARIANCE | Autocovariance and the ACF as the time-domain object | | [2] | reference/02-fundamentals/index.md |
| P5_TD_LAG_STRUCTURE | Lag structure and memory | | [2, 3] | reference/02-fundamentals/index.md |

**11.2 Frequency domain (FD).** Flow as drawn (revised in review round 1, see Deviations): Part 1: when to choose it, and spectral estimation: `P5_FD_IN(["Transformed series from P4"])` → `P5_FD_PERIODIC{"Periodic patterns?"}`; `P5_FD_PERIODIC` →|"Yes"| `P5_FD_DFT`; `P5_FD_PERIODIC` →|"No"| `P5_FD_BANDS{"Separate frequency bands?"}`; `P5_FD_BANDS` →|"Yes"| `P5_FD_DFT`; `P5_FD_BANDS` →|"No"| `P5_FD_SPECTRAL{"Spectral content is the question?"}`; `P5_FD_SPECTRAL` →|"Yes"| `P5_FD_DFT`; `P5_FD_SPECTRAL` →|"No"| `P5` (ref); `P5_FD_DFT` → `P5_FD_LEAKAGE`; `P5_FD_LEAKAGE` → `P5_FD_TASK{"Task?"}`; `P5_FD_TASK` →|"Spectrum"| `P5_FD_ESTIMATOR{"Estimator?"}`; `P5_FD_TASK` →|"Filter or vibration"| `P5_FD_TO_PART_2(["Continue in part 2"])`; `P5_FD_ESTIMATOR` →|"Averaging"| `P5_FD_SMOOTHED`; `P5_FD_ESTIMATOR` →|"Tapers"| `P5_FD_MULTITAPER`; `P5_FD_ESTIMATOR` →|"Model-based"| `P5_FD_PARAMETRIC`; `P5_FD_ESTIMATOR` →|"Irregular grid"| `P5_FD_LOMB_SCARGLE`; `P5_FD_SMOOTHED` & `P5_FD_MULTITAPER` & `P5_FD_PARAMETRIC` & `P5_FD_LOMB_SCARGLE` → `P2_SP_SPECTRAL_SHAPE` (ref); `P2_SP_SPECTRAL_SHAPE` → `P2_SP_HARMONIC_REGRESSION` (ref); `P2_SP_SPECTRAL_SHAPE` → `P6_ARFIMA` (ref); `P2_SP_SPECTRAL_SHAPE` & `P2_SP_HARMONIC_REGRESSION` & `P6_ARFIMA` → `P6` (ref). Part 2: filters and vibration analysis: `P5_FD_PART_2_IN(["From part 1"])` → `P5_FD_TASK_2{"Task?"}`; `P5_FD_TASK_2` →|"Filter"| `P5_FD_FILTERS`; `P5_FD_TASK_2` →|"Vibration"| `P5_FD_ENVELOPE`; `P5_FD_FILTERS` & `P5_FD_ENVELOPE` → `P6` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_FD_DFT | Discrete Fourier transform and the periodogram | | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_SMOOTHED | Smoothed spectral estimates | Welch, Bartlett | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_MULTITAPER | Multitaper spectral estimation | | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_PARAMETRIC | Parametric spectra | AR and ARMA spectral estimates | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_LOMB_SCARGLE | Lomb-Scargle periodogram | irregular sampling | [13, 15] | reference/13-spectral-analysis/index.md |
| P5_FD_LEAKAGE | Leakage, tapering and the Nyquist frequency | | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_FILTERS | FIR and IIR filter design | low-pass, high-pass, band-pass, notch; zero-phase | [13] | reference/13-spectral-analysis/index.md |
| P5_FD_ENVELOPE | Machine-vibration analysis | envelope analysis, cepstrum, order tracking, spectral kurtosis | [26, 13] | reference/26-applied-domains/index.md |

**11.3 Time-frequency (TF).** Flow as drawn (revised in review round 1, see Deviations): Part 1: when to choose it, and Fourier and wavelet transforms: `P5_TF_IN(["Transformed series from P4"])` → `P5_TF_CHANGING{"Frequency content changes over time?"}`; `P5_TF_CHANGING` →|"Yes"| `P5_TF_TRANSFORM{"Transform?"}`; `P5_TF_CHANGING` →|"No"| `P5_TF_TRANSIENTS{"Transients or bursts?"}`; `P5_TF_TRANSIENTS` →|"Yes"| `P5_TF_TRANSFORM`; `P5_TF_TRANSIENTS` →|"No"| `P5_TF_LOCALISATION{"Need both localisations?"}`; `P5_TF_LOCALISATION` →|"Yes"| `P5_TF_TRANSFORM`; `P5_TF_LOCALISATION` →|"No"| `P5` (ref); `P5_TF_TRANSFORM` →|"Fixed window"| `P5_TF_STFT`; `P5_TF_TRANSFORM` →|"Continuous wavelet"| `P5_TF_CWT`; `P5_TF_TRANSFORM` →|"Discrete wavelet"| `P5_TF_DWT`; `P5_TF_TRANSFORM` →|"Adaptive modes"| `P5_TF_TO_PART_2(["Continue in part 2"])`; `P5_TF_CWT` → `P5_TF_SYNCHROSQUEEZING`; `P5_TF_STFT` & `P5_TF_SYNCHROSQUEEZING` → `P2_FE_TF_FEATURES` (ref); `P5_TF_DWT` → `P2_SE_WAVELET_DENOISING` (ref); `P2_FE_TF_FEATURES` & `P2_SE_WAVELET_DENOISING` → `P6` (ref). Part 2: adaptive mode decompositions: `P5_TF_PART_2_IN(["From part 1: adaptive modes"])` → `P5_TF_ADAPTIVE{"Decomposition?"}`; `P5_TF_ADAPTIVE` →|"Empirical"| `P5_TF_EMD`; `P5_TF_ADAPTIVE` →|"Variational"| `P5_TF_VMD`; `P5_TF_EMD` & `P5_TF_VMD` → `P2_FE_TF_FEATURES` (ref); `P2_FE_TF_FEATURES` → `P6` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_TF_STFT | Short-time Fourier transform and the spectrogram | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_CWT | Continuous wavelet transform and the scalogram | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_DWT | Discrete and maximal-overlap wavelet transforms | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_SYNCHROSQUEEZING | Reassignment and synchrosqueezing | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_EMD | Empirical mode decomposition and the Hilbert-Huang transform | | [13] | reference/13-spectral-analysis/index.md |
| P5_TF_VMD | Variational mode decomposition | | [13] | reference/13-spectral-analysis/index.md |

**11.4 State space (SS).** Flow as drawn (revised in review round 1, see Deviations): `P5_SS_IN(["Transformed series from P4"])` → `P5_SS_LATENT_STATES{"Latent states?"}`; `P5_SS_LATENT_STATES` →|"Yes"| `P5_SS_DYNAMICS{"Dynamics?"}`; `P5_SS_LATENT_STATES` →|"No"| `P5_SS_IRREGULAR{"Irregular sampling or gaps?"}`; `P5_SS_IRREGULAR` →|"Yes"| `P5_SS_DYNAMICS`; `P5_SS_IRREGULAR` →|"No"| `P5_SS_ONLINE{"Online updating needed?"}`; `P5_SS_ONLINE` →|"Yes"| `P5_SS_DYNAMICS`; `P5_SS_ONLINE` →|"No"| `P5` (ref); `P5_SS_DYNAMICS` →|"Linear Gaussian"| `P5_SS_FORM`; `P5_SS_DYNAMICS` →|"Nonlinear"| `P5_SS_TAKENS`; `P5_SS_DYNAMICS` →|"Koopman"| `P5_SS_DMD`; `P5_SS_FORM` → `P5_SS_LATENT`; `P5_SS_LATENT` → `P8_KALMAN` (ref); `P8_KALMAN` → `P8_NONLINEAR_FILTERS` (ref); `P8_NONLINEAR_FILTERS` → `P8_PARTICLE_FILTERS` (ref); `P8_PARTICLE_FILTERS` → `P6_STRUCTURAL_TS` (ref); `P8_PARTICLE_FILTERS` → `P6_DLM` (ref); `P8_PARTICLE_FILTERS` → `P6_BSTS` (ref); `B3` (ref) -.- `P5_SS_LATENT`; `P6_STRUCTURAL_TS` & `P6_DLM` & `P6_BSTS` & `P5_SS_TAKENS` & `P5_SS_DMD` → `P6` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_SS_FORM | State-space form and the ARIMA rewriting | | [11] | reference/11-state-space/index.md |
| P5_SS_LATENT | Latent states and missing observations |  | [11] | reference/11-state-space/index.md |
| P5_SS_TAKENS | Takens embedding and phase-space reconstruction | | [33, 8] | reference/33-system-identification/index.md |
| P5_SS_DMD | Dynamic mode decomposition and Koopman operators | | [33] | reference/33-system-identification/index.md |

**11.5 Functional (FN).** Flow as drawn (revised in review round 1, see Deviations): `P5_FN_IN(["Transformed series from P4"])` → `P5_FN_CURVES{"Observations are curves?"}`; `P5_FN_CURVES` →|"Yes"| `P5_FN_BASIS`; `P5_FN_CURVES` →|"No"| `P5_FN_SHAPE{"Shape or derivatives matter?"}`; `P5_FN_SHAPE` →|"Yes"| `P5_FN_BASIS`; `P5_FN_SHAPE` →|"No"| `P5_FN_DENSE{"Dense sampling per curve?"}`; `P5_FN_DENSE` →|"Yes"| `P5_FN_BASIS`; `P5_FN_DENSE` →|"No"| `P5` (ref); `P5_FN_BASIS` → `P5_FN_FPCA`; `P5_FN_FPCA` → `P5_FN_REGRESSION`; `B4` (ref) -.- `P5_FN_BASIS`; `P5_FN_REGRESSION` → `P6_GAUSSIAN_PROCESS` (ref); `P6_GAUSSIAN_PROCESS` → `P6` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_FN_BASIS | Basis representation and smoothing of curves | | [14] | reference/14-functional-high-frequency/index.md |
| P5_FN_FPCA | Functional principal components | | [14] | reference/14-functional-high-frequency/index.md |
| P5_FN_REGRESSION | Functional regression and functional autoregression | | [14] | reference/14-functional-high-frequency/index.md |

**11.6 Hilbert and phase (HP).** Flow as drawn (revised in review round 1, see Deviations): `P5_HP_IN(["Transformed series from P4"])` → `P5_HP_INSTANTANEOUS{"Instantaneous frequency?"}`; `P5_HP_INSTANTANEOUS` →|"Yes"| `P5_HP_ANALYTIC_SIGNAL`; `P5_HP_INSTANTANEOUS` →|"No"| `P5_HP_AMPLITUDE{"Amplitude envelope?"}`; `P5_HP_AMPLITUDE` →|"Yes"| `P5_HP_ANALYTIC_SIGNAL`; `P5_HP_AMPLITUDE` →|"No"| `P5_HP_PHASE_RELATIONS{"Phase relations between signals?"}`; `P5_HP_PHASE_RELATIONS` →|"Yes"| `P5_HP_ANALYTIC_SIGNAL`; `P5_HP_PHASE_RELATIONS` →|"No"| `P5` (ref); `P5_HP_ANALYTIC_SIGNAL` → `P5_HP_PHASE_SYNC`; `P5_HP_PHASE_SYNC` → `P5_TF_EMD` (ref); `P5_HP_PHASE_SYNC` → `P2_FE_NONLINEAR_FEATURES` (ref); `P5_TF_EMD` & `P2_FE_NONLINEAR_FEATURES` → `P6` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| P5_HP_ANALYTIC_SIGNAL | Analytic signal and instantaneous frequency | | [13] | reference/13-spectral-analysis/index.md |
| P5_HP_PHASE_SYNC | Phase synchronisation and the phase-locking value | | [13, 33] | reference/13-spectral-analysis/index.md |

- [ ] **Steps:** replace each pending note, 25 rows `phase: P5`, scaffold, audit, build. Delete the bold "Topics carried over" lead-in and list on `p05-representation/index.md`. Commit `feat(flowchart): six representation sub-charts`.

---

### Task 12: Branch sub-diagrams B1 to B7

**Files:** `docs/reference/16-count-categorical/index.md` (B1), `17-point-processes/index.md` (B2), `15-continuous-time/index.md` (B3), `14-functional-high-frequency/index.md` (B4), `20-spatio-temporal/index.md` (B5), `32-panel-time-series/index.md` (B6), `docs/01-workflow/p01-data-type-gate.md` (B7), inventory. Owner pages: the pages that already define `B1` … `B7`. Each branch diagram replaces the one-node stub under `## Branch sub-diagram` (B7: a new diagram under the existing `B7 Many similar series` leaf section on the P1 page). Structure (spec §5.2): entry box `Bn["Bn …"]` (already defined, keep it) → compressed diagnose → transform → model class → error process → `ref` to the rejoin phase. Sections: the same landing page unless listed.

**B1 (counts and categorical, phase B1):** Flow as drawn (revised in review round 1, see Deviations): `B1` → `B1_COUNT_EDA`; `B1_COUNT_EDA` → `B1_VALUE{"Value type?"}`; `B1_VALUE` →|"Counts"| `B1_COUNT_FAMILY{"Count model family?"}`; `B1_VALUE` →|"Categorical"| `B1_MARKOV_CHAIN`; `B1_VALUE` →|"Compositional"| `B1_COMPOSITIONAL`; `B1_COUNT_FAMILY` →|"Thinning"| `B1_INAR`; `B1_COUNT_FAMILY` →|"Conditional intensity"| `B1_POISSON_AR`; `B1_COUNT_FAMILY` →|"GLM with ARMA terms"| `B1_GLARMA`; `B1_MARKOV_CHAIN` → `B1_AR_LOGIT`; `B1_INAR` & `B1_POISSON_AR` & `B1_GLARMA` → `P7_COUNT_TESTS` (ref); `P7_COUNT_TESTS` → `P8` (ref); `B1_AR_LOGIT` & `B1_COMPOSITIONAL` → `P8`; `F_MARKOV` (ref) -.- `B1_MARKOV_CHAIN`.

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

**B2 (event times, phase B2):** Flow as drawn (revised in review round 1, see Deviations): Part 1: event intensity: `B2` → `B2_EVENT_EDA`; `B2_EVENT_EDA` → `B2_QUESTION{"Object of interest?"}`; `B2_QUESTION` →|"Event intensity"| `B2_CLUSTERING{"Self-exciting?"}`; `B2_QUESTION` →|"Durations or time to failure"| `B2_TO_PART_2(["Continue in part 2"])`; `B2_CLUSTERING` →|"No"| `B2_BASELINE{"Intensity?"}`; `B2_CLUSTERING` →|"Yes"| `B2_EXCITATION{"Excitation model?"}`; `B2_BASELINE` →|"Deterministic"| `B2_POISSON`; `B2_BASELINE` →|"Random"| `B2_COX`; `B2_EXCITATION` →|"Parametric kernel"| `B2_HAWKES`; `B2_EXCITATION` →|"Marks or several streams"| `B2_MARKED`; `B2_EXCITATION` →|"Learned intensity"| `B2_NEURAL_PP`; `B2_POISSON` & `B2_COX` & `B2_HAWKES` & `B2_MARKED` & `B2_NEURAL_PP` → `P7_RESCALING` (ref); `P7_RESCALING` → `P8` (ref). Part 2: durations and time to failure: `B2_PART_2_IN(["From part 1"])` → `B2_QUESTION_2{"Object of interest?"}`; `B2_QUESTION_2` →|"Durations"| `B2_ACD`; `B2_QUESTION_2` →|"Time to failure"| `B2_FAILURE{"Data?"}`; `B2_FAILURE` →|"Failure times"| `B2_SURVIVAL`; `B2_FAILURE` →|"Degradation signal"| `B2_DEGRADATION`; `B2_ACD` & `B2_SURVIVAL` & `B2_DEGRADATION` → `P7_RESCALING` (ref); `P7_RESCALING` → `P8` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| B2_EVENT_EDA | Event-time diagnostics | intensity, inter-event distributions | [17] | reference/17-point-processes/index.md |
| B2_POISSON | Poisson and renewal processes |  | [17] | reference/17-point-processes/index.md |
| B2_COX | Doubly stochastic (Cox) processes |  | [17] | reference/17-point-processes/index.md |
| B2_HAWKES | Hawkes self-exciting processes |  | [17] | reference/17-point-processes/index.md |
| B2_MARKED | Marked and multivariate point processes |  | [17] | reference/17-point-processes/index.md |
| B2_NEURAL_PP | Neural point processes |  | [17, 18] | reference/17-point-processes/index.md |
| B2_ACD | Autoregressive conditional duration | | [14] | reference/14-functional-high-frequency/index.md |
| B2_SURVIVAL | Survival and hazard models | Cox proportional hazards | [17, 26] | reference/17-point-processes/index.md |
| B2_DEGRADATION | Degradation processes and remaining useful life | Wiener and gamma processes | [26, 15] | reference/26-applied-domains/index.md |

**B3 (irregular sampling and continuous time, phase B3):** Flow as drawn (revised in review round 1, see Deviations): `B3` → `B3_ROUTE{"Route?"}`; `B3_ROUTE` -.->|"Resample"| `P0_RESAMPLE` (ref); `B3_ROUTE` →|"Keep the grid"| `B3_IRREGULAR_KALMAN`; `B3_ROUTE` →|"Continuous time"| `B3_OU`; `B3_IRREGULAR_KALMAN` → `P5_FD_LOMB_SCARGLE` (ref); `P5_FD_LOMB_SCARGLE` → `P5` (ref); `B3_OU` → `B3_CARMA`; `B3_CARMA` → `B3_SDE`; `B3_SDE` → `B3_JUMPS{"Jumps?"}`; `B3_JUMPS` →|"Yes"| `P7_JUMPS` (ref); `B3_JUMPS` →|"No"| `B3_SDE_INFERENCE`; `P7_JUMPS` → `B3_SDE_INFERENCE`; `B3_SDE_INFERENCE` → `P8` (ref).

| ID | label | second line | areas |
|---|---|---|---|
| B3_IRREGULAR_KALMAN | Kalman filtering on an irregular grid | | [11, 15] |
| B3_OU | Ornstein-Uhlenbeck process and exact discretisation | | [15] |
| B3_CARMA | CARMA processes | | [15] |
| B3_FBM | Fractional Brownian motion |  | [15, 7] |
| B3_SDE | Diffusions and SDE discretisation | Euler-Maruyama, Milstein | [15] |
| B3_SDE_INFERENCE | Likelihood inference for diffusions | signature methods | [15] |

**B4 (functional, phase B4):** Flow as drawn (revised in review round 1, see Deviations): `B4` → `B4_CURVES`; `B4_CURVES` → `B4_INTRADAY`; `B4_INTRADAY` → `P5_FN_BASIS` (ref); `P5_FN_BASIS` → `P5` (ref).

| ID | label | second line | areas |
|---|---|---|---|
| B4_CURVES | Series as curves | when functional data analysis applies | [14] |
| B4_INTRADAY | Intraday seasonality and curve alignment | ultra-high-frequency data | [14] |

**B5 (spatial and network, phase B5):** Flow as drawn (revised in review round 1, see Deviations): `B5` → `B5_SPATIAL_AUTOCORRELATION`; `B5_SPATIAL_AUTOCORRELATION` → `B5_INDEX{"Index?"}`; `B5_INDEX` →|"Regions or panels"| `B5_SPATIAL_PANEL_VAR`; `B5_INDEX` →|"Continuous space"| `B5_KRIGING`; `B5_INDEX` →|"Graph"| `B5_GRAPH_SIGNAL`; `B5_INDEX` →|"Events in space"| `B5_ST_POINT_PROCESS`; `B5_GRAPH_SIGNAL` → `B5_STGNN`; `B5_STGNN` → `B5_NETWORK_AR`; `B5_SPATIAL_PANEL_VAR` & `B5_KRIGING` & `B5_NETWORK_AR` & `B5_ST_POINT_PROCESS` → `P8` (ref).

| ID | label | second line | areas |
|---|---|---|---|
| B5_SPATIAL_AUTOCORRELATION | Spatial autocorrelation | Moran's I | [20] |
| B5_SPATIAL_PANEL_VAR | Spatial panel VAR and spatial error and lag models | | [20] |
| B5_KRIGING | Spatio-temporal kriging and Gaussian processes | | [20] |
| B5_GRAPH_SIGNAL | Graph signal processing | | [20] |
| B5_STGNN | Spatio-temporal graph neural networks | | [20, 18] |
| B5_NETWORK_AR | Network autoregression | | [20] |
| B5_ST_POINT_PROCESS | Spatio-temporal point processes | | [20, 17] |

**B6 (wide panel, phase B6):** Flow as drawn (revised in review round 1, see Deviations): `B6` → `B6_PANEL_UNIT_ROOT`; `B6_PANEL_UNIT_ROOT` → `B6_DYNAMIC{"Lagged dependent variable?"}`; `B6_DYNAMIC` →|"No"| `B6_STATIC_PANEL`; `B6_DYNAMIC` →|"Yes"| `B6_DYNAMIC_PANEL`; `B6_STATIC_PANEL` & `B6_DYNAMIC_PANEL` → `B6_HETERO{"Heterogeneous slopes?"}`; `B6_HETERO` →|"Yes"| `B6_HETEROGENEOUS`; `B6_HETERO` →|"No"| `B6_CROSS_SECTION_DEPENDENCE`; `B6_HETEROGENEOUS` → `B6_CROSS_SECTION_DEPENDENCE`; `B6_CROSS_SECTION_DEPENDENCE` → `P8` (ref); `B6_CROSS_SECTION_DEPENDENCE` → `P10` (ref).

| ID | label | second line | areas |
|---|---|---|---|
| B6_PANEL_UNIT_ROOT | Panel unit-root and cointegration tests | | [32, 28] |
| B6_STATIC_PANEL | Fixed and random effects | | [32] |
| B6_DYNAMIC_PANEL | Dynamic panel GMM | Arellano-Bond | [32, 4] |
| B6_HETEROGENEOUS | Heterogeneous panels | mean group, pooled mean group | [32] |
| B6_CROSS_SECTION_DEPENDENCE | Cross-sectional dependence | CD test, common correlated effects | [32] |

**B7 (many similar series, phase B7, drawn on `p01-data-type-gate.md` as a second diagram under the `B7 Many similar series` heading; sections in reference pages):** Flow as drawn (revised in review round 1, see Deviations): `B7` (ref) → `B7_GLOBAL_VS_LOCAL`; `B7_GLOBAL_VS_LOCAL` → `B7_STRATEGY{"Strategy?"}`; `B7_STRATEGY` →|"Global"| `P1_GLOBAL_FLAG["Set flag: global model"]`; `B7_STRATEGY` →|"Cluster first"| `B7_CLUSTER_FLAG["Set flag: cluster then local"]`; `B7_STRATEGY` →|"Hierarchy"| `B7_HIERARCHY_FLAG["Set flag: hierarchy"]`; `P1_GLOBAL_FLAG` → `P6_GLOBAL_MODELS` (ref); `P6_GLOBAL_MODELS` → `P6_FOUNDATION_MODELS` (ref); `B7_CLUSTER_FLAG` → `B7_CLUSTER_THEN_LOCAL`; `B7_HIERARCHY_FLAG` → `B7_HIERARCHY`; `B7_HIERARCHY` → `P10_RECONCILIATION` (ref); `P6_FOUNDATION_MODELS` & `B7_CLUSTER_THEN_LOCAL` & `P10_RECONCILIATION` → `P2` (ref).

| ID | label | second line | areas | section file |
|---|---|---|---|---|
| B7_GLOBAL_VS_LOCAL | Pooling strategies for many series | global, cluster then local, hierarchical | [22, 18] | reference/22-forecasting-practice/index.md |
| B7_HIERARCHY | Detect hierarchical and grouped structure | | [22] | reference/22-forecasting-practice/index.md |
| B7_CLUSTER_THEN_LOCAL | Cluster series, then fit local models | | [19, 22] | reference/19-classification-anomaly/index.md |

Note on B7 rows: phase `B7`. The audit makes the page that defines the `B7` entry (the P1 page) the owner of phase B7, so `B7_*` leaves drawn there pass the owner and owner-prefix checks with no audit change; the ids keep the `B7_` prefix.

- [ ] **Steps:** one commit per branch or one for all seven: replace each stub, add rows (`phase` = B1…B7), the `F_MARKOV` row, scaffold, audit, build. Commit `feat(flowchart): branch sub-diagrams B1 to B7`.

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

## Deviations (recorded 2026-10-07)

The diagrams on the pages are authoritative; the flow paragraphs above were regenerated from them after review round 1, and the leaf tables carry the round-1 leaf edits.

### During implementation

- **Coverage test.** Master phase boxes do not count (they are not in a sub-diagram); area 1 is satisfied by foundation rows and areas 2 to 34 by leaves. The test reads the inventory through the audit's loader.
- **Second-line clipping** was a CSS line-height mismatch between Mermaid's measuring context and `.md-typeset`, fixed in `docs/stylesheets/extra.css`; splitting P7 did not fix it.
- **Width rule** (DESIGN-SYSTEM.md, "Width"): a diagram below scale 0.45 at a 1280 px viewport becomes stacked parts, and a diamond with more than six outcomes becomes a two-level choice. Applied: P7 in three parts (not two; the seven-way variance diamond is GARCH family / latent / realised plus a GARCH-variant diamond); P6, P8, P9, P10, P11, the P2 selector, purpose 7, the frequency-domain and time-frequency representations and B2 in stacked parts; the P6 machine-learning, purpose 7 feature-family and P2 purpose diamonds as two-level choices.
- **Split parts end at the next phase's ref box** (`P7`, `P11`) instead of `P6_OUT` / `P10_OUT`, because a terminator id can be defined only once across diagrams.
- **B7 rows carry phase `B7`**, not `P1`; the audit already makes the P1 page the owner of phase B7, so no audit change was needed.
- **Purposes 3 and 8** were committed with the representation sub-charts, because their charts and the frequency-domain and time-frequency charts reference each other's leaves.
- **Representation "choose when" questions are disjunctive**: any Yes leads to the leaves, the third No returns to the P5 selector.
- `F_MARKOV` has `areas: [1]`.

### Review round 1

- **Decision logic and flags.** P8's linear branch has a No edge to the likelihood questions. The P2 selector asks "Question about?" (the future, causes, structure, events, other outputs) and sets a purpose flag; P10 and P11 dispatch on that flag over all ten purposes; risk measures and interpretability are reached from forecasting through their own diamonds. P3 sets each flag only on the positive verdict of its test (variance, deterministic trend, difference, seasonal difference or adjustment, multiple seasonality, breaks, long memory), and P4's diamonds read those flags by name. The global flag is set in B7 on the Global edge, beside cluster and hierarchy flags. P0 asks one "Resample now?" diamond after de-duplication (one diamond instead of the two proposed, since de-duplication is shared by both sampling answers), so irregular series reach P1 and B3. P9 re-runs P7's tests as refs, each with a verdict that loops to P6 (mean) or P7 (innovations). Retraining policy precedes drift detection in P11.
- **Purpose charts route through the spine** and end at the P11 phase box. The causal chart sends experiments straight to counterfactual designs and runs the observational path through P3, P4, the P3 cointegration pre-check (so the VAR or VECM choice follows a test, in spine order), P6 to P9 and the P10 causal questions. P10 and P11 sections on the purpose pages are links to the leaves the charts reference; emphasised phases are the phases whose leaves a chart references.
- **Alternatives are fan-outs** (P6 exogenous forms, smoothing, latent models, input-output structures; P8 moment estimators; P10 causal questions; representation estimators and transforms; B1 count families; B2 intensity, excitation and failure models). P6 is in ten parts with yes/no flag diamonds, BVAR under many-variable shrinkage and TVP-VAR under VAR.
- **Part entries** that carried a decision's answers are followed by a diamond restating the question; single-answer entries name the answer in their label.
- **One method, one leaf.** Deleted (a ref to the surviving leaf replaces them where a chart needs the step): `B3_JUMP_LEVY` (ref `P7_JUMPS`), `B1_NEGATIVE_BINOMIAL`, `P9_RESIDUAL_AUTOCORRELATION`, `P9_RESIDUAL_ARCH`, `P9_RESIDUAL_NORMALITY`, `P9_COUNT_DIAGNOSTICS` (refs to the P7 tests), `P2_SM_STRESS` (ref `P10_SCENARIOS`), `P2_SE_FILTER_DESIGN` (a filter-type diamond over `P5_FD_FILTERS`), `P2_FC_HORIZON`, `P2_DC_PERIOD` (ref `P3_SEASONALITY`), `P2_AN_REGIME` (ref `P6_MARKOV_SWITCHING`), `P11_BACKTESTING` (merged into `P11_ROLLING_ORIGIN`), `P2_AN_TYPE`, `P2_FE_TASK`, `B3_CHOICE` (their diamonds remain). Relabelled: `P7_INGARCH` "Count innovations: Poisson or negative binomial", `B1_POISSON_AR` "Poisson and negative-binomial autoregression", `P2_SE_SNR`, `P2_SM_BOOTSTRAP_PATHS`, `P6_ARX_ARMAX`, `P2_SI_TRANSFER_FUNCTION`, `P5_SS_LATENT`, `P3_PLOT`, `P11_ROLLING_ORIGIN`, `P6_FAVAR` "FAVAR and GVAR", `B2_COX` "Doubly stochastic (Cox) processes". Added: `P8_QUANTILE_REGRESSION`. Moved: `B2_SURVIVAL` to `reference/17-point-processes/index.md`. `P7_ARFIMA_ERRORS` and `P6_ARFIMA` both stay (the error-model versus mean-model split, as for ARMA).
- **Counts after round 1:** 343 inventory rows; 271 added by this plan (262 leaves and 9 foundation rows): P0 13, P2 52, P3 17, P4 13, P5 25, P6 46, P8 22, P9 6, P10 20, P11 10, B1 7, B2 9, B3 5, B4 2, B5 7, B6 5, B7 3.
- **Rendering gate:** `tests/e2e/test_site_smoke.py::test_every_diagram_renders_readably` renders every page with an audited diagram and asserts no Mermaid error, no console error, no clipped label and the width rule.
