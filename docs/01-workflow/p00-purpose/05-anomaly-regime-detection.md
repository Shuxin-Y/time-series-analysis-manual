# Purpose 5: Anomaly and regime detection

**Goal:** Flag unusual observations or periods and identify state switches.

## Sub-chart

**Part 1: task, data and the anomaly kind.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_AN_IN(["Anomaly or regime question"]) --> P0_DETECTION_TASK[["Specify the detection task"]]
    P0_DETECTION_TASK --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P4[["P4: Transformations"]]
    P4 --> P0_AN_KIND{"Anomaly kind?"}
    P0_AN_KIND -->|"Point"| P0_AN_SEASONAL{"Trend or seasonality present?"}
    P0_AN_KIND -->|"Contextual"| P0_AN_CONTEXT{"Detector?"}
    P0_AN_KIND -->|"Collective"| P0_AN_COLLECTIVE{"Detector?"}
    P0_AN_KIND -->|"Regime"| P0_AN_TO_PART_2(["Continue in part 2"])
    P0_AN_SEASONAL -->|"Yes: score the remainder"| P4_SEASONAL_ADJUSTMENT[["Seasonal adjustment"]]
    P0_AN_SEASONAL -->|"No"| P0_AN_STATISTICAL
    P4_SEASONAL_ADJUSTMENT --> P0_AN_STATISTICAL["Statistical outlier scores<br/>modified z-score, robust statistics"]
    P0_AN_CONTEXT -->|"Model residuals"| P0_AN_TO_PART_2
    P0_AN_CONTEXT -->|"Reconstruction error"| P0_AN_AUTOENCODER["Autoencoders and variational autoencoders"]
    P0_AN_COLLECTIVE -->|"Distance-based"| P0_AN_MATRIX_PROFILE["Matrix profile and discord discovery"]
    P0_AN_COLLECTIVE -->|"Isolation-based"| P0_AN_ISOLATION_FOREST["Isolation forests for time series"]
    P0_AN_STATISTICAL & P0_AN_AUTOENCODER & P0_AN_MATRIX_PROFILE & P0_AN_ISOLATION_FOREST --> P0_AN_TO_PART_3(["Continue in part 3"])
    class P0_AN_IN,P0_AN_TO_PART_2,P0_AN_TO_PART_3 terminator
    class P0_AN_KIND,P0_AN_SEASONAL,P0_AN_CONTEXT,P0_AN_COLLECTIVE decision
    class P0_AN_STATISTICAL,P0_AN_AUTOENCODER,P0_AN_MATRIX_PROFILE,P0_AN_ISOLATION_FOREST process
    class P0_DETECTION_TASK,P1,P3,P4,P4_SEASONAL_ADJUSTMENT ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: detection from a fitted model.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_AN_PART_2_IN(["From part 1: regimes or model residuals"]) --> P6[["P6: Conditional-mean model class"]]
    P6 --> P0_AN_FIT{"Model?"}
    P0_AN_FIT -->|"Switching regimes"| P6_MARKOV_SWITCHING[["Markov-switching models"]]
    P0_AN_FIT -->|"Conditional mean"| P6_CANDIDATE_SET[["Candidate set"]]
    P6_MARKOV_SWITCHING & P6_CANDIDATE_SET --> P7[["P7: Error-process specification"]]
    P7 --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> P0_AN_RESIDUAL["Residual-based detection from a fitted model<br/>one-step residuals or regime probabilities: filtered in real time, smoothed offline"]
    P0_AN_RESIDUAL --> P0_AN_PART_2_OUT(["Continue in part 3"])
    class P0_AN_PART_2_IN,P0_AN_PART_2_OUT terminator
    class P0_AN_FIT decision
    class P0_AN_RESIDUAL process
    class P6,P6_MARKOV_SWITCHING,P6_CANDIDATE_SET,P7,P8,P9 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: thresholds, evaluation and monitoring.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_AN_PART_3_IN(["From parts 1 and 2"]) --> P0_AN_THRESHOLD["Set thresholds by the cost of errors"]
    P0_AN_THRESHOLD --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P0_AN_LABELS{"Labels flag?"}
    P0_AN_LABELS -->|"Few"| P10_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    P0_AN_LABELS -->|"None"| P10_UNLABELLED[["Synthetic injection and expert review"]]
    P10_CLASSIFICATION_METRICS & P10_UNLABELLED --> P11[["P11: Inference and interpretation"]]
    P11 --> P12[["P12: Deployment and monitoring"]]
    P12 --> P12_DRIFT_MONITORING[["Drift monitoring"]]
    class P0_AN_PART_3_IN terminator
    class P0_AN_LABELS decision
    class P0_AN_THRESHOLD process
    class P10,P10_CLASSIFICATION_METRICS,P10_UNLABELLED,P11,P12,P12_DRIFT_MONITORING ref
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

[Classification and anomaly metrics](../../reference/19-classification-anomaly/index.md#classification-and-anomaly-metrics), [Synthetic injection and expert review](../../reference/19-classification-anomaly/index.md#synthetic-injection-and-expert-review).

## P11 inference for this purpose

[Set thresholds by the cost of errors](../../reference/19-classification-anomaly/index.md#set-thresholds-by-the-cost-of-errors).

## P12 monitoring for this purpose

[Drift monitoring](../../reference/23-online-adaptive/index.md#drift-monitoring).
