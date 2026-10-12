# Purpose 8: Spectral analysis

**Goal:** Describe the distribution of variance across frequencies.

## Sub-chart

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SP_IN(["Spectral question"]) --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P4[["P4: Transformations"]]
    P4 --> P0_SP_SERIES{"One or two series?"}
    P0_SP_SERIES -->|"One"| P5[["P5: Representation selection"]]
    P0_SP_SERIES -->|"Two"| P0_SP_CROSS_SPECTRUM["Cross-spectrum, coherence and phase"]
    P5 --> P5_FD_DFT[["Discrete Fourier transform and the periodogram"]]
    P5_FD_DFT --> P5_FD_SMOOTHED[["Smoothed spectral estimates"]]
    P5_FD_SMOOTHED --> P0_SP_SPECTRAL_SHAPE["Interpret the spectral shape<br/>white, 1/f, peaks, band-limited"]
    P0_SP_SPECTRAL_SHAPE --> P0_SP_PEAKS{"Peaks?"}
    P0_SP_PEAKS -->|"Yes"| P0_SP_PEAK_SIGNIFICANCE["Peak significance<br/>Fisher's g-test"]
    P0_SP_PEAKS -->|"No"| P10
    P0_SP_PEAK_SIGNIFICANCE --> P0_SP_HARMONIC_REGRESSION["Harmonic regression from detected frequencies"]
    P0_SP_CROSS_SPECTRUM --> P0_SP_FREQ_GRANGER["Frequency-domain Granger causality"]
    P0_SP_HARMONIC_REGRESSION & P0_SP_FREQ_GRANGER --> P10[["P10: Out-of-sample evaluation and selection"]]
    class P0_SP_IN terminator
    class P0_SP_SERIES,P0_SP_PEAKS decision
    class P0_SP_CROSS_SPECTRUM,P0_SP_SPECTRAL_SHAPE,P0_SP_PEAK_SIGNIFICANCE,P0_SP_HARMONIC_REGRESSION,P0_SP_FREQ_GRANGER process
    class P3,P4,P5,P5_FD_DFT,P5_FD_SMOOTHED,P10 ref
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

[Peak significance](../../reference/13-spectral-analysis/index.md#peak-significance).

## P10 metrics for this purpose

[Peak significance](../../reference/13-spectral-analysis/index.md#peak-significance). The same leaf serves as inference and metric.
