# P5: Representation selection

**Question this phase answers:** Which mathematical object is modelled?

Six representations are distinguished. Transforms and estimators that belong to a representation (spectral estimators, filters, wavelets, the analytic signal, embeddings, functional bases) are leaves of this phase; model families remain in P6.

The sampling flag is read first, because the time-domain, time-frequency and Hilbert representations need a regular grid. A series that keeps its irregular times has four representations defined on arbitrary times: the Lomb-Scargle periodogram, the continuous-time state space of branch B3, sparse curves by pooled covariance estimation, and Gaussian-process regression. A regular or resampled series chooses among the six representations.

## Representation selector

**Part 1: the sampling gate.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_IN(["Transformed series from P4"]) --> P5_GRID{"Sampling flag?"}
    P5_GRID -->|"Regular or resampled"| P5_TO_PART_2(["Continue in part 2"])
    P5_GRID -->|"Irregular, kept"| P5_IRREGULAR{"What is represented on the irregular times?"}
    P5_IRREGULAR -->|"Spectrum"| P5_FD_LOMB_SCARGLE[["Lomb-Scargle periodogram"]]
    P5_IRREGULAR -->|"Latent continuous-time process"| B3[["B3 Irregular sampling and continuous time"]]
    P5_IRREGULAR -->|"Sparse curves"| P5_FN_PACE[["Sparse curves by pooled covariance estimation"]]
    P5_IRREGULAR -->|"A smooth function of time"| P6_GAUSSIAN_PROCESS[["Gaussian-process regression"]]
    P5_FD_LOMB_SCARGLE & P5_FN_PACE & P6_GAUSSIAN_PROCESS --> P6[["P6: Conditional-mean model class"]]
    class P5_IN,P5_TO_PART_2 terminator
    class P5_GRID,P5_IRREGULAR decision
    class P5_FD_LOMB_SCARGLE,B3,P5_FN_PACE,P6_GAUSSIAN_PROCESS,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: representation by dominant character.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_PART_2_IN(["From part 1"]) --> P5_CHARACTER{"Dominant character?"}
    P5_CHARACTER -->|"Sequential dependence"| P5_TIME_DOMAIN["Representation 1: Time domain"]
    P5_CHARACTER -->|"Periodic"| P5_FREQUENCY_DOMAIN["Representation 2: Frequency domain"]
    P5_CHARACTER -->|"Spectrum changes over time"| P5_TIME_FREQUENCY["Representation 3: Time-frequency"]
    P5_CHARACTER -->|"Latent states, gaps"| P5_STATE_SPACE["Representation 4: State space"]
    P5_CHARACTER -->|"Curves"| P5_FUNCTIONAL["Representation 5: Functional"]
    P5_CHARACTER -->|"Instantaneous frequency"| P5_HILBERT["Representation 6: Hilbert and phase"]
    P5_TIME_DOMAIN & P5_FREQUENCY_DOMAIN & P5_TIME_FREQUENCY & P5_STATE_SPACE & P5_FUNCTIONAL & P5_HILBERT --> P6[["P6: Conditional-mean model class"]]
    class P5_PART_2_IN terminator
    class P5_CHARACTER decision
    class P5_TIME_DOMAIN,P5_FREQUENCY_DOMAIN,P5_TIME_FREQUENCY,P5_STATE_SPACE,P5_FUNCTIONAL,P5_HILBERT process
    class P6 ref
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

| Representation | Choose when | Key leaves |
|---|---|---|
| [1. Time domain](01-time-domain.md) | Predicting next values, a causal question, or sequential dependence | Autocovariance and the ACF as the time-domain object; Lag structure and memory |
| [2. Frequency domain](02-frequency-domain.md) | Periodic patterns, separate frequency bands, or spectral content as the question | Discrete Fourier transform and the periodogram; Multitaper spectral estimation; FIR and IIR filter design |
| [3. Time-frequency](03-time-frequency.md) | Frequency content that changes over time, transients or bursts, or both localisations | Short-time Fourier transform and the spectrogram; Continuous wavelet transform and the scalogram; Empirical mode decomposition and the Hilbert-Huang transform |
| [4. State space](04-state-space.md) | Latent states, gaps on a regular grid, or online updating | State-space form and the ARIMA rewriting; Latent states and missing observations; Takens embedding and phase-space reconstruction |
| [5. Functional](05-functional.md) | Observations that are curves, shape or derivatives that matter, or dense sampling per curve | Basis representation and smoothing of curves; Functional principal components; Functional regression and functional autoregression |
| [6. Hilbert and phase](06-hilbert-phase.md) | Instantaneous frequency, amplitude envelope, or phase relations between signals | Analytic signal and instantaneous frequency; Phase synchronisation and the phase-locking value |
