# P12: Deployment and monitoring

**Question this phase answers:** Does the deployed model keep working?

Documentation, the retraining policy, drift monitoring, statistical process control and the response to drift.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P12_IN(["Selected model and outputs from P11"]) --> P12_DOCUMENTATION["Document the model specification"]
    P12_DOCUMENTATION --> P12_RETRAINING["Retraining policy"]
    P12_RETRAINING --> P12_DRIFT_MONITORING["Drift monitoring<br/>KL divergence, spectral shift, ADWIN, DDM"]
    P12_DRIFT_MONITORING --> P12_SPC["Statistical process control<br/>Shewhart and EWMA charts"]
    P12_SPC --> P12_DRIFT{"Drift detected?"}
    P12_DRIFT -->|"Yes"| P12_ONLINE_UPDATING["Online updating<br/>recursive least squares, forgetting factors, online Kalman, online gradient"]
    P12_DRIFT -->|"No"| P12_OUT(["Validated model deployed"])
    P12_ONLINE_UPDATING -.-> P8[["P8: Estimation"]]
    P0_CP_CUSUM[["Sequential detection"]] -.- P12_SPC
    P0_CP_CUSUM -.- P12_DRIFT_MONITORING
    P0_CP_BOCPD[["Bayesian online change-point detection"]] -.- P12_DRIFT_MONITORING
    class P12_IN,P12_OUT terminator
    class P12_DRIFT decision
    class P12_DOCUMENTATION,P12_RETRAINING,P12_DRIFT_MONITORING,P12_SPC,P12_ONLINE_UPDATING process
    class P8,P0_CP_CUSUM,P0_CP_BOCPD ref
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
