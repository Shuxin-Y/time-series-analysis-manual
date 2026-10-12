# P2: Data-type gate

**Question this phase answers:** What kind of object is this?

Three routing questions (value type, sampling, cross-sectional structure) send the series down the standard path or into one of seven branches, and set flags that later phases read.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_IN(["Prepared series from P1"]) --> P2_VALUE_TYPE{"Value type?"}
    P2_VALUE_TYPE -->|"Continuous"| P2_SAMPLING{"Sampling?"}
    P2_VALUE_TYPE -->|"Counts, categorical, compositional"| B1[["B1 Counts and categorical"]]
    P2_VALUE_TYPE -->|"Curves"| B4[["B4 Functional"]]
    P2_VALUE_TYPE -->|"Event times"| B2[["B2 Event times"]]
    P2_SAMPLING -->|"Regular"| P2_STRUCTURE{"Cross-section?"}
    P2_SAMPLING -->|"Irregular"| B3[["B3 Irregular sampling and continuous time"]]
    P2_SAMPLING -->|"Mixed frequency"| P2_MIXED_FREQ_FLAG["Set flag: mixed frequency"]
    P2_MIXED_FREQ_FLAG --> P2_STRUCTURE
    P2_STRUCTURE -->|"Single"| P2_OUT
    P2_STRUCTURE -->|"Few related"| P2_MULTIVARIATE_FLAG["Set flag: multivariate"]
    P2_STRUCTURE -->|"Many similar"| B7["B7 Many similar series"]
    P2_STRUCTURE -->|"Wide panel"| B6[["B6 Wide panel"]]
    P2_STRUCTURE -->|"Spatial or network"| B5[["B5 Spatial and network"]]
    P2_MULTIVARIATE_FLAG --> P2_OUT
    B7 --> P2_OUT
    B3 -.->|"Resample"| P1[["P1: Data acquisition and cleaning"]]
    B3 --> P5[["P5: Representation selection"]]
    B4 --> P5
    B1 --> P8[["P8: Estimation"]]
    B2 --> P8
    B5 --> P8
    B6 --> P8
    P2_OUT(["To P0 Purpose"])
    class P2_IN,P2_OUT terminator
    class P2_VALUE_TYPE,P2_SAMPLING,P2_STRUCTURE decision
    class P2_MIXED_FREQ_FLAG,P2_MULTIVARIATE_FLAG,B7 process
    class B1,B2,B3,B4,B5,B6,P1,P5,P8 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Routing variables

| Variable | Values | Effect |
|---|---|---|
| Value type | continuous / counts / categorical or ordinal / compositional / curves / event times | Continuous stays on the spine; counts, categorical and compositional enter B1; curves enter B4; event times enter B2 |
| Sampling | regular / irregular / mixed frequency | Irregular enters B3; mixed frequency sets a flag read by P6 and P11 |
| Cross-sectional structure | single / few related / many similar / wide panel / spatial or network | Few related sets the multivariate flag; many similar enters B7; wide panel enters B6; spatial enters B5 |

## Branches

| Branch | Chapter | Rejoins |
|---|---|---|
| B1 Counts and categorical | [Count and Categorical](../reference/16-count-categorical/index.md) | P8 |
| B2 Event times | [Point Processes](../reference/17-point-processes/index.md) | P8 |
| B3 Irregular sampling and continuous time | [Continuous-Time Models](../reference/15-continuous-time/index.md) | P5 or P8; may resample back to P1 |
| B4 Functional | [Functional and High-Frequency](../reference/14-functional-high-frequency/index.md) | P5 |
| B5 Spatial and network | [Spatio-Temporal Models](../reference/20-spatio-temporal/index.md) | P8 |
| B6 Wide panel | [Panel Time Series](../reference/32-panel-time-series/index.md) | P8, P11 |
| B7 Many similar series | this page | Stays on the spine with the global, cluster or hierarchy flag set |

## B7 Many similar series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B7`). Write this section following the content rules in `.claude/rules/writing.md`.

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B7[["B7 Many similar series"]] --> B7_GLOBAL_VS_LOCAL["Pooling strategies for many series<br/>global, cluster then local, hierarchical"]
    B7_GLOBAL_VS_LOCAL --> B7_STRATEGY{"Strategy?"}
    B7_STRATEGY -->|"Global"| P2_GLOBAL_FLAG["Set flag: global model"]
    B7_STRATEGY -->|"Cluster first"| B7_CLUSTER_FLAG["Set flag: cluster then local"]
    B7_STRATEGY -->|"Hierarchy"| B7_HIERARCHY_FLAG["Set flag: hierarchy"]
    P2_GLOBAL_FLAG --> P6_GLOBAL_MODELS[["Global models across many series"]]
    P6_GLOBAL_MODELS --> P6_FOUNDATION_MODELS[["Foundation models"]]
    B7_CLUSTER_FLAG --> B7_CLUSTER_THEN_LOCAL["Cluster series, then fit local models"]
    B7_HIERARCHY_FLAG --> B7_HIERARCHY["Detect hierarchical and grouped structure"]
    B7_HIERARCHY --> P11_RECONCILIATION[["Hierarchical and temporal reconciliation"]]
    P6_FOUNDATION_MODELS & B7_CLUSTER_THEN_LOCAL & P11_RECONCILIATION --> P0[["P0: Purpose and evaluation plan"]]
    class B7_STRATEGY decision
    class B7_GLOBAL_VS_LOCAL,P2_GLOBAL_FLAG,B7_CLUSTER_FLAG,B7_HIERARCHY_FLAG,B7_CLUSTER_THEN_LOCAL,B7_HIERARCHY process
    class B7,P6_GLOBAL_MODELS,P6_FOUNDATION_MODELS,P11_RECONCILIATION,P0 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

