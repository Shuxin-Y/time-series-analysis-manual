# P8: Estimation

**Question this phase answers:** How are parameters obtained?

P8 reads the prior-specified and model-kind flags first, because Bayesian inference and loss minimisation are choices of paradigm made before any question about tractability. A likelihood model then asks whether every component is observable and whether a regressor is endogenous, because latent states need a filter and an endogenous regressor makes least squares inconsistent. The remaining routes are least squares and moments, cointegrating, robust and quantile regression, and likelihood (exact, conditional, quasi, spectral, conditional sum of squares, simulation-based). Every route ends in the convergence and numerical checks.

## Sub-diagram

**Part 1: prior, model kind, observability and endogeneity.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_IN(["Joint model from P7"]) --> P8_PRIOR_Q{"Prior-specified flag?"}
    P8_PRIOR_Q -->|"Yes"| P8_TO_PART_6(["Continue in part 6"])
    P8_PRIOR_Q -->|"No"| P8_KIND_Q{"Model-kind flag?"}
    P8_KIND_Q -->|"Loss minimisation"| P8_EMPIRICAL_LOSS["Empirical-loss minimisation<br/>training loss from the forecast task; gradient descent, boosting"]
    P8_KIND_Q -->|"Likelihood"| P8_TYPE{"Value-type flag?"}
    P8_TYPE -->|"Continuous or compositional"| P8_OBSERVABLE{"All components observable?"}
    P8_TYPE -->|"Counts, categories, events"| P8_TO_PART_4
    P8_TYPE -->|"Curves: basis coefficients"| P8_TO_PART_2
    P8_EMPIRICAL_LOSS --> P8_HYPERPARAMETERS["Time-aware hyperparameter tuning<br/>nested inside each training window"]
    P8_HYPERPARAMETERS --> P8_LOSS_TO_PART_6(["Convergence in part 6"])
    P8_OBSERVABLE -->|"No: latent states"| P8_TO_PART_5(["Continue in part 5"])
    P8_OBSERVABLE -->|"Yes"| P8_ENDOGENOUS{"Endogenous regressors?"}
    P8_ENDOGENOUS -->|"Yes"| P8_GMM["Generalised method of moments<br/>instrumental variables for endogenous regressors"]
    P8_ENDOGENOUS -->|"No"| P8_FAMILY{"Estimator?"}
    P8_GMM --> P8_GMM_TO_PART_6(["Convergence in part 6"])
    P8_FAMILY -->|"Least squares or moments"| P8_TO_PART_2(["Continue in part 2"])
    P8_FAMILY -->|"Cointegrating, robust or quantile"| P8_TO_PART_3(["Continue in part 3"])
    P8_FAMILY -->|"Likelihood"| P8_TO_PART_4(["Continue in part 4"])
    class P8_EMPIRICAL_LOSS,P8_HYPERPARAMETERS,P8_GMM escalate
    class P8_IN,P8_TO_PART_6,P8_LOSS_TO_PART_6,P8_TO_PART_5,P8_GMM_TO_PART_6,P8_TO_PART_2,P8_TO_PART_3,P8_TO_PART_4 terminator
    class P8_PRIOR_Q,P8_KIND_Q,P8_TYPE,P8_OBSERVABLE,P8_ENDOGENOUS,P8_FAMILY decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: least squares and moment estimators.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_PART_2_IN(["From part 1: least squares or moments"]) --> P8_LINEAR{"Model?"}
    P8_LINEAR -->|"Linear regression"| P8_OLS_GLS["OLS, GLS and feasible GLS<br/>Cochrane-Orcutt and Prais-Winsten for AR(p) errors; inconsistent with a lagged dependent variable"]
    P8_LINEAR -->|"Regression with ARMA errors"| P8_JOINT_TO_PART_4(["Joint ML in part 4"])
    P8_LINEAR -->|"AR or ARMA by moments"| P8_MOMENTS{"Algorithm?"}
    P8_MOMENTS -->|"Moment equations"| P8_YULE_WALKER["Yule-Walker and the method of moments"]
    P8_MOMENTS -->|"Recursive"| P8_DURBIN_LEVINSON["Durbin-Levinson and the innovations algorithm"]
    P8_MOMENTS -->|"Forward-backward errors"| P8_BURG["Burg estimation"]
    P8_MOMENTS -->|"Two-stage regression"| P8_HANNAN_RISSANEN["Hannan-Rissanen estimation"]
    P8_OLS_GLS & P8_YULE_WALKER & P8_DURBIN_LEVINSON & P8_BURG & P8_HANNAN_RISSANEN --> P8_PART_2_OUT(["Convergence in part 6"])
    class P8_OLS_GLS,P8_YULE_WALKER,P8_DURBIN_LEVINSON,P8_BURG,P8_HANNAN_RISSANEN escalate
    class P8_PART_2_IN,P8_JOINT_TO_PART_4,P8_PART_2_OUT terminator
    class P8_LINEAR,P8_MOMENTS decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: cointegrating, robust and quantile regression.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_PART_3_IN(["From part 1"]) --> P8_SPECIAL{"Which case?"}
    P8_SPECIAL -->|"Cointegrated system, rank r"| P8_RRR["Reduced-rank regression<br/>Johansen ML of the VECM"]
    P8_SPECIAL -->|"Single cointegrating equation"| P8_FMOLS_DOLS["Cointegrating regression<br/>FMOLS, DOLS"]
    P8_SPECIAL -->|"Outliers"| P8_ROBUST["Robust estimation<br/>M-estimators, LAD"]
    P8_SPECIAL -->|"Conditional quantiles"| P8_QUANTILE_REGRESSION["Quantile regression and quantile autoregression"]
    P8_RRR & P8_FMOLS_DOLS & P8_ROBUST & P8_QUANTILE_REGRESSION --> P8_PART_3_OUT(["Convergence in part 6"])
    class P8_RRR,P8_FMOLS_DOLS,P8_ROBUST,P8_QUANTILE_REGRESSION escalate
    class P8_PART_3_IN,P8_PART_3_OUT terminator
    class P8_SPECIAL decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: likelihood.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_PART_4_IN(["From parts 1 and 2"]) --> P8_LIKELIHOOD{"Likelihood?"}
    P8_LIKELIHOOD -->|"Closed form"| P8_MLE["Maximum likelihood, exact and conditional<br/>joint ML of the regression and its ARMA errors"]
    P8_LIKELIHOOD -->|"Misspecified distribution"| P8_QMLE["Quasi-maximum likelihood and sandwich standard errors"]
    P8_LIKELIHOOD -->|"Spectral: large n or semiparametric d"| P8_WHITTLE["Whittle and local Whittle estimation"]
    P8_LIKELIHOOD -->|"Nonstationary fractional d"| P8_CSS["Conditional sum of squares<br/>consistent for any d"]
    P8_LIKELIHOOD -->|"Intractable"| P8_SIMULATION_INFERENCE["Simulation-based inference<br/>ABC, indirect inference"]
    P8_MLE & P8_QMLE & P8_WHITTLE & P8_CSS & P8_SIMULATION_INFERENCE --> P8_PART_4_OUT(["Convergence in part 6"])
    F_LLN[["Law of large numbers"]] -.- P8_MLE
    F_CLT[["Central limit theorem"]] -.- P8_QMLE
    class P8_MLE,P8_QMLE,P8_WHITTLE,P8_CSS,P8_SIMULATION_INFERENCE escalate
    class P8_PART_4_IN,P8_PART_4_OUT terminator
    class P8_LIKELIHOOD decision
    class F_LLN,F_CLT ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: latent states.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_PART_5_IN(["From part 1: latent states"]) --> P8_STATE_Q{"State-space model?"}
    P8_STATE_Q -->|"Linear Gaussian"| P8_PREDICTION_ERROR["Prediction-error decomposition"]
    P8_STATE_Q -->|"Near-Gaussian posterior, mild nonlinearity"| P8_NONLINEAR_FILTERS["Extended and unscented Kalman filters"]
    P8_STATE_Q -->|"Multimodal, heavy-tailed or non-Gaussian observations"| P8_PARTICLE_FILTERS["Particle filters"]
    P8_PREDICTION_ERROR --> P8_KALMAN["Kalman filter and smoother<br/>stationary or diffuse initialisation; imputed points treated as missing"]
    P8_KALMAN --> P8_KALMAN_FIT{"Parameter estimation?"}
    P8_KALMAN_FIT -->|"Numerical optimisation"| P8_MLE[["Maximum likelihood, exact and conditional"]]
    P8_KALMAN_FIT -->|"Expectation-maximisation"| P8_EM["EM for state-space models"]
    P8_MLE & P8_EM & P8_NONLINEAR_FILTERS & P8_PARTICLE_FILTERS --> P8_PART_5_OUT(["Convergence in part 6"])
    class P8_PREDICTION_ERROR,P8_KALMAN,P8_EM,P8_NONLINEAR_FILTERS,P8_PARTICLE_FILTERS escalate
    class P8_PART_5_IN,P8_PART_5_OUT terminator
    class P8_STATE_Q,P8_KALMAN_FIT decision
    class P8_MLE ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 6: Bayesian computation and convergence.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_PART_6_IN(["From part 1: prior specified"]) --> P8_POSTERIOR{"Posterior?"}
    P8_POSTERIOR -->|"Sampled"| P8_MCMC["Bayesian computation<br/>conjugate updates, Gibbs, Metropolis-Hastings, HMC"]
    P8_POSTERIOR -->|"Approximated"| P8_VARIATIONAL["Variational inference"]
    P8_PART_6_ALL_IN(["From parts 1 to 5"]) --> P8_CONVERGENCE
    P8_MCMC & P8_VARIATIONAL --> P8_CONVERGENCE["Convergence and numerical checks"]
    P8_CONVERGENCE --> P8_CONVERGED{"Converged?"}
    P8_CONVERGED -->|"Yes"| P8_OUT(["To P9 In-sample diagnostics"])
    P8_CONVERGED -.->|"No: simplify or re-initialise"| P6[["P6: Conditional-mean model class"]]
    class P8_MCMC,P8_VARIATIONAL escalate
    class P8_PART_6_IN,P8_PART_6_ALL_IN,P8_OUT terminator
    class P8_POSTERIOR,P8_CONVERGED decision
    class P8_CONVERGENCE process
    class P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Phase guide

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8`). Write this section following the content rules in `.claude/rules/writing.md`.

## Convergence and numerical checks

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_CONVERGENCE`). Write this section following the content rules in `.claude/rules/writing.md`.
