# Purpose 4: Change-point detection

**Goal:** Locate the times at which the statistical properties change.

## Sub-chart

**Part 1: task, data and the property that changes.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_CP_IN(["Change-point question"]) --> P0_DETECTION_TASK[["Specify the detection task"]]
    P0_DETECTION_TASK --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P3_STRUCTURAL_BREAKS[["Structural-break tests"]]
    P3_STRUCTURAL_BREAKS --> P4[["P4: Transformations"]]
    P4 --> P0_CP_PROPERTY{"Which property changes?"}
    P4_INTEGRATED_LEVELS[["Integrated series kept in levels"]] -.- P4
    P0_CP_PROPERTY -->|"Mean, variance or distribution"| P0_CP_SERIAL{"Serial dependence within segments?"}
    P0_CP_PROPERTY -->|"A recurring regime"| P6[["P6: Conditional-mean model class"]]
    P0_CP_SERIAL -->|"Yes"| P0_CP_DEPENDENT["Dependence-aware detection<br/>AR-aware costs, long-run variance scaling, prewhitened residuals"]
    P0_CP_SERIAL -->|"No"| P0_CP_TO_PART_2
    P0_CP_DEPENDENT --> P0_CP_TO_PART_2(["Continue in part 2"])
    P6 --> P6_MARKOV_SWITCHING[["Markov-switching models"]]
    P6_MARKOV_SWITCHING --> P7[["P7: Error-process specification"]]
    P7 --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> P0_CP_REGIME_TO_PART_3(["Continue in part 3"])
    P7_MS_GARCH[["Markov-switching GARCH and segmented variance"]] -.- P7
    class P0_CP_IN,P0_CP_TO_PART_2,P0_CP_REGIME_TO_PART_3 terminator
    class P0_CP_PROPERTY,P0_CP_SERIAL decision
    class P0_CP_DEPENDENT process
    class P0_DETECTION_TASK,P1,P3,P3_STRUCTURAL_BREAKS,P4,P6,P6_MARKOV_SWITCHING,P7,P8,P9,P7_MS_GARCH,P4_INTEGRATED_LEVELS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: online or offline, then dimension.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_CP_PART_2_IN(["From part 1"]) --> P0_CP_MODE{"Online or offline?"}
    P0_CP_MODE -->|"Online"| P0_CP_DIM_ONLINE{"Univariate or multivariate?"}
    P0_CP_MODE -->|"Offline"| P0_CP_DIM_OFFLINE{"Univariate or multivariate?"}
    P0_CP_DIM_ONLINE -->|"Univariate"| P0_CP_ONLINE{"Detector?"}
    P0_CP_DIM_ONLINE -->|"Multivariate"| P0_CP_MULTIVARIATE
    P0_CP_DIM_OFFLINE -->|"Univariate"| P0_CP_PELT["Offline segmentation<br/>PELT, binary segmentation"]
    P0_CP_DIM_OFFLINE -->|"Multivariate"| P0_CP_MULTIVARIATE["Multivariate change points<br/>online: multivariate CUSUM and BOCPD; offline: E-divisive"]
    P0_CP_ONLINE -->|"Sequential statistic"| P0_CP_CUSUM["Sequential detection<br/>CUSUM, Page-Hinkley"]
    P0_CP_ONLINE -->|"Bayesian"| P0_CP_BOCPD["Bayesian online change-point detection"]
    P0_CP_CUSUM & P0_CP_BOCPD --> P0_CP_CALIBRATE["Calibrate the threshold<br/>ARL0 against detection delay on in-control data"]
    P0_CP_PELT --> P0_CP_PENALTY["Choose the number of change points<br/>penalty, BIC"]
    P0_CP_CALIBRATE & P0_CP_PENALTY & P0_CP_MULTIVARIATE --> P0_CP_TYPE["Classify the change<br/>mean, variance, regime"]
    P0_CP_TYPE --> P0_CP_PART_2_OUT(["Continue in part 3"])
    class P0_CP_PART_2_IN,P0_CP_PART_2_OUT terminator
    class P0_CP_MODE,P0_CP_DIM_ONLINE,P0_CP_DIM_OFFLINE,P0_CP_ONLINE decision
    class P0_CP_PELT,P0_CP_MULTIVARIATE,P0_CP_CUSUM,P0_CP_BOCPD,P0_CP_CALIBRATE,P0_CP_PENALTY,P0_CP_TYPE process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: evaluation, inference and deployment.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_CP_PART_3_IN(["From parts 1 and 2"]) --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P10_CHANGE_POINT_METRICS[["Change-point metrics"]]
    P10_CHANGE_POINT_METRICS --> P11[["P11: Inference and interpretation"]]
    P11 --> P11_BREAK_DATE_CI[["Break-date confidence intervals"]]
    P11_BREAK_DATE_CI --> P12[["P12: Deployment and monitoring"]]
    class P0_CP_PART_3_IN terminator
    class P10,P10_CHANGE_POINT_METRICS,P11,P11_BREAK_DATE_CI,P12 ref
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

[Change-point metrics](../../reference/19-classification-anomaly/index.md#change-point-metrics).

## P11 inference for this purpose

[Break-date confidence intervals](../../reference/30-structural-change/index.md#break-date-confidence-intervals).
