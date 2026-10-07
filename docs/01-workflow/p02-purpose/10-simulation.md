# Purpose 10: Simulation and scenario generation

**Goal:** Generate paths from a fitted model for stress tests, scenarios or synthetic data.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_SM_IN(["Simulation question"]) --> P2_SM_SOURCE{"Generator?"}
    P2_SM_SOURCE -->|"Fitted model"| P2_SM_MONTE_CARLO["Monte Carlo simulation from a fitted model"]
    P2_SM_SOURCE -->|"Resampling"| P2_SM_BOOTSTRAP_PATHS["Bootstrap path simulation<br/>block, stationary, sieve"]
    P2_SM_SOURCE -->|"Learned"| P2_SM_SYNTHETIC["Synthetic data generation<br/>TimeGAN, diffusion models"]
    P2_SM_MONTE_CARLO & P2_SM_BOOTSTRAP_PATHS & P2_SM_SYNTHETIC --> P2_SM_STRESS["Stress scenarios and shock design"]
    P2_SM_STRESS --> P2_SM_DISTRIBUTION_MATCH["Check distribution and dependence matching"]
    P2_SM_DISTRIBUTION_MATCH --> P10_SCENARIOS[["Scenario simulation and stress testing"]]
    P10_SCENARIOS --> P10_RISK_MEASURES[["Risk measures and their backtests"]]
    P10_RISK_MEASURES --> P2_SM_OUT(["Simulated paths and scenarios"])
    class P2_SM_IN,P2_SM_OUT terminator
    class P2_SM_SOURCE decision
    class P2_SM_MONTE_CARLO,P2_SM_BOOTSTRAP_PATHS,P2_SM_SYNTHETIC,P2_SM_STRESS,P2_SM_DISTRIBUTION_MATCH process
    class P10_SCENARIOS,P10_RISK_MEASURES ref
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

Path simulation, stress testing, synthetic data.

## P11 metrics for this purpose

Distribution matching, bootstrap coverage.
