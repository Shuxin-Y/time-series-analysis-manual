# Purpose 9: System identification

**Goal:** Identify a dynamic input-output model of a system.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_SI_IN(["Input-output data"]) --> P2_SI_EXPERIMENT_DESIGN["Input design and persistent excitation"]
    P2_SI_EXPERIMENT_DESIGN --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P2_SI_MODEL_STRUCTURE["Choose the model structure<br/>polynomial ARX and ARMAX, state space, block-oriented"]
    P2_SI_MODEL_STRUCTURE --> P6[["P6: Conditional-mean model class"]]
    P6 --> P2_SI_STRUCTURE_Q{"Structure?"}
    P2_SI_STRUCTURE_Q -->|"Polynomial"| P6_ARX_ARMAX[["ARX and ARMAX input-output models"]]
    P2_SI_STRUCTURE_Q -->|"State space"| P6_SUBSPACE[["Subspace identification"]]
    P2_SI_STRUCTURE_Q -->|"Block-oriented"| P6_HAMMERSTEIN_WIENER[["Hammerstein-Wiener models"]]
    P6_ARX_ARMAX & P6_SUBSPACE & P6_HAMMERSTEIN_WIENER --> P2_SI_ORDER_SELECTION["Order selection<br/>Hankel singular values"]
    P2_SI_ORDER_SELECTION --> P8[["P8: Estimation"]]
    P8 --> P2_SI_TRANSFER_FUNCTION["Estimate the frequency response<br/>empirical transfer-function estimate"]
    P2_SI_TRANSFER_FUNCTION --> P2_SI_STABILITY["Poles, zeros and stability"]
    P2_SI_STABILITY --> P2_SI_VALIDATION["Validate on held-out input-output data"]
    P2_SI_VALIDATION --> P11[["P11: Validation and deployment"]]
    class P2_SI_IN terminator
    class P2_SI_STRUCTURE_Q decision
    class P2_SI_EXPERIMENT_DESIGN,P2_SI_MODEL_STRUCTURE,P2_SI_ORDER_SELECTION,P2_SI_TRANSFER_FUNCTION,P2_SI_STABILITY,P2_SI_VALIDATION process
    class P3,P6,P6_ARX_ARMAX,P6_SUBSPACE,P6_HAMMERSTEIN_WIENER,P8,P11 ref
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

[Estimate the frequency response](../../reference/33-system-identification/index.md#estimate-the-frequency-response), [Poles, zeros and stability](../../reference/33-system-identification/index.md#poles-zeros-and-stability).

## P11 metrics for this purpose

[Validate on held-out input-output data](../../reference/33-system-identification/index.md#validate-on-held-out-input-output-data).
