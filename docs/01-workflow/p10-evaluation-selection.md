# P10: Out-of-sample evaluation and selection

**Question this phase answers:** Which candidate predicts or detects best on data it has not seen?

Rolling-origin validation and backtesting, purpose-specific metrics, and the acceptance decision.

## Sub-diagram

**Part 1: backtesting and metrics for the future, causes and structure.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_IN(["Adequate candidates from P9"]) --> P10_ROLLING_ORIGIN["Rolling-origin backtesting<br/>look-ahead bias, backtest overfitting"]
    P10_ROLLING_ORIGIN --> P10_METRIC_KIND{"Purpose flag?"}
    P10_METRIC_KIND -->|"The future"| P10_POINT_METRICS["Point-forecast metrics<br/>RMSE, MAE, MAPE, MASE"]
    P10_METRIC_KIND -->|"Causes"| P0_CA_SENSITIVITY[["Sensitivity analysis across specifications"]]
    P10_METRIC_KIND -->|"Structure in the series"| P10_STRUCTURE{"Which structure?"}
    P10_METRIC_KIND -->|"Events or other outputs"| P10_TO_PART_2(["Continue in part 2"])
    P10_POINT_METRICS --> P10_PROBABILISTIC_METRICS["Probabilistic metrics<br/>coverage, CRPS, pinball loss, log score, PIT"]
    P10_STRUCTURE -->|"Signal versus noise"| P0_SE_SNR[["Evaluate the signal-to-noise ratio"]]
    P10_STRUCTURE -->|"Components"| P7_MEAN_TESTS[["Test residual autocorrelation"]]
    P10_STRUCTURE -->|"Frequencies"| P0_SP_PEAK_SIGNIFICANCE[["Peak significance"]]
    P10_PROBABILISTIC_METRICS & P0_CA_SENSITIVITY & P0_SE_SNR & P7_MEAN_TESTS & P0_SP_PEAK_SIGNIFICANCE --> P10_METRICS_TO_PART_3(["Continue in part 3"])
    class P10_IN,P10_TO_PART_2,P10_METRICS_TO_PART_3 terminator
    class P10_METRIC_KIND,P10_STRUCTURE decision
    class P10_ROLLING_ORIGIN,P10_POINT_METRICS,P10_PROBABILISTIC_METRICS process
    class P0_CA_SENSITIVITY,P0_SE_SNR,P7_MEAN_TESTS,P0_SP_PEAK_SIGNIFICANCE ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: metrics for events and other outputs.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_2_IN(["From part 1"]) --> P10_METRIC_KIND_2{"Purpose flag?"}
    P10_METRIC_KIND_2 -->|"Events"| P10_EVENTS{"Which events?"}
    P10_METRIC_KIND_2 -->|"Other outputs"| P10_OUTPUTS{"Which output?"}
    P10_EVENTS -->|"Changes"| P10_CHANGE_POINT_METRICS["Change-point metrics<br/>detection delay, false-alarm rate"]
    P10_EVENTS -->|"Anomalies or regimes"| P10_CLASSIFICATION_METRICS["Classification and anomaly metrics<br/>F1, event-level precision and recall, NAB score"]
    P10_OUTPUTS -->|"Features and labels"| P10_CLASSIFICATION_METRICS
    P10_OUTPUTS -->|"A system model"| P0_SI_VALIDATION[["Validate on held-out input-output data"]]
    P10_OUTPUTS -->|"Simulated paths"| P0_SM_DISTRIBUTION_MATCH[["Check distribution and dependence matching"]]
    P10_CHANGE_POINT_METRICS & P10_CLASSIFICATION_METRICS & P0_SI_VALIDATION & P0_SM_DISTRIBUTION_MATCH --> P10_TO_PART_3(["Continue in part 3"])
    class P10_PART_2_IN,P10_TO_PART_3 terminator
    class P10_METRIC_KIND_2,P10_EVENTS,P10_OUTPUTS decision
    class P10_CHANGE_POINT_METRICS,P10_CLASSIFICATION_METRICS process
    class P0_SI_VALIDATION,P0_SM_DISTRIBUTION_MATCH ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: acceptance.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P10_PART_3_IN(["From parts 1 and 2"]) --> P10_ACCEPTABLE{"Performance acceptable?"}
    P10_ACCEPTABLE -.->|"No"| P6[["P6: Conditional-mean model class"]]
    P10_ACCEPTABLE -->|"Yes"| P10_OUT(["To P11 Inference and interpretation"])
    class P10_PART_3_IN,P10_OUT terminator
    class P10_ACCEPTABLE decision
    class P6 ref
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
