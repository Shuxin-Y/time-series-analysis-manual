"""Acceptance routes of the purpose-first spine (design spec section 8) and the flag contract (section 3), walked on
the charts as the Markdown sources draw them."""
import pytest

import audit_flowcharts as audit
import sitekit
from spine_graph import SPINE, Graph

PURPOSE_INDEX = [r"01-workflow/p00-purpose/index\.md$"]
SIGNAL_EXTRACTION = [r"01-workflow/p00-purpose/03-signal-extraction\.md$"]
P4_PAGE = [r"01-workflow/p04-transformations\.md$"]
P11_PAGE = [r"01-workflow/p11-inference\.md$"]
COUNTS = SPINE + [r"reference/16-count-categorical/index\.md$"]


@pytest.fixture(scope="module")
def g() -> Graph:
    return Graph.from_site(audit.Site(audit.load_site_config(sitekit.REPO / "mkdocs.yml"), sitekit.REPO / "docs"))


def test_purpose_5_keeps_the_anomalies_through_p1_and_p4(g):
    assert g.ordered(["P0_KEEP_ANOMALIES_FLAG", "P1_SCREEN", "P4_OUTLIERS"], pages=SPINE)
    assert g.label_has("P1_SCREEN", "mark candidate outliers")
    assert g.edge("P4_OUTLIERS", "P4_TO_PART_2", "Kept as the target")
    # Robust prefiltering replaces values; no spine route reaches it around the purpose-aware gate.
    assert not g.reach("P1_IN", "P4_ROBUST_PREFILTER", pages=SPINE, avoid={"P4_OUTLIER_GATE"})


def test_purpose_8_reaches_the_periodogram_with_its_periodic_content(g):
    assert g.edge("P4_KEEP_LEVELS", "P4_TO_PART_5", "frequencies")
    assert g.reach("P4_TO_PART_5", "P5_FD_DFT", pages=SPINE)
    for step in ("P4_SEASONAL_DIFFERENCE", "P4_SEASONAL_ADJUSTMENT", "P4_DIFFERENCE"):
        assert not g.reach("P4_TO_PART_5", step, pages=P4_PAGE), step


def test_purpose_6_decomposes_levels(g):
    assert not g.reach("P4_IN", "P4_DIFFERENCE", pages=P4_PAGE, avoid={"P4_DECOMP"})
    assert g.reach("P4_DECOMP", "P4_FILTER_DECOMPOSITION", pages=P4_PAGE)
    assert g.edge("P4_KEEP_LEVELS", "P4_COMPONENTS_TO_PART_4", "components")
    assert not g.reach("P4_COMPONENTS_TO_PART_4", "P4_DIFFERENCE", pages=P4_PAGE)


def test_purpose_3_in_real_time_reaches_a_causal_filter_or_the_kalman_filter(g):
    assert g.ordered(["P0_IN", "P0_REAL_TIME_FLAG", "P1"], pages=PURPOSE_INDEX)
    assert g.reach("P0_SE_IN", "P5_FD_FILTERS", pages=SIGNAL_EXTRACTION)
    assert g.reach("P0_SE_IN", "P8_KALMAN", pages=SIGNAL_EXTRACTION)
    assert g.label_has("P5_FD_FILTERS", "causal in real time")
    assert g.label_has("P8_KALMAN", "filter in real time, smoother offline")


def test_forecasting_compares_candidates_and_baselines_out_of_sample_before_selection(g):
    assert g.ordered(["P10_IN", "P10_ROLLING_ORIGIN", "P0_FC_BASELINES", "P10_FORECAST_PRODUCT", "P10_POINT_METRICS",
                      "P10_PROBABILISTIC_METRICS", "P10_FORECAST_COMPARISON", "P10_SELECT", "P10_FINAL_HOLDOUT",
                      "P11_POINT_FORECASTS"], pages=SPINE)
    assert not g.reach("P8_IN", "P10_FORECAST_COMPARISON", pages=SPINE, avoid={"P10_ROLLING_ORIGIN"})
    assert g.label_has("P10_FINAL_HOLDOUT", "reserved in P0")


def test_the_forecast_product_is_assembled_from_paths_with_intervals_last(g):
    order = ["P11_POINT_FORECASTS", "P11_BACK_TRANSFORM", "P11_COMBINATION", "P11_JUDGMENTAL", "P11_RECONCILIATION",
             "P11_INTERVALS", "P11_DENSITY_QUANTILE"]
    assert g.ordered(order, pages=P11_PAGE)
    for later, earlier in zip(order[1:], order):
        assert not g.reach(later, earlier, pages=P11_PAGE), (later, earlier)


def test_m5_reader_reaches_a_global_count_learner_count_baselines_and_reconciliation(g):
    assert g.ordered(["P2_VALUE_TYPE", "B1", "P2_STRUCTURE", "B7", "B7_HIERARCHY_FLAG", "B7_GLOBAL_FLAG", "P3",
                      "B1_COUNT_EDA", "B1_POOLING"], pages=COUNTS)
    assert g.edge("B1_POOLING", "P6_GLOBAL_MODELS", "Global")
    assert g.label_has("P6_GLOBAL_MODELS", "count loss")
    assert g.ordered(["P6_GLOBAL_MODELS", "P7_COUNT_TESTS", "P9", "B1_OUT", "P10_IN", "P10_ROLLING_ORIGIN",
                      "P0_FC_BASELINES", "P10_POINT_METRICS", "P11_RECONCILIATION"], pages=COUNTS)
    assert g.label_has("P0_FC_BASELINES", "Croston")
    assert g.label_has("P10_POINT_METRICS", "RMSSE")


def test_probabilistic_forecasts_are_produced_per_origin_and_scored_by_proper_scores(g):
    assert g.ordered(["P10_ROLLING_ORIGIN", "P10_FORECAST_PRODUCT", "P10_PROBABILISTIC_METRICS"], pages=SPINE)
    assert g.label_has("P10_FORECAST_PRODUCT", "intervals and quantiles")
    assert g.label_has("P10_PROBABILISTIC_METRICS", "interval score")


def test_count_reader_with_local_pooling_reaches_the_b1_families_p9_and_p10(g):
    assert g.edge("B1_POOLING", "B1_COUNT_FAMILY", "Local")
    assert g.ordered(["B1_COUNT_FAMILY", "B1_INAR", "P7_COUNT_TESTS", "P9", "B1_OUT", "P10_IN"], pages=COUNTS)


def test_a_failed_in_sample_check_keeps_forecasting_candidates_for_p10(g):
    assert g.ordered(["P9_PART_4_FAIL_IN", "P9_GATE", "P9_OUT", "P10_IN"], pages=SPINE)
    assert any("keep as candidate" in a for a in g.answers("P9_GATE"))


def test_a_purpose_without_a_mean_model_skips_p7_to_p9(g):
    assert g.reach("P6_NO_MODEL", "P10_IN", pages=SPINE, avoid={"P7", "P8", "P9"})


# Flag contract: every flag a chart sets is read later. Each reader is named with the words in its label or answers
# that show the read, so a reader that stops asking breaks the contract here.
FLAG_READERS = {
    "P0_PURPOSE_FLAG": {"P6_NO_MODEL": "Purpose flag?", "P9_GATE": "Purpose flag?", "P10_PURPOSE": "Purpose flag?",
                        "P11_PURPOSE": "Purpose flag?"},
    "P0_REAL_TIME_FLAG": {"P1_MISSING_IMPUTE": "one-sided in real time", "P5_FD_FILTERS": "causal in real time",
                          "P8_KALMAN": "filter in real time"},
    "P0_KEEP_ANOMALIES_FLAG": {"P4_OUTLIERS": "Kept as the target"},
    "P0_KEEP_LEVELS_FLAG": {"P4_OUTLIER_GATE": "Keep-levels flag?", "P4_KEEP_LEVELS": "Keep-levels flag?"},
    "P0_FORECAST_FLAG": {"P0_FC_BASELINES": "Baselines for comparison", "P11_POINT_FORECASTS": "the P0 functional"},
    "P0_DETECTION_FLAG": {"P10_LABELS": "Labels flag?"},
    "P0_SPLIT_FLAG": {"P10_GROUPED_SPLITS": "split unit from P0"},
    "P0_COVARIATE_FLAG": {"P3_MULTI": "Covariates or multivariate flag?", "P6_COVARIATE_Q": "Covariates flag?"},
    "P0_HOLDOUT_FLAG": {"P10_FINAL_HOLDOUT": "reserved in P0"},
    "P1_VALUE_TYPE_FLAG": {nid: "Value-type flag?" for nid in
                           ("P2_VALUE_TYPE", "P3_TYPE", "P4_TYPE", "P6_VALUE_TYPE", "P7_TYPE", "P8_TYPE", "P9_TYPE")},
    "P1_IRREGULAR_FLAG": {"P2_SAMPLING": "Irregular", "P3_SAMPLING": "Irregular, kept", "P4_GRID": "Irregular, kept",
                          "P5_GRID": "Irregular, kept"},
    "P1_RESAMPLED_FLAG": {"P2_SAMPLING": "resampled", "P3_SAMPLING": "resampled", "P4_GRID": "resampled"},
    "P1_CALENDAR_FLAG": {"P6_DETERMINISTIC_Q": "calendar flags?"},
    "P1_DELAY_FLAG": {"P0_FC_EPIDEMIC": "delay-corrected counts of P1"},
    "P1_IMPUTED_FLAG": {"P8_KALMAN": "imputed points treated as missing"},
    "P1_OUTLIER_FLAG": {"P4_OUTLIERS": "Candidate outliers", "P6_INTERVENTION_Q": "candidate-outlier mask"},
    "P2_MIXED_FREQ_FLAG": {"P6_MIXED_Q": "Mixed-frequency flag?", "P11_MIXED": "Mixed-frequency flag?"},
    "P2_MULTIVARIATE_FLAG": {"P3_MULTI": "multivariate flag?", "P7_MULTI": "Multivariate flag?",
                             "P9_MULTI": "Multivariate flag?", "P11_SYSTEM": "Multivariate flag?"},
    "B1_MULTIVARIATE_FLAG": {"P7_MULTI": "Multivariate flag?", "P9_MULTI": "Multivariate flag?"},
    "B3_KEPT_FLAG": {"P3_SAMPLING": "Irregular, kept", "P4_GRID": "Irregular, kept", "P5_GRID": "Irregular, kept"},
    "B6_CD_FLAG": {"B6_ESTIMATOR": "Cross-sectional dependence"},
    "B6_COINT_FLAG": {"B6_ESTIMATOR": "Panel cointegration"},
    "B7_HIERARCHY_FLAG": {"P11_HIERARCHY": "Hierarchy flag?"},
    "B7_GLOBAL_FLAG": {"P4_POOLING": "Global pooling?", "B1_POOLING": "Global", "P6_POOLING": "Global"},
    "B7_COMPARE_FLAG": {"P4_POOLING": "compare local and global", "B1_POOLING": "compare", "P6_POOLING": "Compare"},
    "B7_PARTIAL_FLAG": {"P6_POOLING": "Partial"},
    "B7_CLUSTER_FLAG": {"P6_POOLING": "cluster then local"},
    "P3_VARIANCE_FLAG": {"P4_VARIANCE": "Variance flag?"},
    "P3_ORDER_FLAG": {"P4_INTEGRATION": "Integration flag?", "P4_SPECTRAL_ORDER": "Integration flag?",
                      "P4_LEVELS_ORDER": "Integration flag?"},
    "P3_SEASONAL_FILTER_FLAG": {"P4_INTEGRATION": "Seasonal filter only"},
    "P3_TREND_FLAG": {"P6_DETERMINISTIC_Q": "Trend"},
    "P3_DRIFT_FLAG": {"P6_DETERMINISTIC_Q": "drift"},
    "P3_DET_SEASON_FLAG": {"P6_DETERMINISTIC_Q": "seasonality"},
    "P3_MULTI_SEASON_FLAG": {"P4_SEASON": "Multiple seasonality"},
    "P3_BREAK_FLAG": {"P3_LM_BREAKS": "Break flag set?", "P4_BREAKS": "Break or explosive flag?"},
    "P3_EXPLOSIVE_FLAG": {"P4_BREAKS": "Break or explosive flag?"},
    "P3_NONLINEAR_FLAG": {"P6_DEPENDENCE": "Nonlinear flag"},
    "P3_COINT_FLAG": {"P6_COINTEGRATED": "Rank r of at least 1", "P8_SPECIAL": "Cointegrated system, rank r"},
    "P3_NO_COINT_FLAG": {"P6_COINTEGRATED": "no cointegration"},
    "P3_MIXED_FLAG": {"P6_COINTEGRATED": "Mixed orders"},
    "P4_TREND_FLAG": {"P6_DETERMINISTIC_Q": "Trend"},
    "P4_SEASON_FLAG": {"P6_DETERMINISTIC_Q": "seasonality"},
    "P4_FRACTIONAL_FLAG": {"P6_FD_Q": "Fractional remainder flag?", "P6_LINEAR": "Fractional remainder flag?"},
    "P4_INTERVENTION_FLAG": {"P6_INTERVENTION_Q": "Intervention-terms flag?"},
    "P6_KIND_FLAG": {"P7_KIND": "Model-kind flag?", "P8_KIND_Q": "Model-kind flag?", "P9_KIND": "Model-kind flag?"},
    "P6_PRIOR_FLAG": {"P8_PRIOR_Q": "Prior-specified flag?"},
    "P6_REGRESSION_FLAG": {"P7_MEAN_DEP": "regression flag"},
}
BRANCH_PHASE = 2  # a branch chart's flags are set where P2 hands the reader to it


def test_every_flag_a_chart_sets_has_a_contract(g):
    drawn = {nid for nid, shapes in g.shapes.items() if nid.endswith("_FLAG") and shapes & {"rect"}}
    assert drawn == set(FLAG_READERS)


@pytest.mark.parametrize("flag", sorted(FLAG_READERS))
def test_each_flag_is_read_after_it_is_set(g, flag):
    set_at = min(g.spine_phases(flag), default=BRANCH_PHASE)
    for reader, words in FLAG_READERS[flag].items():
        assert reader in g.appears, f"{flag}: reader {reader} is drawn nowhere"
        assert g.label_has(reader, words) or any(words in a for a in g.answers(reader)), \
            f"{flag}: {reader} no longer shows {words!r}"
        assert g.reach(flag, reader), f"{flag}: no route to {reader}"
        assert max(g.spine_phases(reader), default=BRANCH_PHASE) >= set_at, f"{flag}: {reader} sits before P{set_at}"
