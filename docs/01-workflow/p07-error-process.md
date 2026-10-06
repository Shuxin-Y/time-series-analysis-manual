# P7: Error-process specification

**Question this phase answers:** What process do the innovations follow?

Given the residuals of the P6 mean model, decide the innovation process: remaining mean dependence, conditional heteroskedasticity, distribution, variance regimes, cross-series dependence, and the count and event-time variants. The output is a joint model handed to P8 for joint estimation, which is where Cochrane-Orcutt two-step estimation is replaced by joint maximum likelihood.

## Sub-diagram

The order of the questions is itself a derivation chain: each step's test assumes the previous step's structure has been removed. ARCH-LM assumes no serial correlation; distribution tests run on standardised residuals and assume the variance model is fixed; correlation tests run on each series' standardised residuals.

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P7_IN(["Residuals of the P6 mean model"]) --> P7_TYPE{"Innovation type?"}
    P7_TYPE -->|"Continuous"| P7_MEAN_TESTS["Test residual autocorrelation<br/>Ljung-Box, Breusch-Godfrey, ACF"]
    P7_TYPE -->|"Counts"| P7_COUNT_TESTS["Test overdispersion of count innovations"]
    P7_TYPE -->|"Event times"| P7_RESCALING["Time-rescaling check of event-time residuals"]
    P7_COUNT_TESTS --> P7_INGARCH["INGARCH and negative-binomial innovations"]
    P7_RESCALING --> P7_INTENSITY["Intensity misspecification"]
    P7_INGARCH & P7_INTENSITY --> P7_OUT
    P7_MEAN_TESTS --> P7_MEAN_DEP{"Mean dependence?"}
    P7_MEAN_DEP -->|"None"| P7_VAR_TESTS
    P7_MEAN_DEP -->|"Short memory"| P7_ARMA_ERRORS["Regression with ARMA errors"]
    P7_MEAN_DEP -->|"Slow decay"| P7_ARFIMA_ERRORS["ARFIMA errors"]
    P7_MEAN_DEP -.->|"Already ARMA: raise the order"| P6[["P6: Conditional-mean model class"]]
    P7_ARMA_ERRORS & P7_ARFIMA_ERRORS --> P7_VAR_TESTS["Test conditional heteroskedasticity<br/>ARCH-LM, McLeod-Li"]
    P7_VAR_TESTS --> P7_VAR_DEP{"Variance dependence?"}
    P7_VAR_DEP -->|"None"| P7_DIST_TESTS
    P7_VAR_DEP -->|"Present"| P7_VAR_TYPE{"Variance process?"}
    P7_VAR_TYPE -->|"Symmetric"| P7_GARCH["GARCH"]
    P7_VAR_TYPE -->|"Asymmetric"| P7_ASYM_GARCH["Asymmetric GARCH: EGARCH, GJR, TGARCH"]
    P7_VAR_TYPE -->|"Long memory"| P7_FIGARCH["FIGARCH"]
    P7_VAR_TYPE -->|"Persistence near one"| P7_IGARCH["IGARCH"]
    P7_VAR_TYPE -->|"Risk premium"| P7_GARCH_M["GARCH-in-mean"]
    P7_VAR_TYPE -->|"Latent variance"| P7_SV["Stochastic volatility"]
    P7_VAR_TYPE -->|"Realised measures"| P7_REALIZED["Realised measures: HAR-RV and Realized GARCH"]
    P7_GARCH & P7_ASYM_GARCH & P7_FIGARCH & P7_IGARCH --> P7_DIST_TESTS
    P7_GARCH_M & P7_SV & P7_REALIZED --> P7_DIST_TESTS["Test the distribution of standardised innovations<br/>Jarque-Bera, QQ, Hill, BNS"]
    P7_DIST_TESTS --> P7_DIST{"Distribution?"}
    P7_DIST -->|"Gaussian"| P7_GAUSSIAN["Gaussian innovations"]
    P7_DIST -->|"Heavy tails"| P7_HEAVY_TAILS["Heavy-tailed innovations: Student-t, GED, QMLE"]
    P7_DIST -->|"Skew"| P7_SKEWED["Skewed innovations"]
    P7_DIST -->|"Extreme tails"| P7_EVT["Extreme value theory for tails"]
    P7_DIST -->|"Jumps"| P7_JUMPS["Jump diffusion"]
    P7_GAUSSIAN & P7_HEAVY_TAILS & P7_SKEWED & P7_EVT & P7_JUMPS --> P7_REGIME_TESTS["Test for variance regimes<br/>ICSS, Markov-switching LR"]
    P7_REGIME_TESTS --> P7_REGIME{"Regimes?"}
    P7_REGIME -->|"None"| P7_MULTI
    P7_REGIME -->|"Present"| P7_MS_GARCH["Markov-switching GARCH and segmented variance"]
    P7_MS_GARCH --> P7_MULTI{"Several series?"}
    P7_MULTI -->|"No"| P7_OUT
    P7_MULTI -->|"Yes"| P7_CORR_TESTS["Test innovation correlation structure<br/>Engle-Sheppard, tail dependence"]
    P7_CORR_TESTS --> P7_CORR{"Correlation structure?"}
    P7_CORR -->|"Constant"| P7_CCC["Constant conditional correlation"]
    P7_CORR -->|"Time-varying"| P7_DCC["Dynamic conditional correlation and BEKK"]
    P7_CORR -->|"Non-Gaussian dependence"| P7_COPULA["Copula dependence"]
    P7_CCC & P7_DCC & P7_COPULA --> P7_OUT["Assemble the joint model<br/>mean + innovations"]
    P7_OUT --> P8[["P8: Estimation"]]
    F_WHITE_NOISE[["White noise, martingale difference, independence"]] -.- P7_MEAN_DEP
    F_WOLD[["Wold decomposition"]] -.- P7_ARMA_ERRORS
    F_LONG_MEMORY[["Long memory and hyperbolic decay"]] -.- P7_ARFIMA_ERRORS
    F_GARCH_STATIONARITY[["Stationarity conditions of GARCH"]] -.- P7_GARCH
    F_LATENT_FILTERING[["Latent processes and filtering"]] -.- P7_SV
    F_LEVY[["Brownian motion, Poisson jumps, Levy processes"]] -.- P7_JUMPS
    F_HMM[["Hidden Markov chains"]] -.- P7_MS_GARCH
    F_SKLAR[["Sklar's theorem"]] -.- P7_COPULA
    F_TIME_RESCALING[["Time-rescaling theorem"]] -.- P7_RESCALING
    class P7_IN terminator
    class P7_TYPE,P7_MEAN_DEP,P7_VAR_DEP,P7_VAR_TYPE,P7_DIST,P7_REGIME,P7_MULTI,P7_CORR decision
    class P7_MEAN_TESTS,P7_VAR_TESTS,P7_DIST_TESTS,P7_REGIME_TESTS,P7_CORR_TESTS,P7_COUNT_TESTS,P7_RESCALING,P7_OUT process
    class P7_ARMA_ERRORS,P7_ARFIMA_ERRORS,P7_GARCH,P7_ASYM_GARCH,P7_FIGARCH,P7_IGARCH,P7_GARCH_M,P7_SV,P7_REALIZED escalate
    class P7_GAUSSIAN good
    class P7_HEAVY_TAILS,P7_SKEWED,P7_EVT,P7_JUMPS,P7_MS_GARCH,P7_CCC,P7_DCC,P7_COPULA,P7_INGARCH,P7_INTENSITY escalate
    class P6,P8,F_WHITE_NOISE,F_WOLD,F_LONG_MEMORY,F_GARCH_STATIONARITY,F_LATENT_FILTERING,F_LEVY,F_HMM,F_SKLAR,F_TIME_RESCALING ref
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
| 1 | Mean dependence left? | Ljung-Box, Breusch-Godfrey, residual ACF | None: step 2. Short memory: ARMA errors. Slow decay: ARFIMA errors. Already ARMA and still dependent: back to P6 |
| 2 | Second-moment dependence? | ARCH-LM, McLeod-Li, squared-residual ACF | None: step 3. Present: step 2a |
| 2a | Which variance process? | Sign-bias test, squared-residual ACF decay, availability of high-frequency data | GARCH; EGARCH / GJR / TGARCH; FIGARCH; IGARCH; GARCH-in-mean; stochastic volatility; HAR-RV / Realized GARCH |
| 3 | Distribution of standardised innovations? | Jarque-Bera, QQ, Hill tail index, BNS jump test | Gaussian; Student-t / GED or QMLE; skewed-t; EVT; jump diffusion |
| 4 | Regimes in variance? | ICSS, Markov-switching LR | None: step 5. Present: MS-GARCH or segmented variance |
| 5 | Several series? | Engle-Sheppard constant-correlation test, tail dependence | CCC; DCC / BEKK; copula |
| 6 | Branch data types | Overdispersion tests; time-rescaling KS test | Counts: INGARCH / negative binomial. Event times: intensity misspecification |

Terminals name **model → estimator → inference**; for example, regression + ARMA errors + GARCH-t → joint MLE → asymptotic-normal standard errors.

## Part 0 hooks

| Branch | Stochastic-process concept | Chain link |
|---|---|---|
| White noise terminal | White noise, martingale difference, independence | Ljung-Box tests only uncorrelatedness and cannot detect ARCH, because ARCH is a martingale difference but not independent |
| ARMA errors | Wold decomposition | Any covariance-stationary process is MA(∞); ARMA is its rational approximation |
| ARFIMA errors | Long memory, hyperbolic decay | Why no finite-order ARMA reproduces it |
| GARCH | Weak stationarity α + β < 1; strict stationarity E[log(α z² + β)] < 0 | IGARCH is strictly stationary with infinite unconditional variance |
| Stochastic volatility | Latent process, filtering | Why the likelihood has no closed form |
| Jump diffusion | Brownian motion, Poisson jumps, Levy processes | Quadratic variation splits into continuous and jump parts |
| Markov switching | Hidden Markov chain | Hamilton filter |
| Event times | Conditional intensity, time-rescaling theorem | Under the true intensity, rescaled event times form a unit Poisson process |
| Copula | Sklar's theorem | Marginals and dependence separate |

## Relation to P9

P7 is specified once. After joint estimation in P8, P9 re-runs steps 1 to 5 on the complete model and loops back to P6 or P7 on failure.

## Test residual autocorrelation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_MEAN_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test conditional heteroskedasticity

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_VAR_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test the distribution of standardised innovations

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_DIST_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test for variance regimes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_REGIME_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test innovation correlation structure

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_CORR_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test overdispersion of count innovations

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_COUNT_TESTS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Time-rescaling check of event-time residuals

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_RESCALING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Assemble the joint model

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_OUT`). Write this section following the content rules in `.claude/rules/writing.md`.
