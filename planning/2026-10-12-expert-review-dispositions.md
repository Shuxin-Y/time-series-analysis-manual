# Expert review 2026-10-12: finding dispositions

Every finding of the four reports (econometrics E, forecasting and machine learning F, signal processing and stochastic processes S, theory and pedagogy T) was checked against the source at the branch head. All 175 are fixed; none was judged false. The table names the file that carries the fix and the commit that introduced it. The design-review rounds (identifiers such as fc R1 or sig S3) are folded into `planning/2026-10-12-purpose-first-spine-design.md`, which this branch implements.

| Finding | Summary | Fixed in | Commit |
|---|---|---|---|
| E-1 | (major) No loop from diagnostics back to P3/P4 | `01-workflow/index.md` | 351cbf9 |
| E-2 | (major) Outlier types classified before any model, then all filtered | `01-workflow/p01-data.md` | 9216f60 |
| E-3 | (minor) Timestamp and DST alignment only on the irregular branch | `01-workflow/p01-data.md` | 9216f60 |
| E-4 | (minor) Resampling without stock/flow rules or aggregation effects | `01-workflow/p01-data.md` | 9216f60 |
| E-5 | (minor) Calendar effects are marked but no later diamond reads them | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| E-6 | (minor) Linear-interpolation formula in the glossary is wrong | `glossary/p01-data.yml` | 8c3a0b2 |
| E-7 | (major) B6 runs panel unit-root tests before the cross-sectional dependence test | `reference/32-panel-time-series/index.md` | 313a59c |
| E-8 | (minor) Branches rejoin at P8 without purpose or diagnostics; counts get no trend or seasonality check | `reference/16-count-categorical/index.md` | 313a59c |
| E-9 | (minor) Distribution tests on the raw series | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-10 | (major) "ARCH-LM on levels", with mutually exclusive variance answers | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-11 | (major) Unit-root tests run on the untransformed scale | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-12 | (blocker) Explosive branch: verdict precedes the test, and nothing downstream handles it | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-13 | (major) No answer for conflicting ADF and KPSS results | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-14 | (minor) Deterministic terms of the unit-root test are chosen after the verdict | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-15 | (major) Break tests and unit-root tests are each run under the other's failure mode | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-16 | (minor) No test for a second unit root | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-17 | (minor) Variance-ratio test placed in the unit-root block | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-18 | (major) Seasonal and zero-frequency unit roots decided separately; the combined filter is never checked | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-19 | (major) "No seasonal unit root" maps only to seasonal adjustment | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| E-20 | (major) Long memory with d in (0.5, 1) is undetectable on this route | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-21 | (minor) Spurious long memory from breaks; R/S bias | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-22 | (major) Nonlinearity tests on the raw series, confounded by ARCH | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-23 | (minor) Nonparametric trend tests sit after the trend decision and feed nothing | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-24 | (minor) Cross-correlation and lead-lag without prewhitening | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-25 | (major) Cointegration decided by a "pre-check"; formal rank tests come after estimation; mixed integration orders have no answer | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| E-26 | (blocker) Trend-cycle decomposition is applied to the already differenced or detrended series | `01-workflow/p04-transformations.md` | 9216f60 |
| E-27 | (minor, gap) Variance transforms for series with zeros or negative values | `01-workflow/p04-transformations.md` | 9216f60 |
| E-28 | (major) Exogenous regressors enter after P3/P4 and are never tested or transformed | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-29 | (minor) Integrated families after P4 transforms invite double differencing | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| E-30 | (minor) "Exogenous flag" is an answer to "Family?" | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| E-31 | (nit) DLM second line "Bayesian ARIMA" | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| E-32 | (major) Variance regimes are tested after the GARCH variant and after the distribution | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-33 | (minor) Portmanteau tests under conditional heteroskedasticity | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-34 | (minor) BNS listed as a test on standardised innovations | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-35 | (minor) "Markov-switching LR" as a regime test | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-36 | (minor, gap) Multivariate residual tests | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-37 | (nit) P7 input needs a preliminary fit | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-38 | (nit) Wold statement | `01-workflow/p07-error-process.md` | 8b1c07a |
| E-39 | (major) Bayesian computation is reachable only when the likelihood is intractable | `01-workflow/p08-estimation.md` | 9aaf6fc |
| E-40 | (major) No estimator for a VECM | `01-workflow/p08-estimation.md` | 9aaf6fc |
| E-41 | (minor) Whittle and GMM offered only for intractable likelihoods; no IV route | `01-workflow/p08-estimation.md` | 9aaf6fc |
| E-42 | (minor) OLS/FGLS (Cochrane-Orcutt, Prais-Winsten) for "linear" models contradicts the P7 thesis and fails with a lagged dependent variable | `01-workflow/p08-estimation.md` | 9aaf6fc |
| E-43 | (nit) Burg under "regression on innovations"; EKF/UKF drawn as a step before particle filters | `01-workflow/p08-estimation.md` | 9aaf6fc |
| E-44 | (minor) MLE glossary chain uses the i.i.d. form | `glossary/maximum-likelihood.yml` | 8c3a0b2 |
| E-45 | (blocker) Distribution re-test sends every non-Gaussian model back to P7 | `01-workflow/p09-in-sample-diagnostics.md` | 1739248 |
| E-46 | (minor) ARCH and BDS tests on standardised residuals need corrected versions | `01-workflow/p09-in-sample-diagnostics.md` | 1739248 |
| E-47 | (major, gap) No parameter-stability diagnostics | `01-workflow/p09-in-sample-diagnostics.md` | 1739248 |
| E-48 | (minor, gap) No root and redundancy check of the estimated model | `01-workflow/p09-in-sample-diagnostics.md` | 1739248 |
| E-49 | (minor) Forecast-comparison tests run for every model, before the out-of-sample machinery | `01-workflow/p10-evaluation-selection.md` | 1739248 |
| E-50 | (major) Causal chart: natural experiments skip all time-series modelling | `01-workflow/p00-purpose/02-causal-inference.md` | e419a39 |
| E-51 | (minor) Toda-Yamamoto after P4 differencing | `01-workflow/p11-inference.md` | 83cde51 |
| E-52 | (nit) "Coefficient and restriction tests → HAC inference" order | `01-workflow/p11-inference.md` | e419a39 |
| E-53 | (minor) Change-point chart: segmentation under autocorrelation; break-date intervals; "Multivariate" as an online/offline answer | `01-workflow/p11-inference.md` | 83cde51 |
| E-54 | (minor) ADF, KPSS and differencing definitions | `glossary/p04-transformations.yml` | 8c3a0b2 |
| E-55 | (nit) Dates in glossary history | `glossary/p03-exploratory-diagnostics.yml` | 8c3a0b2 |
| F-1 | blocker — Branch data never reach P2, so P10 and P11 dispatch on an unset purpose flag | `reference/16-count-categorical/index.md` | 313a59c |
| F-2 | blocker — P0 replaces outliers before the purpose is known, removing the anomalies Purpose 5 is meant to find | `01-workflow/p00-purpose/index.md` | f326ddd |
| F-3 | blocker — Model comparison and selection happen before any out-of-sample evidence exists | `01-workflow/p10-evaluation-selection.md` | 1739248 |
| F-4 | major — Baselines come after the candidate models are selected and compared | `01-workflow/p00-purpose/01-forecasting.md` | e419a39 |
| F-5 | major — Horizon, forecast functional and evaluation loss are fixed only after fitting | `01-workflow/p00-purpose/index.md` | f326ddd |
| F-6 | major — The multi-step strategy is chosen after the forecasts and intervals exist | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| F-7 | major — "Future covariates known? Yes" overrides the family choice and sends every case with covariates to ARIMAX | `01-workflow/p00-purpose/01-forecasting.md` | e419a39 |
| F-8 | major — Epidemic nowcasting is applied after the model is fitted and compared | `01-workflow/p01-data.md` | 9216f60 |
| F-9 | major — Reconciliation precedes combination and judgmental adjustment, so the final forecasts can be incoherent | `01-workflow/p11-inference.md` | 83cde51 |
| F-10 | minor — Metric labels mix calibration diagnostics with proper scores and omit the interval score | `01-workflow/p10-evaluation-selection.md` | 1739248 |
| F-11 | nit — Conformal intervals need time-series variants | `01-workflow/p11-inference.md` | 83cde51 |
| F-12 | major — B7 makes global pooling, clustering and hierarchy mutually exclusive | `01-workflow/p02-data-type-gate.md` | 313a59c |
| F-13 | minor — B7 solid edges run ahead of the spine | `01-workflow/p02-data-type-gate.md` | 313a59c |
| F-14 | major — The global route skips the learner choice, and ML families are reachable only on the single-series route | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| F-15 | gap, minor — No leaf for feature construction and scaling in ML and global models | `01-workflow/p04-transformations.md` | 9216f60 |
| F-16 | minor — The exogenous diamond misses two common covariate situations | `01-workflow/p00-purpose/index.md` | f326ddd |
| F-17 | minor — P8 and P9 have no route for likelihood-free ML fits | `01-workflow/p08-estimation.md` | 9aaf6fc |
| F-18 | major — The only response to detected drift is online updating of parameters | `01-workflow/p12-deployment-monitoring.md` | 83cde51 |
| F-19 | major — Point anomalies are scored on the raw series | `01-workflow/p00-purpose/05-anomaly-regime-detection.md` | e419a39 |
| F-20 | major — The labels question covers two of six detectors, and evaluation always assumes labels | `01-workflow/p10-evaluation-selection.md` | 1739248 |
| F-21 | gap, major — No online versus offline decision for anomaly detection | `01-workflow/p00-purpose/05-anomaly-regime-detection.md` | e419a39 |
| F-22 | major — No check for serial dependence before segmentation or sequential detection | `01-workflow/p00-purpose/04-change-point-detection.md` | e419a39 |
| F-23 | minor — "Multivariate" is offered as an answer to "Online or offline?" | `01-workflow/p00-purpose/04-change-point-detection.md` | e419a39 |
| F-24 | minor — Change type is classified after detection, and online thresholds have no calibration step | `01-workflow/p00-purpose/04-change-point-detection.md` | e419a39 |
| F-25 | minor — Change-point metrics cover online detection only | `01-workflow/p10-evaluation-selection.md` | 1739248 |
| F-26 | major — Feature vectors are routed to series-level classifiers, and the raw-series entry is missing | `01-workflow/p00-purpose/07-feature-extraction-classification.md` | e419a39 |
| F-27 | major — Regression on a whole series is routed to forecasting with lag features | `01-workflow/p00-purpose/07-feature-extraction-classification.md` | e419a39 |
| F-28 | major — No leakage-safe split design on the classification route | `01-workflow/p10-evaluation-selection.md` | 1739248 |
| F-29 | minor — Clustering passes through data augmentation and ends at classification metrics | `01-workflow/p00-purpose/07-feature-extraction-classification.md` | e419a39 |
| F-30 | minor — The fitted-model route omits error-process specification and parameter uncertainty | `01-workflow/p00-purpose/10-simulation.md` | e419a39 |
| F-31 | minor — Every simulation use is routed through stress testing and VaR backtests | `01-workflow/p00-purpose/10-simulation.md` | e419a39 |
| F-32 | gap, minor — No purpose for predicting a future event from an ongoing series | `01-workflow/p00-purpose/index.md` | f326ddd |
| S-1 | blocker · `docs/01-workflow/p04-transformations.md:17,24-41`; `docs/01-workflow/p02-purpose/06-decomposition.md:15-21` | `01-workflow/p04-transformations.md` | 9216f60 |
| S-2 | major · `docs/01-workflow/p03-exploratory-diagnostics.md:20-31,44-46`; `docs/01-workflow/p04-transformations.md:24-28` | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| S-3 | major · `docs/01-workflow/p03-exploratory-diagnostics.md:23-29,46-50` | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| S-4 | major · `docs/01-workflow/p04-transformations.md:19,22,27`; `docs/01-workflow/p06-mean-model-class.md:107,112` | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| S-5 | minor · `docs/01-workflow/p03-exploratory-diagnostics.md:51` | `01-workflow/p05-representation/04-state-space.md` | 9028783 |
| S-6 | blocker · `docs/01-workflow/p02-purpose/08-spectral-analysis.md:10-11`; `docs/01-workflow/p04-transformations.md:17,29-32`; `docs/01-workflow/ | `01-workflow/p04-transformations.md` | 9216f60 |
| S-7 | major · `docs/01-workflow/p02-purpose/08-spectral-analysis.md:16-19` | `01-workflow/p00-purpose/08-spectral-analysis.md` | e419a39 |
| S-8 | major · `docs/01-workflow/p02-purpose/08-spectral-analysis.md:13-14,22` | `01-workflow/p00-purpose/08-spectral-analysis.md` | e419a39 |
| S-9 | minor · `docs/01-workflow/p02-purpose/08-spectral-analysis.md:15-16` | `01-workflow/p00-purpose/08-spectral-analysis.md` | e419a39 |
| S-10 | minor · gap · `docs/01-workflow/p02-purpose/08-spectral-analysis.md:20,38-44` | `01-workflow/p00-purpose/08-spectral-analysis.md` | e419a39 |
| S-11 | major · `docs/01-workflow/p05-representation/index.md:12-19`; `docs/01-workflow/p01-data-type-gate.md:29` | `01-workflow/p05-representation/index.md` | 9028783 |
| S-12 | minor · `docs/01-workflow/p05-representation/02-frequency-domain.md:13,19,26` | `01-workflow/p05-representation/02-frequency-domain.md` | 9028783 |
| S-13 | minor · `docs/01-workflow/p05-representation/02-frequency-domain.md:27-28` | `01-workflow/p05-representation/02-frequency-domain.md` | 9028783 |
| S-14 | minor · `docs/01-workflow/p00-data.md:13,18-19`; `docs/01-workflow/p05-representation/02-frequency-domain.md:19` | `01-workflow/p01-data.md` | 9216f60 |
| S-15 | minor · gap · `docs/01-workflow/p05-representation/03-time-frequency.md:19-23` | `01-workflow/p05-representation/03-time-frequency.md` | 9028783 |
| S-16 | minor · `docs/01-workflow/p05-representation/03-time-frequency.md:21,25` | `01-workflow/p05-representation/03-time-frequency.md` | 9028783 |
| S-17 | minor · gap · `docs/01-workflow/p05-representation/03-time-frequency.md:19-24` | `01-workflow/p05-representation/03-time-frequency.md` | 9028783 |
| S-18 | blocker · `docs/01-workflow/p05-representation/06-hilbert-phase.md:10-19` | `01-workflow/p05-representation/06-hilbert-phase.md` | 9028783 |
| S-19 | minor · `docs/01-workflow/p05-representation/06-hilbert-phase.md:19-20` | `01-workflow/p05-representation/06-hilbert-phase.md` | 9028783 |
| S-20 | minor · `docs/01-workflow/p05-representation/04-state-space.md:18,23-24,27`; `docs/01-workflow/p08-estimation.md:70,75` | `01-workflow/p08-estimation.md` | 9aaf6fc |
| S-21 | minor · `docs/01-workflow/p05-representation/04-state-space.md:12-13,17,19-20` | `01-workflow/p05-representation/04-state-space.md` | 9028783 |
| S-22 | minor · gap · `docs/01-workflow/p08-estimation.md:67,73-74` | `01-workflow/p08-estimation.md` | 9aaf6fc |
| S-23 | minor · `docs/01-workflow/p08-estimation.md:102`; `docs/reference/15-continuous-time/index.md:21` | `01-workflow/p08-estimation.md` | 9aaf6fc |
| S-24 | minor · `docs/01-workflow/p05-representation/05-functional.md:17-21` | `01-workflow/p05-representation/05-functional.md` | 313a59c |
| S-25 | minor · gap · `docs/01-workflow/p05-representation/05-functional.md:10-16` | `01-workflow/p05-representation/05-functional.md` | 313a59c |
| S-26 | minor · `docs/reference/14-functional-high-frequency/index.md:10-12` | `reference/14-functional-high-frequency/index.md` | 313a59c |
| S-27 | nit · `docs/01-workflow/p05-representation/01-time-domain.md:17-21` | `01-workflow/p05-representation/01-time-domain.md` | 9028783 |
| S-28 | nit · `docs/01-workflow/p06-mean-model-class.md:199` | `01-workflow/p06-mean-model-class.md` | cf64d5b |
| S-29 | major · `docs/01-workflow/p07-error-process.md:9,57-66,98-101` | `01-workflow/p07-error-process.md` | 8b1c07a |
| S-30 | major · `docs/01-workflow/p02-purpose/03-signal-extraction.md:10-13,19-22` | `01-workflow/p00-purpose/03-signal-extraction.md` | e419a39 |
| S-31 | major · `docs/01-workflow/p02-purpose/03-signal-extraction.md:20-24`; `docs/01-workflow/p05-representation/04-state-space.md:14-15,22`; `docs | `01-workflow/p00-purpose/03-signal-extraction.md` | e419a39 |
| S-32 | minor · `docs/01-workflow/p02-purpose/06-decomposition.md:23-25` | `01-workflow/p00-purpose/06-decomposition.md` | e419a39 |
| S-33 | minor · gap · `docs/01-workflow/p02-purpose/06-decomposition.md:16-21` | `01-workflow/p00-purpose/06-decomposition.md` | e419a39 |
| S-34 | major · gap · `docs/01-workflow/p02-purpose/09-system-identification.md:10-24` | `01-workflow/p00-purpose/09-system-identification.md` | e419a39 |
| S-35 | minor · `docs/01-workflow/p02-purpose/09-system-identification.md:19-22` | `01-workflow/p00-purpose/09-system-identification.md` | e419a39 |
| S-36 | minor · `docs/01-workflow/p02-purpose/09-system-identification.md:15-18,23`; `docs/01-workflow/p06-mean-model-class.md:222,226` | `01-workflow/p00-purpose/09-system-identification.md` | e419a39 |
| S-37 | minor · gap · `docs/reference/16-count-categorical/index.md:10,16-22` | `reference/16-count-categorical/index.md` | 313a59c |
| S-38 | minor · `docs/reference/17-point-processes/index.md:14-22` | `reference/17-point-processes/index.md` | 313a59c |
| S-39 | minor · `docs/reference/17-point-processes/index.md:23-24,49-50` | `reference/17-point-processes/index.md` | 313a59c |
| S-40 | major · `docs/reference/15-continuous-time/index.md:10-20`; `docs/01-workflow/p01-data-type-gate.md:29` | `reference/15-continuous-time/index.md` | 313a59c |
| S-41 | major · `docs/reference/15-continuous-time/index.md:16,21` | `reference/15-continuous-time/index.md` | 313a59c |
| S-42 | minor · `docs/reference/15-continuous-time/index.md:17,22-26` | `reference/15-continuous-time/index.md` | 313a59c |
| S-43 | minor · gap · `docs/reference/15-continuous-time/index.md:10-13`; `docs/01-workflow/p01-data-type-gate.md:18` | `reference/15-continuous-time/index.md` | 313a59c |
| S-44 | major · `docs/reference/32-panel-time-series/index.md:10-17` | `reference/32-panel-time-series/index.md` | 313a59c |
| T-1 | (blocker) Summary tables say OLS with a lagged dependent variable is inconsistent; the body says it is consistent | `00-foundations/ols-assumptions.md` | bad616a |
| T-2 | (blocker) ARCH is presented as a violation of A2 given X, with false consequences | `00-foundations/ols-assumptions.md` | bad616a |
| T-3 | (major) The A1/A4 split is stated as two distinct failure mechanisms, but A4 implies A1; the role of the intercept is misattributed | `00-foundations/ols-assumptions.md` | bad616a |
| T-4 | (major) "Predetermined holds as long as eps_t is not autocorrelated" is false | `00-foundations/ols-assumptions.md` | bad616a |
| T-5 | (minor) The LLN is said to need a rate of decay; the rate is a CLT condition | `00-foundations/asymptotics.md` | 8c3a0b2 |
| T-6 | (minor) "Positive autocorrelation understates standard errors" omits the condition on the regressors | `00-foundations/ols-assumptions.md` | bad616a |
| T-7 | (minor) "OLS achieves BLUE only when those assumptions hold" | `00-foundations/ols-assumptions.md` | bad616a |
| T-8 | (minor) A5 and the asymptotic-normality statements | `00-foundations/ols-assumptions.md` | bad616a |
| T-9 | (minor) A4 failures cannot be read from OLS residuals | `00-foundations/ols-assumptions.md` | bad616a |
| T-10 | (minor) Weak exogeneity is defined on the error density | `00-foundations/ols-assumptions.md` | bad616a |
| T-11 | (minor) Appendix A, which this page names as the derivation home, has errors and contradicts the writing rules | `appendices/A-ols-derivation.md` | bad616a |
| T-12 | (nit) Titles, navigation and delimiters | `00-foundations/ols-assumptions.md` | bad616a |
| T-13 | (blocker) The "core question" and its operational test are stated on y and as zero autocovariance | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-14 | (blocker) Cochrane-Orcutt is misdefined and called inefficient | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-15 | (major) Regression with ARMA errors is equated with ARIMAX; the spine separates them | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-16 | (major) Diamond "Residuals i.i.d.?" decided by ACF and Ljung-Box, followed by a squared-residual check on its Yes branch | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-17 | (major) "No finite feature set can capture" dependence on the series' own past | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-18 | (minor) Unit-root verdict precedes the choice of deterministic terms; ADF+KPSS shown as yes/no | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-19 | (nit) VAR/VECM estimation sentence and a stale pointer | `00-foundations/do-you-need-time-series-analysis.md` | bad616a |
| T-20 | (major, gap) Test logic lacks size, power, p-value and the meaning of non-rejection | `00-foundations/logic-of-statistical-analysis.md` | bad616a |
| T-21 | (minor) "MLE is required whenever the model contains unobservable error components" | `00-foundations/logic-of-statistical-analysis.md` | bad616a |
| T-22 | (minor) BLUE and AR(p) in one sentence | `00-foundations/logic-of-statistical-analysis.md` | bad616a |
| T-23 | (nit) Smaller points on this page | `00-foundations/logic-of-statistical-analysis.md` | bad616a |
| T-24 | (major, gap) Every foundation section is a placeholder | `00-foundations/stochastic-processes.md` | 8c3a0b2 |
| T-25 | (major) Part 0 reading order uses concepts before they are defined | `index.md` | 8c3a0b2 |
| T-26 | (nit) White test listed under serial correlation | `index.md` | 8c3a0b2 |
| T-27 | (blocker) The one written chain justifies MLE in i.i.d. form and drops identification | `glossary/maximum-likelihood.yml` | 8c3a0b2 |
| T-28 | (minor) Step 2: phi does appear in the AR(1) marginal | `glossary/maximum-likelihood.yml` | 8c3a0b2 |
| T-29 | (minor) Foundation definitions: Kolmogorov, probability density, independence | `glossary/stochastic-processes.yml` | 8c3a0b2 |
| T-30 | (major) LLN is a foundation although its definition names its prerequisites | `glossary/asymptotics.yml` | 8c3a0b2 |
| T-31 | (major) ACF bands and Ljung-Box stated for white noise; both need i.i.d.; P7 runs Ljung-Box before ARCH is removed | `glossary/p03-exploratory-diagnostics.yml` | 8c3a0b2 |
| T-32 | (minor) Stationarity entry | `glossary/stochastic-processes.yml` | 8c3a0b2 |
| T-33 | (minor) White noise entry: strong white noise and the missing MDS | `glossary/stochastic-processes.yml` | 8c3a0b2 |
| T-34 | (minor) i.i.d. entry | `glossary/stochastic-processes.yml` | 8c3a0b2 |
| T-35 | (minor) ADF and KPSS entries | `glossary/p03-exploratory-diagnostics.yml` | 8c3a0b2 |
| T-36 | (major) Linear interpolation formula is wrong | `glossary/p01-data.yml` | 8c3a0b2 |
| T-37 | (minor) Periodogram presented as a PSD estimate without the inconsistency caveat; two normalisations | `glossary/02-frequency-domain.yml` | 8c3a0b2 |
| T-38 | (minor) Gauss-Markov conditions enumerated differently from the page that develops them | `glossary/ols-assumptions.yml` | 8c3a0b2 |
| T-39 | (nit) Other glossary details | `glossary/p03-exploratory-diagnostics.yml` | 8c3a0b2 |
| T-40 | (major, gap) Chains and the terms they need are mostly absent | `glossary/maximum-likelihood.yml` | 8c3a0b2 |
| T-41 | (major) P7 needs residuals before anything is estimated; no page states why the phases come in this order | `01-workflow/index.md` | c4ee7e9 |
| T-42 | (minor) P3 runs ARCH-LM on levels and unit-root tests on the untransformed scale | `01-workflow/p03-exploratory-diagnostics.md` | 834fde3 |
| T-43 | (minor) HAC is unconditional on the causal route after the error process has been modelled | `01-workflow/p11-inference.md` | 83cde51 |
| T-44 | (minor) Wold decomposition stated without the deterministic part and with unqualified innovations | `00-foundations/stochastic-processes.md` | 8c3a0b2 |
