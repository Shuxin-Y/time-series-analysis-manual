# Purpose 3: Signal extraction and denoising

**Goal:** Separate the signal of interest from noise.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SE_IN(["Noisy signal"]) --> P0_SE_NOISE_TYPE["Characterise the noise<br/>white, coloured, impulsive, non-stationary, 1/f"]
    P0_SE_NOISE_TYPE --> P0_SE_NOISE_Q{"Noise character?"}
    P0_SE_NOISE_Q -->|"White or 1/f"| P5
    P0_SE_NOISE_Q -->|"Coloured"| P0_SE_WIENER["Wiener filtering"]
    P0_SE_NOISE_Q -->|"Impulsive"| P1[["P1: Data acquisition and cleaning"]]
    P0_SE_NOISE_Q -->|"Non-stationary: state-space model"| P6[["P6: Conditional-mean model class"]]
    P6 --> P8[["P8: Estimation"]]
    P1 --> P4[["P4: Transformations"]]
    P4 --> P4_ROBUST_PREFILTER[["Robust prefiltering"]]
    P4_ROBUST_PREFILTER --> P5[["P5: Representation selection"]]
    P5 --> P0_SE_TRANSFORM{"Noise colour?"}
    P0_SE_TRANSFORM -->|"White: filter"| P5_FD_FILTERS[["FIR and IIR filter design"]]
    P0_SE_TRANSFORM -->|"1/f: wavelet thresholding"| P5_TF_DWT[["Discrete and maximal-overlap wavelet transforms"]]
    P5_TF_DWT --> P0_SE_WAVELET_DENOISING["Wavelet denoising"]
    P8 --> P8_KALMAN[["Kalman filter and smoother"]]
    P5_FD_FILTERS & P0_SE_WIENER & P8_KALMAN & P0_SE_WAVELET_DENOISING --> P0_SE_SNR["Evaluate the signal-to-noise ratio"]
    P0_SE_SNR --> P0_SE_OK{"Signal preserved?"}
    P0_SE_OK -.->|"No"| P0_SE_NOISE_TYPE
    P0_SE_OK -->|"Yes"| P10[["P10: Out-of-sample evaluation and selection"]]
    class P0_SE_IN terminator
    class P0_SE_NOISE_Q,P0_SE_TRANSFORM,P0_SE_OK decision
    class P0_SE_NOISE_TYPE,P0_SE_WIENER,P0_SE_WAVELET_DENOISING,P0_SE_SNR process
    class P1,P4,P6,P8,P4_ROBUST_PREFILTER,P5,P5_FD_FILTERS,P5_TF_DWT,P8_KALMAN,P10 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P11 inference for this purpose

[Evaluate the signal-to-noise ratio](../../reference/13-spectral-analysis/index.md#evaluate-the-signal-to-noise-ratio).

## P10 metrics for this purpose

[Evaluate the signal-to-noise ratio](../../reference/13-spectral-analysis/index.md#evaluate-the-signal-to-noise-ratio). The same leaf serves as inference and metric.
