# P10: Out-of-sample evaluation and selection

**Question this phase answers:** Which candidate, or baseline, predicts or detects best on data it has not seen?

P10 is an as-of-origin simulation for forecasting and online detection. At each origin, every data-dependent choice of P1 to P9 is refitted on the data before the origin (imputation, clustering, break dates and the integration, seasonal and cointegration verdicts, the variance transform, d, decomposition, seasonal adjustment, features and scaling, model orders, the error specification, tuning and information-criterion selection), because a choice fitted on the full sample leaks the future into the evaluation. The final hold-out reserved in P0 is touched by no phase before P10. Data enter as they stood at the origin (vintages, right-truncated counts when the reporting-delay flag is set), covariates that are external forecasts enter as issued, and the refit cadence and window type match the retraining policy of P12. A forecaster scores the complete product it will issue, on the target scale against raw actuals, with the P0 baselines in the comparison set. The selected candidate's accuracy is reported on data the selection never saw. Documentation and the retraining policy follow in [P12](p12-deployment-monitoring.md).

## Sub-diagram

**Part 1: the as-of-origin simulation and the purpose routes.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_IN(["Candidates from P9, or outputs of routes that fit no model"]) --> P10_PURPOSE{"Purpose flag?"}
    P10_PURPOSE -->|"Forecasting or online detection"| P10_ROLLING_ORIGIN["Rolling-origin backtesting<br/>at the P0 horizons, as of each origin: refit every data-dependent choice of P1 to P9 on earlier data; vintages; covariate forecasts as issued"]
    P10_PURPOSE -->|"Offline detection, collections"| P10_COLLECTIONS_TO_PART_3(["Continue in part 3"])
    P10_PURPOSE -->|"Other purposes"| P10_TO_PART_4(["Continue in part 4"])
    P10_ROLLING_ORIGIN --> P10_TIME_PURPOSE{"Forecasting or detection?"}
    P10_TIME_PURPOSE -->|"Forecasting"| P10_TO_PART_2(["Continue in part 2"])
    P10_TIME_PURPOSE -->|"Online detection"| P10_TO_PART_3(["Continue in part 3"])
    class P10_IN,P10_TO_PART_2,P10_TO_PART_3,P10_COLLECTIONS_TO_PART_3,P10_TO_PART_4 terminator
    class P10_PURPOSE,P10_TIME_PURPOSE decision
    class P10_ROLLING_ORIGIN process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: forecasting.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_2_IN(["From part 1: forecasting"]) --> P0_FC_BASELINES[["Baselines for comparison"]]
    P0_FC_BASELINES --> P10_FORECAST_PRODUCT["Complete forecast product per origin<br/>point functional and paths, back-transformation, combination, reconciliation, then intervals and quantiles"]
    P10_FORECAST_PRODUCT --> P10_POINT_METRICS["Point-forecast metrics<br/>MAE, RMSE, MASE, RMSSE; MAPE only for strictly positive data"]
    P10_POINT_METRICS --> P10_PROBABILISTIC_METRICS["Probabilistic metrics<br/>CRPS, pinball loss, log score, interval score; PIT and coverage"]
    P10_PROBABILISTIC_METRICS --> P10_FORECAST_COMPARISON["Forecast comparison tests<br/>Diebold-Mariano, Clark-West, reality check, model confidence set"]
    P10_FORECAST_COMPARISON --> P10_ENCOMPASSING["Forecast encompassing"]
    P10_ENCOMPASSING --> P10_PART_2_OUT(["Continue in part 5"])
    class P10_PART_2_IN,P10_PART_2_OUT terminator
    class P10_FORECAST_PRODUCT,P10_POINT_METRICS,P10_PROBABILISTIC_METRICS,P10_FORECAST_COMPARISON,P10_ENCOMPASSING process
    class P0_FC_BASELINES ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: detection and collections.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_3_IN(["From part 1: detection or collections"]) --> P10_EVENTS{"What is evaluated?"}
    P10_EVENTS -->|"Collections"| P10_GROUPED_SPLITS["Grouped and temporal splits<br/>split unit from P0; augmentation and tuning inside training folds; cluster stability"]
    P10_EVENTS -->|"Anomalies or regimes"| P0_AN_THRESHOLD[["Set thresholds by the cost of errors<br/>at each origin, on earlier data"]]
    P0_AN_THRESHOLD --> P10_LABELS{"Labels flag?"}
    P10_EVENTS -->|"Change points"| P10_CHANGE_POINT_METRICS["Change-point metrics<br/>online: ARL0, detection delay; offline: F1 with margin, Hausdorff, Rand index"]
    P10_LABELS -->|"Few"| P10_CLASSIFICATION_METRICS["Classification and anomaly metrics<br/>event-level and range-based precision and recall; delay; lead time"]
    P10_LABELS -->|"None"| P10_UNLABELLED["Synthetic injection and expert review<br/>injected anomalies; review of the top alarms"]
    P10_GROUPED_SPLITS --> P10_COLLECTION_TASK{"Task?"}
    P10_COLLECTION_TASK -->|"Supervised"| P10_CLASSIFICATION_METRICS
    P10_COLLECTION_TASK -->|"Clustering"| P10_CLUSTER_VALIDATION["Cluster validation<br/>internal indices, stability under resampling"]
    P10_CLASSIFICATION_METRICS & P10_UNLABELLED & P10_CHANGE_POINT_METRICS & P10_CLUSTER_VALIDATION --> P10_PART_3_OUT(["Continue in part 5"])
    class P10_PART_3_IN,P10_PART_3_OUT terminator
    class P10_EVENTS,P10_LABELS,P10_COLLECTION_TASK decision
    class P0_AN_THRESHOLD ref
    class P10_GROUPED_SPLITS,P10_CHANGE_POINT_METRICS,P10_CLASSIFICATION_METRICS,P10_UNLABELLED,P10_CLUSTER_VALIDATION process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: signal extraction, simulation, system identification and inference-only purposes.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_4_IN(["From part 1"]) --> P10_OUTPUTS{"Purpose?"}
    P10_OUTPUTS -->|"Signal extraction"| P10_SIGNAL_EVALUATION["Signal-extraction evaluation<br/>synthetic signal; level-wise SURE"]
    P10_OUTPUTS -->|"Simulation"| P0_SM_DISTRIBUTION_MATCH[["Check distribution and dependence matching"]]
    P10_OUTPUTS -->|"System identification"| P0_SI_VALIDATION[["Validate on held-out input-output data"]]
    P10_OUTPUTS -->|"Inference only"| P10_INFERENCE_ONLY{"What is inferred?"}
    P10_INFERENCE_ONLY -->|"Causes"| P0_CA_PLACEBO[["Placebo and falsification tests"]]
    P0_CA_PLACEBO --> P0_CA_SENSITIVITY[["Sensitivity analysis across specifications"]]
    P10_INFERENCE_ONLY -->|"Components"| P0_DC_DIAGNOSTICS[["Decomposition diagnostics"]]
    P10_INFERENCE_ONLY -->|"Frequencies"| P0_SP_PEAK_SIGNIFICANCE[["Peak significance"]]
    P10_SIGNAL_EVALUATION & P0_SM_DISTRIBUTION_MATCH & P0_SI_VALIDATION --> P10_PART_4_OUT(["Continue in part 5"])
    P0_CA_SENSITIVITY & P0_DC_DIAGNOSTICS & P0_SP_PEAK_SIGNIFICANCE --> P10_PART_4_OUT
    class P10_PART_4_IN,P10_PART_4_OUT terminator
    class P10_OUTPUTS,P10_INFERENCE_ONLY decision
    class P10_SIGNAL_EVALUATION process
    class P0_SM_DISTRIBUTION_MATCH,P0_SI_VALIDATION,P0_CA_PLACEBO,P0_CA_SENSITIVITY,P0_DC_DIAGNOSTICS,P0_SP_PEAK_SIGNIFICANCE ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: selection and exits.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_5_IN(["From parts 2 to 4"]) --> P10_SELECT{"Outcome?"}
    P10_SELECT -->|"Select: forecasting, online detection, collections"| P10_FINAL_HOLDOUT["Final hold-out or nested rolling origin<br/>on the data reserved in P0; reports the selected candidate's accuracy"]
    P10_SELECT -->|"Checks passed: other purposes"| P10_OUT
    P10_SELECT -->|"Add a candidate, or none acceptable"| P10_REVISE{"What is revised?"}
    P10_REVISE -.->|"A model"| P6[["P6: Conditional-mean model class"]]
    P10_REVISE -.->|"A method that fits no model"| P0[["P0: Purpose and evaluation plan<br/>the method part of the purpose chart"]]
    P10_REVISE -.->|"Causal identification"| P0_CA_IDENTIFICATION[["Identification strategy and exogeneity"]]
    P10_FINAL_HOLDOUT --> P10_OUT(["To P11 Inference and interpretation"])
    class P10_PART_5_IN,P10_OUT terminator
    class P10_SELECT,P10_REVISE decision
    class P10_FINAL_HOLDOUT process
    class P6,P0,P0_CA_IDENTIFICATION ref
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

## Rolling-origin backtesting

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P10_ROLLING_ORIGIN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Complete forecast product per origin

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P10_FORECAST_PRODUCT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Final hold-out or nested rolling origin

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P10_FINAL_HOLDOUT`). Write this section following the content rules in `.claude/rules/writing.md`.
