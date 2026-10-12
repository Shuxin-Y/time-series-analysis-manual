# Purpose 9: System identification

**Goal:** Identify a dynamic input-output model of a system.

## Sub-chart

**Part 1: experiment, feedback, nonparametric analysis and structure.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SI_IN(["Input-output data"]) --> P0_ESTIMAND[["Specify the estimand"]]
    P0_ESTIMAND --> P0_SI_EXPERIMENT_DESIGN["Input design and persistent excitation"]
    P0_SI_EXPERIMENT_DESIGN --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P0_SI_FEEDBACK{"Data collected under feedback?"}
    P0_SI_FEEDBACK -->|"Yes"| P0_SI_CLOSED_LOOP["Closed-loop identification<br/>direct PEM with a noise model, indirect or joint input-output, closed-loop subspace"]
    P0_SI_FEEDBACK -->|"No"| P3
    P0_SI_CLOSED_LOOP --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P0_SI_NONPARAMETRIC["Nonparametric analysis of the system<br/>smoothed empirical transfer-function estimate, coherence, impulse response and delay"]
    P0_SI_NONPARAMETRIC --> P0_SI_MODEL_STRUCTURE["Choose the model structure<br/>polynomial, state space, block-oriented"]
    P0_SI_MODEL_STRUCTURE --> P6[["P6: Conditional-mean model class"]]
    P6 --> P0_SI_STRUCTURE_Q{"Structure?"}
    P0_SI_STRUCTURE_Q -->|"Noise shares the system poles"| P6_ARX_ARMAX[["ARX and ARMAX input-output models"]]
    P0_SI_STRUCTURE_Q -->|"Independent noise model"| P6_TRANSFER_FUNCTION[["Transfer-function and intervention models"]]
    P0_SI_STRUCTURE_Q -->|"No noise model"| P6_OUTPUT_ERROR[["Output-error models"]]
    P0_SI_STRUCTURE_Q -->|"State space"| P6_SUBSPACE[["Subspace identification"]]
    P0_SI_STRUCTURE_Q -->|"Block-oriented"| P6_HAMMERSTEIN_WIENER[["Hammerstein-Wiener models"]]
    P6_ARX_ARMAX & P6_TRANSFER_FUNCTION & P6_OUTPUT_ERROR & P6_SUBSPACE & P6_HAMMERSTEIN_WIENER --> P0_SI_TO_PART_2(["Continue in part 2"])
    class P0_SI_IN,P0_SI_TO_PART_2 terminator
    class P0_SI_FEEDBACK,P0_SI_STRUCTURE_Q decision
    class P0_SI_EXPERIMENT_DESIGN,P0_SI_CLOSED_LOOP,P0_SI_NONPARAMETRIC,P0_SI_MODEL_STRUCTURE process
    class P0_ESTIMAND,P1,P3,P6,P6_ARX_ARMAX,P6_TRANSFER_FUNCTION,P6_OUTPUT_ERROR,P6_SUBSPACE,P6_HAMMERSTEIN_WIENER ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: order, estimation, validation and the system's properties.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SI_PART_2_IN(["From part 1"]) --> P0_SI_ORDER_SELECTION["Order selection<br/>AIC, FPE, MDL, cross-validation; Hankel singular values for subspace"]
    P0_SI_ORDER_SELECTION --> P8[["P8: Estimation"]]
    P8 --> P0_SI_ORDER_OK{"Order adequate?"}
    P0_SI_ORDER_OK -.->|"No"| P0_SI_ORDER_SELECTION
    P0_SI_ORDER_OK -->|"Yes"| P9[["P9: In-sample diagnostics"]]
    P9 --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P0_SI_VALIDATION["Validate on held-out input-output data<br/>residual autocorrelation, residual-input cross-correlation, simulation fit on fresh data"]
    P0_SI_VALIDATION --> P11[["P11: Inference and interpretation"]]
    P11 --> P0_SI_TRANSFER_FUNCTION["Estimate the frequency response<br/>of the fitted model, with confidence bands"]
    P0_SI_TRANSFER_FUNCTION --> P0_SI_STABILITY["Poles, zeros and stability"]
    P0_SI_STABILITY --> P12[["P12: Deployment and monitoring"]]
    class P0_SI_PART_2_IN terminator
    class P0_SI_ORDER_OK decision
    class P0_SI_ORDER_SELECTION,P0_SI_VALIDATION,P0_SI_TRANSFER_FUNCTION,P0_SI_STABILITY process
    class P8,P9,P10,P11,P12 ref
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

[Validate on held-out input-output data](../../reference/33-system-identification/index.md#validate-on-held-out-input-output-data).

## P11 inference for this purpose

[Estimate the frequency response](../../reference/33-system-identification/index.md#estimate-the-frequency-response), [Poles, zeros and stability](../../reference/33-system-identification/index.md#poles-zeros-and-stability).
