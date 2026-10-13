# P7: Error-process specification

**Question this phase answers:** What process do the innovations follow?

P7 reads the model-kind flag first. A learner fitted by loss minimisation gets an output distribution or quantile heads chosen from the forecast task, because it has no likelihood for a variance model to enter. A likelihood or Bayesian model is fitted once by the class's default consistent method (OLS or conditional least squares for linear classes), because residuals exist only after a fit; the error questions are asked on those residuals: remaining mean dependence, variance regimes, conditional heteroskedasticity, distribution, cross-series dependence, and the count and event-time variants. The output is a joint model that P8 estimates jointly, usually by maximum likelihood; feasible GLS (Cochrane-Orcutt, Prais-Winsten) is the classical approximation for AR(p) errors with strictly exogenous regressors, and fitting ARMA to OLS residuals and stopping leaves the regression coefficients at their OLS values.

## Sub-diagram

The order of the questions is a derivation chain: each step's test assumes the previous step's structure has been removed. Portmanteau tests are oversized under conditional heteroskedasticity, so step 1 uses heteroskedasticity-robust versions and is re-run on standardised residuals after the variance model. Variance regimes are tested before the GARCH variant, because a neglected break in the unconditional variance pushes estimated GARCH persistence towards one and makes squared residuals decay slowly. Distribution tests run on standardised residuals and assume the variance model is fixed; correlation tests run on each series' standardised residuals.

**Part 1: model kind, preliminary fit and value type.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_IN(["Candidate set and flags from P6"]) --> P7_KIND{"Model-kind flag?"}
    P7_KIND -->|"Loss minimisation"| P7_LEARNER_OUTPUT["Output distribution or quantile heads<br/>chosen from the forecast task"]
    P7_KIND -->|"Likelihood or Bayesian"| P7_PRELIM_FIT["Preliminary fit of the P6 class<br/>OLS or conditional least squares; the class default otherwise"]
    P7_LEARNER_OUTPUT --> P7_LEARNER_TO_PART_5(["Continue in part 5"])
    P7_PRELIM_FIT --> P7_TYPE{"Value-type flag?"}
    P7_TYPE -->|"Continuous, or log-ratios"| P7_TO_PART_2(["Continue in part 2"])
    P7_TYPE -->|"Categorical or curves"| P7_COUNTS_TO_PART_5
    P7_TYPE -->|"Counts"| P7_COUNT_TESTS["Test overdispersion of count innovations"]
    P7_TYPE -->|"Event times"| P7_RESCALING["Time-rescaling check of event-time residuals"]
    P7_COUNT_TESTS --> P7_INGARCH["Count innovations: Poisson or negative binomial"]
    P7_RESCALING --> P7_INTENSITY["Intensity misspecification"]
    P7_INGARCH & P7_INTENSITY --> P7_COUNTS_TO_PART_5(["Continue in part 5"])
    F_TIME_RESCALING[["Time-rescaling theorem"]] -.- P7_RESCALING
    class P7_IN,P7_LEARNER_TO_PART_5,P7_TO_PART_2,P7_COUNTS_TO_PART_5 terminator
    class P7_KIND,P7_TYPE decision
    class P7_LEARNER_OUTPUT,P7_PRELIM_FIT,P7_COUNT_TESTS,P7_RESCALING process
    class P7_INGARCH,P7_INTENSITY escalate
    class F_TIME_RESCALING ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: mean dependence.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_PART_2_IN(["From part 1: continuous"]) --> P7_MEAN_TESTS["Test residual autocorrelation<br/>Ljung–Box, heteroskedasticity-robust portmanteau, Breusch-Godfrey with a lagged dependent variable; multivariate portmanteau and LM"]
    P7_MEAN_TESTS --> P7_MEAN_DEP{"Mean dependence?"}
    P7_MEAN_DEP -->|"None"| P7_TO_PART_3
    P7_MEAN_DEP -->|"Short memory, regression flag"| P7_ARMA_ERRORS["Regression with ARMA errors<br/>beta is a marginal effect"]
    P7_MEAN_DEP -->|"Slow decay, regression flag"| P7_ARFIMA_ERRORS["Regression with ARFIMA errors"]
    P7_MEAN_DEP -.->|"Dynamic family: raise the order"| P6[["P6: Conditional-mean model class"]]
    P7_MEAN_DEP -.->|"Unit root: spurious regression, difference every series"| P4[["P4: Transformations"]]
    P7_ARMA_ERRORS & P7_ARFIMA_ERRORS --> P7_TO_PART_3(["Continue in part 3"])
    F_WHITE_NOISE[["White noise, martingale difference, independence"]] -.- P7_MEAN_DEP
    F_WOLD[["Wold decomposition"]] -.- P7_ARMA_ERRORS
    F_LONG_MEMORY[["Long memory and hyperbolic decay"]] -.- P7_ARFIMA_ERRORS
    class P7_PART_2_IN,P7_TO_PART_3 terminator
    class P7_MEAN_DEP decision
    class P7_MEAN_TESTS process
    class P7_ARMA_ERRORS,P7_ARFIMA_ERRORS escalate
    class P6,P4,F_WHITE_NOISE,F_WOLD,F_LONG_MEMORY ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: variance regimes, then conditional variance.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_PART_3_IN(["From part 2"]) --> P7_REGIME_TESTS["Test for variance regimes<br/>kappa-2 ICSS; Hansen, Garcia, Carrasco-Hu-Ploberger tests for Markov switching"]
    P7_REGIME_TESTS --> P7_REGIME{"Variance regimes?"}
    P7_REGIME -->|"Present"| P7_MS_GARCH["Markov-switching GARCH and segmented variance"]
    P7_REGIME -->|"None"| P7_VAR_TESTS["Test conditional heteroskedasticity<br/>ARCH-LM, McLeod-Li; multivariate ARCH-LM"]
    P7_VAR_TESTS --> P7_VAR_DEP{"Variance dependence?"}
    P7_VAR_DEP -->|"None"| P7_PART_3_TO_PART_5(["Continue in part 5"])
    P7_VAR_DEP -->|"Present"| P7_VAR_TYPE{"Variance process?"}
    P7_VAR_TYPE -->|"GARCH family"| P7_TO_PART_4(["Continue in part 4"])
    P7_VAR_TYPE -->|"Latent variance"| P7_SV["Stochastic volatility"]
    P7_VAR_TYPE -->|"Intraday data"| P7_REALIZED["Realised measures: HAR-RV and Realized GARCH<br/>BNS jump test from realised and bipower variation"]
    P7_MS_GARCH & P7_SV & P7_REALIZED --> P7_PART_3_TO_RECHECK(["Re-check in part 4"])
    F_LATENT_FILTERING[["Latent processes and filtering"]] -.- P7_SV
    F_HMM[["Hidden Markov chains"]] -.- P7_MS_GARCH
    class P7_PART_3_IN,P7_PART_3_TO_PART_5,P7_TO_PART_4,P7_PART_3_TO_RECHECK terminator
    class P7_REGIME,P7_VAR_DEP,P7_VAR_TYPE decision
    class P7_REGIME_TESTS,P7_VAR_TESTS process
    class P7_MS_GARCH,P7_SV,P7_REALIZED escalate
    class F_LATENT_FILTERING,F_HMM ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: GARCH variant and the re-check on standardised residuals.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_PART_4_IN(["From part 3: GARCH family"]) --> P7_GARCH_TYPE{"GARCH variant?"}
    P7_GARCH_TYPE -->|"Symmetric"| P7_GARCH["GARCH"]
    P7_GARCH_TYPE -->|"Asymmetric"| P7_ASYM_GARCH["Asymmetric GARCH: EGARCH, GJR, TGARCH"]
    P7_GARCH_TYPE -->|"Long memory"| P7_FIGARCH["FIGARCH"]
    P7_GARCH_TYPE -->|"Persistence near one"| P7_IGARCH["IGARCH"]
    P7_GARCH_TYPE -->|"Risk premium"| P7_GARCH_M["GARCH-in-mean"]
    P7_GARCH & P7_ASYM_GARCH & P7_FIGARCH & P7_IGARCH & P7_GARCH_M --> P7_STD_RECHECK["Re-check mean dependence on standardised residuals<br/>dependence left: back to part 2"]
    P7_PART_4_RECHECK_IN(["From part 3: regimes, latent variance, realised measures"]) --> P7_STD_RECHECK
    P7_STD_RECHECK --> P7_TO_PART_5(["Continue in part 5"])
    F_GARCH_STATIONARITY[["Stationarity conditions of GARCH"]] -.- P7_GARCH
    class P7_PART_4_IN,P7_PART_4_RECHECK_IN,P7_TO_PART_5 terminator
    class P7_GARCH_TYPE decision
    class P7_STD_RECHECK process
    class P7_GARCH,P7_ASYM_GARCH,P7_FIGARCH,P7_IGARCH,P7_GARCH_M escalate
    class F_GARCH_STATIONARITY ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: distribution, correlation and assembly.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_PART_5_IN(["From parts 1, 3 and 4"]) --> P7_TYPE_4{"Continuous innovations with a likelihood?"}
    P7_TYPE_4 -->|"Yes"| P7_DIST_TESTS["Test the distribution of standardised innovations<br/>Jarque-Bera, QQ, Hill; multivariate normality"]
    P7_TYPE_4 -->|"No: learner, counts or event times"| P7_OUT
    P7_DIST_TESTS --> P7_DIST{"Distribution?"}
    P7_DIST -->|"Gaussian"| P7_GAUSSIAN["Gaussian innovations"]
    P7_DIST -->|"Heavy tails"| P7_HEAVY_TAILS["Heavy-tailed innovations: Student-t, GED, QMLE"]
    P7_DIST -->|"Skew"| P7_SKEWED["Skewed innovations"]
    P7_DIST -->|"Extreme tails"| P7_EVT["Extreme value theory for tails"]
    P7_DIST -->|"Jumps"| P7_JUMPS["Jump diffusion<br/>GARCH-jump in discrete time"]
    P7_GAUSSIAN & P7_HEAVY_TAILS & P7_SKEWED & P7_EVT & P7_JUMPS --> P7_MULTI{"Multivariate flag?"}
    P7_MULTI -->|"No"| P7_OUT
    P7_MULTI -->|"Yes"| P7_CORR_TESTS["Test innovation correlation structure<br/>Engle-Sheppard, tail dependence"]
    P7_CORR_TESTS --> P7_CORR{"Correlation structure?"}
    P7_CORR -->|"Constant"| P7_CCC["Constant conditional correlation"]
    P7_CORR -->|"Time-varying"| P7_DCC["Dynamic conditional correlation and BEKK"]
    P7_CORR -->|"Non-Gaussian dependence"| P7_COPULA["Copula dependence"]
    P7_CCC & P7_DCC & P7_COPULA --> P7_OUT["Assemble the joint model<br/>mean + innovations, estimated jointly in P8"]
    P7_OUT --> P8[["P8: Estimation"]]
    F_LEVY[["Brownian motion, Poisson jumps, Levy processes"]] -.- P7_JUMPS
    F_SKLAR[["Sklar's theorem"]] -.- P7_COPULA
    class P7_PART_5_IN terminator
    class P7_TYPE_4,P7_DIST,P7_MULTI,P7_CORR decision
    class P7_DIST_TESTS,P7_CORR_TESTS,P7_OUT process
    class P7_GAUSSIAN good
    class P7_HEAVY_TAILS,P7_SKEWED,P7_EVT,P7_JUMPS,P7_CCC,P7_DCC,P7_COPULA escalate
    class P8,F_LEVY,F_SKLAR ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Question order

| Step | Question | Tests | Branches |
|---|---|---|---|
| 0 | Model kind and value type? | Overdispersion tests for counts; time-rescaling KS test for event times | Loss minimisation: output distribution or quantile heads. Likelihood or Bayesian: preliminary fit, then the value type: continuous or compositional to step 1; counts to Poisson or negative-binomial innovations; event times to intensity misspecification; categorical series and curves to their branch model |
| 1 | Mean dependence left? | Ljung–Box, heteroskedasticity-robust portmanteau, Breusch-Godfrey with a lagged dependent variable; multivariate portmanteau and LM | None: step 2. Short memory with the regression flag: ARMA errors. Slow decay with the regression flag: ARFIMA errors. Dynamic family still dependent: back to P6. Unit root in the residuals: spurious regression; difference every series in P4 |
| 2 | Variance regimes? | kappa-2 ICSS; Hansen, Garcia and Carrasco-Hu-Ploberger tests for Markov switching | Present: MS-GARCH or segmented variance. None: step 3 |
| 3 | Second-moment dependence? | ARCH-LM, McLeod-Li, squared-residual ACF; multivariate ARCH-LM | None: step 4. Present: GARCH; EGARCH / GJR / TGARCH; FIGARCH or IGARCH, reachable only after step 2 ruled out regimes; GARCH-in-mean; stochastic volatility; HAR-RV / Realized GARCH with intraday data. Then step 1 again on standardised residuals |
| 4 | Distribution of standardised innovations? | Jarque-Bera, QQ, Hill tail index; multivariate normality | Gaussian; Student-t / GED or QMLE; skewed-t; EVT; jumps |
| 5 | Several series? | Engle-Sheppard constant-correlation test, tail dependence | CCC; DCC / BEKK; copula |

Terminals name **model → estimator → inference**; for example, regression + ARMA errors + GARCH-t → joint MLE → asymptotic-normal standard errors.

## Part 0 hooks

| Branch | Stochastic-process concept | Chain link |
|---|---|---|
| White noise terminal | White noise, martingale difference, independence | Ljung–Box tests uncorrelatedness only; ARCH errors are a martingale difference with dependent squares |
| ARMA errors | Wold decomposition | Any purely non-deterministic covariance-stationary process is MA(∞) in its white-noise linear innovations; ARMA is a rational approximation of that MA(∞) |
| ARFIMA errors | Long memory, hyperbolic decay | Why no finite-order ARMA reproduces it |
| GARCH | Weak stationarity α + β < 1; strict stationarity E[log(α z² + β)] < 0 | IGARCH is strictly stationary with infinite unconditional variance |
| Stochastic volatility | Latent process, filtering | Why the likelihood has no closed form |
| Jump diffusion | Brownian motion, Poisson jumps, Levy processes | Quadratic variation splits into continuous and jump parts |
| Markov switching | Hidden Markov chain | Hamilton filter |
| Event times | Conditional intensity, time-rescaling theorem | Under the true intensity, rescaled event times form a unit Poisson process |
| Copula | Sklar's theorem | Marginals and dependence separate |

## Relation to P9

P7 is specified once. After joint estimation in P8, P9 re-runs steps 0 to 5 on the complete model. A failed check goes to the P9 purpose gate, which keeps forecasting, detection and collection candidates for P10 and sends the other purposes back to P3, P4, P6 or P7.

## Preliminary fit of the P6 class

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_PRELIM_FIT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test overdispersion of count innovations

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_COUNT_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Time-rescaling check of event-time residuals

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_RESCALING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test residual autocorrelation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_MEAN_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test for variance regimes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_REGIME_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test conditional heteroskedasticity

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_VAR_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Re-check mean dependence on standardised residuals

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_STD_RECHECK`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test the distribution of standardised innovations

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_DIST_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test innovation correlation structure

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_CORR_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Assemble the joint model

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_OUT`). Write this section following the content rules in `.claude/rules/writing.md`.
