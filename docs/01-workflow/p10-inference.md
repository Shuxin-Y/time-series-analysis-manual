# P10: Inference and interpretation

**Question this phase answers:** What does the model say, for this purpose?

Coefficient and restriction tests, HAC inference, cointegration and causality inference, structural identification and impulse responses, counterfactuals, forecasting outputs, nowcasting, risk measures and their backtests, scenario simulation, and interpretability.

## Sub-diagram

**Part 1: dispatch on the purpose flag, and forecasting.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_IN(["Validated model and purpose flag"]) --> P10_PURPOSE{"Purpose flag?"}
    P10_PURPOSE -->|"The future"| P10_POINT_FORECASTS["Point forecasts and horizons"]
    P10_PURPOSE -->|"Causes"| P10_TO_PART_2(["Continue in part 2"])
    P10_PURPOSE -->|"Structure in the series or events"| P10_TO_PART_4(["Continue in part 4"])
    P10_PURPOSE -->|"Other outputs"| P10_TO_PART_5(["Continue in part 5"])
    P10_POINT_FORECASTS --> P10_INTERVALS["Prediction intervals<br/>analytical, bootstrap, conformal"]
    P10_INTERVALS --> P10_DENSITY_QUANTILE["Density and quantile forecasts"]
    P10_DENSITY_QUANTILE --> P10_RISK{"Risk measures needed?"}
    P10_RISK -->|"Yes"| P10_RISK_MEASURES[["Risk measures and their backtests"]]
    P10_RISK -->|"No"| P10_MULTISTEP_Q
    P10_RISK_MEASURES --> P10_MULTISTEP_Q{"Multi-step flag?"}
    P10_MULTISTEP_Q -->|"Yes"| P10_MULTISTEP["Multi-step strategies<br/>recursive, direct, MIMO"]
    P10_MULTISTEP_Q -->|"No"| P10_HIERARCHY
    P10_MULTISTEP --> P10_HIERARCHY{"Hierarchy flag?"}
    P10_HIERARCHY -->|"Yes"| P10_RECONCILIATION["Hierarchical and temporal reconciliation<br/>bottom-up, top-down, MinT"]
    P10_HIERARCHY -->|"No"| P10_COMBINATION
    P10_RECONCILIATION --> P10_COMBINATION["Forecast combination and model averaging"]
    P10_COMBINATION --> P10_JUDGMENTAL["Judgmental adjustment"]
    P10_JUDGMENTAL --> P10_BLACK_BOX{"Black-box model?"}
    P10_BLACK_BOX -->|"Yes"| P10_INTERPRETABILITY[["Interpretability"]]
    P10_BLACK_BOX -->|"No"| P10_MIXED
    P10_INTERPRETABILITY --> P10_MIXED{"Mixed-frequency flag?"}
    P10_MIXED -->|"Yes"| P10_NOWCASTING["Nowcasting<br/>bridge equations, factor models"]
    P10_MIXED -->|"No"| P11
    P10_NOWCASTING --> P11[["P11: Validation and deployment"]]
    F_CONDITIONAL_EXPECTATION[["Conditional expectation as the optimal forecast"]] -.- P10_POINT_FORECASTS
    F_PROJECTION[["Projection theorem and best linear prediction"]] -.- P10_INTERVALS
    P6_MIXED_FREQUENCY[["Mixed-frequency models"]] -.- P10_NOWCASTING
    class P10_IN,P10_TO_PART_2,P10_TO_PART_4,P10_TO_PART_5 terminator
    class P10_PURPOSE,P10_RISK,P10_MULTISTEP_Q,P10_HIERARCHY,P10_BLACK_BOX,P10_MIXED decision
    class P10_POINT_FORECASTS,P10_INTERVALS,P10_DENSITY_QUANTILE,P10_MULTISTEP,P10_RECONCILIATION,P10_COMBINATION,P10_JUDGMENTAL,P10_NOWCASTING process
    class P10_RISK_MEASURES,P10_INTERPRETABILITY,P11,F_CONDITIONAL_EXPECTATION,F_PROJECTION,P6_MIXED_FREQUENCY ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: causal and structural inference.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_2_IN(["From part 1: causes"]) --> P10_COEFFICIENT_TESTS["Coefficient and restriction tests<br/>t, F, likelihood ratio, Wald, Lagrange multiplier"]
    P10_COEFFICIENT_TESTS --> P10_HAC["HAC inference<br/>Newey-West, bandwidth choice"]
    P10_HAC --> P10_SYSTEM{"Multivariate flag?"}
    P10_SYSTEM -->|"Yes"| P10_TO_PART_3(["Continue in part 3"])
    P10_SYSTEM -->|"No"| P10_COUNTERFACTUALS["Counterfactual designs<br/>intervention analysis, interrupted time series, difference-in-differences, synthetic control, CausalImpact"]
    P10_COUNTERFACTUALS --> P11[["P11: Validation and deployment"]]
    class P10_PART_2_IN,P10_TO_PART_3 terminator
    class P10_SYSTEM decision
    class P10_COEFFICIENT_TESTS,P10_HAC,P10_COUNTERFACTUALS process
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

**Part 3: causal questions for several series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_3_IN(["From part 2: several series"]) --> P10_CAUSAL_Q{"Causal question?"}
    P10_CAUSAL_Q -->|"Long-run relations"| P10_COINTEGRATION["Cointegration inference<br/>Engle-Granger, Johansen, ARDL bounds"]
    P10_CAUSAL_Q -->|"Predictive causality"| P10_GRANGER["Granger, Sims and Toda-Yamamoto causality"]
    P10_CAUSAL_Q -->|"Nonlinear dependence"| P10_NONLINEAR_CAUSALITY["Nonlinear causal discovery<br/>transfer entropy, convergent cross mapping, PCMCI"]
    P10_CAUSAL_Q -->|"Structural shocks"| P10_SVAR_IDENTIFICATION["SVAR identification<br/>Cholesky, sign restrictions, long-run, external instruments"]
    P10_CAUSAL_Q -->|"Dynamic effects"| P10_LOCAL_PROJECTIONS["Local projections"]
    P10_SVAR_IDENTIFICATION --> P10_IRF_FEVD["Impulse responses and variance decompositions"]
    P10_COINTEGRATION & P10_GRANGER & P10_NONLINEAR_CAUSALITY --> P11
    P10_IRF_FEVD & P10_LOCAL_PROJECTIONS --> P11[["P11: Validation and deployment"]]
    class P10_PART_3_IN terminator
    class P10_CAUSAL_Q decision
    class P10_COINTEGRATION,P10_GRANGER,P10_NONLINEAR_CAUSALITY,P10_SVAR_IDENTIFICATION,P10_LOCAL_PROJECTIONS,P10_IRF_FEVD process
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

**Part 4: structure in the series and events.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_4_IN(["From part 1"]) --> P10_PURPOSE_4{"Purpose flag?"}
    P10_PURPOSE_4 -->|"Structure in the series"| P10_STRUCTURE{"Which structure?"}
    P10_PURPOSE_4 -->|"Events"| P10_EVENTS{"Which events?"}
    P10_STRUCTURE -->|"Signal versus noise"| P2_SE_SNR[["Evaluate the signal-to-noise ratio"]]
    P10_STRUCTURE -->|"Components"| P2_DC_COMPONENT_ANALYSIS[["Analyse and interpret the components"]]
    P10_STRUCTURE -->|"Frequencies"| P2_SP_PEAK_SIGNIFICANCE[["Peak significance"]]
    P10_EVENTS -->|"Changes"| P2_CP_TYPE[["Classify the change"]]
    P10_EVENTS -->|"Anomalies or regimes"| P2_AN_THRESHOLD[["Set thresholds by the cost of errors"]]
    P2_SE_SNR & P2_DC_COMPONENT_ANALYSIS & P2_SP_PEAK_SIGNIFICANCE & P2_CP_TYPE & P2_AN_THRESHOLD --> P11[["P11: Validation and deployment"]]
    class P10_PART_4_IN terminator
    class P10_PURPOSE_4,P10_STRUCTURE,P10_EVENTS decision
    class P2_SE_SNR,P2_DC_COMPONENT_ANALYSIS,P2_SP_PEAK_SIGNIFICANCE,P2_CP_TYPE,P2_AN_THRESHOLD,P11 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: other outputs.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_5_IN(["From part 1: other outputs"]) --> P10_OUTPUTS{"Which output?"}
    P10_OUTPUTS -->|"Features and labels"| P10_INTERPRETABILITY["Interpretability<br/>SHAP, attention"]
    P10_OUTPUTS -->|"A system model"| P2_SI_TRANSFER_FUNCTION[["Estimate the frequency response"]]
    P10_OUTPUTS -->|"Simulated paths"| P10_SCENARIOS["Scenario simulation and stress testing"]
    P2_SI_TRANSFER_FUNCTION --> P2_SI_STABILITY[["Poles, zeros and stability"]]
    P10_SCENARIOS --> P10_RISK_MEASURES["Risk measures and their backtests<br/>VaR, expected shortfall, Kupiec, Christoffersen"]
    P10_INTERPRETABILITY & P2_SI_STABILITY & P10_RISK_MEASURES --> P11[["P11: Validation and deployment"]]
    class P10_PART_5_IN terminator
    class P10_OUTPUTS decision
    class P10_INTERPRETABILITY,P10_SCENARIOS,P10_RISK_MEASURES process
    class P2_SI_TRANSFER_FUNCTION,P2_SI_STABILITY,P11 ref
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
