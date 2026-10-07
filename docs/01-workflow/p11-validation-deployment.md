# P11: Validation and deployment

**Question this phase answers:** Does it work out of sample and keep working?

Rolling-origin validation and backtesting, purpose-specific metrics, documentation, drift monitoring, statistical process control, online updating, and the retraining policy.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P11_IN(["Model and forecasts from P10"]) --> P11_ROLLING_ORIGIN["Rolling-origin backtesting<br/>look-ahead bias, backtest overfitting"]
    P11_ROLLING_ORIGIN --> P11_METRIC_KIND{"Output type?"}
    P11_METRIC_KIND -->|"Point"| P11_POINT_METRICS["Point-forecast metrics<br/>RMSE, MAE, MAPE, MASE"]
    P11_METRIC_KIND -->|"Probabilistic"| P11_PROBABILISTIC_METRICS["Probabilistic metrics<br/>coverage, CRPS, pinball loss, log score, PIT"]
    P11_METRIC_KIND -->|"Labels or anomalies"| P11_CLASSIFICATION_METRICS["Classification and anomaly metrics<br/>F1, event-level precision and recall, NAB score"]
    P11_METRIC_KIND -->|"Change points"| P11_CHANGE_POINT_METRICS["Change-point metrics<br/>detection delay, false-alarm rate"]
    P11_POINT_METRICS & P11_PROBABILISTIC_METRICS & P11_CLASSIFICATION_METRICS & P11_CHANGE_POINT_METRICS --> P11_ACCEPTABLE{"Performance acceptable?"}
    P11_ACCEPTABLE -.->|"No"| P6[["P6: Conditional-mean model class"]]
    P11_ACCEPTABLE -->|"Yes"| P11_DOCUMENTATION["Document the model specification"]
    P11_DOCUMENTATION --> P11_DRIFT_MONITORING["Drift monitoring<br/>KL divergence, spectral shift, ADWIN, DDM"]
    P11_DRIFT_MONITORING --> P11_SPC["Statistical process control<br/>Shewhart and EWMA charts"]
    P11_SPC --> P11_DRIFT{"Drift detected?"}
    P11_DRIFT -->|"Yes"| P11_ONLINE_UPDATING["Online updating<br/>recursive least squares, forgetting factors, online Kalman, online gradient"]
    P11_DRIFT -->|"No"| P11_RETRAINING["Retraining policy"]
    P11_ONLINE_UPDATING -.-> P8[["P8: Estimation"]]
    P11_RETRAINING --> P11_OUT(["Validated model deployed"])
    P2_CP_CUSUM[["Sequential detection"]] -.- P11_SPC
    P2_CP_CUSUM -.- P11_DRIFT_MONITORING
    P2_CP_BOCPD[["Bayesian online change-point detection"]] -.- P11_DRIFT_MONITORING
    class P11_IN,P11_OUT terminator
    class P11_METRIC_KIND,P11_ACCEPTABLE,P11_DRIFT decision
    class P11_ROLLING_ORIGIN,P11_POINT_METRICS,P11_PROBABILISTIC_METRICS,P11_CLASSIFICATION_METRICS,P11_CHANGE_POINT_METRICS,P11_DOCUMENTATION,P11_DRIFT_MONITORING,P11_SPC,P11_ONLINE_UPDATING,P11_RETRAINING process
    class P6,P8 ref
    class P2_CP_CUSUM,P2_CP_BOCPD ref
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



## Document the model specification

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P11_DOCUMENTATION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Retraining policy

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P11_RETRAINING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Rolling-origin backtesting

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P11_ROLLING_ORIGIN`). Write this section following the content rules in `.claude/rules/writing.md`.
