# Purpose 4: Change-point detection

**Goal:** Locate the times at which the statistical properties change.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_CP_IN(["Change-point question"]) --> P3_STRUCTURAL_BREAKS[["Structural-break tests"]]
    P3_STRUCTURAL_BREAKS --> P2_CP_MODE{"Online or offline?"}
    P2_CP_MODE -->|"Online"| P2_CP_ONLINE{"Detector?"}
    P2_CP_MODE -->|"Offline"| P2_CP_PELT["Offline segmentation<br/>PELT, binary segmentation"]
    P2_CP_MODE -->|"Multivariate"| P2_CP_MULTIVARIATE["Multivariate change points<br/>E-divisive"]
    P2_CP_ONLINE -->|"Sequential statistic"| P2_CP_CUSUM["Sequential detection<br/>CUSUM, Page-Hinkley"]
    P2_CP_ONLINE -->|"Bayesian"| P2_CP_BOCPD["Bayesian online change-point detection"]
    P2_CP_PELT --> P2_CP_PENALTY["Choose the number of change points<br/>penalty, BIC"]
    P2_CP_CUSUM & P2_CP_BOCPD & P2_CP_PENALTY & P2_CP_MULTIVARIATE --> P2_CP_TYPE["Classify the change<br/>mean, variance, regime"]
    P2_CP_TYPE --> P2_CP_KIND{"Change kind?"}
    P2_CP_KIND -->|"Mean"| P4_BREAK_HANDLING[["Handle structural breaks"]]
    P2_CP_KIND -->|"Regime"| P6_MARKOV_SWITCHING[["Markov-switching models"]]
    P2_CP_KIND -->|"Variance"| P7_MS_GARCH[["Markov-switching GARCH and segmented variance"]]
    P4_BREAK_HANDLING & P6_MARKOV_SWITCHING & P7_MS_GARCH --> P11_CHANGE_POINT_METRICS[["Change-point metrics"]]
    P11_CHANGE_POINT_METRICS --> P11[["P11: Validation and deployment"]]
    class P2_CP_IN terminator
    class P2_CP_MODE,P2_CP_ONLINE,P2_CP_KIND decision
    class P2_CP_PELT,P2_CP_MULTIVARIATE,P2_CP_CUSUM,P2_CP_BOCPD,P2_CP_PENALTY,P2_CP_TYPE process
    class P3_STRUCTURAL_BREAKS,P4_BREAK_HANDLING,P6_MARKOV_SWITCHING,P7_MS_GARCH,P11_CHANGE_POINT_METRICS,P11 ref
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

[Classify the change](../../reference/30-structural-change/index.md#classify-the-change).

## P11 metrics for this purpose

[Change-point metrics](../../reference/19-classification-anomaly/index.md#change-point-metrics).
