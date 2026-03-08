# Introduction

---
## What is Time Series Analysis?

Time series analysis is the study of data points collected or recorded at successive time intervals. Unlike cross-sectional data (snapshots at a single point in time), time series data has inherent temporal structure that we must respect and leverage.

A time-series is simply a sequence of data points indexed in time order. What makes it fundamentally different from regular tabular data is **temporal dependence** — observations are not independent of each other. Yesterday's stock price influences today's. Last month's temperature influences this month's. That single fact changes almost everything about how you model it.


**Examples of time series data:**

- Stock prices recorded every second
- Monthly unemployment rates
- Daily temperature measurements
- Quarterly GDP figures
- Sensor readings from industrial equipment


## Time Domain vs Frequency Domain

Time series analysis operates in two complementary domains:

### Time Domain
- Analyze values as they change over time (observation by observation)
- Models describe how current values depend on past values
- **Use when:** questions are about predictability, causality, "what happens next"
- **Methods:** ARIMA, VAR, GARCH, state-space models

### Frequency Domain
- Decompose signals into sine and cosine waves
- Reveals energy distribution across frequencies
- **Use when:** questions involve periodicity, cycles, spectral content
- **Methods:** Fourier transform, PSD, filtering, wavelets

**In practice:** Skilled analysts move between domains:
1. Start in time domain (check trends, autocorrelation)
2. Move to frequency domain (find hidden cycles)
3. Return to time domain (build forecasting model with periodic components)


---


**[Next: General Flowchart →](../01-master-flowchart/01-general-flowchart.md)**
