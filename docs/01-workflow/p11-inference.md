# P11: Inference and interpretation

**Question this phase answers:** What does the selected model say, for this purpose?

P11 issues and interprets the output of the candidate selected in P10. A forecaster issues, for the live origin, the same product P10 scored, built on sample paths or predictive distributions: back-transformation and re-seasonalisation to the target scale, combination, judgmental adjustment and reconciliation act on the paths, and intervals and quantiles are derived last. The order follows from two facts: aggregation constraints are linear on the target scale, and quantiles are not additive, so intervals computed before combination and reconciliation would surround a different centre. Causal and structural inference accounts for the specification search that produced the model. Structure, events and other outputs are interpreted with their uncertainty: confidence bands for spectra, confidence intervals for break dates.

## Sub-diagram

**Part 1: dispatch on the purpose flag, and forecasting.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P11_IN(["Selected candidate and purpose flag from P10"]) --> P11_PURPOSE{"Purpose flag?"}
    P11_PURPOSE -->|"The future"| P11_POINT_FORECASTS["Point forecasts and horizons<br/>the P0 functional with sample paths or a predictive distribution, for the live origin"]
    P11_PURPOSE -->|"Causes"| P11_TO_PART_2(["Continue in part 2"])
    P11_PURPOSE -->|"Structure in the series or events"| P11_TO_PART_4(["Continue in part 4"])
    P11_PURPOSE -->|"Other outputs"| P11_TO_PART_5(["Continue in part 5"])
    P11_POINT_FORECASTS --> P11_BACK_TRANSFORM["Back-transformation and re-seasonalisation<br/>of the paths; a point forecast back-transformed alone needs a bias adjustment for the mean"]
    P11_BACK_TRANSFORM --> P11_COMBINATION["Forecast combination and model averaging<br/>of the paths or distributions; weights from earlier origins"]
    P11_COMBINATION --> P11_JUDGMENTAL["Judgmental adjustment<br/>tracked by forecast value added"]
    P11_JUDGMENTAL --> P11_HIERARCHY{"Hierarchy flag?"}
    P11_HIERARCHY -->|"Yes"| P11_RECONCILIATION["Hierarchical and temporal reconciliation<br/>bottom-up, top-down, MinT; the paths are reconciled, quantiles are not added"]
    P11_HIERARCHY -->|"No"| P11_INTERVALS
    P11_RECONCILIATION --> P11_INTERVALS["Prediction intervals<br/>from the final paths, or conformal on the final product's errors"]
    P11_INTERVALS --> P11_DENSITY_QUANTILE["Density and quantile forecasts"]
    P11_DENSITY_QUANTILE --> P11_EPIDEMIC_Q{"Epidemic counts?"}
    P11_EPIDEMIC_Q -->|"Yes"| P0_FC_EPIDEMIC[["Reproduction number and SIR fitting"]]
    P11_EPIDEMIC_Q -->|"No"| P11_FC_TO_PART_6
    P0_FC_EPIDEMIC --> P11_FC_TO_PART_6(["Continue in part 6"])
    F_CONDITIONAL_EXPECTATION[["Conditional expectation as the optimal forecast"]] -.- P11_POINT_FORECASTS
    F_PROJECTION[["Projection theorem and best linear prediction"]] -.- P11_INTERVALS
    class P11_IN,P11_TO_PART_2,P11_TO_PART_4,P11_TO_PART_5,P11_FC_TO_PART_6 terminator
    class P11_PURPOSE,P11_HIERARCHY,P11_EPIDEMIC_Q decision
    class P11_POINT_FORECASTS,P11_INTERVALS,P11_DENSITY_QUANTILE,P11_BACK_TRANSFORM,P11_COMBINATION,P11_JUDGMENTAL,P11_RECONCILIATION process
    class F_CONDITIONAL_EXPECTATION,F_PROJECTION,P0_FC_EPIDEMIC ref
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
    P11_PART_2_IN(["From part 1: causes"]) --> P11_POST_SELECTION["Inference after a specification search<br/>pre-specification, sample splitting, bootstrap of the whole procedure"]
    P11_POST_SELECTION --> P11_ERRORS_Q{"Error process modelled?"}
    P11_ERRORS_Q -->|"No"| P11_HAC["HAC inference<br/>Newey-West, bandwidth choice"]
    P11_ERRORS_Q -->|"Yes"| P8_QMLE[["Quasi-maximum likelihood and sandwich standard errors"]]
    P11_HAC & P8_QMLE --> P11_COEFFICIENT_TESTS["Coefficient and restriction tests<br/>t, F, likelihood ratio, Wald, Lagrange multiplier"]
    P11_COEFFICIENT_TESTS --> P11_SYSTEM{"Multivariate flag?"}
    P11_SYSTEM -->|"Yes"| P11_TO_PART_3(["Continue in part 3"])
    P11_SYSTEM -->|"No"| P11_COUNTERFACTUALS["Counterfactual designs<br/>interrupted time series, difference-in-differences, synthetic control, CausalImpact"]
    P11_COUNTERFACTUALS --> P11_PART_2_OUT(["Continue in part 6"])
    class P11_PART_2_IN,P11_TO_PART_3,P11_PART_2_OUT terminator
    class P11_ERRORS_Q,P11_SYSTEM decision
    class P11_POST_SELECTION,P11_COEFFICIENT_TESTS,P11_HAC,P11_COUNTERFACTUALS process
    class P8_QMLE ref
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
    P11_CAUSAL_Q -->|"Long-run relations"| P11_COINTEGRATION["Cointegration inference<br/>restrictions on alpha and beta, weak exogeneity; rank r from P3"]
    P11_CAUSAL_Q -->|"Predictive causality"| P11_GRANGER["Granger, Sims and Toda-Yamamoto causality<br/>Toda-Yamamoto on the levels VAR with d_max from P3"]
    P11_CAUSAL_Q -->|"Nonlinear dependence"| P11_NONLINEAR_CAUSALITY["Nonlinear causal discovery<br/>transfer entropy, convergent cross mapping, PCMCI"]
    P11_CAUSAL_Q -->|"Structural shocks"| P11_SVAR_IDENTIFICATION["SVAR identification<br/>Cholesky, sign restrictions, long-run, external instruments"]
    P11_CAUSAL_Q -->|"Dynamic effects"| P11_LOCAL_PROJECTIONS["Local projections"]
    P11_SVAR_IDENTIFICATION --> P11_IRF_FEVD["Impulse responses and variance decompositions"]
    P11_COINTEGRATION & P11_GRANGER & P11_NONLINEAR_CAUSALITY --> P11_PART_3_OUT
    P11_IRF_FEVD & P11_LOCAL_PROJECTIONS --> P11_PART_3_OUT(["Continue in part 6"])
    class P11_PART_3_IN,P11_PART_3_OUT terminator
    class P11_CAUSAL_Q decision
    class P11_COINTEGRATION,P11_GRANGER,P11_NONLINEAR_CAUSALITY,P11_SVAR_IDENTIFICATION,P11_LOCAL_PROJECTIONS,P11_IRF_FEVD process
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
    P11_STRUCTURE -->|"Frequencies"| P11_SPECTRAL_BANDS["Confidence bands for spectral estimates"]
    P11_EVENTS -->|"Changes"| P11_BREAK_DATE_CI["Break-date confidence intervals"]
    P11_EVENTS -->|"Anomalies or regimes: the operating point from P10"| P11_PART_4_OUT
    P0_SE_SNR & P0_DC_COMPONENT_ANALYSIS & P11_SPECTRAL_BANDS & P11_BREAK_DATE_CI --> P11_PART_4_OUT(["Continue in part 6"])
    class P11_PART_4_IN,P11_PART_4_OUT terminator
    class P11_PURPOSE_4,P11_STRUCTURE,P11_EVENTS decision
    class P11_SPECTRAL_BANDS,P11_BREAK_DATE_CI process
    class P0_SE_SNR,P0_DC_COMPONENT_ANALYSIS ref
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
    P11_OUTPUTS -->|"Features and labels"| P11_FEATURES_TO_PART_6(["Interpretability in part 6"])
    P11_OUTPUTS -->|"A system model"| P0_SI_TRANSFER_FUNCTION[["Estimate the frequency response"]]
    P11_OUTPUTS -->|"Paths for risk and stress"| P11_SCENARIOS["Stress testing and scenario design"]
    P11_OUTPUTS -->|"Synthetic training data"| P0_SM_TSTR[["Train on synthetic, test on real"]]
    P11_OUTPUTS -->|"Paths for uncertainty"| P11_INTERVALS[["Prediction intervals"]]
    P0_SI_TRANSFER_FUNCTION --> P0_SI_STABILITY[["Poles, zeros and stability"]]
    P11_SCENARIOS --> P11_RISK_TO_PART_6(["Risk measures in part 6"])
    P0_SI_STABILITY & P0_SM_TSTR & P11_INTERVALS --> P11_PART_5_OUT(["Continue in part 6"])
    class P11_PART_5_IN,P11_FEATURES_TO_PART_6,P11_RISK_TO_PART_6,P11_PART_5_OUT terminator
    class P11_OUTPUTS decision
    class P11_SCENARIOS process
    class P0_SI_TRANSFER_FUNCTION,P0_SI_STABILITY,P0_SM_TSTR,P11_INTERVALS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 6: risk measures, interpretability and nowcasting.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P11_PART_6_IN(["From parts 1 to 5"]) --> P11_RISK{"Risk measures needed?"}
    P11_RISK -->|"Yes"| P11_RISK_MEASURES["Risk measures and their backtests<br/>VaR, expected shortfall, Kupiec, Christoffersen"]
    P11_RISK -->|"No"| P11_BLACK_BOX
    P11_RISK_MEASURES --> P11_BLACK_BOX{"Black-box model?"}
    P11_BLACK_BOX -->|"Yes"| P11_INTERPRETABILITY["Interpretability<br/>SHAP, attention"]
    P11_BLACK_BOX -->|"No"| P11_MIXED
    P11_INTERPRETABILITY --> P11_MIXED{"Mixed-frequency flag?"}
    P11_MIXED -->|"Yes"| P11_NOWCASTING["Nowcasting<br/>bridge equations, factor models"]
    P11_MIXED -->|"No"| P12
    P11_NOWCASTING --> P12[["P12: Deployment and monitoring"]]
    P6_MIXED_FREQUENCY[["Mixed-frequency models"]] -.- P11_NOWCASTING
    class P11_PART_6_IN terminator
    class P11_RISK,P11_BLACK_BOX,P11_MIXED decision
    class P11_RISK_MEASURES,P11_INTERPRETABILITY,P11_NOWCASTING process
    class P12,P6_MIXED_FREQUENCY ref
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
