# P2: Purpose

**Question this phase answers:** What is the question?

The purpose decides which later phases matter most and which inference and metrics apply at the end. Ten purposes are distinguished. Methods that belong to a purpose rather than to the standard pipeline (change-point algorithms, anomaly methods, decomposition methods, feature extraction, classification, clustering, simulation) are leaves of this phase.

## Purpose selector

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_IN(["Series and flags from P1"]) --> P2_PURPOSE{"Purpose?"}
    P2_PURPOSE -->|"Predict"| P2_FORECASTING["Purpose 1: Forecasting"]
    P2_PURPOSE -->|"Explain"| P2_CAUSAL["Purpose 2: Causal and structural inference"]
    P2_PURPOSE -->|"Clean"| P2_SIGNAL["Purpose 3: Signal extraction and denoising"]
    P2_PURPOSE -->|"Locate changes"| P2_CHANGE_POINT["Purpose 4: Change-point detection"]
    P2_PURPOSE -->|"Flag unusual"| P2_ANOMALY["Purpose 5: Anomaly and regime detection"]
    P2_PURPOSE -->|"Split"| P2_DECOMPOSITION["Purpose 6: Decomposition"]
    P2_PURPOSE -->|"Label or group"| P2_FEATURES["Purpose 7: Feature extraction, classification and clustering"]
    P2_PURPOSE -->|"Describe cycles"| P2_SPECTRAL["Purpose 8: Spectral analysis"]
    P2_PURPOSE -->|"Identify a system"| P2_SYSTEM_ID["Purpose 9: System identification"]
    P2_PURPOSE -->|"Generate paths"| P2_SIMULATION["Purpose 10: Simulation and scenario generation"]
    P2_FORECASTING & P2_CAUSAL & P2_SIGNAL & P2_CHANGE_POINT & P2_ANOMALY --> P3[["P3: Exploratory diagnostics"]]
    P2_DECOMPOSITION & P2_FEATURES & P2_SPECTRAL & P2_SYSTEM_ID & P2_SIMULATION --> P3
    class P2_IN terminator
    class P2_PURPOSE decision
    class P2_FORECASTING,P2_CAUSAL,P2_SIGNAL,P2_CHANGE_POINT,P2_ANOMALY,P2_DECOMPOSITION,P2_FEATURES,P2_SPECTRAL,P2_SYSTEM_ID,P2_SIMULATION process
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

## Quick navigation

| Purpose | Emphasised phases | Key leaves |
|---|---|---|
| [1. Forecasting](01-forecasting.md) | P6, P9, P10, P11 | Choose the forecast horizon and origin; Naive and seasonal-naive baselines; Epidemic nowcasting |
| [2. Causal and structural inference](02-causal-inference.md) | P6, P10 | Identification strategy and exogeneity; Placebo and falsification tests; Sensitivity analysis across specifications |
| [3. Signal extraction and denoising](03-signal-extraction.md) | P0, P5, P8 | Characterise the noise; Choose the filter; Wavelet denoising |
| [4. Change-point detection](04-change-point-detection.md) | P3, P4, P6, P7, P11 | Sequential detection; Bayesian online change-point detection; Offline segmentation |
| [5. Anomaly and regime detection](05-anomaly-regime-detection.md) | P8, P11 | Point, contextual or collective anomaly; Matrix profile and discord discovery; Set thresholds by the cost of errors |
| [6. Decomposition](06-decomposition.md) | P4, P9 | Detect the period; Additive or multiplicative decomposition; Revision stability of real-time decompositions |
| [7. Feature extraction, classification and clustering](07-feature-extraction-classification.md) | P6, P8, P11 | Time-domain features; Shapelets and ROCKET; Clustering |
| [8. Spectral analysis](08-spectral-analysis.md) | P5 | Interpret the spectral shape; Peak significance; Cross-spectrum, coherence and phase |
| [9. System identification](09-system-identification.md) | P6 | Input design and persistent excitation; Order selection; Poles, zeros and stability |
| [10. Simulation and scenario generation](10-simulation.md) | P10 | Monte Carlo simulation from a fitted model; Bootstrap path simulation; Stress scenarios and shock design |
