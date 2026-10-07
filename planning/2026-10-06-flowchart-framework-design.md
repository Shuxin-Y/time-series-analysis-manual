# Flowchart Framework Design

Date: 2026-10-06
Status: approved in conversation; amended 2026-10-07 after the review of the skeleton PR (sections 10.1, 10.2, 10.4, 10.5, 11 state the rules the audit enforces)
Supersedes: the "Flowcharts" and "structure" sections of `book_plan.md`

## 1. Purpose

The manual has two goals, in priority order.

1. **Understanding.** A reader who knows "use MLE here" has not understood anything. The reader must be able to follow why MLE, why the likelihood is a joint density, what "joint" means and why a joint object is needed, why the log, why the log helps, and so on down to a foundation that needs no further justification. Every method in the book carries an explicit chain of "because" steps back to Part 0.
2. **Coverage.** The book covers 34 areas (section 8). The 26 areas on the landing page plus 8 approved additions.

The three flowcharts are the organising framework. They place every piece of content the book will teach into a workflow. A reader follows arrows, runs the named test, and lands on the section that teaches the method the result calls for.

## 2. Scope

This design covers the framework: the flowchart architecture, the phase sequence, the branch and sub-diagram structure, the content rules each section must follow, file and naming conventions, the node inventory, the glossary schema, and the audit that keeps them consistent.

Out of scope: writing the content itself; the per-section depth cap (open, see section 13); visual restyling beyond the existing decision-flowchart notation in `DESIGN-SYSTEM.md`.

## 3. Architecture

### 3.1 Three axes of the book

| Axis | Role | Location |
|---|---|---|
| Part 0 — Foundations | Roots of every why-chain. Statistical-analysis logic, OLS assumptions, stochastic processes, asymptotics for dependent data | `docs/00-foundations/` |
| Workflow | The general flowchart, one chapter per phase P0–P11. Procedural content: what to do, which test, which branch | `docs/01-workflow/` |
| Reference | One chapter group per area (34). Model families, transforms, estimators, theory | `docs/reference/` |

### 3.2 One spine, two indexes

- The **general flowchart** is the single spine. A master diagram shows only the twelve phase boxes. Each phase has its own sub-diagram in its chapter. Leaf nodes of sub-diagrams are the book's content units.
- The **purpose chart** is the P2 chapter. The **representation chart** is the P5 chapter. Both are phases of the general flowchart, so their sub-diagrams own purpose-specific and representation-specific leaves. Everything else they show is a `ref` to a leaf owned by another phase.
- **Invariant.** Every non-`ref` node ID is defined in exactly one sub-diagram across the whole book. Every `ref` node ID matches a defined node. Every leaf node has exactly one inventory row (section 10.4) pointing at exactly one section.

### 3.3 Node = content unit

Every leaf node links to one section. The three charts together are the table of contents in graph form. Every method section is a leaf's section; its subsections (H3 and deeper) belong to that leaf and need no node of their own. Concept homes for glossary terms sit in a leaf's section (its heading or a subsection) or on a reachable `kind: theory` page (reachability: `.claude/rules/writing.md`, "Section kinds"). A node without content is a to-do item, visible in the audit.

## 4. The general flowchart: phases P0–P11

Each phase is one chapter under `docs/01-workflow/`, holding the phase sub-diagram and a phase guide. Content inventories below list leaf candidates; the inventory file (section 10.4) is authoritative once written.

| ID | Phase | Sub-diagram answers | Leaf content (candidates) |
|---|---|---|---|
| P0 | Data acquisition and cleaning | Is the series fit to analyse? | Sampling rate, resolution, alignment; time zones, DST, duplicate stamps; missing-value imputation (interpolation, Kalman-smoother imputation, multiple imputation, segmentation); outlier taxonomy AO / IO / LS / TC (Chen–Liu); robust filtering (median, Hampel); unit and metadata consistency; cumulative-to-flow conversion; anti-aliasing and resampling; calendar effects (trading day, holidays, leap year); temporal disaggregation and benchmarking (Chow–Lin, Denton); data revisions and real-time vintages |
| P1 | Data-type gate | What kind of object is this? | Three routing variables and seven branches (section 5). Flags consumed downstream |
| P2 | Purpose | What is the question? | Ten purpose sub-charts (section 7.1). Owns purpose-specific leaves: change-point algorithms, anomaly methods, decomposition methods, feature extraction, classification, clustering, simulation |
| P3 | Exploratory diagnostics | What structure is present? | Distribution (Shapiro–Wilk, Jarque–Bera, skewness, tail index); variance stability (rolling variance, ARCH-LM on raw); trend-stationary vs difference-stationary; unit roots (ADF, KPSS, PP, DF-GLS, Zivot–Andrews); seasonal unit roots (HEGY, Canova–Hansen, OCSB); variance ratio (Lo–MacKinlay); explosive roots (PSY / GSADF); structural breaks (Chow, CUSUM, Bai–Perron); seasonality detection; ACF / PACF; long-memory indicators (Hurst, GPH); nonlinearity tests (BDS, Teräsvirta, Tsay, Keenan); nonparametric trend (Mann–Kendall, Sen slope, prewhitening); multivariate EDA (CCF, lead–lag, cointegration pre-check, spurious-regression warning) |
| P4 | Transformations | What must change before modelling? | Log / Box–Cox; regular, seasonal, fractional differencing; over-differencing check; detrending; seasonal adjustment (classical, STL, X-13 / SEATS); multiple seasonality (MSTL, TBATS, Fourier terms); filter-based decomposition (HP, BK, CF, Hamilton regression filter) and its end-point problem; model-based decomposition (Beveridge–Nelson, unobserved components); SSA; break handling (segmenting, regime dummies, time-varying parameters); retest loop |
| P5 | Representation selection | Which mathematical object is modelled? | Six representation sub-charts (section 7.2). Owns representation-specific leaves: periodogram, Welch, multitaper, ARMA spectral estimate, Lomb–Scargle, leakage and tapering, Nyquist; cross-spectrum, coherence, phase; FIR / IIR design, phase distortion, zero-phase filtering; STFT, CWT, DWT / MODWT, synchrosqueezing, wavelet denoising; EMD / HHT, analytic signal, instantaneous frequency, phase synchronisation; Takens embedding, DMD; functional representation (basis, smoothing, FPCA); ARIMA in state-space form |
| P6 | Conditional-mean model class | Which family describes the mean? | Routing variables: univariate vs multivariate flag, global vs local flag, exogenous-variable availability (future known / co-forecast / none). Univariate linear (AR, MA, ARMA, ARIMA, SARIMA, ARIMAX / SARIMAX, DLM / ADL, transfer function, ETS, Theta); periodic AR; intermittent demand (Croston, TSB); long memory (ARFIMA); nonlinear (TAR / SETAR, STAR, Markov-switching, bilinear, kernel and local polynomial, GAM); time-varying parameters (TVP regression, TVP-VAR); multivariate (VAR, SVAR, VECM, factor models SFM / DFM, regularised VAR, graphical models, tensor AR, FAVAR, mixed-frequency VAR, MIDAS); structural state-space (local level, local linear trend, BSTS, dynamic linear models); system identification (ARX, ARMAX, Box–Jenkins transfer functions, subspace N4SID, Hammerstein–Wiener, SINDy); count and categorical GLM-type (GLARMA, dynamic GLM) via B1; ML / DL (trees, GP regression, reservoir computing, RNN / LSTM / GRU, TCN, transformers, S4 / Mamba, N-BEATS / N-HiTS / TiDE, foundation models, hybrid); global models |
| P7 | Error-process specification | What process do the innovations follow? | Section 6 |
| P8 | Estimation | How are parameters obtained? | OLS / GLS / FGLS (Cochrane–Orcutt, Prais–Winsten); Yule–Walker, method of moments; Durbin–Levinson, innovations algorithm, Hannan–Rissanen, Burg; exact vs conditional likelihood (prediction-error decomposition, Kalman); MLE / QMLE; GMM; Whittle and local Whittle; FMOLS / DOLS; M-estimation and LAD; Bayesian (MCMC, Gibbs, Metropolis–Hastings, variational inference); EM for state space; particle filters; simulation-based inference (ABC, indirect inference); empirical loss (SGD, boosting), time-aware hyperparameter tuning, leakage-safe splits; convergence and numerical issues |
| P9 | Diagnostics and model selection | Does the fitted model hold up? | Residual tests (Ljung–Box, Breusch–Godfrey, Durbin–Watson, ARCH-LM, McLeod–Li, Jarque–Bera, BDS); volatility diagnostics (standardised residuals, sign-bias, news impact curve); count diagnostics (overdispersion, zero inflation); information criteria (AIC, BIC, HQIC, WAIC, LOO); bootstrap (block, stationary, sieve); forecast comparison (Diebold–Mariano, Clark–West, reality check, model confidence set, encompassing); loops back to P6 or P7 |
| P10 | Inference and interpretation | What does the model say, for this purpose? | Coefficient tests (t, F, LR, Wald, LM); HAC inference (Newey–West, bandwidth); cointegration inference (Engle–Granger, Johansen, ARDL bounds); causality (Granger, Sims, Toda–Yamamoto, transfer entropy, CCM, PCMCI); SVAR identification (Cholesky, sign restrictions, long-run, proxy / external instruments); IRF / FEVD; local projections; counterfactuals (intervention analysis, interrupted time series, DiD, synthetic control, CausalImpact); forecasting (point, intervals analytical / bootstrap / conformal, density, quantile, multi-step recursive / direct / MIMO, hierarchical and temporal reconciliation incl. MinT, combination / BMA, judgmental adjustment); nowcasting (MIDAS, bridge equations, DFM); risk measures (VaR, ES) and their backtests (Kupiec, Christoffersen); scenario simulation and stress testing; interpretability (SHAP, attention) |
| P11 | Validation and deployment | Does it work out of sample and keep working? | Rolling-origin CV, backtesting, backtest overfitting and look-ahead bias; metrics by purpose (RMSE / MAE / MAPE / MASE, interval coverage, CRPS, pinball, log score, PIT; F1; event-level precision / recall, NAB; detection delay and false-alarm rate); documentation; drift monitoring (KL, spectral shift, BOCPD, ADWIN, Page–Hinkley, DDM); statistical process control (Shewhart, EWMA, CUSUM charts); online updating (recursive least squares, forgetting factors, online Kalman, online gradient); retraining policy |

**Cross-cutting layers.** Three kinds of content have no phase of their own and appear as `ref` nodes inside the phases that use them: Part 0 foundations; simulation methods (Monte Carlo, bootstrap variants, simulation-based inference; referenced from P8, P9, P10); applied-domain case studies (referenced at terminals).

**Part 0 contents.** Derived bottom-up from the roots of the why-chains (section 9.3). Currently identified roots: independence and factorisation of joint densities; chain rule of probability; Kolmogorov extension theorem; monotonicity and additivity of the log; LLN and CLT for dependent data; delta method; strict and weak stationarity; ergodicity (why one realisation suffices); mixing; white noise vs martingale difference vs independence; Wold decomposition; L² projection theorem and best linear prediction; conditional expectation as the MSE-optimal forecast (the reason the book's primary notation is the conditional-expectation form); Bayes' rule; KL divergence; lag-operator algebra, difference equations, characteristic roots, causality and invertibility; Markov chains; random walks and unit roots; Brownian motion, Itô basics, Lévy processes; exact discretisation of OU to AR(1); point-process intensity; Toeplitz covariance structure. Files: `logic-of-statistical-analysis.md`, `do-you-need-time-series-analysis.md`, `ols-assumptions.md` (renamed from `overview.md`), `stochastic-processes.md` (new), `asymptotics.md` (new).

## 5. P1: data-type gate and branches

### 5.1 Routing variables

Asked in order. Each is one decision diamond; method names go on edges.

| Variable | Values | Effect |
|---|---|---|
| Value type | continuous real / counts / categorical or ordinal / compositional / curves / event times | Continuous stays on the spine; counts, categorical, compositional → B1; curves → B4; event times → B2 |
| Sampling | regular / irregular / mixed frequency | Irregular → B3; mixed frequency sets a flag read by P6 and P10 (MIDAS, bridge equations, mixed-frequency VAR, DFM nowcasting) |
| Cross-sectional structure | single / few related / many similar / wide panel N ≫ T / spatial or network index | Few related sets the multivariate flag (P3 CCF, P6 VAR); many similar → B7; wide panel → B6; spatial → B5 |

Flags use the existing notation: a `process` node labelled "Set flag: …"; downstream decision diamonds read the flag.

### 5.2 Branches

Each branch is a reference-axis chapter. Internally each follows the phase logic in compressed form (diagnose → transform → model class → error process) and rejoins the spine where stated.

| Branch | Areas | Content | Rejoins |
|---|---|---|---|
| B1 Counts and categorical | 16 | INAR, Poisson autoregression / INGARCH, GLARMA / dynamic GLM, negative binomial; Markov chains, autoregressive logit / probit, multinomial; compositional log-ratio. Diagnostics: overdispersion, zero inflation | P8; P9 with branch diagnostics |
| B2 Event times | 17, 14, 26 | Poisson, renewal, Cox, Hawkes, marked point processes; durations (ACD); survival and hazard (Cox PH); degradation processes and remaining useful life. Residuals: time-rescaling theorem | P8 |
| B3 Irregular sampling and continuous time | 15, 11, 13 | One of four: resample back to P0 (drawn `-.->`, the only backward edge out of the gate); unequal-interval Kalman; OU, CARMA, SDE discretisation (Euler–Maruyama, Milstein); Lomb–Scargle spectrum | P5 or P8 |
| B4 Functional | 14 | Basis representation and smoothing, FPCA, functional regression, functional autoregression | P5 (functional representation) → P8 |
| B5 Spatial and network | 20 | Moran's I; spatial panel VAR, spatial error / lag; kriging, spatio-temporal GP; graph signal processing, STGNN, network autoregression | P8 |
| B6 Wide panel | 32 | Panel unit roots and cointegration; FE / RE, dynamic panel GMM; heterogeneous panels (MG / PMG); cross-sectional dependence (CD test, CCE) | P8, P10 |
| B7 Many similar series | 22, 18, 34, 19 | Global vs local choice; hierarchy detection → P10 reconciliation; cluster-then-local; foundation models | Stays on the spine with the global flag set for P6 |

B7 has no area directory of its own; its leaves live in areas 22, 18, 34, 19 and its sub-chart lives in the P1 chapter.

## 6. P7: error-process specification

Input: residuals of the P6 mean model, $\hat\varepsilon_t = y_t - \hat{\mathbb{E}}[y_t \mid \mathcal{F}_{t-1}]$. Output: a complete innovation specification (mean structure, variance structure, distribution, cross-series dependence) that, with the P6 mean model, forms one joint model handed to P8 for joint estimation. This is where the book's entry thesis lands: Cochrane–Orcutt two-step estimation is replaced by joint MLE.

### 6.1 Question order

The order is a derivation chain in itself and is stated at the top of the chapter: each step's test assumes the previous step's structure has been removed. ARCH-LM assumes no serial correlation; distribution tests run on standardised residuals and assume the variance model is fixed; correlation tests run on each series' standardised residuals.

| Step | Question | Tests (on edges) | Branches → terminals |
|---|---|---|---|
| 1 | Mean dependence left? | Ljung–Box, Breusch–Godfrey, residual ACF | None → step 2. Short memory → ARMA errors (regression + ARMA errors = ARIMAX). Slow decay → ARFIMA errors. Already ARMA and still dependent → `-.->` back to P6 to raise the order |
| 2 | Second-moment dependence? | ARCH-LM, McLeod–Li, squared-residual ACF | None → step 3. Present → step 2a |
| 2a | Which variance process? | Sign-bias test, squared-residual ACF decay, availability of high-frequency data | Symmetric → GARCH. Asymmetric → EGARCH / GJR / TGARCH. Long memory → FIGARCH. Persistence ≈ 1 → IGARCH. Risk premium → GARCH-M. Latent-variance preference → SV. Realised measures available → HAR-RV / Realized GARCH |
| 3 | Distribution of standardised innovations? | Jarque–Bera, QQ, Hill tail index, BNS jump test | Gaussian → full MLE. Heavy tails → Student-t / GED, or QMLE with sandwich SE. Skew → skewed-t. Extreme tails → EVT (POT / GPD). Jumps → jump diffusion |
| 4 | Regimes in variance? | ICSS variance breaks, Markov-switching LR | None → step 5. Present → MS-GARCH / segmented variance |
| 5 | Several series? Innovation correlation structure? | Constant-correlation test (Engle–Sheppard), tail dependence | Single → terminal. Constant → CCC. Time-varying → DCC / BEKK. Non-Gaussian dependence → copula |
| 6 | Branch data types | Overdispersion tests; time-rescaling KS test | Counts → INGARCH / negative-binomial innovations. Point processes → intensity misspecification → change kernel or add marks |

Terminals name **model → estimator → inference**, for example: regression + ARMA errors + GARCH-t → joint MLE → asymptotic-normal SE.

### 6.2 Part 0 hooks

Each branch carries a `ref` to a specific section of the stochastic-processes chapter. This is the operational form of "stochastic processes for residual modelling".

| Branch | Stochastic-process concept | Example chain link |
|---|---|---|
| Step 1 terminal "white noise" | White noise vs martingale difference vs independence: three definitions of increasing strength | Ljung–Box tests only uncorrelatedness and cannot detect ARCH, because ARCH is a martingale difference but not independent |
| ARMA errors | Wold decomposition | Any covariance-stationary process is MA(∞); ARMA is its rational approximation, so ARMA for residual correlation is general |
| ARFIMA errors | Long memory, hyperbolic autocovariance decay | Why no finite-order ARMA can reproduce it |
| GARCH family | Weak stationarity $\alpha + \beta < 1$; strict stationarity $\mathbb{E}[\log(\alpha z^2 + \beta)] < 0$ | IGARCH is strictly stationary with infinite unconditional variance: the first place the two stationarity notions have different consequences |
| SV | Latent process, filtering | Why the likelihood has no closed form and needs MCMC or particle filtering |
| Jump diffusion | Brownian motion, Poisson jumps, Lévy processes | Quadratic-variation split into continuous and jump parts |
| Markov switching | Hidden Markov chain | Hamilton filter |
| Point processes | Conditional intensity, time-rescaling theorem | Under the true intensity, rescaled event times are a unit Poisson process |
| Copula | Sklar's theorem | Marginals and dependence separate |

The P7 chapter also carries a summary table: process ↔ dependence captured ↔ stationarity condition ↔ estimator.

### 6.3 Relation to P9

P7 is specified once. After joint estimation in P8, P9 re-runs steps 1–5 on the complete model and loops back to P6 or P7 on failure.

## 7. Purpose and representation charts as indexes

### 7.1 Purposes (P2 chapter)

Ten purpose sub-charts. Purposes 9 and 10 are new: 9 is split from the former "spectral analysis and system identification" and carries area 33; 10 carries area 25, which otherwise appears only as `ref` nodes.

| # | Purpose | P10 inference | P11 metrics |
|---|---|---|---|
| 1 | Forecasting | Point and interval, multi-step strategies, combination, reconciliation | Rolling CV, RMSE / MAE / MASE, coverage, CRPS |
| 2 | Causal and structural inference | Identification, IRF / FEVD, local projections, counterfactuals, placebo tests | Robustness across specifications, pre-trends |
| 3 | Signal extraction and denoising | Filters, Kalman smoothing | SNR, spectral comparison, phase distortion |
| 4 | Change-point detection | Locations with confidence intervals | Detection delay, false-alarm rate |
| 5 | Anomaly and regime detection | Thresholds, regime probabilities | Event-level precision / recall, NAB score |
| 6 | Decomposition | Component interpretation | Residual white-noise check, revision stability |
| 7 | Feature extraction, classification and clustering | Feature importance, prototypes | Downstream CV, F1, silhouette |
| 8 | Spectral analysis | Peak significance, coherence, phase | Fisher's g-test, confidence bands |
| 9 | System identification | Transfer function, poles and zeros, stability | Prediction error, cross-validated fit |
| 10 | Simulation and scenario generation | Path simulation, stress testing, synthetic data | Distribution matching, bootstrap coverage |

Fixed structure of every purpose sub-chart: purpose-specific preliminary questions → spine phases in order, with this purpose's emphasis marked → purpose-specific leaves, if any → this purpose's P10 inference → this purpose's P11 metrics. The reader's route is the spine; a chart indexes it and may omit phases but never reorders them. The spine's purpose-flag diamonds (P6 entry, P10, P11) make every purpose's route total. A chart that refs a phase's leaves also draws that phase's box.

### 7.2 Representations (P5 chapter)

Six representation sub-charts: time domain, frequency domain, time–frequency, state space, functional, Hilbert / phase. Fixed structure: when to choose this representation (three discriminating questions) → representation-specific leaves (transforms and estimators) → available P6 model families as `ref` → back to P6. The state-space sub-chart's model families are all `ref` to P6 (structural models) and P8 (Kalman, EM, particle filters); its owned leaves are the state-space rewriting of ARIMA, latent states and missing observations, Takens embedding, and dynamic mode decomposition.

### 7.3 Index rules

1. Any node that belongs to another phase is drawn as a `[[ ]]` subroutine box with the `ref` class, carries that leaf's canonical label, and resolves to the same section.
2. The now-empty "Quick Navigation" sections become tables: purpose or representation → emphasised phases → key leaves.
3. The landing page's Quick Start anchors into purposes and representations are kept.
4. File layout: `01-workflow/p02-purpose/index.md` plus one page per purpose; `01-workflow/p05-representation/index.md` plus one page per representation.

## 8. The 34 areas

Numbering appends 27–34; the original 26 numbers are unchanged. The landing page groups areas into tabs, not by number, and the glossary YAML comments are keyed by number.

| # | Area | Phases where its leaves live |
|---|---|---|
| 1 | Math foundations | Part 0; `ref` from P3, P6, P7, P8 |
| 2 | Fundamentals | P3, P4 |
| 3 | Classical | P4 decomposition, P5 periodogram, P6 ARIMA / ETS / DLM / ADL / transfer function |
| 4 | Estimation | P8 |
| 5 | Hypothesis testing | P3 unit root / breaks / nonlinearity, P9 serial correlation / normality, P10 causality / cointegration |
| 6 | Model selection | P9, P11 |
| 7 | Long memory | P3 Hurst / GPH, P6 ARFIMA, P7 FIGARCH, P8 local Whittle |
| 8 | Nonlinear | P3 tests, P6 TAR / STAR / MS / bilinear / nonparametric, P9 BDS |
| 9 | Multivariate | P3 CCF, P6 VAR / VECM / factor / regularised / tensor, P10 IRF |
| 10 | Volatility | P7, P9 volatility diagnostics, P10 VaR / ES |
| 11 | State space | P1 irregular branch, P6 structural / UC models, P8 Kalman / EM / particle filters |
| 12 | Bayesian | P6 BVAR / TVP-VAR, P8 MCMC / VI, P9 WAIC / LOO, P10 posterior predictive |
| 13 | Spectral | P5 |
| 14 | Functional and high frequency | P1 curve and event-time branches, P5 functional representation, P7 realised volatility / microstructure |
| 15 | Continuous time | P1 irregular / continuous branch; Part 0 Brownian motion / Itô |
| 16 | Count and categorical | P1 count branch, P9 overdispersion |
| 17 | Point processes | P1 event-time branch, P7 time-rescaling residuals |
| 18 | ML and DL | P6 models, P8 empirical loss / tuning, P10 conformal / interpretability |
| 19 | Classification, clustering, anomaly | P2 purpose leaves, P11 event-level metrics |
| 20 | Spatio-temporal | P1 spatial branch |
| 21 | Causal | P2 purpose 2, P10 |
| 22 | Forecasting theory and practice | P2 purpose 1, P10, P11 |
| 23 | Online learning | P11 |
| 24 | Robust and nonparametric | P0 robust filtering, P3 Mann–Kendall, P6 nonparametric, P8 M-estimation, P10 QAR |
| 25 | Simulation | P2 purpose 10; `ref` from P8, P9, P10 |
| 26 | Applied domains | Case-study `ref` at terminals. Explicit sub-domains: condition monitoring and reliability (vibration analysis: envelope, cepstrum, order tracking, spectral kurtosis; degradation processes; RUL), environmental trend methods, epidemiology (Rt estimation, SIR fitting) |
| 27 | Regression with time-series data | Part 0 entry chapters, P6 dynamic regression, P8 FGLS / Cochrane–Orcutt, P10 HAC |
| 28 | Nonstationarity theory | P3 TS vs DS / bubbles, P4 differencing, P6 VECM, P10 cointegration inference; Part 0 functional CLT |
| 29 | Seasonality and calendar | P0 calendar, P3 seasonal unit roots, P4 seasonal adjustment / MSTL, P6 periodic AR / TBATS |
| 30 | Structural change and time-varying parameters | P3 break tests, P4 break handling, P6 TVP / MS, P11 SPC / drift |
| 31 | Data preparation and missing data | P0, P1 |
| 32 | Panel time series | P1 wide-panel branch |
| 33 | System identification and dynamical systems | P5 Takens / DMD, P6 ARX / ARMAX / subspace / SINDy |
| 34 | Probabilistic forecasting and evaluation | P10 density / quantile / multi-step / reconciliation, P11 scoring rules / calibration |

Every phase receives at least one area; every area lands in at least one phase.

**Landing-page tab placement of the new areas.** 27, 28 → Theory & Inference; 29, 30, 32 → Core Models; 33 → Specialized Models; 31, 34 → ML, Forecasting & Practice.

**Naming clash.** PAR is reserved for Periodic Autoregression (the established time-series usage). Poisson autoregression is written out in full and treated as the INGARCH(p, 0) special case. The landing-page abbreviation list changes accordingly.

**Explicit exclusions.** Reinforcement learning and optimal control; time-series database engineering.

## 9. Content rules

### 9.1 Section kinds

- **Method section**: what to do and when. Must be a leaf node. Its home chapter follows the split in section 10.2.
- **Theory section**: why it holds. Need not be a node, but must be reachable (rule: `.claude/rules/writing.md`, "Section kinds"). Marked with `kind: theory` in the page's YAML front matter.
- **Heading rule.** On a page under `reference/` or `01-workflow/`, every H2 is an inventory anchor (a leaf's section) or a structural heading (`STRUCTURAL_H2` in `scripts/audit_flowcharts.py`, the one home of that list). Headings H3 and deeper under a leaf's H2 belong to that leaf and need no node of their own. An H3 or deeper heading inherits its H2's status: under a leaf's H2 it belongs to that leaf; under a structural H2, or before the first H2, it is not allowed unless it is itself a leaf's heading or the page is `kind: theory`. A glossary `reference` anchor is valid as a leaf's own heading, as an H3 or deeper under a leaf's H2, or as any heading, H2 included, on a `kind: theory` page.

### 9.2 Terminals and body text

- Outcome terminals name **model → estimator → inference** in that order (existing rule in `DESIGN-SYSTEM.md`).
- Body text states each claim in one sentence and names methods as glossary terms. Multi-step derivations never appear inline.

### 9.3 Why-chains live in the glossary drawer

The derivation chain is the study-notes layer. It lives in the drawer so body text is never interrupted.

- Each glossary term gains `derivation` (numbered "because" steps, Markdown with math) and `depends_on` (upstream term names). Part 0 terms carry `foundation: true` and are the roots.
- The drawer gains three blocks: "Why it holds" (`derivation`), "Rests on" (`depends_on`, rendered as clickable chips that open the upstream term's drawer, with a back stack and breadcrumb), and "First developed in" (`reference`).
- **Every noun that appears in a chain is itself a term with its own drawer entry.** "Joint density" is not a step inside the MLE chain; it is a term with its own definition, its own reasons, and its own dependencies.
- For time series the chain must be done correctly: the likelihood factorises by the chain rule of probability into conditional densities (prediction-error decomposition), and i.i.d. is the special case in which conditional densities reduce to marginals.

**Worked example: the standard every term meets.** The MLE chain is MLE → likelihood → joint density → chain rule → conditional densities / prediction-error decomposition → log and the law of large numbers → stationarity and ergodicity. The "joint density" entry reads, in outline:

```yaml
- term: "Joint density"
  definition: "The probability per unit volume of the whole sample (y_1, ..., y_T) regarded as one point in R^T."
  derivation: |
    1. The T observations form one point in $\mathbb{R}^T$. The joint density $p(y_1, \ldots, y_T; \theta)$ is the probability per unit volume near that point. A density is used because a continuous variable takes any exact value with probability zero; only "falls in a small neighbourhood" has positive probability, and dividing by the neighbourhood's volume gives the density. The volume factor does not depend on $\theta$, so it does not move the argmax.
    2. The object must be joint because the information about $\theta$ sits in the relations between observations. In AR(1), $\phi$ appears only in the conditional distribution of $y_t$ given $y_{t-1}$; the marginal $\mathcal{N}(0, \sigma^2/(1-\phi^2))$ confounds $\phi$ with $\sigma$. Using marginals alone discards the part being estimated.
    3. A process has a joint distribution to speak of because of the Kolmogorov extension theorem: a consistent family of finite-dimensional joint distributions determines the law of the whole process. This is also what makes the model-class definition "a family of distributions indexed by parameters" legitimate.
    4. Density and likelihood are one function read two ways. Fix $\theta$ and vary $y$: a density, integrating to one over $y$. Fix the observed $y$ and vary $\theta$: a likelihood, which does not integrate to one over $\theta$, so it is not a probability distribution of $\theta$. Adding a prior makes it one; that is the link to Bayesian estimation.
    5. "Highest data density" means "most reasonable $\theta$" because $\frac{1}{T}\log L(\theta) \to \mathbb{E}[\log p(y; \theta)]$, and maximising that minimises $\mathrm{KL}(\text{truth} \,\|\, p_\theta)$. MLE picks the model closest to the truth in KL divergence, even when the model class is wrong (the QMLE pseudo-true value).
  depends_on: ["Probability density", "Independence", "Kolmogorov extension theorem", "KL divergence", "Law of large numbers"]
  reference: "reference/04-estimation/maximum-likelihood.md#joint-density"
```

### 9.4 Single source

- Every concept has one home: the section where it is first developed in reading order (the `nav:` order). The glossary `reference` field points there, and the drawer shows it as "First developed in".
- The first occurrence develops the concept in full. Every later occurrence writes only the term name, which the glossary highlights and links. Authors do not re-explain.
- Part 0 takes only two kinds of concept: those needed before any method can be stated (stochastic process, stationarity, white noise, conditional expectation) and those used across several phases with no natural home (LLN / CLT, Kolmogorov extension). Everything else is homed at first use; joint density is homed in the MLE section.
- Appendix pages such as "Statistical tests reference" and "Datasets and resources" are pure link indexes pointing at homes; they contain no explanations.

These rules are to be carried into `DESIGN-SYSTEM.md` (writing tier) and into `.claude/rules/writing.md`, which `CLAUDE.md` already references but which does not yet exist.

## 10. Conventions

### 10.1 Node IDs and labels

- `<OWNER>_<SEMANTIC_NAME>` in SCREAMING_SNAKE_CASE, where OWNER is the owning sub-diagram: `P3_ADF`, `P7_GARCH`, `B2_HAWKES`, `P2_CPD_PELT` (purpose 4, change-point), `P5_TF_CWT`. Master-diagram phase boxes are `P0` … `P11`.
- `ref` nodes reuse the owner's ID verbatim. Mermaid requires uniqueness only within one diagram, so a `ref` never collides with the definition.
- **Leaf definition.** A defined node drawn as a rectangle `[ ]` (including outcome rectangles carrying `good` / `escalate` / `problem`) is a leaf and must have an inventory row. Decision diamonds `{ }`, terminators `([ ])`, parallelograms `[/ /]` (data in/out), `ref` subroutine boxes `[[ ]]`, and flag nodes (ID suffix `_FLAG`) are not leaves.
- **Audit opt-out.** A diagram containing the comment line `%% audit: skip` inside its fence is excluded from the audit. Only the illustrative diagrams on the Part 0 gateway chart page and the design-system showcase may carry it (`AUDIT_SKIP_PAGES`); on any other page the marker is an error and the diagram is audited.
- **Owner prefix on every defined ID.** Decision and terminator nodes carry the owner prefix too (`P7_MULTI`, `P1_IN`), because the audit checks uniqueness of every defined ID across the book.
- Leaf label is the short form of the section title. Linkage is through the inventory ID; the first line of a node's label (the text before `<br/>`) equals the inventory `label`, for leaves and for `ref` nodes, and the audit checks the equality.
- **Parsing is total.** `%%` comment lines define nothing; `subgraph` headers are clusters, never nodes. Every token in a node position is read, and a non-SCREAMING_SNAKE_CASE ID, a shape outside the notation, one ID drawn with two shapes in one diagram, or an inline `:::class` is an audit error.
- Notation (shapes, `classDef` sets, quoting, edge semantics, direction, `class` statements) follows "Decision-flowchart notation" in `DESIGN-SYSTEM.md` unchanged.
- Mermaid blocks contain no URLs. Links are resolved at runtime (section 10.5). A `click` directive, `href=` or `http(s)://` in a diagram that does not opt out is an audit error.

### 10.2 File layout and navigation

```
docs/
  00-foundations/                   renamed from 00-introduction; Part 0
    logic-of-statistical-analysis.md
    do-you-need-time-series-analysis.md
    ols-assumptions.md              renamed from overview.md
    stochastic-processes.md         new
    asymptotics.md                  new
  01-workflow/
    index.md                        master diagram
    p00-data.md
    p01-data-type-gate.md
    p02-purpose/                    index.md + one page per purpose (10)
    p03-exploratory-diagnostics.md
    p04-transformations.md
    p05-representation/             index.md + one page per representation (6)
    p06-mean-model-class.md
    p07-error-process.md
    p08-estimation.md
    p09-diagnostics-selection.md
    p10-inference.md
    p11-validation-deployment.md
  reference/
    01-math-foundations/ … 34-probabilistic-forecasting/
                                    one directory per area; nav groups them under the five landing-page tabs
  appendices/                       link-index pages only: tests index, datasets, software ecosystem, Python setup
  flowcharts/inventory.yml          leaf-node inventory (served; read at runtime and by the audit)
  glossary/<page>.yml               one glossary file per reference page, named after the page stem, or after its directory when the page is an index.md (stochastic-processes, p03-exploratory-diagnostics, 04-estimation); a term lives in the file of its reference page
  glossary/index.yml                generated list of glossary files (gitignored; written by the pre-build hook)
```

- Workflow chapters hold procedural leaves (P0, P3, P4, P9, P11 items such as ADF, differencing, Ljung–Box, rolling CV). Reference chapters hold model families, transforms, estimators and theory (P5, P6, P7, P8 and the B branches).
- File names carry the phase ID or the area number, so chapter numbering cannot drift. Flowchart nodes never carry "Ch N" labels.
- The current `02-data-preparation` … `07-validation-deployment` directories merge into the corresponding workflow pages during implementation.
- `nav:` order: Foundations → Workflow (master, P0–P11) → Reference (five groups) → Appendices → Design System Showcase.

### 10.3 Paths

Both the inventory and the glossary use `docs/`-relative source paths with the `.md` extension and a heading anchor, for example `reference/10-volatility/garch.md#garch-family`. JavaScript converts them to site URLs (strip `.md`, directory URL, anchor). Anchors must equal the Python-Markdown `toc` default slugify of the heading text, which is what MkDocs generates; inventory and glossary targets must be heading anchors (the audit reads the rendered heading ids), so `<a id>` tags, attr-list ids on paragraphs and footnote ids are not targets. The existing glossary `reference` values (site paths ending in `.html#…`) are converted during migration.

### 10.4 Inventory format

`docs/flowcharts/inventory.yml`:

```yaml
nodes:
  - id: P7_GARCH
    label: "GARCH family"
    phase: P7            # P0–P11, B1–B7, MASTER (phase boxes) or F (Part 0 sections)
    areas: [10]
    section: "reference/10-volatility/garch.md#garch-family"
```

One row per leaf node. Decision, flag and terminal nodes are not listed. Master phase boxes `P0`–`P11` are leaves (phase `MASTER`) whose sections are the phase pages. Rows of phase `F` are Part 0 sections: they have no diagram definition and must be referenced by at least one `ref` node.

**Row validation.** Every row is a mapping. `id` is a string matching `^[A-Z][A-Z0-9_]*$`; `label` is a non-empty string; `phase` is one of P0–P11, B1–B7, MASTER, F; `areas` is a list of integers in 1–34; `section` matches `path.md#anchor` and its anchor is a heading id of the rendered page. The ID prefix equals the phase (`P7_GARCH` / `P7`), with two named exceptions: `P0`–`P11` carry phase MASTER and only they do, and `B1`–`B7` carry their own ID as phase. Each phase has one owner: the page of its phase box or branch entry row (MASTER: `01-workflow/index.md`; B7: the P1 page), except P2 and P5, which are owned by their chapter directories `01-workflow/p02-purpose/` and `01-workflow/p05-representation/` because their sub-chart pages own the purpose-specific and representation-specific leaves (sections 4, 7.1, 10.1). A leaf must be defined in a diagram on its phase's owner page, or for P2 and P5 on any page in the owner directory. A YAML parse error, a duplicate key or a type error is a finding naming the file, never a traceback.

### 10.5 Runtime node linking

New script `docs/javascripts/flowchart-links.js`. After `mermaid-init.js` inserts a rendered container it dispatches `mermaid:rendered`; flowchart-links also scans containers already rendered when it loads, so script order does not matter. The script loads `flowcharts/inventory.yml` once (js-yaml is already loaded), matches each SVG node whose id matches `^flowchart-(.+)-\d+$` against inventory IDs, and attaches a click handler navigating to the section URL plus a hover title showing label and area numbers. `securityLevel` stays as is; Mermaid `click` directives are not used.

The section-to-URL mapping lives once, in `docs/javascripts/site-urls.js` (`window.tsamSite.docUrl`, loaded first; the root `index.md` maps to the site root), and glossary links use the same helper. `mkdocs.yml` sets `use_directory_urls: true` explicitly, because the mapping depends on it. Fetches check `response.ok` and log the URL on failure. Mermaid is pinned to an exact version (`mermaid@10.9.8`), because the SVG id format is the linking contract, and fences are emitted as `div.mermaid` so `mermaid-init.js` is the only renderer. A Playwright smoke test (`tests/e2e/test_site_smoke.py`) builds and serves the site and clicks a leaf.

### 10.6 Glossary schema

```yaml
terms:
  - term: "…"
    definition: "…"
    mathematical: |           # existing
    historical: |             # existing
    derivation: |             # new: numbered "because" steps
    depends_on: ["…", "…"]    # new: upstream term names
    foundation: true          # new, Part 0 roots only
    reference: "path.md#anchor"   # semantics: first developed in
```

`glossary.js` changes: load the file list from `glossary/index.yml` instead of the hard-coded `GLOSSARY_CHAPTERS`; replace `ENABLED_PATHS` with a short disabled list (home page, design-system showcase); render the three new drawer blocks; drawer-to-drawer navigation from term data with a back stack.

## 11. Audit

`scripts/audit_flowcharts.py`, run in CI on every pull request to `main` and every push to `main`, before `mkdocs build --strict`, exits non-zero on any error. Precedent: `scripts/audit_palette.py`. It renders every page with the MkDocs configuration (`mkdocs.yml` `markdown_extensions`, front matter stripped as MkDocs does), so diagram sources, heading ids and link targets are those of the built site: fences indented in admonitions or tabs, `~~~`, four-backtick and snippet fences are all seen, and anchors are the rendered toc ids.

| Object | Check | Severity |
|---|---|---|
| Mermaid nodes | Defined (non-`ref`) IDs unique across all diagrams; every `ref` ID has a definition; every defined leaf ID has an inventory row; every inventory ID is defined in some diagram; label first line equals the inventory label; the parsing and no-URL rules of section 10.1 | error |
| Inventory | Row validation of section 10.4; `section` file exists; anchor is a rendered heading id | error |
| Sections | Every non-index `.md` under `reference/` and `01-workflow/` is referenced by an inventory row (method) or, if `kind: theory`, is reachable (rule: `.claude/rules/writing.md`, "Section kinds") | error |
| Headings | The heading rule of section 9.1 on every page under `reference/` and `01-workflow/`, index pages included: each H2 is an inventory anchor or a `STRUCTURAL_H2` entry (or a glossary anchor on a `kind: theory` page); each glossary `reference` anchor is a leaf's own heading, an H3 or deeper under a leaf's H2, or a heading on a `kind: theory` page | error |
| Glossary | Every `depends_on` is a list of names that resolve to terms; every chain terminates at a `foundation: true` term; a foundation term is homed under `00-foundations/` and has no `depends_on`; any other term is homed under `reference/`, `01-workflow/` or `00-foundations/`, never on appendices, the home page or the showcase; no cycles, each reported once; `reference` anchor exists; no duplicate keys, so exactly one `reference` per term; each term sits in the glossary file named after its reference page. A term with no `depends_on` key is a chain not yet written and is reported as a warning; a term with an empty `depends_on` and no `foundation: true` is a dead end and is an error | error |
| Glossary | Scan every `nav:` page in order except the pages where the glossary is disabled (`GLOSSARY_DISABLED_PAGES`: the home page and the design-system showcase, which also feed the drawer through `glossary/index.yml`); list terms whose first-mention page differs from the `reference` page, for manual review | warning |

Node classification in Mermaid: a node is `ref` when it uses the `[[ ]]` shape or is assigned the `ref` class; otherwise it is defined. Among defined nodes, leaf status follows the shape rule in section 10.1. `index.md` pages are exempt from the page-level sections check, not from the heading check.

CI also switches `mkdocs build` to `--strict`, as `CLAUDE.md` already requires, and runs on `pull_request` so the gates block a merge rather than a deploy; only a push to `main` deploys. The glossary file index is written by a MkDocs `on_pre_build` hook (`scripts/mkdocs_hooks.py`), which also logs audit errors as build warnings so `--strict` fails on them; the hook rewrites the index only when its content changed, so `mkdocs serve` does not loop.

## 12. Migration from the current state

- Rename `docs/00-introduction/` → `docs/00-foundations/`, `overview.md` → `ols-assumptions.md`; update nav labels ("Introduction" → "Foundations") and the landing page's description of the section.
- Replace the three flowchart files with the workflow structure of section 10.2. The legacy files move to `planning/legacy-flowcharts/` (outside the site) so later plans can mine their diagrams and Phase-by-Phase Guide prose.
- Create `reference/` with 34 area directories and stub `index.md` pages that state the area's leaves (from the inventory) as a to-do list.
- Create `docs/flowcharts/inventory.yml` with every leaf drawn in the new diagrams.
- Convert existing glossary `reference` values to source paths; add `derivation`, `depends_on`, `foundation` to existing terms where the chain is already written in the body (OLS assumptions, i.i.d., full column rank).
- Implement `flowchart-links.js`, the glossary changes, `mkdocs_hooks.py`, `audit_flowcharts.py`, `scaffold_stubs.py`, and the CI changes.
- Landing page: 34 areas in tabs; PAR abbreviation fix; Quick Start anchors re-pointed.
- `book_plan.md`: add a pointer to this document at the top.
- README: remove or satisfy the references to `code/`, `CONTRIBUTING.md`, `LICENSE`, `LICENSE-CODE`.
- `CLAUDE.md`: fix the chapter list (00–07 → the three axes) and create `.claude/rules/writing.md` carrying section 9.

## 12b. Phasing

The framework is implemented before content is written, in two separate plans.

1. **Plan A — skeleton and tooling.** Directory layout, `nav:`, the master diagram, the P1 and P7 sub-diagrams, the P2 and P5 selector diagrams, one-node entry stubs for B1–B6, the inventory for what is drawn, stub reference pages, `flowchart-links.js`, glossary schema and drawer changes, the MkDocs hook (glossary index + audit warnings), `audit_flowcharts.py`, `scaffold_stubs.py`, CI. Ends when acceptance criteria 1, 2, 4, 5, 6 pass on stubs. Plan: `planning/2026-10-06-flowchart-skeleton-plan.md`.
2. **Plan B — remaining diagrams.** Sub-diagrams for P0, P3, P4, P6, P8–P11, the ten purpose sub-charts, the six representation sub-charts, B1–B7, with their inventory rows and scaffolded stubs. Ends when acceptance criterion 3 passes (every area has a leaf).
3. **Plan C — content migration and writing.** Move existing prose into its home sections, re-point glossary references from phase-page anchors to their own sections, then write sections phase by phase following section 9.

## 13. Open items

- **Depth cap per leaf section.** Not decided. The why-chain moved to the drawer, so body sections are shorter than first estimated; a cap is still needed for planning volume.
- **Theory-section detection.** The `kind: theory` front-matter marker is the proposed mechanism; confirm during implementation that MkDocs Material does not render the key.
- **First-mention warning noise.** The warning-level glossary scan is noisy where a page mentions many later-homed terms as examples: Part 0, and the temporary phase-page homes until each term is re-pointed to its own leaf. Pages where the glossary is disabled (home, showcase) are not scanned. Keep it a warning and review after each round.

## 14. Acceptance criteria for the implementation plan

1. `mkdocs build --strict` passes.
2. `scripts/audit_flowcharts.py` passes with zero errors on the new skeleton: every drawn leaf has an inventory row and a target section (stub pages count), every `ref` resolves, no duplicate definitions.
3. Every one of the 34 areas has at least one leaf node in some sub-diagram, verified from the inventory's `areas` field.
4. Clicking a leaf node in the rendered site navigates to its section; opening a glossary term with `depends_on` shows chips that open the upstream drawer and allow returning.
5. The P7 sub-diagram's terminals each name model → estimator → inference, and each of its branches carries a `ref` into `00-foundations/stochastic-processes.md`.
6. No "Ch N" labels remain in any diagram or phase guide.
