# Purpose 8: Spectral analysis

**Goal:** Describe the distribution of variance across frequencies.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_SP_IN(["Spectral question"]) --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P4[["P4: Transformations"]]
    P4 --> P2_SP_SERIES{"One or two series?"}
    P2_SP_SERIES -->|"One"| P5_FD_DFT[["Discrete Fourier transform and the periodogram"]]
    P2_SP_SERIES -->|"Two"| P2_SP_CROSS_SPECTRUM["Cross-spectrum, coherence and phase"]
    P5_FD_DFT --> P5_FD_SMOOTHED[["Smoothed spectral estimates"]]
    P5_FD_SMOOTHED --> P2_SP_SPECTRAL_SHAPE["Interpret the spectral shape<br/>white, 1/f, peaks, band-limited"]
    P2_SP_SPECTRAL_SHAPE --> P2_SP_PEAKS{"Peaks?"}
    P2_SP_PEAKS -->|"Yes"| P2_SP_PEAK_SIGNIFICANCE["Peak significance<br/>Fisher's g-test"]
    P2_SP_PEAKS -->|"No"| P11
    P2_SP_PEAK_SIGNIFICANCE --> P2_SP_HARMONIC_REGRESSION["Harmonic regression from detected frequencies"]
    P2_SP_CROSS_SPECTRUM --> P2_SP_FREQ_GRANGER["Frequency-domain Granger causality"]
    P2_SP_HARMONIC_REGRESSION & P2_SP_FREQ_GRANGER --> P11[["P11: Validation and deployment"]]
    class P2_SP_IN terminator
    class P2_SP_SERIES,P2_SP_PEAKS decision
    class P2_SP_CROSS_SPECTRUM,P2_SP_SPECTRAL_SHAPE,P2_SP_PEAK_SIGNIFICANCE,P2_SP_HARMONIC_REGRESSION,P2_SP_FREQ_GRANGER process
    class P3,P4,P5_FD_DFT,P5_FD_SMOOTHED,P11 ref
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

[Peak significance](../../reference/13-spectral-analysis/index.md#peak-significance).

## P11 metrics for this purpose

[Peak significance](../../reference/13-spectral-analysis/index.md#peak-significance).
