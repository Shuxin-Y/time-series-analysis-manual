# P12: Deployment and monitoring

**Question this phase answers:** Does the deployed model keep working?

Documentation, the retraining policy, drift monitoring and statistical process control, and a response chosen by the type and source of the drift: a data fault is fixed at acquisition, gradual drift is tracked by online updating, a sudden or structural change triggers retraining on a recent window or re-specification with a baseline in service meanwhile, and a recurring regime reuses a stored model. The retraining policy is the refit cadence and window that P10 evaluated, so the accuracy reported there is the accuracy the policy delivers.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P12_IN(["Issued outputs from P11"]) --> P12_DOCUMENTATION["Document the model specification"]
    P12_DOCUMENTATION --> P12_RETRAINING["Retraining policy<br/>the refit cadence and window evaluated in P10"]
    P12_RETRAINING --> P12_DRIFT_MONITORING["Drift monitoring<br/>KL divergence, spectral shift, ADWIN, DDM"]
    P12_DRIFT_MONITORING --> P12_SPC["Statistical process control<br/>Shewhart and EWMA charts; threshold calibrated on in-control data, ARL0 against delay"]
    P12_SPC --> P12_DRIFT{"Drift detected?"}
    P12_DRIFT -->|"No"| P12_OUT(["Model in service"])
    P12_DRIFT -->|"Yes"| P12_DRIFT_TYPE{"Drift type and source?"}
    P12_DRIFT_TYPE -.->|"Data fault"| P1[["P1: Data acquisition and cleaning"]]
    P12_DRIFT_TYPE -->|"Gradual"| P12_ONLINE_UPDATING["Online updating<br/>recursive least squares, forgetting factors, online Kalman, online gradient"]
    P12_DRIFT_TYPE -->|"Sudden or structural"| P12_RETRAIN_RECENT["Retrain on a recent window or re-specify<br/>baseline in service during the transition"]
    P12_DRIFT_TYPE -->|"Recurring"| P12_REUSE["Reuse a stored model"]
    P12_ONLINE_UPDATING -.-> P8[["P8: Estimation"]]
    P12_RETRAIN_RECENT -.-> P6[["P6: Conditional-mean model class"]]
    P12_REUSE --> P12_OUT
    P0_CP_CUSUM[["Sequential detection"]] -.- P12_SPC
    P0_CP_CUSUM -.- P12_DRIFT_MONITORING
    P0_CP_BOCPD[["Bayesian online change-point detection"]] -.- P12_DRIFT_MONITORING
    class P12_IN,P12_OUT terminator
    class P12_DRIFT,P12_DRIFT_TYPE decision
    class P12_DOCUMENTATION,P12_RETRAINING,P12_DRIFT_MONITORING,P12_SPC,P12_ONLINE_UPDATING,P12_RETRAIN_RECENT,P12_REUSE process
    class P1,P8,P6,P0_CP_CUSUM,P0_CP_BOCPD ref
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
    To-do item created from the flowchart inventory (node `P12`). Write this section following the content rules in `.claude/rules/writing.md`.

## Document the model specification

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P12_DOCUMENTATION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Retraining policy

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P12_RETRAINING`). Write this section following the content rules in `.claude/rules/writing.md`.
