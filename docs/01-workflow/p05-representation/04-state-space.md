# Representation 4: State space

**Best for:** Latent states, irregular sampling, missing observations and online updating.

## Sub-chart

**Part 1: latent states and the linear Gaussian filter.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_SS_IN(["Transformed series from P4"]) --> P5_SS_LATENT_STATES{"Latent states?"}
    P5_SS_LATENT_STATES -->|"Yes"| P5_SS_DYNAMICS{"Dynamics?"}
    P5_SS_LATENT_STATES -->|"No"| P5_SS_IRREGULAR{"Gaps or irregular spacing?"}
    P5_SS_IRREGULAR -->|"Gaps on a regular grid"| P5_SS_DYNAMICS
    P5_SS_IRREGULAR -->|"Irregular spacing"| B3[["B3 Irregular sampling and continuous time"]]
    P5_SS_IRREGULAR -->|"Neither"| P5_SS_ONLINE{"Online updating needed?"}
    P5_SS_ONLINE -->|"Yes"| P5_SS_DYNAMICS
    P5_SS_ONLINE -->|"No"| P5[["P5: Representation selection"]]
    P5_SS_DYNAMICS -->|"Linear Gaussian"| P5_SS_FORM["State-space form and the ARIMA rewriting"]
    P5_SS_DYNAMICS -->|"Nonlinear or non-Gaussian"| P5_SS_TO_PART_2(["Continue in part 2"])
    P5_SS_DYNAMICS -->|"Reconstructed from regular dense data"| P5_SS_TO_PART_3(["Continue in part 3"])
    P5_SS_FORM --> P5_SS_LATENT["Latent states and missing observations"]
    P5_SS_LATENT --> P8_KALMAN[["Kalman filter and smoother<br/>filter in real time, smoother offline"]]
    P8_KALMAN --> P6_DLM[["Dynamic linear models"]]
    P8_KALMAN --> P6_BSTS[["Bayesian structural time series"]]
    P8_KALMAN --> P6_STRUCTURAL_TS[["Structural time-series models"]]
    P6_DLM & P6_BSTS & P6_STRUCTURAL_TS --> P6[["P6: Conditional-mean model class"]]
    class P5_SS_IN,P5_SS_TO_PART_2,P5_SS_TO_PART_3 terminator
    class P5_SS_LATENT_STATES,P5_SS_DYNAMICS,P5_SS_IRREGULAR,P5_SS_ONLINE decision
    class P5_SS_FORM,P5_SS_LATENT process
    class P5,B3,P8_KALMAN,P6_DLM,P6_BSTS,P6_STRUCTURAL_TS,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: nonlinear and non-Gaussian filtering.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_SS_PART_2_IN(["From part 1: nonlinear or non-Gaussian"]) --> P5_SS_FILTER_Q{"Shape of the filtering distribution?"}
    P5_SS_FILTER_Q -->|"Near-Gaussian, mild nonlinearity"| P8_NONLINEAR_FILTERS[["Extended and unscented Kalman filters"]]
    P5_SS_FILTER_Q -->|"Multimodal, heavy-tailed, non-Gaussian observations"| P8_PARTICLE_FILTERS[["Particle filters"]]
    P8_NONLINEAR_FILTERS & P8_PARTICLE_FILTERS --> P7_SV[["Stochastic volatility"]]
    P8_NONLINEAR_FILTERS & P8_PARTICLE_FILTERS --> P6_MARKOV_SWITCHING[["Markov-switching models"]]
    P7_SV & P6_MARKOV_SWITCHING --> P6[["P6: Conditional-mean model class"]]
    class P5_SS_PART_2_IN terminator
    class P5_SS_FILTER_Q decision
    class P8_NONLINEAR_FILTERS,P8_PARTICLE_FILTERS,P7_SV,P6_MARKOV_SWITCHING,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: dynamics reconstructed from dense data.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_SS_PART_3_IN(["From part 1: regular dense data"]) --> P5_SS_RECON{"Object of the reconstruction?"}
    P5_SS_RECON -->|"Attractor geometry"| P5_SS_TAKENS["Takens embedding and phase-space reconstruction<br/>delay and dimension by mutual information, false neighbours"]
    P5_SS_RECON -->|"Linear modes of the evolution operator"| P5_SS_DMD["Dynamic mode decomposition and Koopman operators"]
    P5_SS_TAKENS --> P5_SS_CHAOS["Chaos indicators with surrogate data<br/>Lyapunov exponents, correlation dimension"]
    P5_SS_CHAOS & P5_SS_DMD --> P6[["P6: Conditional-mean model class"]]
    class P5_SS_PART_3_IN terminator
    class P5_SS_RECON decision
    class P5_SS_TAKENS,P5_SS_DMD,P5_SS_CHAOS process
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

