# P8: Estimation

**Question this phase answers:** How are parameters obtained?

Least squares and its generalisations, moment methods, exact and conditional likelihood, quasi-likelihood, GMM, Whittle, cointegrating-regression estimators, robust estimators, Bayesian computation, EM and filtering, simulation-based inference, empirical-loss minimisation with time-aware tuning, and convergence checks.

## Sub-diagram

**Part 1: observable components.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_IN(["Joint model from P7"]) --> P8_OBSERVABLE{"All components observable?"}
    P8_OBSERVABLE -->|"Yes"| P8_LINEAR{"Linear in parameters?"}
    P8_OBSERVABLE -->|"No"| P8_TO_PART_2(["Continue in part 2"])
    P8_LINEAR -->|"Yes"| P8_OLS_GLS["OLS, GLS and feasible GLS<br/>Cochrane-Orcutt, Prais-Winsten"]
    P8_LINEAR -->|"Moments only"| P8_MOMENTS{"Algorithm?"}
    P8_MOMENTS -->|"Moment equations"| P8_YULE_WALKER["Yule-Walker and the method of moments"]
    P8_MOMENTS -->|"Recursive"| P8_DURBIN_LEVINSON["Durbin-Levinson and the innovations algorithm"]
    P8_MOMENTS -->|"Regression on innovations"| P8_HANNAN_RISSANEN["Hannan-Rissanen and Burg estimation"]
    P8_LINEAR -->|"Cointegrating regression"| P8_FMOLS_DOLS["Cointegrating regression<br/>FMOLS, DOLS"]
    P8_LINEAR -->|"Outlier-prone"| P8_ROBUST["Robust estimation<br/>M-estimators, LAD"]
    P8_LINEAR -->|"No"| P8_TO_PART_2
    P8_YULE_WALKER & P8_DURBIN_LEVINSON --> P8_LINEAR_TO_PART_3
    P8_OLS_GLS & P8_HANNAN_RISSANEN & P8_FMOLS_DOLS & P8_ROBUST --> P8_LINEAR_TO_PART_3(["Continue in part 3"])
    class P8_IN,P8_TO_PART_2,P8_LINEAR_TO_PART_3 terminator
    class P8_OBSERVABLE,P8_LINEAR decision
    class P8_OLS_GLS,P8_YULE_WALKER,P8_DURBIN_LEVINSON,P8_HANNAN_RISSANEN,P8_FMOLS_DOLS,P8_ROBUST escalate
    class P8_MOMENTS decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: tractable likelihoods.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_FROM_PART_1(["From part 1"]) --> P8_LIKELIHOOD{"Likelihood tractable?"}
    P8_LIKELIHOOD -->|"Gaussian state space"| P8_PREDICTION_ERROR["Prediction-error decomposition"]
    P8_LIKELIHOOD -->|"Closed form"| P8_MLE
    P8_LIKELIHOOD -->|"Misspecified distribution"| P8_QMLE["Quasi-maximum likelihood and sandwich standard errors"]
    P8_LIKELIHOOD -->|"Nonlinear state"| P8_NONLINEAR_FILTERS["Extended and unscented Kalman filters"]
    P8_LIKELIHOOD -->|"Latent variables"| P8_EM["EM for state-space models"]
    P8_LIKELIHOOD -->|"Intractable"| P8_TO_PART_3
    P8_PREDICTION_ERROR --> P8_KALMAN["Kalman filter and smoother"]
    P8_KALMAN --> P8_MLE["Maximum likelihood, exact and conditional"]
    P8_NONLINEAR_FILTERS --> P8_PARTICLE_FILTERS["Particle filters"]
    P8_MLE & P8_QMLE & P8_PARTICLE_FILTERS & P8_EM --> P8_TO_PART_3(["Continue in part 3"])
    F_LLN[["Law of large numbers"]] -.- P8_MLE
    F_CLT[["Central limit theorem"]] -.- P8_QMLE
    class P8_FROM_PART_1,P8_TO_PART_3 terminator
    class P8_LIKELIHOOD decision
    class P8_PREDICTION_ERROR,P8_KALMAN,P8_MLE,P8_QMLE,P8_NONLINEAR_FILTERS,P8_PARTICLE_FILTERS,P8_EM escalate
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

**Part 3: intractable likelihoods and convergence.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P8_FROM_PART_2(["From parts 1 and 2"]) -->|"Intractable likelihood"| P8_INTRACTABLE{"Approach?"}
    P8_FROM_PART_2 -->|"Estimated"| P8_CONVERGENCE
    P8_INTRACTABLE -->|"Moment conditions"| P8_GMM["Generalised method of moments"]
    P8_INTRACTABLE -->|"Frequency domain"| P8_WHITTLE["Whittle and local Whittle estimation"]
    P8_INTRACTABLE -->|"Priors"| P8_MCMC["Bayesian computation<br/>MCMC, Gibbs, Metropolis-Hastings"]
    P8_INTRACTABLE -->|"Simulate"| P8_SIMULATION_INFERENCE["Simulation-based inference<br/>ABC, indirect inference"]
    P8_INTRACTABLE -->|"Loss minimisation"| P8_EMPIRICAL_LOSS["Empirical-loss minimisation<br/>gradient descent, boosting"]
    P8_MCMC --> P8_VARIATIONAL["Variational inference"]
    P8_EMPIRICAL_LOSS --> P8_HYPERPARAMETERS["Time-aware hyperparameter tuning<br/>leakage-safe splits"]
    P8_GMM & P8_WHITTLE & P8_VARIATIONAL & P8_SIMULATION_INFERENCE & P8_HYPERPARAMETERS --> P8_CONVERGENCE["Convergence and numerical checks"]
    P8_CONVERGENCE --> P8_CONVERGED{"Converged?"}
    P8_CONVERGED -->|"Yes"| P8_OUT(["To P9 Diagnostics"])
    P8_CONVERGED -.->|"No: simplify or re-initialise"| P6[["P6: Conditional-mean model class"]]
    class P8_FROM_PART_2,P8_OUT terminator
    class P8_INTRACTABLE,P8_CONVERGED decision
    class P8_GMM,P8_WHITTLE,P8_MCMC,P8_VARIATIONAL,P8_SIMULATION_INFERENCE,P8_EMPIRICAL_LOSS,P8_HYPERPARAMETERS escalate
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
