# P0: Purpose and evaluation plan

**Question this phase answers:** What is the question?

The purpose decides which later phases matter most and which inference and metrics apply at the end. Ten purposes are distinguished. Methods that belong to a purpose rather than to the standard pipeline (change-point algorithms, anomaly methods, component analysis, feature extraction, classification, clustering, simulation) are leaves of this phase.

## Purpose selector

**Part 1: the future, causes and structure in the series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_IN(["Series and flags from P2"]) --> P0_QUESTION{"Question about?"}
    P0_QUESTION -->|"The future"| P0_FORECASTING["Purpose 1: Forecasting"]
    P0_QUESTION -->|"Causes"| P0_CAUSAL["Purpose 2: Causal and structural inference"]
    P0_QUESTION -->|"Structure in the series"| P0_STRUCTURE{"Which structure?"}
    P0_QUESTION -->|"Events or other outputs"| P0_TO_PART_2(["Continue in part 2"])
    P0_STRUCTURE -->|"Signal versus noise"| P0_SIGNAL["Purpose 3: Signal extraction and denoising"]
    P0_STRUCTURE -->|"Components"| P0_DECOMPOSITION["Purpose 6: Decomposition"]
    P0_STRUCTURE -->|"Frequencies"| P0_SPECTRAL["Purpose 8: Spectral analysis"]
    P0_FORECASTING & P0_CAUSAL & P0_SIGNAL & P0_DECOMPOSITION & P0_SPECTRAL --> P0_PURPOSE_FLAG["Set flag: purpose"]
    P0_PURPOSE_FLAG --> P3[["P3: Exploratory diagnostics"]]
    class P0_IN,P0_TO_PART_2 terminator
    class P0_QUESTION,P0_STRUCTURE decision
    class P0_FORECASTING,P0_CAUSAL,P0_SIGNAL,P0_DECOMPOSITION,P0_SPECTRAL,P0_PURPOSE_FLAG process
    class P3 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: events and other outputs.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_PART_2_IN(["From part 1"]) --> P0_QUESTION_2{"Question about?"}
    P0_QUESTION_2 -->|"Events"| P0_EVENTS{"Which events?"}
    P0_QUESTION_2 -->|"Other outputs"| P0_OUTPUTS{"Which output?"}
    P0_EVENTS -->|"Changes"| P0_CHANGE_POINT["Purpose 4: Change-point detection"]
    P0_EVENTS -->|"Anomalies or regimes"| P0_ANOMALY["Purpose 5: Anomaly and regime detection"]
    P0_OUTPUTS -->|"Features and labels"| P0_FEATURES["Purpose 7: Feature extraction, classification and clustering"]
    P0_OUTPUTS -->|"A system model"| P0_SYSTEM_ID["Purpose 9: System identification"]
    P0_OUTPUTS -->|"Simulated paths"| P0_SIMULATION["Purpose 10: Simulation and scenario generation"]
    P0_CHANGE_POINT & P0_ANOMALY & P0_FEATURES & P0_SYSTEM_ID & P0_SIMULATION --> P0_PURPOSE_FLAG[["Set flag: purpose"]]
    P0_PURPOSE_FLAG --> P3[["P3: Exploratory diagnostics"]]
    class P0_PART_2_IN terminator
    class P0_QUESTION_2,P0_EVENTS,P0_OUTPUTS decision
    class P0_CHANGE_POINT,P0_ANOMALY,P0_FEATURES,P0_SYSTEM_ID,P0_SIMULATION process
    class P0_PURPOSE_FLAG,P3 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Quick navigation

Emphasised phases are the phases whose leaves the purpose's sub-chart routes through (dotted pointers excluded).

| Purpose | Emphasised phases | Key leaves |
|---|---|---|
| [1. Forecasting](01-forecasting.md) | P6, P9, P11, P10 | Naive and seasonal-naive baselines; Epidemic nowcasting |
| [2. Causal and structural inference](02-causal-inference.md) | P3, P6, P11 | Identification strategy and exogeneity; Placebo and falsification tests; Sensitivity analysis across specifications |
| [3. Signal extraction and denoising](03-signal-extraction.md) | P1, P5, P8 | Characterise the noise; Wavelet denoising; Evaluate the signal-to-noise ratio |
| [4. Change-point detection](04-change-point-detection.md) | P3, P4, P6, P10 | Sequential detection; Bayesian online change-point detection; Offline segmentation |
| [5. Anomaly and regime detection](05-anomaly-regime-detection.md) | P6, P8, P10 | Statistical outlier scores; Matrix profile and discord discovery; Set thresholds by the cost of errors |
| [6. Decomposition](06-decomposition.md) | P3, P4 | Analyse and interpret the components; Additive or multiplicative decomposition; Revision stability of real-time decompositions |
| [7. Feature extraction, classification and clustering](07-feature-extraction-classification.md) | P6, P8, P11, P10 | Time-domain features; Shapelets and ROCKET; Clustering |
| [8. Spectral analysis](08-spectral-analysis.md) | P5 | Interpret the spectral shape; Peak significance; Cross-spectrum, coherence and phase |
| [9. System identification](09-system-identification.md) | P6 | Input design and persistent excitation; Order selection; Poles, zeros and stability |
| [10. Simulation and scenario generation](10-simulation.md) | P6, P11 | Monte Carlo simulation from a fitted model; Simulating paths by resampling; Check distribution and dependence matching |
