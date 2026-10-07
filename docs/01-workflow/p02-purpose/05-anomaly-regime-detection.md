# Purpose 5: Anomaly and regime detection

**Goal:** Flag unusual observations or periods and identify state switches.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_AN_IN(["Anomaly or regime question"]) --> P2_AN_TYPE["Point, contextual or collective anomaly"]
    P2_AN_TYPE --> P2_AN_KIND{"Anomaly kind?"}
    P2_AN_KIND -->|"Point"| P2_AN_STATISTICAL["Statistical outlier scores<br/>modified z-score, robust statistics"]
    P2_AN_KIND -->|"Contextual"| P2_AN_RESIDUAL["Residual-based detection from a fitted model"]
    P2_AN_KIND -->|"Collective"| P2_AN_MATRIX_PROFILE["Matrix profile and discord discovery"]
    P2_AN_KIND -->|"Regime"| P2_AN_REGIME["Regime detection with hidden Markov models"]
    P2_AN_RESIDUAL --> P2_AN_AUTOENCODER["Autoencoders and variational autoencoders"]
    P2_AN_MATRIX_PROFILE --> P2_AN_ISOLATION_FOREST["Isolation forests for time series"]
    P2_AN_STATISTICAL & P2_AN_AUTOENCODER & P2_AN_ISOLATION_FOREST & P2_AN_REGIME --> P2_AN_THRESHOLD["Set thresholds by the cost of errors"]
    P2_AN_THRESHOLD --> P2_AN_LABELS{"Labels available?"}
    P2_AN_LABELS -->|"Yes"| P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]]
    P2_AN_LABELS -->|"No"| P11_DRIFT_MONITORING[["Drift monitoring"]]
    P8_HYPERPARAMETERS & P11_DRIFT_MONITORING --> P11_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    P11_CLASSIFICATION_METRICS --> P2_AN_OUT(["Anomalies and regimes flagged"])
    class P2_AN_IN,P2_AN_OUT terminator
    class P2_AN_KIND,P2_AN_LABELS decision
    class P2_AN_TYPE,P2_AN_STATISTICAL,P2_AN_RESIDUAL,P2_AN_MATRIX_PROFILE,P2_AN_REGIME,P2_AN_AUTOENCODER,P2_AN_ISOLATION_FOREST,P2_AN_THRESHOLD process
    class P8_HYPERPARAMETERS,P11_DRIFT_MONITORING,P11_CLASSIFICATION_METRICS ref
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

Thresholds and regime probabilities.

## P11 metrics for this purpose

Event-level precision and recall, NAB score.
