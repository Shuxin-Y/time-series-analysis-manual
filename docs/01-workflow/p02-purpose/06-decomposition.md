# Purpose 6: Decomposition

**Goal:** Split the series into interpretable components.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_DC_IN(["Decomposition question"]) --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P3_SEASONALITY[["Detect seasonality"]]
    P3_SEASONALITY --> P2_DC_SEASONAL{"Seasonal?"}
    P2_DC_SEASONAL -->|"Yes"| P2_DC_ADDITIVE_MULTIPLICATIVE["Additive or multiplicative decomposition"]
    P2_DC_SEASONAL -->|"No"| P4
    P2_DC_ADDITIVE_MULTIPLICATIVE --> P4[["P4: Transformations"]]
    P4 --> P2_DC_METHOD{"Method?"}
    P2_DC_METHOD -->|"STL or X-13"| P4_SEASONAL_ADJUSTMENT[["Seasonal adjustment"]]
    P2_DC_METHOD -->|"Several periods"| P4_MULTIPLE_SEASONALITY[["Multiple seasonality"]]
    P2_DC_METHOD -->|"Model-based"| P4_MODEL_DECOMPOSITION[["Model-based decomposition"]]
    P2_DC_METHOD -->|"Nonparametric"| P4_SSA[["Singular spectrum analysis"]]
    P2_DC_METHOD -->|"Filter-based, no seasonality"| P4_FILTER_DECOMPOSITION[["Filter-based decomposition"]]
    P4_SEASONAL_ADJUSTMENT & P4_MULTIPLE_SEASONALITY & P4_MODEL_DECOMPOSITION & P4_SSA & P4_FILTER_DECOMPOSITION --> P2_DC_COMPONENT_ANALYSIS["Analyse and interpret the components"]
    P2_DC_COMPONENT_ANALYSIS --> P7[["P7: Error-process specification"]]
    P7 --> P7_MEAN_TESTS[["Test residual autocorrelation"]]
    P7_MEAN_TESTS --> P2_DC_RESIDUAL{"Residual white?"}
    P2_DC_RESIDUAL -.->|"No"| P2_DC_METHOD
    P2_DC_RESIDUAL -->|"Yes"| P2_DC_REVISION["Revision stability of real-time decompositions"]
    P2_DC_REVISION --> P11[["P11: Validation and deployment"]]
    class P2_DC_IN terminator
    class P2_DC_SEASONAL,P2_DC_METHOD,P2_DC_RESIDUAL decision
    class P2_DC_ADDITIVE_MULTIPLICATIVE,P2_DC_COMPONENT_ANALYSIS,P2_DC_REVISION process
    class P3,P3_SEASONALITY,P4,P4_SEASONAL_ADJUSTMENT,P4_MULTIPLE_SEASONALITY,P4_MODEL_DECOMPOSITION,P4_SSA,P4_FILTER_DECOMPOSITION,P7,P7_MEAN_TESTS,P11 ref
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

[Analyse and interpret the components](../../reference/03-classical/index.md#analyse-and-interpret-the-components).

## P11 metrics for this purpose

[Test residual autocorrelation](../p07-error-process.md#test-residual-autocorrelation).
