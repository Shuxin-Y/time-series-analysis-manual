# Purpose 8: Spectral analysis

**Goal:** Describe the distribution of variance across frequencies.

## Sub-chart

**Part 1: data, representation and the estimator.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SP_IN(["Spectral question"]) --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P4[["P4: Transformations"]]
    P4 --> P5[["P5: Representation selection"]]
    P5 --> P0_SP_CHANGES{"Spectrum changes over time?"}
    P0_SP_CHANGES -->|"Yes"| P5_TIME_FREQUENCY[["Representation 3: Time-frequency"]]
    P0_SP_CHANGES -->|"No"| P5_FD_DFT[["Discrete Fourier transform and the periodogram"]]
    P5_FD_DFT --> P5_FD_LEAKAGE[["Leakage, tapering and the Nyquist frequency"]]
    P5_FD_LEAKAGE --> P0_SP_ESTIMATOR{"Estimator?"}
    P0_SP_ESTIMATOR -->|"Smoothed periodogram"| P5_FD_SMOOTHED[["Smoothed spectral estimates"]]
    P0_SP_ESTIMATOR -->|"Multitaper"| P5_FD_MULTITAPER[["Multitaper spectral estimation"]]
    P0_SP_ESTIMATOR -->|"AR or ARMA spectrum"| P6[["P6: Conditional-mean model class"]]
    P6 --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> P5_FD_PARAMETRIC[["Parametric spectra"]]
    P5_FD_SMOOTHED & P5_FD_MULTITAPER & P5_FD_PARAMETRIC --> P0_SP_TO_PART_2(["Continue in part 2"])
    class P0_SP_IN,P0_SP_TO_PART_2 terminator
    class P0_SP_CHANGES,P0_SP_ESTIMATOR decision
    class P1,P3,P4,P5,P5_TIME_FREQUENCY,P5_FD_DFT,P5_FD_LEAKAGE,P5_FD_SMOOTHED,P5_FD_MULTITAPER,P6,P8,P9,P5_FD_PARAMETRIC ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: one, two or several series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SP_PART_2_IN(["From part 1"]) --> P0_SP_SERIES{"One, two or several series?"}
    P0_SP_SERIES -->|"One"| P0_SP_SPECTRAL_SHAPE["Interpret the spectral shape<br/>white, 1/f, peaks, band-limited"]
    P0_SP_SERIES -->|"Two or several"| P0_SP_CROSS_SPECTRUM["Cross-spectrum, coherence and phase<br/>coherence threshold, phase confidence interval; partial coherence for several series"]
    P0_SP_SPECTRAL_SHAPE --> P0_SP_PEAKS{"Peaks?"}
    P0_SP_PEAKS -->|"Yes"| P0_SP_PEAK_SIGNIFICANCE["Peak significance<br/>multitaper F-test; Fisher's g on a prewhitened periodogram; red-noise background"]
    P0_SP_PEAKS -->|"No"| P0_SP_PART_2_OUT
    P0_SP_PEAK_SIGNIFICANCE --> P0_SP_HARMONIC_REGRESSION["Harmonic regression from detected frequencies"]
    P0_SP_CROSS_SPECTRUM --> P0_SP_FREQ_GRANGER["Frequency-domain Granger causality"]
    P0_SP_HARMONIC_REGRESSION & P0_SP_FREQ_GRANGER --> P0_SP_PART_2_OUT(["Continue in part 3"])
    class P0_SP_PART_2_IN,P0_SP_PART_2_OUT terminator
    class P0_SP_SERIES,P0_SP_PEAKS decision
    class P0_SP_SPECTRAL_SHAPE,P0_SP_CROSS_SPECTRUM,P0_SP_PEAK_SIGNIFICANCE,P0_SP_HARMONIC_REGRESSION,P0_SP_FREQ_GRANGER process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: evaluation and inference.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_SP_PART_3_IN(["From part 2"]) --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P11[["P11: Inference and interpretation"]]
    P11 --> P11_SPECTRAL_BANDS[["Confidence bands for spectral estimates"]]
    P11_SPECTRAL_BANDS --> P12[["P12: Deployment and monitoring"]]
    class P0_SP_PART_3_IN terminator
    class P10,P11,P11_SPECTRAL_BANDS,P12 ref
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

[Peak significance](../../reference/13-spectral-analysis/index.md#peak-significance).

## P11 inference for this purpose

[Peak significance](../../reference/13-spectral-analysis/index.md#peak-significance), [Confidence bands for spectral estimates](../../reference/13-spectral-analysis/index.md#confidence-bands-for-spectral-estimates).
