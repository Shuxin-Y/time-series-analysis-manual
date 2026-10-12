# Purpose 10: Simulation and scenario generation

**Goal:** Generate paths from a fitted model for stress tests, scenarios or synthetic data.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SM_IN(["Simulation question"]) --> P0_SM_SOURCE{"Generator?"}
    P0_SM_SOURCE -->|"Learned or fitted model"| P6[["P6: Conditional-mean model class"]]
    P0_SM_SOURCE -->|"Resampling"| P0_SM_BOOTSTRAP_PATHS["Simulating paths by resampling"]
    P6 --> P0_SM_FIT{"Model?"}
    P0_SM_FIT -->|"Generative network"| P6_GENERATIVE[["Generative models for time series"]]
    P0_SM_FIT -->|"Conditional-mean model"| P9[["P9: In-sample diagnostics"]]
    P6_GENERATIVE --> P0_SM_SYNTHETIC["Synthetic data generation<br/>TimeGAN"]
    P9 --> P0_SM_MONTE_CARLO["Monte Carlo simulation from a fitted model"]
    P9_BOOTSTRAP[["Bootstrap inference"]] -.- P0_SM_BOOTSTRAP_PATHS
    P0_SM_MONTE_CARLO & P0_SM_BOOTSTRAP_PATHS & P0_SM_SYNTHETIC --> P0_SM_DISTRIBUTION_MATCH["Check distribution and dependence matching"]
    P0_SM_DISTRIBUTION_MATCH --> P11[["P11: Inference and interpretation"]]
    P11 --> P11_SCENARIOS[["Stress testing and scenario design"]]
    P11_SCENARIOS --> P11_RISK_MEASURES[["Risk measures and their backtests"]]
    P11_RISK_MEASURES --> P10[["P10: Out-of-sample evaluation and selection"]]
    class P0_SM_IN terminator
    class P0_SM_SOURCE,P0_SM_FIT decision
    class P0_SM_BOOTSTRAP_PATHS,P0_SM_SYNTHETIC,P0_SM_MONTE_CARLO,P0_SM_DISTRIBUTION_MATCH process
    class P6,P6_GENERATIVE,P9,P9_BOOTSTRAP,P11,P11_SCENARIOS,P11_RISK_MEASURES,P10 ref
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

[Stress testing and scenario design](../../reference/25-simulation/index.md#stress-testing-and-scenario-design), [Risk measures and their backtests](../../reference/10-volatility/index.md#risk-measures-and-their-backtests).

## P10 metrics for this purpose

[Check distribution and dependence matching](../../reference/25-simulation/index.md#check-distribution-and-dependence-matching).
