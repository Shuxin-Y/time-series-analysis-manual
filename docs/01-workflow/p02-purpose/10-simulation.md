# Purpose 10: Simulation and scenario generation

**Goal:** Generate paths from a fitted model for stress tests, scenarios or synthetic data.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_SM_IN(["Simulation question"]) --> P2_SM_SOURCE{"Generator?"}
    P2_SM_SOURCE -->|"Fitted model"| P9[["P9: Diagnostics and model selection"]]
    P2_SM_SOURCE -->|"Resampling"| P2_SM_BOOTSTRAP_PATHS["Simulating paths by resampling"]
    P2_SM_SOURCE -->|"Learned"| P2_SM_SYNTHETIC["Synthetic data generation<br/>TimeGAN"]
    P9 --> P2_SM_MONTE_CARLO["Monte Carlo simulation from a fitted model"]
    P2_SM_MONTE_CARLO & P2_SM_BOOTSTRAP_PATHS & P2_SM_SYNTHETIC --> P2_SM_DISTRIBUTION_MATCH["Check distribution and dependence matching"]
    P9_BOOTSTRAP[["Bootstrap inference"]] -.- P2_SM_BOOTSTRAP_PATHS
    P6_GENERATIVE[["Generative models for time series"]] -.- P2_SM_SYNTHETIC
    P2_SM_DISTRIBUTION_MATCH --> P10_SCENARIOS[["Scenario simulation and stress testing"]]
    P10_SCENARIOS --> P10_RISK_MEASURES[["Risk measures and their backtests"]]
    P10_RISK_MEASURES --> P11[["P11: Validation and deployment"]]
    class P2_SM_IN terminator
    class P2_SM_SOURCE decision
    class P2_SM_BOOTSTRAP_PATHS,P2_SM_SYNTHETIC,P2_SM_MONTE_CARLO,P2_SM_DISTRIBUTION_MATCH process
    class P9,P9_BOOTSTRAP,P6_GENERATIVE,P10_SCENARIOS,P10_RISK_MEASURES,P11 ref
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

[Scenario simulation and stress testing](../../reference/25-simulation/index.md#scenario-simulation-and-stress-testing), [Risk measures and their backtests](../../reference/10-volatility/index.md#risk-measures-and-their-backtests).

## P11 metrics for this purpose

[Check distribution and dependence matching](../../reference/25-simulation/index.md#check-distribution-and-dependence-matching).
