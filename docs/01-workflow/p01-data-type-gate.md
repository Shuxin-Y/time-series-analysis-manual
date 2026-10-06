# P1: Data-type gate

**Question this phase answers:** What kind of object is this?

Three routing questions (value type, sampling, cross-sectional structure) send the series down the standard path or into one of seven branches, and set flags that later phases read.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P1_IN(["Prepared series from P0"]) --> P1_VALUE_TYPE{"Value type?"}
    P1_VALUE_TYPE -->|"Continuous"| P1_SAMPLING{"Sampling?"}
    P1_VALUE_TYPE -->|"Counts, categorical, compositional"| B1[["B1 Counts and categorical"]]
    P1_VALUE_TYPE -->|"Curves"| B4[["B4 Functional"]]
    P1_VALUE_TYPE -->|"Event times"| B2[["B2 Event times"]]
    P1_SAMPLING -->|"Regular"| P1_STRUCTURE{"Cross-section?"}
    P1_SAMPLING -->|"Irregular"| B3[["B3 Irregular sampling and continuous time"]]
    P1_SAMPLING -->|"Mixed frequency"| P1_MIXED_FREQ_FLAG["Set flag: mixed frequency"]
    P1_MIXED_FREQ_FLAG --> P1_STRUCTURE
    P1_STRUCTURE -->|"Single"| P1_OUT
    P1_STRUCTURE -->|"Few related"| P1_MULTIVARIATE_FLAG["Set flag: multivariate"]
    P1_STRUCTURE -->|"Many similar"| B7["B7 Many similar series"]
    P1_STRUCTURE -->|"Wide panel"| B6[["B6 Wide panel"]]
    P1_STRUCTURE -->|"Spatial or network"| B5[["B5 Spatial and network"]]
    P1_MULTIVARIATE_FLAG --> P1_OUT
    B7 --> P1_GLOBAL_FLAG["Set flag: global model"]
    P1_GLOBAL_FLAG --> P1_OUT
    B3 -.->|"Resample"| P0[["P0: Data acquisition and cleaning"]]
    B3 --> P5[["P5: Representation selection"]]
    B4 --> P5
    B1 --> P8[["P8: Estimation"]]
    B2 --> P8
    B5 --> P8
    B6 --> P8
    P1_OUT(["To P2 Purpose"])
    class P1_IN,P1_OUT terminator
    class P1_VALUE_TYPE,P1_SAMPLING,P1_STRUCTURE decision
    class P1_MIXED_FREQ_FLAG,P1_MULTIVARIATE_FLAG,P1_GLOBAL_FLAG,B7 process
    class B1,B2,B3,B4,B5,B6,P0,P5,P8 ref
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
| Sampling | regular / irregular / mixed frequency | Irregular enters B3; mixed frequency sets a flag read by P6 and P10 |
| Cross-sectional structure | single / few related / many similar / wide panel / spatial or network | Few related sets the multivariate flag; many similar enters B7; wide panel enters B6; spatial enters B5 |

## Branches

| Branch | Chapter | Rejoins |
|---|---|---|
| B1 Counts and categorical | [Count and Categorical](../reference/16-count-categorical/index.md) | P8 |
| B2 Event times | [Point Processes](../reference/17-point-processes/index.md) | P8 |
| B3 Irregular sampling and continuous time | [Continuous-Time Models](../reference/15-continuous-time/index.md) | P5 or P8; may resample back to P0 |
| B4 Functional | [Functional and High-Frequency](../reference/14-functional-high-frequency/index.md) | P5 |
| B5 Spatial and network | [Spatio-Temporal Models](../reference/20-spatio-temporal/index.md) | P8 |
| B6 Wide panel | [Panel Time Series](../reference/32-panel-time-series/index.md) | P8, P10 |
| B7 Many similar series | this page | Stays on the spine with the global flag set |

## B7 Many similar series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B7`). Write this section following the content rules in `.claude/rules/writing.md`.
