# P2: Data-type gate

**Question this phase answers:** How is the series sampled, and how are the series related?

The value type and the sampling were recorded in P1 on aligned, de-duplicated data. This phase reads them, asks the cross-sectional question for every series, and sends every type on to P3. The type flags are read by P3 to P9, and each branch chart is an index over the spine: it lists the type-specific leaves that the spine phases point to, in phase order.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_IN(["Cleaned series and flags from P1"]) --> P2_VALUE_TYPE{"Value-type flag?"}
    P2_VALUE_TYPE -->|"Continuous"| P2_SAMPLING{"Sampling flag?"}
    P2_VALUE_TYPE -->|"Counts, categorical, compositional"| B1[["B1 Counts and categorical"]]
    P2_VALUE_TYPE -->|"Curves"| B4[["B4 Functional"]]
    P2_VALUE_TYPE -->|"Event times"| B2[["B2 Event times"]]
    P2_SAMPLING -->|"Regular or resampled"| P2_STRUCTURE{"Cross-section?"}
    P2_SAMPLING -->|"Irregular"| B3[["B3 Irregular sampling and continuous time"]]
    P2_SAMPLING -->|"Mixed frequency"| P2_MIXED_FREQ_FLAG["Set flag: mixed frequency"]
    P2_MIXED_FREQ_FLAG --> P2_STRUCTURE
    B1 --> P2_SAMPLING
    B2 & B3 & B4 --> P2_STRUCTURE
    B3 -.->|"Resample"| P1[["P1: Data acquisition and cleaning"]]
    P2_STRUCTURE -->|"Single"| P2_STRUCTURE_FLAG
    P2_STRUCTURE -->|"Few related"| P2_MULTIVARIATE_FLAG["Set flag: multivariate"]
    P2_STRUCTURE -->|"Many similar"| B7["B7 Many similar series"]
    P2_STRUCTURE -->|"Wide panel"| B6[["B6 Wide panel"]]
    P2_STRUCTURE -->|"Spatial or network"| B5[["B5 Spatial and network"]]
    P2_MULTIVARIATE_FLAG & B6 & B5 --> P2_STRUCTURE_FLAG["Set flag: structure"]
    P2_STRUCTURE_FLAG --> P2_OUT(["To P3 Exploratory diagnostics"])
    B7 --> P2_TO_PART_2(["Continue in part 2"])
    class P2_IN,P2_OUT,P2_TO_PART_2 terminator
    class P2_VALUE_TYPE,P2_SAMPLING,P2_STRUCTURE decision
    class P2_MIXED_FREQ_FLAG,P2_MULTIVARIATE_FLAG,P2_STRUCTURE_FLAG,B7 process
    class B1,B2,B3,B4,B5,B6,P1 ref
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
| Value type (set in P1) | continuous / counts / categorical or ordinal / compositional / curves / event times | Read by P3 to P9; counts are series with small values or frequent zeros, decided per series, and large counts are continuous; counts, categorical and compositional series use the B1 leaves, curves the B4 leaves, event times the B2 leaves |
| Sampling | regular or irregular (set in P1), irregular resampled (set in P1 after B3), irregular kept (set in B3), mixed frequency (set here) | Asked for every type except event times and curves, whose sampling per curve P5 reads (dense or sparse); irregular series use the B3 leaves, which ask whether to resample; mixed frequency is read by P3 to P6 and P11 |
| Cross-sectional structure (set here) | single / few related / many similar / wide panel / spatial or network | Asked for every series and read by P3 and P6; few related sets the multivariate flag; many similar uses B7; wide panel uses B6; spatial uses B5 |

## Branches

Every type reaches P3 through this page. A branch chart draws the spine phases it uses, in order, with its own leaves inside them, and hands the reader back to the spine at the phase in the last column.

| Branch | Chapter | Its leaves sit in | Back on the spine at |
|---|---|---|---|
| B1 Counts and categorical | [Count and Categorical](../reference/16-count-categorical/index.md) | P3, P6 | P10; compositions at P3, as log-ratios |
| B2 Event times | [Point Processes](../reference/17-point-processes/index.md) | P3, P6, P9 | P10 |
| B3 Irregular sampling and continuous time | [Continuous-Time Models](../reference/15-continuous-time/index.md) | P3, P6, P8, P9; may resample back to P1 | P10 |
| B4 Functional | [Functional and High-Frequency](../reference/14-functional-high-frequency/index.md) | P5 | P7 |
| B5 Spatial and network | [Spatio-Temporal Models](../reference/20-spatio-temporal/index.md) | P3, P6 | P10 |
| B6 Wide panel | [Panel Time Series](../reference/32-panel-time-series/index.md) | P3, P6, P8 | P10 |
| B7 Many similar series | this page | sets the hierarchy and pooling flags read by P6, P10 and P11 | P3 |

## B7 Many similar series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B7`). Write this section following the content rules in `.claude/rules/writing.md`.

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_PART_2_IN(["From part 1: many similar series"]) --> B7_AGGREGATION{"Aggregation constraints across series?"}
    B7_AGGREGATION -->|"Yes"| B7_HIERARCHY["Detect hierarchical and grouped structure"]
    B7_AGGREGATION -->|"No"| B7_GLOBAL_VS_LOCAL
    B7_HIERARCHY --> B7_HIERARCHY_FLAG["Set flag: hierarchy"]
    B7_HIERARCHY_FLAG --> B7_GLOBAL_VS_LOCAL["Pooling strategies for many series<br/>local, cluster then local, partial pooling, global"]
    B7_GLOBAL_VS_LOCAL --> B7_POOLING{"Pooling?"}
    B7_POOLING -->|"Local"| P2_STRUCTURE_FLAG
    B7_POOLING -->|"Cluster then local"| B7_CLUSTER_THEN_LOCAL["Cluster series, then fit local models"]
    B7_POOLING -->|"Partial pooling"| B7_PARTIAL_FLAG["Set flag: partial pooling"]
    B7_POOLING -->|"Global"| B7_GLOBAL_FLAG["Set flag: global pooling"]
    B7_POOLING -->|"Compare local and global"| B7_COMPARE_FLAG["Set flag: compare local and global"]
    B7_CLUSTER_THEN_LOCAL --> B7_CLUSTER_FLAG["Set flag: cluster then local"]
    B7_CLUSTER_FLAG & B7_PARTIAL_FLAG & B7_GLOBAL_FLAG & B7_COMPARE_FLAG --> P2_STRUCTURE_FLAG[["Set flag: structure"]]
    P2_STRUCTURE_FLAG --> P3[["P3: Exploratory diagnostics"]]
    B7_GLOBAL_FLAG -.- P6_GLOBAL_MODELS[["Global models across many series"]]
    B7_GLOBAL_FLAG -.- P6_FOUNDATION_MODELS[["Foundation models"]]
    B7_HIERARCHY_FLAG -.- P11_RECONCILIATION[["Hierarchical and temporal reconciliation"]]
    class B7_AGGREGATION,B7_POOLING decision
    class B7_HIERARCHY,B7_HIERARCHY_FLAG,B7_GLOBAL_VS_LOCAL,B7_CLUSTER_THEN_LOCAL,B7_CLUSTER_FLAG,B7_PARTIAL_FLAG,B7_GLOBAL_FLAG,B7_COMPARE_FLAG process
    class P2_PART_2_IN terminator
    class P2_STRUCTURE_FLAG,P3,P6_GLOBAL_MODELS,P6_FOUNDATION_MODELS,P11_RECONCILIATION ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```
