# Purpose 5: Anomaly and regime detection

**Goal:** Flag unusual observations or periods and identify state switches.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_AN_IN(["Anomaly or regime question"]) --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P2_AN_KIND{"Anomaly kind?"}
    P2_AN_KIND -->|"Point"| P2_AN_STATISTICAL["Statistical outlier scores<br/>modified z-score, robust statistics"]
    P2_AN_KIND -->|"Contextual"| P2_AN_CONTEXT{"Detector?"}
    P2_AN_KIND -->|"Collective"| P2_AN_COLLECTIVE{"Detector?"}
    P2_AN_KIND -->|"Regime"| P6[["P6: Conditional-mean model class"]]
    P6 --> P6_MARKOV_SWITCHING[["Markov-switching models"]]
    P2_AN_CONTEXT -->|"Model residuals"| P2_AN_RESIDUAL["Residual-based detection from a fitted model"]
    P2_AN_CONTEXT -->|"Reconstruction error"| P2_AN_AUTOENCODER["Autoencoders and variational autoencoders"]
    P2_AN_COLLECTIVE -->|"Distance-based"| P2_AN_MATRIX_PROFILE["Matrix profile and discord discovery"]
    P2_AN_COLLECTIVE -->|"Isolation-based"| P2_AN_ISOLATION_FOREST["Isolation forests for time series"]
    P2_AN_RESIDUAL & P2_AN_AUTOENCODER & P6_MARKOV_SWITCHING --> P2_AN_LABELS{"Labels available?"}
    P2_AN_LABELS -->|"Yes: tune the model"| P8[["P8: Estimation"]]
    P2_AN_LABELS -->|"No"| P2_AN_THRESHOLD
    P8 --> P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]]
    P8_HYPERPARAMETERS --> P2_AN_THRESHOLD["Set thresholds by the cost of errors"]
    P2_AN_STATISTICAL & P2_AN_MATRIX_PROFILE & P2_AN_ISOLATION_FOREST --> P2_AN_THRESHOLD
    P2_AN_THRESHOLD --> P11[["P11: Validation and deployment"]]
    P11 --> P11_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    P11_CLASSIFICATION_METRICS --> P11_DRIFT_MONITORING[["Drift monitoring"]]
    class P2_AN_IN terminator
    class P2_AN_KIND,P2_AN_CONTEXT,P2_AN_COLLECTIVE,P2_AN_LABELS decision
    class P2_AN_STATISTICAL,P2_AN_RESIDUAL,P2_AN_AUTOENCODER,P2_AN_MATRIX_PROFILE,P2_AN_ISOLATION_FOREST,P2_AN_THRESHOLD process
    class P3,P6,P6_MARKOV_SWITCHING,P8,P8_HYPERPARAMETERS,P11,P11_CLASSIFICATION_METRICS,P11_DRIFT_MONITORING ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P10 inference for this purpose

[Set thresholds by the cost of errors](../../reference/19-classification-anomaly/index.md#set-thresholds-by-the-cost-of-errors).

## P11 metrics for this purpose

[Classification and anomaly metrics](../../reference/19-classification-anomaly/index.md#classification-and-anomaly-metrics), [Drift monitoring](../../reference/23-online-adaptive/index.md#drift-monitoring).
