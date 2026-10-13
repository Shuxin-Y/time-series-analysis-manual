# Purpose 3: Signal extraction and denoising

**Goal:** Separate the signal of interest from noise.

## Sub-chart

**Part 1: noise, signal structure and the extraction method.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SE_IN(["Noisy signal"]) --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P0_SE_NOISE_TYPE["Characterise the noise<br/>white, coloured, 1/f, impulsive, non-stationary"]
    P0_SE_NOISE_TYPE --> P4[["P4: Transformations"]]
    P4 --> P0_SE_IMPULSIVE{"Impulsive noise?"}
    P4_INTEGRATED_LEVELS[["Integrated series kept in levels"]] -.- P4
    P0_SE_IMPULSIVE -->|"Yes"| P4_ROBUST_PREFILTER[["Robust prefiltering"]]
    P0_SE_IMPULSIVE -->|"No"| P5
    P4_ROBUST_PREFILTER --> P5[["P5: Representation selection"]]
    P5 --> P0_SE_STRUCTURE{"Signal structure?"}
    P0_SE_STRUCTURE -->|"Smooth, band-limited"| P0_SE_COLOUR{"Noise character?"}
    P0_SE_STRUCTURE -->|"Piecewise smooth or transient"| P5_TF_DWT[["Discrete and maximal-overlap wavelet transforms"]]
    P0_SE_STRUCTURE -->|"Latent dynamics"| P6[["P6: Conditional-mean model class"]]
    P0_SE_COLOUR -->|"White"| P5_FD_FILTERS[["FIR and IIR filter design<br/>causal in real time, zero-phase offline"]]
    P0_SE_COLOUR -->|"Coloured, spectra known"| P0_SE_WIENER["Wiener filtering<br/>causal Wiener filter in real time"]
    P5_TF_DWT --> P0_SE_WAVELET_DENOISING["Wavelet denoising<br/>universal or SURE thresholds for white noise; level-dependent for coloured or 1/f"]
    P6 --> P8[["P8: Estimation"]]
    P8 --> P8_KALMAN[["Kalman filter and smoother<br/>filter in real time, smoother offline"]]
    P8_KALMAN --> P9[["P9: In-sample diagnostics"]]
    P5_FD_FILTERS & P0_SE_WIENER & P0_SE_WAVELET_DENOISING & P9 --> P0_SE_TO_PART_2(["Continue in part 2"])
    class P0_SE_IN,P0_SE_TO_PART_2 terminator
    class P0_SE_IMPULSIVE,P0_SE_STRUCTURE,P0_SE_COLOUR decision
    class P0_SE_NOISE_TYPE,P0_SE_WIENER,P0_SE_WAVELET_DENOISING process
    class P1,P3,P4,P4_ROBUST_PREFILTER,P5,P5_TF_DWT,P6,P5_FD_FILTERS,P8,P8_KALMAN,P9,P4_INTEGRATED_LEVELS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: evaluation and use.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SE_PART_2_IN(["From part 1"]) --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P10_SIGNAL_EVALUATION[["Signal-extraction evaluation"]]
    P10_SIGNAL_EVALUATION --> P0_SE_SNR["Evaluate the signal-to-noise ratio"]
    P0_SE_SNR --> P0_SE_OK{"Peaks and edges preserved?"}
    P0_SE_OK -.->|"No"| P0_SE_STRUCTURE[["Signal structure?"]]
    P0_SE_OK -->|"Yes"| P11[["P11: Inference and interpretation"]]
    P11 --> P12[["P12: Deployment and monitoring"]]
    class P0_SE_PART_2_IN terminator
    class P0_SE_OK decision
    class P0_SE_SNR process
    class P10,P10_SIGNAL_EVALUATION,P0_SE_STRUCTURE,P11,P12 ref
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

[Signal-extraction evaluation](../../reference/13-spectral-analysis/index.md#signal-extraction-evaluation), [Evaluate the signal-to-noise ratio](../../reference/13-spectral-analysis/index.md#evaluate-the-signal-to-noise-ratio).

## P11 inference for this purpose

[Evaluate the signal-to-noise ratio](../../reference/13-spectral-analysis/index.md#evaluate-the-signal-to-noise-ratio).
