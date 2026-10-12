# Purpose 2: Causal and structural inference

**Goal:** Determine whether and how one series drives another, and quantify the effect.

## Sub-chart

**Part 1: estimand, design and the modelled route.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_CA_IN(["Causal question"]) --> P0_ESTIMAND[["Specify the estimand"]]
    P0_ESTIMAND --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P0_CA_DESIGN{"Design?"}
    P0_CA_DESIGN -->|"Randomised, many units"| P0_CA_TO_PART_2(["Continue in part 2"])
    P0_CA_DESIGN -->|"Natural experiment, single-series intervention, or observational"| P3
    P3[["P3: Exploratory diagnostics"]] --> P0_CA_MULTI{"Multivariate flag?"}
    P0_CA_MULTI -->|"Yes"| P3_COINTEGRATION_PRECHECK[["Cointegration tests"]]
    P0_CA_MULTI -->|"No"| P4
    P3_COINTEGRATION_PRECHECK --> P4[["P4: Transformations"]]
    P4 --> P6[["P6: Conditional-mean model class"]]
    P6 --> P0_CA_MODEL{"Model?"}
    P0_CA_MODEL -->|"Rank r of at least 1"| P6_VECM[["VECM"]]
    P0_CA_MODEL -->|"No cointegration, or mixed orders"| P6_VAR[["VAR"]]
    P0_CA_MODEL -->|"Single equation or intervention"| P6_TRANSFER_FUNCTION[["Transfer-function and intervention models"]]
    P6_VECM & P6_VAR & P6_TRANSFER_FUNCTION --> P0_CA_IDENTIFICATION["Identification strategy and exogeneity"]
    P0_CA_IDENTIFICATION --> P7[["P7: Error-process specification"]]
    P7 --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> P0_CA_TO_PART_2
    class P0_CA_IN,P0_CA_TO_PART_2 terminator
    class P0_CA_DESIGN,P0_CA_MULTI,P0_CA_MODEL decision
    class P0_CA_IDENTIFICATION process
    class P0_ESTIMAND,P1,P3,P3_COINTEGRATION_PRECHECK,P4,P6,P6_VECM,P6_VAR,P6_TRANSFER_FUNCTION,P7,P8,P9 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: robustness of the identification.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_CA_PART_2_IN(["From part 1"]) --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P0_CA_PLACEBO["Placebo and falsification tests"]
    P0_CA_PLACEBO --> P0_CA_SENSITIVITY["Sensitivity analysis across specifications"]
    P0_CA_SENSITIVITY --> P0_CA_VERDICT{"Identification holds?"}
    P0_CA_VERDICT -->|"Robust"| P0_CA_PART_2_OUT(["Continue in part 3"])
    P0_CA_VERDICT -.->|"Fragile, experiment: revisit the design"| P0_CA_DESIGN[["Design?"]]
    P0_CA_VERDICT -.->|"Fragile, observational: revisit identification"| P0_CA_IDENTIFICATION[["Identification strategy and exogeneity"]]
    class P0_CA_PART_2_IN,P0_CA_PART_2_OUT terminator
    class P0_CA_VERDICT decision
    class P0_CA_PLACEBO,P0_CA_SENSITIVITY process
    class P10,P0_CA_DESIGN,P0_CA_IDENTIFICATION ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: inference.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_CA_PART_3_IN(["From part 2"]) --> P11[["P11: Inference and interpretation"]]
    P11 --> P11_POST_SELECTION[["Inference after a specification search"]]
    P11_POST_SELECTION --> P0_CA_ANALYSIS{"Analysis?"}
    P0_CA_ANALYSIS -->|"Experiment, or one series"| P11_COUNTERFACTUALS[["Counterfactual designs"]]
    P0_CA_ANALYSIS -->|"Multivariate flag"| P0_CA_QUESTION{"Causal question?"}
    P0_CA_QUESTION -->|"Long-run relations"| P11_COINTEGRATION[["Cointegration inference"]]
    P0_CA_QUESTION -->|"Predictive causality"| P11_GRANGER[["Granger, Sims and Toda-Yamamoto causality"]]
    P0_CA_QUESTION -->|"Nonlinear dependence"| P11_NONLINEAR_CAUSALITY[["Nonlinear causal discovery"]]
    P0_CA_QUESTION -->|"Structural shocks"| P11_SVAR_IDENTIFICATION[["SVAR identification"]]
    P0_CA_QUESTION -->|"Dynamic effects"| P11_LOCAL_PROJECTIONS[["Local projections"]]
    P11_SVAR_IDENTIFICATION --> P11_IRF_FEVD[["Impulse responses and variance decompositions"]]
    P11_COINTEGRATION & P11_GRANGER & P11_NONLINEAR_CAUSALITY & P11_IRF_FEVD --> P11_COEFFICIENT_TESTS
    P11_LOCAL_PROJECTIONS & P11_COUNTERFACTUALS --> P11_COEFFICIENT_TESTS[["Coefficient and restriction tests"]]
    P11_COEFFICIENT_TESTS --> P12[["P12: Deployment and monitoring"]]
    P11_HAC[["HAC inference"]] -.- P11_COEFFICIENT_TESTS
    class P0_CA_PART_3_IN terminator
    class P0_CA_ANALYSIS,P0_CA_QUESTION decision
    class P11,P11_POST_SELECTION,P11_COUNTERFACTUALS,P11_COINTEGRATION,P11_GRANGER,P11_NONLINEAR_CAUSALITY,P11_SVAR_IDENTIFICATION,P11_LOCAL_PROJECTIONS,P11_IRF_FEVD,P11_COEFFICIENT_TESTS,P11_HAC,P12 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P10 metrics for this purpose

[Placebo and falsification tests](../../reference/21-causal-inference/index.md#placebo-and-falsification-tests), [Sensitivity analysis across specifications](../../reference/21-causal-inference/index.md#sensitivity-analysis-across-specifications).

## P11 inference for this purpose

[Inference after a specification search](../../reference/05-hypothesis-testing/index.md#inference-after-a-specification-search), [Counterfactual designs](../../reference/21-causal-inference/index.md#counterfactual-designs), [Cointegration inference](../../reference/28-nonstationarity-theory/index.md#cointegration-inference), [Granger, Sims and Toda-Yamamoto causality](../../reference/21-causal-inference/index.md#granger-sims-and-toda-yamamoto-causality), [Nonlinear causal discovery](../../reference/21-causal-inference/index.md#nonlinear-causal-discovery), [SVAR identification](../../reference/21-causal-inference/index.md#svar-identification), [Impulse responses and variance decompositions](../../reference/09-multivariate/index.md#impulse-responses-and-variance-decompositions), [Local projections](../../reference/21-causal-inference/index.md#local-projections), [Coefficient and restriction tests](../../reference/05-hypothesis-testing/index.md#coefficient-and-restriction-tests), [HAC inference](../../reference/27-regression-time-series/index.md#hac-inference).
