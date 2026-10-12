# General Flowchart

The general flowchart is the spine of this book. The master diagram below shows the thirteen phases of the workflow; each phase box opens the chapter that holds that phase's sub-diagram, and every leaf node in a sub-diagram opens the section that teaches it.

## Master diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    MASTER_START(["Question and raw time-stamped data"]) --> P0["P0: Purpose and evaluation plan"]
    P0 --> P1["P1: Data acquisition and cleaning"]
    P1 --> P2["P2: Data-type gate"]
    P2 --> P3["P3: Exploratory diagnostics"]
    P3 --> P4["P4: Transformations"]
    P4 --> P5["P5: Representation selection"]
    P5 --> P6["P6: Conditional-mean model class"]
    P6 --> P7["P7: Error-process specification"]
    P7 --> P8["P8: Estimation"]
    P8 --> P9["P9: In-sample diagnostics"]
    P9 --> P10["P10: Out-of-sample evaluation and selection"]
    P10 --> P11["P11: Inference and interpretation"]
    P11 --> P12["P12: Deployment and monitoring"]
    P9 -.->|"Integration order or transform wrong"| P3
    P9 -.->|"Mean misspecified"| P6
    P9 -.->|"Innovations misspecified"| P7
    P10 -.->|"Add a candidate, or none acceptable"| P6
    P12 -.->|"Data fault"| P1
    P12 -.->|"Structural change"| P6
    P12 -.->|"Gradual drift"| P8
    P12 --> MASTER_END(["Validated model deployed"])
    class MASTER_START,MASTER_END terminator
    class P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12 process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Why this order

Each phase comes where it does because of what the earlier phases supply.

| Phase | Because |
|---|---|
| P0 first | The question decides what cleaning may remove, what transformations may destroy and how the answer will be judged; fixing it before seeing the data is pre-specification. |
| P1 after P0 | The value type, asked at P1 entry, decides which cleaning steps are valid: interpolation produces non-integers for counts, event times have nothing to impute, and stock and flow series aggregate differently. |
| P2 after P1 | The sampling and structure questions are answered on aligned, de-duplicated data. |
| P3 after P2 | Valid diagnostics depend on the value type, the sampling and the cross-sectional structure; unit-root and ACF theory assumes a regularly sampled continuous series. |
| P4 after P3 | Transforms are chosen from diagnosed structure. |
| P5 after P4 | A model family is a family of processes written in one representation, and the representation decides which families are candidates. |
| P6 after P5 | The class is chosen for the series at the scale and integration order at which it will be modelled. Structure the class does not represent (variance scaling, integration when the class is stationary, deterministic terms, breaks) is removed or turned into regressors first; structure the class represents (integration in ARIMA or ARFIMA, cointegration in a VECM) is left to the class. |
| P7 after P6 | Error tests are valid on residuals of a mean model, from a preliminary fit of the P6 class. |
| P8 after P7 | The estimator is chosen for the complete joint model; the preliminary fit ignored the error process and is not the estimate. |
| P9 after P8 | Diagnostics apply to the jointly estimated model. |
| P10 after P9 | P9 screens specification errors and selects which variants go forward; P10 compares them with the baselines, which are exempt from the P9 screen, because in-sample adequacy is neither necessary nor sufficient for out-of-sample accuracy. |
| P11 after P10 | Inference is drawn from the selected model and is conditional on the specification search (the P3 pre-tests, the P9 and P10 loops); P11 states that caveat and its remedies. |
| P12 last | Monitoring needs a deployed model. |

## How to read the diagrams

Shapes follow the decision-flowchart notation in the design system: stadiums start and end a chart, diamonds ask a question, rectangles are steps or outcomes, dashed subroutine boxes point to another chapter, and dotted edges are feedback or optional flow. Every rectangle is a section of this book; click it.
