# P5: Representation selection

**Question this phase answers:** Which mathematical object is modelled?

Six representations are distinguished. Transforms and estimators that belong to a representation (spectral estimators, filters, wavelets, the analytic signal, embeddings, functional bases) are leaves of this phase; model families remain in P6.

## Representation selector

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P5_IN(["Transformed series from P4"]) --> P5_CHARACTER{"Dominant character?"}
    P5_CHARACTER -->|"Sequential dependence"| P5_TIME_DOMAIN["1 Time domain"]
    P5_CHARACTER -->|"Periodic"| P5_FREQUENCY_DOMAIN["2 Frequency domain"]
    P5_CHARACTER -->|"Spectrum changes over time"| P5_TIME_FREQUENCY["3 Time-frequency"]
    P5_CHARACTER -->|"Latent states, gaps"| P5_STATE_SPACE["4 State space"]
    P5_CHARACTER -->|"Curves"| P5_FUNCTIONAL["5 Functional"]
    P5_CHARACTER -->|"Instantaneous frequency"| P5_HILBERT["6 Hilbert and phase"]
    P5_TIME_DOMAIN & P5_FREQUENCY_DOMAIN & P5_TIME_FREQUENCY & P5_STATE_SPACE & P5_FUNCTIONAL & P5_HILBERT --> P6[["P6 Conditional-mean model class"]]
    class P5_IN terminator
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
| Pending | Pending | Filled in Plan B |

### Topics carried over from the previous outline

- Fourier theory
- Power spectral density
- Periodicity detection
- Spectral analysis
- Filtering techniques
