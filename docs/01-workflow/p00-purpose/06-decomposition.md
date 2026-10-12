# Purpose 6: Decomposition

**Goal:** Split the series into interpretable components.

## Sub-chart

**Part 1: seasonality and the decomposition method, on the variance-stabilised levels.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_DC_IN(["Decomposition question"]) --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P3_SEASONALITY[["Detect seasonality"]]
    P3_SEASONALITY --> P0_DC_SEASONAL{"Seasonal?"}
    P0_DC_SEASONAL -->|"Yes"| P0_DC_ADDITIVE_MULTIPLICATIVE["Additive or multiplicative decomposition"]
    P0_DC_SEASONAL -->|"No"| P4
    P0_DC_ADDITIVE_MULTIPLICATIVE --> P4[["P4: Transformations"]]
    P4 --> P0_DC_METHOD{"Method?"}
    P0_DC_METHOD -->|"STL or X-13"| P4_SEASONAL_ADJUSTMENT[["Seasonal adjustment"]]
    P0_DC_METHOD -->|"Several periods"| P4_MULTIPLE_SEASONALITY[["Multiple seasonality"]]
    P0_DC_METHOD -->|"Filter-based, no seasonality"| P4_FILTER_DECOMPOSITION[["Filter-based decomposition"]]
    P0_DC_METHOD -->|"Nonparametric"| P4_SSA[["Singular spectrum analysis"]]
    P0_DC_METHOD -->|"Model-based or adaptive"| P0_DC_TO_PART_2(["Continue in part 2"])
    P4_SEASONAL_ADJUSTMENT & P4_MULTIPLE_SEASONALITY & P4_FILTER_DECOMPOSITION & P4_SSA --> P0_DC_TO_PART_3(["Continue in part 3"])
    class P0_DC_IN,P0_DC_TO_PART_2,P0_DC_TO_PART_3 terminator
    class P0_DC_SEASONAL,P0_DC_METHOD decision
    class P0_DC_ADDITIVE_MULTIPLICATIVE process
    class P1,P3,P3_SEASONALITY,P4,P4_SEASONAL_ADJUSTMENT,P4_MULTIPLE_SEASONALITY,P4_FILTER_DECOMPOSITION,P4_SSA ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: model-based, adaptive and multiscale methods.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_DC_PART_2_IN(["From part 1"]) --> P0_DC_FAMILY{"Which?"}
    P0_DC_FAMILY -->|"Model-based"| P4_MODEL_DECOMPOSITION[["Model-based decomposition"]]
    P0_DC_FAMILY -->|"Adaptive or multiscale"| P5[["P5: Representation selection"]]
    P4_MODEL_DECOMPOSITION --> P6[["P6: Conditional-mean model class"]]
    P6 --> P6_STRUCTURAL_TS[["Structural time-series models"]]
    P6_STRUCTURAL_TS --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P5 --> P0_DC_ADAPTIVE{"Decomposition?"}
    P0_DC_ADAPTIVE -->|"Empirical modes"| P5_TF_EMD[["Empirical mode decomposition and the Hilbert-Huang transform"]]
    P0_DC_ADAPTIVE -->|"Variational modes"| P5_TF_VMD[["Variational mode decomposition"]]
    P0_DC_ADAPTIVE -->|"Scales"| P5_TF_MRA[["Multiresolution analysis"]]
    P9 & P5_TF_EMD & P5_TF_VMD & P5_TF_MRA --> P0_DC_PART_2_OUT(["Continue in part 3"])
    class P0_DC_PART_2_IN,P0_DC_PART_2_OUT terminator
    class P0_DC_FAMILY,P0_DC_ADAPTIVE decision
    class P4_MODEL_DECOMPOSITION,P6,P6_STRUCTURAL_TS,P8,P9,P5,P5_TF_EMD,P5_TF_VMD,P5_TF_MRA ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: adequacy, interpretation and revisions.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_DC_PART_3_IN(["From parts 1 and 2"]) --> P0_DC_COMPONENT_ANALYSIS["Analyse and interpret the components"]
    P0_DC_COMPONENT_ANALYSIS --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P0_DC_DIAGNOSTICS["Decomposition diagnostics<br/>residual seasonality, sliding spans, whiteness of model-based irregulars"]
    P0_DC_DIAGNOSTICS --> P0_DC_ADEQUATE{"Components adequate?"}
    P0_DC_ADEQUATE -.->|"No"| P0_DC_METHOD[["Method?"]]
    P0_DC_ADEQUATE -->|"Yes"| P0_DC_REVISION["Revision stability of real-time decompositions"]
    P0_DC_REVISION --> P11[["P11: Inference and interpretation"]]
    P11 --> P12[["P12: Deployment and monitoring"]]
    class P0_DC_PART_3_IN terminator
    class P0_DC_ADEQUATE decision
    class P0_DC_COMPONENT_ANALYSIS,P0_DC_DIAGNOSTICS,P0_DC_REVISION process
    class P10,P0_DC_METHOD,P11,P12 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P10 metrics for this purpose

[Decomposition diagnostics](../../reference/29-seasonality-calendar/index.md#decomposition-diagnostics), [Revision stability of real-time decompositions](../../reference/29-seasonality-calendar/index.md#revision-stability-of-real-time-decompositions).

## P11 inference for this purpose

[Analyse and interpret the components](../../reference/03-classical/index.md#analyse-and-interpret-the-components).
