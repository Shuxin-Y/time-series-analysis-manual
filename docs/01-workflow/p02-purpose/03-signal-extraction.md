# Purpose 3: Signal extraction and denoising

**Goal:** Separate the signal of interest from noise.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_SE_IN(["Noisy signal"]) --> P2_SE_NOISE_TYPE["Characterise the noise<br/>white, coloured, impulsive, non-stationary, 1/f"]
    P2_SE_NOISE_TYPE --> P2_SE_NOISE_Q{"Noise character?"}
    P2_SE_NOISE_Q -->|"White"| P5
    P2_SE_NOISE_Q -->|"Coloured"| P2_SE_WIENER["Wiener filtering"]
    P2_SE_NOISE_Q -->|"Impulsive"| P0[["P0: Data acquisition and cleaning"]]
    P2_SE_NOISE_Q -->|"Non-stationary"| P8[["P8: Estimation"]]
    P2_SE_NOISE_Q -->|"1/f"| P5
    P0 --> P0_ROBUST_FILTER[["Robust filtering"]]
    P0_ROBUST_FILTER --> P5[["P5: Representation selection"]]
    P5 --> P2_SE_TRANSFORM{"Filter or wavelet?"}
    P2_SE_TRANSFORM -->|"Filter"| P5_FD_FILTERS[["FIR and IIR filter design"]]
    P2_SE_TRANSFORM -->|"Wavelet"| P5_TF_DWT[["Discrete and maximal-overlap wavelet transforms"]]
    P5_TF_DWT --> P2_SE_WAVELET_DENOISING["Wavelet denoising"]
    P8 --> P8_KALMAN[["Kalman filter and smoother"]]
    P5_FD_FILTERS & P2_SE_WIENER & P8_KALMAN & P2_SE_WAVELET_DENOISING --> P2_SE_SNR["Evaluate the signal-to-noise ratio"]
    P2_SE_SNR --> P2_SE_OK{"Signal preserved?"}
    P2_SE_OK -.->|"No"| P2_SE_NOISE_Q
    P2_SE_OK -->|"Yes"| P11[["P11: Validation and deployment"]]
    class P2_SE_IN terminator
    class P2_SE_NOISE_Q,P2_SE_TRANSFORM,P2_SE_OK decision
    class P2_SE_NOISE_TYPE,P2_SE_WIENER,P2_SE_WAVELET_DENOISING,P2_SE_SNR process
    class P0,P8,P0_ROBUST_FILTER,P5,P5_FD_FILTERS,P5_TF_DWT,P8_KALMAN,P11 ref
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

[Evaluate the signal-to-noise ratio](../../reference/13-spectral-analysis/index.md#evaluate-the-signal-to-noise-ratio).

## P11 metrics for this purpose

[Evaluate the signal-to-noise ratio](../../reference/13-spectral-analysis/index.md#evaluate-the-signal-to-noise-ratio).
