# Purpose 5: Anomaly and regime detection

**Goal:** Flag unusual observations or periods and identify state switches.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_AN_IN(["Anomaly or regime question"]) --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P0_AN_KIND{"Anomaly kind?"}
    P0_AN_KIND -->|"Point"| P0_AN_STATISTICAL["Statistical outlier scores<br/>modified z-score, robust statistics"]
    P0_AN_KIND -->|"Contextual"| P0_AN_CONTEXT{"Detector?"}
    P0_AN_KIND -->|"Collective"| P0_AN_COLLECTIVE{"Detector?"}
    P0_AN_KIND -->|"Regime"| P6[["P6: Conditional-mean model class"]]
    P0_AN_CONTEXT -->|"Model residuals"| P6
    P0_AN_CONTEXT -->|"Reconstruction error"| P0_AN_AUTOENCODER["Autoencoders and variational autoencoders"]
    P6 --> P0_AN_FIT{"Fitted model?"}
    P0_AN_FIT -->|"Switching regimes"| P6_MARKOV_SWITCHING[["Markov-switching models"]]
    P0_AN_FIT -->|"Conditional mean"| P0_AN_RESIDUAL["Residual-based detection from a fitted model"]
    P0_AN_COLLECTIVE -->|"Distance-based"| P0_AN_MATRIX_PROFILE["Matrix profile and discord discovery"]
    P0_AN_COLLECTIVE -->|"Isolation-based"| P0_AN_ISOLATION_FOREST["Isolation forests for time series"]
    P0_AN_RESIDUAL & P6_MARKOV_SWITCHING --> P0_AN_LABELS{"Labels available?"}
    P0_AN_LABELS -->|"Yes: tune the model"| P8[["P8: Estimation"]]
    P0_AN_LABELS -->|"No"| P0_AN_THRESHOLD
    P8 --> P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]]
    P8_HYPERPARAMETERS --> P0_AN_THRESHOLD["Set thresholds by the cost of errors"]
    P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]] -.- P0_AN_AUTOENCODER
    P0_AN_STATISTICAL & P0_AN_AUTOENCODER & P0_AN_MATRIX_PROFILE & P0_AN_ISOLATION_FOREST --> P0_AN_THRESHOLD
    P0_AN_THRESHOLD --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P10_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    P10_CLASSIFICATION_METRICS --> P12_DRIFT_MONITORING[["Drift monitoring"]]
    class P0_AN_IN terminator
    class P0_AN_KIND,P0_AN_CONTEXT,P0_AN_COLLECTIVE,P0_AN_FIT,P0_AN_LABELS decision
    class P0_AN_STATISTICAL,P0_AN_AUTOENCODER,P0_AN_RESIDUAL,P0_AN_MATRIX_PROFILE,P0_AN_ISOLATION_FOREST,P0_AN_THRESHOLD process
    class P3,P6,P6_MARKOV_SWITCHING,P8,P8_HYPERPARAMETERS,P10,P10_CLASSIFICATION_METRICS,P12_DRIFT_MONITORING ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P11 inference for this purpose

[Set thresholds by the cost of errors](../../reference/19-classification-anomaly/index.md#set-thresholds-by-the-cost-of-errors).

## P10 metrics for this purpose

[Classification and anomaly metrics](../../reference/19-classification-anomaly/index.md#classification-and-anomaly-metrics), [Drift monitoring](../../reference/23-online-adaptive/index.md#drift-monitoring).
