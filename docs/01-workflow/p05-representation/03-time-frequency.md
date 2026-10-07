# Representation 3: Time-frequency

**Best for:** Non-stationary signals, transients and evolving spectra.

## Sub-chart

**Part 1: when to choose it, and Fourier and wavelet transforms.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_TF_IN(["Transformed series from P4"]) --> P5_TF_CHANGING{"Frequency content changes over time?"}
    P5_TF_CHANGING -->|"Yes"| P5_TF_TRANSFORM{"Transform?"}
    P5_TF_CHANGING -->|"No"| P5_TF_TRANSIENTS{"Transients or bursts?"}
    P5_TF_TRANSIENTS -->|"Yes"| P5_TF_TRANSFORM
    P5_TF_TRANSIENTS -->|"No"| P5_TF_LOCALISATION{"Need both localisations?"}
    P5_TF_LOCALISATION -->|"Yes"| P5_TF_TRANSFORM
    P5_TF_LOCALISATION -->|"No"| P5[["P5: Representation selection"]]
    P5_TF_TRANSFORM -->|"Fixed window"| P5_TF_STFT["Short-time Fourier transform and the spectrogram"]
    P5_TF_TRANSFORM -->|"Continuous wavelet"| P5_TF_CWT["Continuous wavelet transform and the scalogram"]
    P5_TF_TRANSFORM -->|"Discrete wavelet"| P5_TF_DWT["Discrete and maximal-overlap wavelet transforms"]
    P5_TF_TRANSFORM -->|"Adaptive modes"| P5_TF_TO_PART_2(["Continue in part 2"])
    P5_TF_CWT --> P5_TF_SYNCHROSQUEEZING["Reassignment and synchrosqueezing"]
    P5_TF_STFT & P5_TF_SYNCHROSQUEEZING --> P2_FE_TF_FEATURES[["Time-frequency features"]]
    P5_TF_DWT --> P2_SE_WAVELET_DENOISING[["Wavelet denoising"]]
    P2_FE_TF_FEATURES & P2_SE_WAVELET_DENOISING --> P6[["P6: Conditional-mean model class"]]
    class P5_TF_IN,P5_TF_TO_PART_2 terminator
    class P5_TF_CHANGING,P5_TF_TRANSFORM,P5_TF_TRANSIENTS,P5_TF_LOCALISATION decision
    class P5_TF_STFT,P5_TF_CWT,P5_TF_DWT,P5_TF_SYNCHROSQUEEZING process
    class P5,P2_FE_TF_FEATURES,P2_SE_WAVELET_DENOISING,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: adaptive mode decompositions.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_TF_PART_2_IN(["From part 1: adaptive modes"]) --> P5_TF_ADAPTIVE{"Decomposition?"}
    P5_TF_ADAPTIVE -->|"Empirical"| P5_TF_EMD["Empirical mode decomposition and the Hilbert-Huang transform"]
    P5_TF_ADAPTIVE -->|"Variational"| P5_TF_VMD["Variational mode decomposition"]
    P5_TF_EMD & P5_TF_VMD --> P2_FE_TF_FEATURES[["Time-frequency features"]]
    P2_FE_TF_FEATURES --> P6[["P6: Conditional-mean model class"]]
    class P5_TF_PART_2_IN terminator
    class P5_TF_ADAPTIVE decision
    class P5_TF_EMD,P5_TF_VMD process
    class P2_FE_TF_FEATURES,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

