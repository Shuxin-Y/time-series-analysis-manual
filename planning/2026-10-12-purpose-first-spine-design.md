# Purpose-first spine: design

Date: 2026-10-12. Status: approved by the four reviewers on 2026-10-12 (revision 3 with the round-3 and round-4 corrections; review rounds: econometrics 5, forecasting 3, signal processing 3, theory 4). Revision 2 answered the first design review (four REVISE verdicts, 27 required changes, all adopted; suggested changes adopted where marked); revision 3 answers the second (13 required changes, cited as econ r2, fc r2, sig r2, th r2, all adopted). Supersedes sections 4, 5, 7 and the phase-dependent parts of 10.1–10.4 of `planning/2026-10-06-flowchart-framework-design.md`; every other section of that spec still applies.

Input: the independent expert review of `main` at `e44030e` (econometrics E-1–E-55, forecasting and ML F-1–F-32, signal processing and stochastic processes S-1–S-44, theory and pedagogy T-1–T-44) and the design reviews of revision 1 (required changes cited as econ R1–R5, fc R1–R5, sig R1–R5, th R1–R12; suggested changes as econ S1–S9, fc S1–S10, sig S1–S8, th S1–S7).

## 1. Goal and decisions

A reader who follows the arrows performs a methodologically valid analysis for the question they have. The review found that the spine was purpose-blind before P5: P0 cleaning and P4 transformations ran whatever the purpose (F-2, S-1, S-6, E-26), the type branches left the spine before the purpose and diagnostics phases (F-1, E-8, S-40), model selection came before out-of-sample evidence (F-3, E-49), and diagnostics could not return to the identification phases (E-1).

Owner decisions: the purpose is decided first; phases are renumbered (13 phases); every finding is resolved in this round; written-content errors are fixed in the same round. The owner delegated approval of this design to the four reviewers.

## 2. The spine

| ID | Phase | Old ID | Answers |
|---|---|---|---|
| P0 | Purpose and evaluation plan | P2 | What is the question, how will the answer be judged, and what must the data keep? |
| P1 | Data acquisition and cleaning | P0 | What is measured, and is the series fit to analyse, without deciding anything the purpose decides? |
| P2 | Data-type gate | P1 | How is it sampled and how are the series related? (with the value type: sets the type flags) |
| P3 | Exploratory diagnostics | P3 | What structure is present? |
| P4 | Transformations | P4 | What must change before modelling, given the purpose and the P3 flags? |
| P5 | Representation selection | P5 | Which mathematical object is modelled? |
| P6 | Conditional-mean model class | P6 | Which families are candidates for the mean? |
| P7 | Error-process specification | P7 | What process do the innovations follow? |
| P8 | Estimation | P8 | How are parameters obtained? |
| P9 | In-sample diagnostics | P9 | Which specification errors does the fit show, and which variants go forward? |
| P10 | Out-of-sample evaluation and selection | new (from P11 and P9) | Which candidate, or baseline, predicts or detects best on data it has not seen? |
| P11 | Inference and interpretation | P10 | What does the selected model say, for this purpose? |
| P12 | Deployment and monitoring | new (from P11) | Does it keep working? |

Master-chart feedback edges (dotted): P9 → P3 (integration order or transform wrong, triggered by the root check, E-1, E-48); P9 → P6 (mean misspecified); P9 → P7 (innovations misspecified); P10 → P6 ("Add a candidate" and "No candidate acceptable", fc R4); P12 → P1 (data fault), P12 → P6 (structural change), P12 → P8 (gradual drift) (F-18).

The master page gives one "because" sentence per phase (T-41b, th R1–R5):
- P0 first: the question decides what cleaning may remove, what transformations may destroy and how the answer will be judged; fixing it before seeing the data is pre-specification.
- P1 after P0: the value type, asked at P1 entry, decides which cleaning steps are valid (interpolation produces non-integers for counts; event times have nothing to impute; stock and flow series aggregate differently).
- P2 after P1: the sampling and structure questions are answered on aligned, de-duplicated data.
- P3 after P2: valid diagnostics depend on the value type, the sampling and the cross-sectional structure; unit-root and ACF theory assumes a regularly sampled continuous series.
- P4 after P3: transforms are chosen from diagnosed structure.
- P5 after P4: a model family is a family of processes written in one representation, and the representation decides which families are candidates.
- P6 after P5: the class is chosen for the series at the scale and integration order at which it will be modelled. Structure the class does not represent (variance scaling, integration when the class is stationary, deterministic terms, breaks) is removed or turned into regressors first; structure the class represents (integration in ARIMA or ARFIMA, cointegration in a VECM) is left to the class.
- P7 after P6: error tests are valid on residuals of a mean model, from a preliminary fit of the P6 class (T-41a, E-37).
- P8 after P7: the estimator is chosen for the complete joint model; the preliminary fit ignored the error process and is not the estimate.
- P9 after P8: diagnostics apply to the jointly estimated model.
- P10 after P9: P9 screens specification errors and selects which variants to carry forward; P10 compares them, together with the baselines, which are exempt from the P9 screen, because in-sample adequacy is neither necessary nor sufficient for out-of-sample accuracy (Clements and Hendry 1998).
- P11 after P10: inference is drawn from the selected model, and it is conditional on the specification search (P3 pre-tests, P9 and P10 loops); P11 states the post-selection caveat and its remedies.
- P12 last: monitoring needs a deployed model.

## 3. Flags

A flag is set once and read later (framework rule unchanged: every "Set flag" has a reader).

| Flag | Set in | Values | Read by |
|---|---|---|---|
| purpose | P0 | ten purposes | P1, P4, P6 entry, P9, P10, P11, P12 |
| forecast task | P0 | horizons, issuance frequency, functional or quantile levels, loss | P6 (multi-step strategy, lag sets), P7 (output distribution for learners), P8 (training loss), P10 (metrics, back-transformation), P11 (point functional) |
| baselines | P0 | by value type and functional: naive, seasonal naive, Theta or automatic ETS; zero forecast, Croston, empirical quantiles for intermittent data; bootstrapped naive or climatology for probabilistic tasks (fc S2) | P10 comparison set (eligible for selection) |
| covariates | P0 | none; known future deterministic; external forecast; lagged only (lags at least h); co-forecast | P3, P4, P6 (modifier inside each family), P10 (external forecasts as issued at each origin) |
| timing | P0 | offline; real time. Real-time uses of purposes 3, 4 and 5 use one-sided versions of every two-sided operation. Purpose 1 and every purpose evaluated by rolling origin use one-sided versions for learner features and for the live output; their two-sided P1 and P4 operations (imputation by smoothing, STL, X-13) are allowed because P10 refits them inside each training window, where they see only data before the origin (sig R4, fc r2) | P1 and P4 (one-sided versions of two-sided operations), P5 (filter versus smoother, zero-phase filtering, Hilbert phase), purposes 3, 4, 5, P10, P12 |
| labels | P0 | many; few; none | purposes 5 and 7, P10 |
| split unit | P0 | time; unit (subject, recording, series); unit and time (fc S5) | P10, purpose 7 |
| keep anomalies | P0 (purposes 4, 5) | yes | P1 (data errors labelled and kept in the mask, fc S1), P4 |
| keep levels | P0 (purposes 3, 4, 6, 8; sig R1, sig S7) | yes | P4 (selective skip, section 4.5) |
| value type | P1 entry (th R1) | continuous; counts (small counts or frequent zeros, decided per series; large counts such as passenger numbers are treated as continuous, so log-ARIMA stays available, fc r2); categorical; compositional; curves; event times | P1 cleaning, P3, P4, P5, P6, P7, P8, P9 |
| sampling | P1 (after alignment), recorded by P2 | regular; irregular resampled; irregular kept; mixed frequency | P3 entry, P4, P5 |
| structure | P2 | single; few related (multivariate); many similar; wide panel; spatial or network | P3, P6, P7, P9 |
| reporting delay | P1 (which also corrects the right-truncated tail on the raw scale, econ r2) | yes | P10 (data as they stood at each origin, correction refitted per window) |
| calendar effects | P1 | yes | P3 test regressions, P6 deterministic regressors |
| candidate outliers | P1 | mask (statistical outliers; data errors when anomalies are kept) | P3 (unit-root tests with outlier dummies or AO-robust tests, econ S2), P4, P6 intervention models, purposes 4 and 5 |
| imputed | P1 | mask | P8 (the Kalman likelihood treats imputed points as missing, econ S5) |
| pooling, aggregation | P2 (B7) | local; cluster then local; partial pooling; global; compare local and global (fc R4). Hierarchy yes or no | P6, P10 (reconciliation at every origin, fc r2), P11 reconciliation |
| variance transform | P3 | none; log; Box-Cox λ; Yeo-Johnson | P3 tests (run on that scale), P4, P9 (criteria compared within one transform), P10 and P11 (back-transformation with bias adjustment for the mean, econ S6) |
| integration | P3 | the single source of d (sig R3, econ S8, th S5): the integer order k and, only when the evidence requires it, a fractional remainder. When the unit-root tests agree (HEGY π1 for seasonal series; Dickey–Pantula with ADF and KPSS otherwise) and the bias-controlled exact local Whittle interval contains their k, k comes from them; otherwise (tests conflict, or the interval excludes their k, as for d̂ near 0.3–0.45 where ADF and KPSS can agree on 1) k is the integer nearest to the exact local Whittle d̂ (th r3, sig r3). A fractional remainder d̂ − k, in [−0.5, 0.5), is carried only when the exact local Whittle interval excludes k after a short-memory bias control (Andrews–Sun local polynomial Whittle, or an ARFIMA test of d = k), because a strong AR(1) reads as fractional or as a unit root to plain local Whittle (econ r2). Also the seasonal filter (Δ_s, partial) | P4 (applies Δ^k and the seasonal filter; keep-levels purposes 3, 4, 8 read k), P6 (estimates the remainder) |
| deterministic terms | P3 | constant, trend, deterministic seasonality | P4 retest, P6 regressors |
| breaks, explosive episode | P3 | with dates | P4, P6, P7 |
| cointegration | P3 | rank r; mixed I(0) and I(1) | P4 (levels kept when r ≥ 1 or orders are mixed; differences when r = 0 and all series are I(1), econ R4), P6 (VECM, VAR in levels, or ARDL, econ R5), P8 (reduced-rank ML) |
| nonlinear mean | P3 | yes | P6 |
| outlier treatment | P4 step 2 | prefilter; intervention terms | P6 (Chen–Liu intervention models only when intervention terms were chosen) |
| prior specified | P6 (Bayesian families) | yes | P8 entry |
| model kind | P6 | likelihood; loss minimisation; Bayesian; counts; events | P7 entry, P8, P9 |

Removed: the separate long-memory flag (folded into integration), the multi-step flag (part of the forecast task), and the B7 "Strategy?" exclusive choice.

Every data-dependent step that P1, P4 or P8 fits on the series (imputation, λ, d̂, decomposition, seasonal adjustment, prefilter windows, features and scaling, hyperparameter tuning) is refitted inside each training window when P10 evaluates out of sample (fc R1, sig R4).

## 4. Phase content

Each subsection lists the redesign and the findings it resolves. Leaves keep their ids except where the phase changes (section 6).

### 4.1 P0 Purpose and evaluation plan (owner-approved; extended by the review)

Part 1, "Question about?": the two-part selector with its ten purposes, plus F-32: under "The future", "Values or events?"; events in a future window go to purpose 7 learners with a time-respecting split (unit and time) and lead-time metrics, with a pointer to B2 survival and remaining useful life.

Part 2, evaluation plan, leaves by purpose family:
- forecasting: "Specify the forecasting task: horizons, issuance frequency, functional or quantile levels, loss" (F-5); "Choose the baselines" with the value-type and functional cases (F-4, fc S2); "Covariates and their availability" (F-7, F-16);
- detection (purposes 4, 5): "Online or offline?" (F-21, F-23), "Labels available?" with many (→ purpose 7 supervised learners, fc S7), few, none (F-20), "Detection delay against false alarms" (F-24);
- inference (purposes 2, 9): "Estimand and identification strategy"; purpose 9 asks "Data collected under feedback?" in its own chart (S-34);
- collections (purpose 7): "Split unit: subject, recording or series; temporal if deployment runs forward; both for cold-start and future-event prediction" (F-28, fc S5).

Part 3, preservation and timing: "Set flag: keep anomalies" (purposes 4, 5), "Set flag: keep levels" (purposes 3, 4, 6, 8), "Set flag: timing" (section 3).

### 4.2 P1 Data acquisition and cleaning

Entry: "Value type?" sets the value-type flag (th R1). Then: inspect sampling (second line "signal bandwidth against Nyquist; anti-alias filter at acquisition", S-14) → align timestamps, time zones, daylight saving (all series, E-3) → regular sampling? (sets the sampling flag; irregular → B3 resample question) → duplicates → units and metadata → cumulative to flow (counts and flows) → calendar effects ("Set flag: calendar effects", E-5) → reporting delays and right truncation (new leaf, F-8): the delay distribution is estimated and the truncated tail corrected (nowcast) on the raw scale here, before P3 sees the series, so that no spurious end-of-sample break reaches the tests (econ r2) → revisions and real-time vintages → "Screen data errors and mark candidate outliers" before any imputation (econ S5, sig S3): data errors are corrected, except under keep anomalies, where they are labelled and kept in the mask (fc S1); statistical outliers are masked, never replaced (F-2, E-2) → missing values by value type (counts: no interpolation; event times: none; continuous: impute short gaps, segment long gaps; purposes 3 and 8 prefer gap-tolerant estimation, sig S3), one-sided methods where the timing flag requires them (section 3: real-time uses, learner features and live outputs; two-sided smoothing is allowed inside each P10 training window) (sig R4, F-21), "Set flag: imputed" → resample now? (reads purpose, timing and value type; second line "sum flows, sample stocks; averaging adds MA terms; anti-alias before downsampling", E-4, S-14) → frequency conversion.
The Chen–Liu classification (AO, IO, LS, TC) moves to P6 intervention models; the median and Hampel filter leaf moves to P4 (section 4.5 step 2).

### 4.3 P2 Data-type gate and the branches

P2 records the value type and sampling from P1 and asks the structure question (single, few related, many similar, wide panel, spatial or network) for every series (F-1). The page ends at P3 for every type. B3's entry question "Resample to a regular grid?" (yes and purpose allows → P1 resample with the interpolation caveat; no → continuous-time route) and "Sampling times informative?" (S-43) set the sampling value read by P3, P4 and P5 (sig S5).

Branch charts B1–B6 become index charts under the purpose-chart rule: they draw the spine phase boxes they use, in phase order, with their type-specific leaves inside the right phase. The spine pages read the type flags at P3, P4, P5, P6, P7, P8 and P9 and point to the branch leaves as refs. B7 asks two independent questions, "Aggregation constraints across series?" and "Pooling?" (local, cluster then local, partial pooling, global, compare local and global) (F-12, fc R4); its edges to model leaves become dotted pointers (F-13).

Branch content: B1 adds trend, seasonality and covariate checks to its diagnostics (E-8), zero-inflated and hurdle families and Poisson hidden Markov models (S-37), a pointer to intermittent demand (F-1), and sends log-ratio compositions to the spine with the multivariate flag. B2 replaces "Self-exciting?" with "Fit and compare: inhomogeneous Poisson, Cox, Hawkes" (time-varying baseline on the Hawkes line), relabels renewal processes ("hazard of the age"), makes marks a separate question, and draws estimation before time rescaling; degradation models get an increment check (S-38, S-39). B3 follows S-40–S-43: diagnostics of the sampling pattern and trend → optional Lomb–Scargle → process type → OU or CARMA → exact discretisation → Kalman filter on the irregular grid → prediction-error likelihood; long memory → "fBm, fractional OU or CARFIMA observed at irregular times, exact Gaussian likelihood from the covariance at those times" (sig S1); diffusion likelihood methods named (Euler pseudo-likelihood and its bias, Aït-Sahalia expansions, simulated likelihood, MCMC augmentation); signatures moved to feature extraction. B4 smooths before registration and offers sparse curves (PACE) (S-24–S-26). B6 tests cross-sectional dependence first, branches to first- or second-generation tests (E-7, S-44), and branches on the panel unit-root and cointegration verdict to panel cointegration estimators (panel DOLS and FMOLS, pooled mean group) or to differencing (econ S9).

### 4.4 P3 Exploratory diagnostics

Entry reads value type and sampling (sig R2): non-continuous types go to their branch diagnostics; irregular series that were not resampled go to the B3 diagnostics (Δt distribution, window function, trend, slotted ACF or variogram, grid-free long-memory estimators such as the variogram slope or lifting-wavelet Hurst estimators). For regularly sampled continuous series:
1. plot; descriptive distribution (no tests, E-9);
2. level-dependent variance: range-mean plot, Box-Cox profile, Guerrero λ, and the choice of scale; every later test runs on that scale (E-10, E-11, T-42); ARCH-LM leaves P3;
3. seasonal series first: HEGY, OCSB, Canova–Hansen, with the deterministic terms (seasonal dummies, trend) chosen inside the HEGY regression and the zero-frequency verdict taken from π1 (econ S1); break-robust seasonal tests when level shifts are masked; the result is the combined filter (E-18); deterministic seasonality sets a flag read by P6 (E-19);
4. deterministic terms with the unit-root tests (sequential procedure, E-14, T-18); from the highest plausible order down (Dickey–Pantula, E-16); the tests read the candidate-outlier mask (econ S2);
5. break tests robust to I(0) and I(1) (Perron–Yabu; Harvey, Leybourne and Taylor) and unit-root tests with breaks under both hypotheses (Lee–Strazicich; Perron for a known date) (E-15); candidate level shifts from P1 feed this step;
6. explosive episode suspected? → right-tailed SADF and GSADF on the log scale → date stamping → "Set flag: explosive episode" with its treatment; the integration verdict that follows is taken on the non-explosive sample (E-12, econ S3);
7. joint verdict as a decision matrix of ADF-type and KPSS outcomes, with a back-reference to the non-rejection rule on the logic page (th R6); agreement proposes k and step 8 confirms or replaces it by the rule in section 3; "Conflicting" goes to the estimation of d and to the break check, and k then comes from step 8 (E-13, econ r2, th r2, econ r4);
8. d on the levels: exact local Whittle (two-step version with unknown mean or trend, Shimotsu 2010; bandwidth below the first seasonal frequency, sig S2), with a short-memory bias control (Andrews–Sun local polynomial Whittle, or an ARFIMA test of d = k), and Robinson's tests; when k = 2 is proposed, or a trend is included and d̂ exceeds 1.5, the estimator runs on Δy and 1 is added, because on the levels the interval falls outside the estimator's valid range (econ r4); when the break flag is set, a test that separates breaks from long memory (Qu; Shimotsu) (E-20, E-21, S-2, S-3); the result sets the integration flag by the rule in section 3 (econ r2);
9. ACF and PACF of the series at its integration order; the variance-ratio test sits here (E-17); ACF bands stated for i.i.d. noise with the robust alternative (T-31);
10. nonlinearity tests on residuals of a linear AR fitted to the transformed series, heteroskedasticity-robust versions, and deferral to P7 and P9 when volatility clustering is evident (E-22); chaos indicators move to P5 after the delay embedding, with surrogate data (S-5);
11. nonparametric trend tests as an alternative input to the trend decision, conditional on the unit-root verdict (E-23);
12. covariates (from P0) and multivariate series: per-series integration order for the target and every covariate; CCF after prewhitening (E-24); cointegration by Johansen (deterministic case, lag order), Engle–Granger or the ARDL bounds test, with break-robust versions when the break flag is set (Gregory–Hansen; Johansen, Mosconi and Nielsen; econ S4). The verdict: rank r ≥ 1 → levels, VECM; r = 0 with all series I(1) → differences; mixed I(0) and I(1): one equation of interest with weakly exogenous regressors → ARDL or a single-equation ECM; a system with feedback → VAR or VECM in levels, with the rank counting the I(0) variables (E-25, E-28, econ R4, econ R5).

### 4.5 P4 Transformations

Entry reads value type and sampling (sig R2): counts skip the variance transform and differencing (trend and seasonality enter the count model through its link); event times skip P4; irregular series skip differencing (the continuous-time model carries nonstationarity). Every two-sided operation has a one-sided version, used where the timing flag requires it (section 3); a forecaster's STL or X-13 stays two-sided inside each P10 training window (sig R4, fc r3). Steps, in order:
1. variance transform (log, Box-Cox, Yeo-Johnson; λ by Guerrero) (E-27);
2. "Outliers: prefilter, or intervention terms in the model?" sets "Set flag: outlier treatment", read by P6 (th r2). Prefilter → robust prefiltering (median, Hampel) on the variance-transformed level, before any differencing, with points flagged as level shifts or breaks excluded; intervention terms → no prefilter, P6 estimates the outliers (Chen–Liu). The question is skipped when anomalies are kept; one treatment per outlier (econ R3, F-2);
3. "Decomposition wanted?" on the (log) level, before any differencing (purpose 6, or modelling by components); the retest then applies to the component that will be modelled (S-1, E-26);
4. integration filter: Δ^k and the seasonal filter from the integration flag; levels kept when the cointegration flag says so; the over-differencing check after the whole filter, with answers "trend-stationary" and "antipersistent: fractional" (E-18, sig R3); the fractional remainder is not removed here and goes to P6 (S-4, E-29);
5. deterministic seasonality and calendar effects as regressors for P6; seasonal adjustment only when the purpose needs an adjusted series, with re-seasonalisation before scoring (E-19, E-5, fc R2);
6. breaks and explosive episodes: segmenting, regime dummies, time-varying parameters, date-stamped episodes (E-12);
7. features for learners: calendar features and per-series scaling here; lag and window sets are built on the P6 learner route after the multi-step strategy (lags at least h under the direct strategy) (F-15, fc S3); every feature is computed from data available at the forecast origin;
8. retest stationarity around the deterministic terms P6 will include (trend, seasonal and break dummies, calendar regressors), break-aware when the break flag is set; exits: stationary; fractional remainder flagged for P6; cointegrated levels kept; episode segmented; loop to P3 only when none of these accounts for the failure (econ R1).

Keep levels (purposes 3, 4, 6, 8) is a selective skip (sig R1): steps 1 and 6 run; step 3 runs for purpose 6; step 2 runs only for purpose 3 when the noise is impulsive, never for purposes 4 and 8 (it would remove the impacts, QRS complexes and spikes they study and reshape the spectrum, sig r2); step 4 and the seasonal adjustment of step 5 are skipped. Purposes 3, 4 and 8 read the integration flag (sig r2, econ r2):
- purpose 8: k = 0 or trend-stationary → mean or trend removal; k ≥ 1 → difference as prewhitening, recolour by dividing by the filter's squared gain, and report a pseudo-spectrum (Nelson and Kang 1981 on detrending a random walk; S-6);
- purpose 3: k ≥ 1 → state-space or Wiener–Kolmogorov extraction, or a smoother with unit gain at frequency zero;
- purpose 4: k = 0 → segment the levels; k ≥ 1 → drift changes on Δ^k y, level shifts through a stochastic-level model, or the I(0)/I(1)-robust break tests of P3; mean-shift segmentation of I(1) levels finds spurious change points.

### 4.6 P5 Representation selection

Entry reads the sampling flag (sig S5): irregular kept → Lomb–Scargle (window function, false-alarm probability, red-noise background), continuous-time state space, Gaussian processes, functional smoothing (S-11, S-12, S-14). Frequency domain: peak significance before harmonic regression (S-13). Time frequency: answers phrased as signal criteria; STFT synchrosqueezing and reassignment; a Wigner–Ville and Cohen-class leaf; after the discrete wavelet transform, denoising, multiresolution analysis or wavelet variance and long memory; significance and cone of influence; locally stationary spectral estimation (S-15–S-17). Hilbert: "Narrow-band, single component?" before the analytic signal; no → band-pass filter or EMD and VMD, then the analytic signal per component; phase synchronisation with PLV, PLI, weighted PLI and surrogate thresholds; real time → causal phase estimation (endpoint-corrected Hilbert transform, AR-forecast phase) (S-18, S-19, sig S4). State space: "Gaps on a regular grid" versus "irregular spacing" (B3); Takens and DMD restricted to regular dense data; chaos indicators after Takens with surrogates; "Nonlinear or non-Gaussian" with EKF and UKF for near-Gaussian posteriors and sequential Monte Carlo otherwise; nonlinear filters lead to nonlinear and non-Gaussian families; timing decides filter versus smoother (S-5, S-20, S-21, S-31). Functional: "Task?" after basis smoothing (FPCA, functional regression, curve forecasting); Gaussian-process regression as a smoother; sparse curves → PACE (S-24, S-25). Time domain: ARFIMA ref (S-27).

### 4.7 P6 Conditional-mean model class

- Candidate set (fc R4): P6 may emit several candidate families and pooling regimes (for example local ETS and a global gradient-boosting model), each passing P7–P9; pooling "compare local and global" produces both; the P0 baselines join in P10.
- Value type and pooling combine (fc R5): global pooling with counts → a global learner whose loss or likelihood is Poisson, Tweedie or negative binomial, or the quantile loss from the forecast task; local pooling with counts → the B1 families and intermittent demand (F-1, S-37).
- The covariate flag is read inside each family as a modifier after the family choice (E-30, F-7, F-16): regression with ARMA errors, transfer function and ADL, ARIMAX in its own sense (T-15), covariate features for learners.
- Global and multivariate routes reach the learner choice (pooled linear AR, gradient boosting on features, neural forecasters, foundation models); "Learn from data" is guarded by series length and number of series (F-14).
- Multi-step strategy (recursive, direct, MIMO) is a modelling choice read from the forecast task (F-6); lag and window sets follow it (fc S3).
- Intervention and outlier models (Chen–Liu AO, IO, LS, TC) read the candidate-outlier mask when the outlier-treatment flag says intervention terms (E-2, th r2).
- Deterministic seasonality, calendar and trend regressors (E-5, E-19).
- Integration: ARMA on the P4-filtered series, or ARIMA on the original series, one of the two (E-29). Fractional remainder: ARFIMA(p, d − k, q) on the Δ^k series with d estimated jointly by exact ML, or conditional sum of squares on the levels, which is consistent for any d (Hualde and Robinson 2011) (econ R2, sig R3, S-4).
- Cointegration: VECM for r ≥ 1; VAR or VECM in levels for mixed systems with feedback; ARDL or a single-equation ECM for one equation with weakly exogenous regressors (E-25, econ R5).
- Fractional differencing for learners that need short-memory input is a P6 leaf on the learner route, with d̂ estimated inside each training window (sig S6).
- DLM second line "linear Gaussian state space; ARIMA as a special case" (E-31, S-28).
- Bayesian families set "Set flag: prior specified" (E-39); every family sets the model kind.
- The forecasting purpose chart's family list adds Theta, intermittent demand, local ML, structural models and multivariate co-forecast (fc S8).

### 4.8 P7 Error-process specification

Entry reads the model kind (fc S4): learners choose an output distribution or quantile heads from the forecast task; the GARCH path applies to likelihood families. Input: residuals of the class's default consistent preliminary fit (OLS or conditional least squares for linear classes; the class default for nonlinear, state-space and Bayesian classes), re-estimated jointly in P8 (E-37, T-41a, th S1). Step 1 portmanteau tests with heteroskedasticity-robust versions, Breusch–Godfrey when a lagged dependent variable is present, re-checked on standardised residuals after step 2 (E-33, T-31, th S1); "Unit root in residuals → spurious regression → P3" (E-28). Variance regimes (κ2-ICSS; valid Markov-switching tests by Hansen, Garcia, Carrasco–Hu–Ploberger) are tested before the GARCH variant; IGARCH and FIGARCH answers require "variance breaks ruled out" (E-32, E-35, S-29). BNS moves to the realised-measures branch (intraday data) (E-34). Multivariate portmanteau, LM, ARCH and normality tests when the structure flag is multivariate (E-36). Wold statement corrected (E-38, T-44).

### 4.9 P8 Estimation

Entry diamonds: "Prior specified?" → Bayesian computation (conjugate, Gibbs, MCMC, variational) (E-39); "Fitted by likelihood or by loss minimisation?" → loss route with time-aware tuning nested inside the training windows (F-17, fc R1). Part 1 asks "Endogenous regressors?" → IV and GMM (E-41). Regression with ARMA errors → joint ML; FGLS (Cochrane–Orcutt, Prais–Winsten) for AR(p) errors as the classical approximation with the lagged-dependent-variable caveat (E-42, T-14, th S2). Cointegrated systems → reduced-rank regression (Johansen ML); FMOLS and DOLS for single equations (E-40). Whittle and local Whittle as "spectral likelihood: large n or semiparametric d", outside the intractable branch (E-41, S-23); conditional sum of squares for nonstationary fractional d (econ R2). Burg separated from Hannan–Rissanen; EKF and UKF siblings of particle filters (E-43, S-20). Kalman leaf second line "stationary or diffuse initialisation; imputed points treated as missing" (S-22, econ S5). Continuous-time and diffusion estimation as in 4.3 (S-40–S-42).

### 4.10 P9 In-sample diagnostics

Model kind first. Residual autocorrelation and ARCH tests with Li–Mak corrections; BDS with bootstrap critical values, and variance asymmetry checked before a BDS rejection is sent to P6 (E-46). The distribution check tests the assumed law on probability integral transforms, with a parametric bootstrap or Bai's (2003) transformed test because the parameters are estimated; QMLE fits exit with sandwich standard errors (E-45, th R12). Parameter-stability tests (recursive estimates, CUSUM and CUSUMSQ, Nyblom, Hansen, Andrews sup-F, VAR stability), with failure routed to P4 break handling or P6 time-varying and switching families (E-47, econ S7). Roots, invertibility and parameter redundancy, which also triggers the loop to P3 (E-1, E-48). Information criteria "within one model class, one transform and one differencing order" (F-3, econ S6); loss-minimisation fits use validation loss from P8 tuning and pooled residual diagnostics (F-17). Forecast-comparison tests and encompassing move to P10 (F-3, E-49).
The gate depends on the purpose; every purpose has one answer, matching the P10 groups (fc R3, th R3, sig r2, th r2):
- loop back as drawn: inference purposes (2, 9, coefficient inference); the model-based routes of purposes 3, 6 and 8 (state-space extraction, unobserved-components decomposition, AR or ARMA spectra); simulation from a fitted model (purpose 10). Their outputs are valid only under the fitted model;
- improvement signal with the exit "Keep as candidate" to P10: forecasting (1), detection (4, 5) and collections (7), whose candidates are judged out of sample; intervals then come from out-of-sample errors;
- routes that fit no model (the nonparametric routes of 3, 4, 5, 6, 8, resampling in 10) do not pass P9.

### 4.11 P10 Out-of-sample evaluation and selection

P10 is an as-of-origin simulation (fc R1, sig R4): at each origin every data-dependent step of P1, P4 and P8 is refitted on the data before the origin; data enter as they existed then (vintages; right-truncated counts when the reporting-delay flag is set); external-forecast covariates use the forecasts issued at that origin; the refit cadence and window type match the P12 retraining policy (fc S6).

Forecast-type purposes: per origin, generate the complete forecast product before scoring (fc R2), in this order: the point forecast of the P0 functional with sample paths or a predictive distribution, back-transformation and re-seasonalisation of the paths, combination with weights from earlier origins, judgmental adjustment, reconciliation, and last the intervals and quantiles (from the final paths, or conformal calibrated on earlier-origin errors of the final product). Score on the target scale against raw actuals (data errors corrected, statistical outliers kept) with the P0 baselines in the comparison set (F-3, F-4): point metrics MAE, RMSE, MASE and RMSSE, MAPE only for strictly positive data; probabilistic proper scores CRPS, pinball, log score, interval score; calibration PIT and coverage (F-10) → forecast comparison (Diebold–Mariano, Clark–West, reality check, model confidence set) and encompassing → select a candidate or a baseline. A final hold-out not used for selection, or nested rolling origin, reports the selected candidate's accuracy (fc S10, th S4).
Collections (purpose 7): grouped splits by unit, temporal when deployment runs forward, both when the split unit says so; augmentation and tuning inside training folds (F-28); clustering validated by internal indices and stability (F-29).
Detection: labels many → event-level and range-based precision and recall with the point-adjustment caveat; few → threshold tuning; none → synthetic injection and expert review of top alarms (F-20); online detection adds detection delay (fc S7); change points online (ARL0, detection delay) and offline (F1 with margin, Hausdorff, Rand index) (F-25).
Signal extraction (purpose 3, sig R5): error on synthetic signal injected into real noise, or on reference recordings; thresholds and bandwidths tuned by SURE or GCV; "Signal preserved?" on peak amplitudes and edges, not on SNR alone (S-30).
Simulation: train on synthetic and test on real, discriminative score, privacy check for synthetic data; VaR backtests only for risk use (F-31). System identification: simulation fit on fresh data and residual-input cross-correlation (S-36).
Inference-only purposes (2, 6, 8) pass through with their own adequacy checks. Exits: "Select" → P11; "Add a candidate" → P6; "No candidate acceptable" → P6 (fc R4).

### 4.12 P11 Inference and interpretation (old P10)

Forecasting: issue the product selected in P10 for the live origin; judgmental adjustment tracked by forecast value added, then reconciliation again (F-9, fc R2); re-seasonalisation and back-transformation as in P10 (E-19, econ S6); conformal intervals with adaptive variants for dependent data (F-11). Causal: coefficient tests using HAC only when the error process is unmodelled, the QML sandwich otherwise (T-43, E-52); cointegration inference on α and β restrictions and weak exogeneity (E-25); Toda–Yamamoto on the levels VAR with d_max from P3 (E-51); natural experiments and single-series interventions are modelled through P3–P9 before the counterfactual design (E-50). New leaf "Inference after a specification search" (th R4): the P3 pre-tests and the P9 and P10 loops make naive standard errors and intervals invalid near the selection boundary (Leeb and Pötscher 2005; Berk et al. 2013); remedies: pre-specification for causal purposes, sample splitting, bootstrapping the whole procedure, sensitivity across specifications (the purpose-2 sensitivity leaf). Spectral confidence bands (S-10); break-date confidence intervals (E-53). Epidemic Rt and SIR fitting stay here as a domain case.

### 4.13 P12 Deployment and monitoring

Documentation; retraining policy (matching the P10 refit scheme); drift monitoring; statistical process control; "Drift type and source?": data fault → P1; gradual → online updating; sudden or structural → retrain on a recent window or re-specify in P6, with a baseline fallback meanwhile; recurring → reuse a stored model (F-18). Online detectors calibrate the threshold on in-control data (ARL0 against delay, F-24).

### 4.14 Purpose charts (P0 directory)

Every purpose chart is redrawn against the new spine (boxes in the new phase order) and fixes its own findings: forecasting F-3–F-9 and fc S8 (task and baselines at entry, covariates as a modifier, reporting-delay correction in P1, candidate set, P10 product scoring, combination before reconciliation); causal E-50–E-52; signal extraction S-30 ("Signal structure?" then "Noise character?") and S-31 (timing); change points F-22 (serial dependence before segmentation, AR-aware costs, long-run variance scaling), F-23, F-24, E-53, keep levels; anomalies F-19 (score residuals or the remainder, not the raw seasonal series), F-20, F-21; decomposition S-1 (levels), S-32 ("Components adequate?" with residual seasonality and sliding spans), S-33 (adaptive and multiscale methods); classification F-26 (learner input: raw series versus features), F-27 (extrinsic regression), F-28, F-29; spectral S-6–S-10; system identification S-34–S-36; simulation F-30 (P7 and P8 drawn, parameter uncertainty), F-31 (use of the paths).

## 5. Written content

- Part 0 pages, the index page, Appendix A and the glossary are corrected per T-1–T-23, T-26, T-28–T-39, E-6, E-44, E-54, E-55, each fix checked against the source first. Cochrane–Orcutt is corrected on the gateway page and on `p07-error-process.md:5` (T-14, th S2). Appendix A: the rule in `.claude/rules/writing.md` is amended so that appendices hold link indexes and derivations referenced from Part 0 (T-11, th S3).
- Part 0 reading order: logic → stochastic processes → asymptotics → OLS assumptions → do-you-need-time-series-analysis (T-25).
- Logic page (th R6, T-20): size, power, the p-value, non-rejection, and the pre-test and specification-search effect (Giles and Giles 1993; Leeb and Pötscher 2005), with a coefficient t-test as the example. The ADF and KPSS decision matrix sits in the stochastic-processes unit-root section and in P3 step 7, after stationarity is defined.
- Gateway page (th R11, T-13): reduced to the independence question stated on the errors (are the regression errors i.i.d., or at least an MDS?), with the residual and squared-residual checks, routing to P0; it no longer differences before a purpose is known.
- Foundation sections written this round (T-24, th R7, th S7): strict and weak stationarity; white noise, martingale difference sequences and independence; ergodicity and mixing; random walks and unit roots (definition part); the law of large numbers; the central limit theorem with the long-run variance; the delta method; conditional expectation as the optimal predictor under squared loss, with the loss-to-functional map (absolute loss → median, pinball → quantile, proper scores of the distribution → the predictive distribution; Gneiting 2011) read by P0 and P11 (th R10); the chain rule of probability; probability density; KL divergence; the Wold decomposition; the prediction-error decomposition (home moved to a written section). On the maximum-likelihood page (th r2): joint density, likelihood, maximum likelihood, identification, uniform LLN (consistency of extremum estimators) and the pseudo-true value each get a written home section.
- Glossary (T-27, T-30, T-40, th R8, th R9): the MLE chain in conditional form; Kolmogorov extension removed from the Joint density chain (T-29a) and kept as a foundation with the corrected definition. New terms: likelihood, maximum likelihood, chain rule, prediction-error decomposition, ergodicity, mixing, martingale difference sequence, CLT, Wold decomposition, conditional expectation, identification, uniform LLN (consistency of extremum estimators), long-run variance, pseudo-true value, integrated process. Dependency rule: a theorem term depends on the terms in its hypotheses; foundations are definitions plus theorems taken as given whose hypotheses are foundations; LLN, CLT, Wold and MLE are not foundations; ergodicity depends on stationarity. Chains this round for ADF, KPSS, ACF, PACF, Ljung–Box, ARIMA, Differencing, Gauss–Markov and Full column rank; the remaining chainless terms are listed in the PR as a recorded deferral to Plan C with the reason (their method sections are unwritten).
- Part 0 math delimiters become `\( \)` and `\[ \]` (T-12).

## 6. Renumbering mechanics

ID map, applied simultaneously by a script (placeholders, then final ids): `P2_` → `P0_`, `P0_` → `P1_`, `P1_` → `P2_`, `P10_` → `P11_`; `P11_` → `P10_` (rolling origin, metrics, acceptance) or `P12_` (documentation, drift, SPC, online updating, retraining); master boxes `P0`–`P11` renumbered the same way and `P12` added; `P3`–`P9`, `B1`–`B7` and `F_` unchanged. Moved leaves take their new owner's prefix (for example the multi-step strategy → `P6_MULTISTEP`; forecast comparison `P9_FORECAST_COMPARISON` → `P10_FORECAST_COMPARISON`; Chen–Liu classification → P6; robust filtering → P4; the value-type diamond → P1).

Files: `p02-purpose/` → `p00-purpose/`; `p00-data.md` → `p01-data.md`; `p01-data-type-gate.md` → `p02-data-type-gate.md`; `p09-diagnostics-selection.md` → `p09-in-sample-diagnostics.md`; `p10-inference.md` → `p11-inference.md`; `p11-validation-deployment.md` → `p10-evaluation-selection.md` and `p12-deployment-monitoring.md`. Glossary files follow their pages. `mkdocs-redirects` maps every old URL to its new page (the old P11 page to P10).

Code and rules: the audit's phase set becomes P0–P12 with P0 owned by `01-workflow/p00-purpose/` and P5 by `01-workflow/p05-representation/`; tests, `nav:`, `.claude/rules/writing.md`, `DESIGN-SYSTEM.md`, `README.md` and the framework spec's phase-dependent sections are updated. The 2026-10-07 Plan B document is a historical record and gets a superseded note; its flow paragraphs are not regenerated.

## 7. Process

Every finding is first checked against the source at the branch head; a finding that does not hold is recorded as false with the reason. The renumbering lands first as its own commit with all gates green, then the content changes by phase, one commit per finding class. The width rule (scale at least 0.45 at 1280 px; container scroll at 390 px) applies to every redrawn diagram; diagrams that exceed it are split into parts.

## 8. Acceptance

- The master chart shows P0–P12 with the feedback edges of section 2; every page, inventory row, glossary file, audit rule, test, nav entry and redirect is consistent; old URLs redirect.
- Every finding has a disposition: fixed (commit) or false (reason). The four reviewers approve this design and re-check their findings at the PR head.
- Gates: `TSAM_REQUIRE_E2E=1 pytest tests` passes; the flowchart audit reports 0 errors; `mkdocs build --strict` passes; the scaffold dry-run reports 0 actions; PR CI is green.
- End to end on the built site, routes walked by following the arrows:
  - a purpose-5 reader keeps the anomalies through P1 and P4;
  - a purpose-8 reader reaches the periodogram on data that kept its periodic content (sig R1, th S6);
  - a purpose-6 reader decomposes levels;
  - a purpose-3 real-time reader reaches a causal filter or the Kalman filter, not the smoother (sig S8);
  - a forecasting reader compares candidates and baselines out of sample, on the complete product, before selection;
  - an M5-type reader (counts, many series, hierarchy, global pooling) reaches a global learner with a count loss, P10 with count-appropriate baselines and metrics, and reconciliation (fc R5);
  - a probabilistic-forecast reader has intervals and quantiles produced per origin and scored by proper scores in P10 (fc S9);
  - a count reader with local pooling reaches the B1 families, P9 count diagnostics and P10.
