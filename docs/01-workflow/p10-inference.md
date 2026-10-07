# P10: Inference and interpretation

**Question this phase answers:** What does the model say, for this purpose?

Coefficient and restriction tests, HAC inference, cointegration and causality inference, structural identification and impulse responses, counterfactuals, forecasting outputs, nowcasting, risk measures and their backtests, scenario simulation, and interpretability.

## Sub-diagram

**Part 1: purpose routing and forecasting.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_IN(["Validated model and purpose flag"]) --> P10_PURPOSE{"Purpose?"}
    P10_PURPOSE -->|"Forecasting"| P10_POINT_FORECASTS["Point forecasts and horizons"]
    P10_PURPOSE -->|"Causal, risk or black-box"| P10_TO_PART_2(["Continue in part 2"])
    P10_POINT_FORECASTS --> P10_INTERVALS["Prediction intervals<br/>analytical, bootstrap, conformal"]
    P10_INTERVALS --> P10_DENSITY_QUANTILE["Density and quantile forecasts"]
    P10_DENSITY_QUANTILE --> P10_MULTISTEP["Multi-step strategies<br/>recursive, direct, MIMO"]
    P10_MULTISTEP --> P10_HIERARCHY{"Hierarchy or many series?"}
    P10_HIERARCHY -->|"Yes"| P10_RECONCILIATION["Hierarchical and temporal reconciliation<br/>bottom-up, top-down, MinT"]
    P10_HIERARCHY -->|"No"| P10_COMBINATION
    P10_RECONCILIATION --> P10_COMBINATION["Forecast combination and model averaging"]
    P10_COMBINATION --> P10_JUDGMENTAL["Judgmental adjustment"]
    P10_JUDGMENTAL --> P10_MIXED{"Mixed-frequency flag?"}
    P10_MIXED -->|"Yes"| P10_NOWCASTING["Nowcasting<br/>MIDAS, bridge equations, factor models"]
    P10_MIXED -->|"No"| P11
    F_CONDITIONAL_EXPECTATION[["Conditional expectation as the optimal forecast"]] -.- P10_POINT_FORECASTS
    F_PROJECTION[["Projection theorem and best linear prediction"]] -.- P10_INTERVALS
    P10_NOWCASTING --> P11[["P11: Validation and deployment"]]
    class P10_IN,P10_TO_PART_2 terminator
    class P10_PURPOSE,P10_HIERARCHY,P10_MIXED decision
    class P10_POINT_FORECASTS,P10_INTERVALS,P10_DENSITY_QUANTILE,P10_MULTISTEP,P10_RECONCILIATION,P10_COMBINATION,P10_JUDGMENTAL,P10_NOWCASTING process
    class P11,F_CONDITIONAL_EXPECTATION,F_PROJECTION ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: causal and structural inference, risk and interpretability.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_FROM_PART_1(["From part 1"]) -->|"Causal or structural"| P10_COEFFICIENT_TESTS["Coefficient and restriction tests<br/>t, F, likelihood ratio, Wald, Lagrange multiplier"]
    P10_FROM_PART_1 -->|"Risk"| P10_RISK_MEASURES["Risk measures and their backtests<br/>VaR, expected shortfall, Kupiec, Christoffersen"]
    P10_FROM_PART_1 -->|"Black-box model"| P10_INTERPRETABILITY["Interpretability<br/>SHAP, attention"]
    P10_COEFFICIENT_TESTS --> P10_HAC["HAC inference<br/>Newey-West, bandwidth choice"]
    P10_HAC --> P10_SYSTEM{"Multivariate?"}
    P10_SYSTEM -->|"Yes"| P10_COINTEGRATION["Cointegration inference<br/>Engle-Granger, Johansen, ARDL bounds"]
    P10_SYSTEM -->|"No"| P10_COUNTERFACTUALS["Counterfactual designs<br/>intervention analysis, interrupted time series, difference-in-differences, synthetic control, CausalImpact"]
    P10_COINTEGRATION --> P10_GRANGER["Granger, Sims and Toda-Yamamoto causality"]
    P10_GRANGER --> P10_NONLINEAR_CAUSALITY["Nonlinear causal discovery<br/>transfer entropy, convergent cross mapping, PCMCI"]
    P10_NONLINEAR_CAUSALITY --> P10_SVAR_IDENTIFICATION["SVAR identification<br/>Cholesky, sign restrictions, long-run, external instruments"]
    P10_SVAR_IDENTIFICATION --> P10_IRF_FEVD["Impulse responses and variance decompositions"]
    P10_IRF_FEVD --> P10_LOCAL_PROJECTIONS["Local projections"]
    P10_RISK_MEASURES --> P10_SCENARIOS["Scenario simulation and stress testing"]
    P10_LOCAL_PROJECTIONS & P10_COUNTERFACTUALS & P10_SCENARIOS & P10_INTERPRETABILITY --> P11[["P11: Validation and deployment"]]
    class P10_FROM_PART_1 terminator
    class P10_SYSTEM decision
    class P10_COEFFICIENT_TESTS,P10_HAC,P10_COINTEGRATION,P10_GRANGER,P10_NONLINEAR_CAUSALITY,P10_SVAR_IDENTIFICATION,P10_IRF_FEVD,P10_LOCAL_PROJECTIONS,P10_COUNTERFACTUALS process
    class P10_RISK_MEASURES,P10_SCENARIOS,P10_INTERPRETABILITY process
    class P11 ref
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
    To-do item created from the flowchart inventory (node `P10`). Write this section following the content rules in `.claude/rules/writing.md`.
