# P11: Inference and interpretation

**Question this phase answers:** What does the model say, for this purpose?

Coefficient and restriction tests, HAC inference, cointegration and causality inference, structural identification and impulse responses, counterfactuals, forecasting outputs, nowcasting, risk measures and their backtests, scenario simulation, and interpretability.

## Sub-diagram

**Part 1: dispatch on the purpose flag, and forecasting.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P11_IN(["Validated model and purpose flag"]) --> P11_PURPOSE{"Purpose flag?"}
    P11_PURPOSE -->|"The future"| P11_POINT_FORECASTS["Point forecasts and horizons"]
    P11_PURPOSE -->|"Causes"| P11_TO_PART_2(["Continue in part 2"])
    P11_PURPOSE -->|"Structure in the series or events"| P11_TO_PART_4(["Continue in part 4"])
    P11_PURPOSE -->|"Other outputs"| P11_TO_PART_5(["Continue in part 5"])
    P11_POINT_FORECASTS --> P11_INTERVALS["Prediction intervals<br/>analytical, bootstrap, conformal"]
    P11_INTERVALS --> P11_DENSITY_QUANTILE["Density and quantile forecasts"]
    P11_DENSITY_QUANTILE --> P11_RISK{"Risk measures needed?"}
    P11_RISK -->|"Yes"| P11_RISK_MEASURES[["Risk measures and their backtests"]]
    P11_RISK -->|"No"| P11_MULTISTEP_Q
    P11_RISK_MEASURES --> P11_MULTISTEP_Q{"Horizon beyond one step?"}
    P11_MULTISTEP_Q -->|"Yes"| P11_MULTISTEP["Multi-step strategies<br/>recursive, direct, MIMO"]
    P11_MULTISTEP_Q -->|"No"| P11_HIERARCHY
    P11_MULTISTEP --> P11_HIERARCHY{"Hierarchy flag?"}
    P11_HIERARCHY -->|"Yes"| P11_RECONCILIATION["Hierarchical and temporal reconciliation<br/>bottom-up, top-down, MinT"]
    P11_HIERARCHY -->|"No"| P11_COMBINATION
    P11_RECONCILIATION --> P11_COMBINATION["Forecast combination and model averaging"]
    P11_COMBINATION --> P11_JUDGMENTAL["Judgmental adjustment"]
    P11_JUDGMENTAL --> P11_BLACK_BOX{"Black-box model?"}
    P11_BLACK_BOX -->|"Yes"| P11_INTERPRETABILITY[["Interpretability"]]
    P11_BLACK_BOX -->|"No"| P11_MIXED
    P11_INTERPRETABILITY --> P11_MIXED{"Mixed-frequency flag?"}
    P11_MIXED -->|"Yes"| P11_NOWCASTING["Nowcasting<br/>bridge equations, factor models"]
    P11_MIXED -->|"No"| P10
    P11_NOWCASTING --> P10[["P10: Out-of-sample evaluation and selection"]]
    F_CONDITIONAL_EXPECTATION[["Conditional expectation as the optimal forecast"]] -.- P11_POINT_FORECASTS
    F_PROJECTION[["Projection theorem and best linear prediction"]] -.- P11_INTERVALS
    P6_MIXED_FREQUENCY[["Mixed-frequency models"]] -.- P11_NOWCASTING
    class P11_IN,P11_TO_PART_2,P11_TO_PART_4,P11_TO_PART_5 terminator
    class P11_PURPOSE,P11_RISK,P11_MULTISTEP_Q,P11_HIERARCHY,P11_BLACK_BOX,P11_MIXED decision
    class P11_POINT_FORECASTS,P11_INTERVALS,P11_DENSITY_QUANTILE,P11_MULTISTEP,P11_RECONCILIATION,P11_COMBINATION,P11_JUDGMENTAL,P11_NOWCASTING process
    class P11_RISK_MEASURES,P11_INTERPRETABILITY,P10,F_CONDITIONAL_EXPECTATION,F_PROJECTION,P6_MIXED_FREQUENCY ref
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
    P11_PART_2_IN(["From part 1: causes"]) --> P11_COEFFICIENT_TESTS["Coefficient and restriction tests<br/>t, F, likelihood ratio, Wald, Lagrange multiplier"]
    P11_COEFFICIENT_TESTS --> P11_HAC["HAC inference<br/>Newey-West, bandwidth choice"]
    P11_HAC --> P11_SYSTEM{"Multivariate flag?"}
    P11_SYSTEM -->|"Yes"| P11_TO_PART_3(["Continue in part 3"])
    P11_SYSTEM -->|"No"| P11_COUNTERFACTUALS["Counterfactual designs<br/>interrupted time series, difference-in-differences, synthetic control, CausalImpact"]
    P11_COUNTERFACTUALS --> P10[["P10: Out-of-sample evaluation and selection"]]
    class P11_PART_2_IN,P11_TO_PART_3 terminator
    class P11_SYSTEM decision
    class P11_COEFFICIENT_TESTS,P11_HAC,P11_COUNTERFACTUALS process
    class P10 ref
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
    P11_PART_3_IN(["From part 2: several series"]) --> P11_CAUSAL_Q{"Causal question?"}
    P11_CAUSAL_Q -->|"Long-run relations"| P11_COINTEGRATION["Cointegration inference<br/>Engle-Granger, Johansen, ARDL bounds"]
    P11_CAUSAL_Q -->|"Predictive causality"| P11_GRANGER["Granger, Sims and Toda-Yamamoto causality"]
    P11_CAUSAL_Q -->|"Nonlinear dependence"| P11_NONLINEAR_CAUSALITY["Nonlinear causal discovery<br/>transfer entropy, convergent cross mapping, PCMCI"]
    P11_CAUSAL_Q -->|"Structural shocks"| P11_SVAR_IDENTIFICATION["SVAR identification<br/>Cholesky, sign restrictions, long-run, external instruments"]
    P11_CAUSAL_Q -->|"Dynamic effects"| P11_LOCAL_PROJECTIONS["Local projections"]
    P11_SVAR_IDENTIFICATION --> P11_IRF_FEVD["Impulse responses and variance decompositions"]
    P11_COINTEGRATION & P11_GRANGER & P11_NONLINEAR_CAUSALITY --> P10
    P11_IRF_FEVD & P11_LOCAL_PROJECTIONS --> P10[["P10: Out-of-sample evaluation and selection"]]
    class P11_PART_3_IN terminator
    class P11_CAUSAL_Q decision
    class P11_COINTEGRATION,P11_GRANGER,P11_NONLINEAR_CAUSALITY,P11_SVAR_IDENTIFICATION,P11_LOCAL_PROJECTIONS,P11_IRF_FEVD process
    class P10 ref
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
    P11_PART_4_IN(["From part 1"]) --> P11_PURPOSE_4{"Purpose flag?"}
    P11_PURPOSE_4 -->|"Structure in the series"| P11_STRUCTURE{"Which structure?"}
    P11_PURPOSE_4 -->|"Events"| P11_EVENTS{"Which events?"}
    P11_STRUCTURE -->|"Signal versus noise"| P0_SE_SNR[["Evaluate the signal-to-noise ratio"]]
    P11_STRUCTURE -->|"Components"| P0_DC_COMPONENT_ANALYSIS[["Analyse and interpret the components"]]
    P11_STRUCTURE -->|"Frequencies"| P0_SP_PEAK_SIGNIFICANCE[["Peak significance"]]
    P11_EVENTS -->|"Changes"| P0_CP_TYPE[["Classify the change"]]
    P11_EVENTS -->|"Anomalies or regimes"| P0_AN_THRESHOLD[["Set thresholds by the cost of errors"]]
    P0_SE_SNR & P0_DC_COMPONENT_ANALYSIS & P0_SP_PEAK_SIGNIFICANCE & P0_CP_TYPE & P0_AN_THRESHOLD --> P10[["P10: Out-of-sample evaluation and selection"]]
    class P11_PART_4_IN terminator
    class P11_PURPOSE_4,P11_STRUCTURE,P11_EVENTS decision
    class P0_SE_SNR,P0_DC_COMPONENT_ANALYSIS,P0_SP_PEAK_SIGNIFICANCE,P0_CP_TYPE,P0_AN_THRESHOLD,P10 ref
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
    P11_PART_5_IN(["From part 1: other outputs"]) --> P11_OUTPUTS{"Which output?"}
    P11_OUTPUTS -->|"Features and labels"| P11_INTERPRETABILITY["Interpretability<br/>SHAP, attention"]
    P11_OUTPUTS -->|"A system model"| P0_SI_TRANSFER_FUNCTION[["Estimate the frequency response"]]
    P11_OUTPUTS -->|"Simulated paths"| P11_SCENARIOS["Stress testing and scenario design"]
    P0_SI_TRANSFER_FUNCTION --> P0_SI_STABILITY[["Poles, zeros and stability"]]
    P11_SCENARIOS --> P11_RISK_MEASURES["Risk measures and their backtests<br/>VaR, expected shortfall, Kupiec, Christoffersen"]
    P11_INTERPRETABILITY & P0_SI_STABILITY & P11_RISK_MEASURES --> P10[["P10: Out-of-sample evaluation and selection"]]
    class P11_PART_5_IN terminator
    class P11_OUTPUTS decision
    class P11_INTERPRETABILITY,P11_SCENARIOS,P11_RISK_MEASURES process
    class P0_SI_TRANSFER_FUNCTION,P0_SI_STABILITY,P10 ref
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
    To-do item created from the flowchart inventory (node `P11`). Write this section following the content rules in `.claude/rules/writing.md`.
