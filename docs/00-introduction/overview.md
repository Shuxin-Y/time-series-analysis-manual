# Introduction

## What is Time Series Analysis?

Time series analysis is the study of data points collected or recorded at successive time intervals. Unlike cross-sectional data (snapshots at a single point in time), time series data has inherent temporal structure that we must respect and leverage.

**Examples of time series data:**
- Stock prices recorded every second
- Monthly unemployment rates
- Daily temperature measurements
- Quarterly GDP figures
- Sensor readings from industrial equipment

## Why This Book is Necessary

### The Problem with Current Textbooks

Most time series textbooks fall into one of two camps:

**Classical econometrics texts** (Box-Jenkins, Hamilton, Enders):
- ✓ Rigorous mathematical foundations
- ✓ Strong theoretical grounding in ARIMA methodology
- ✗ Limited practical workflow guidance
- ✗ Minimal coverage of frequency-domain methods
- ✗ Often outdated computational examples (FORTRAN, early R)
- ✗ No integration with modern ML approaches

**Modern ML/data science books** (Hyndman-Athanasopoulos, forecasting packages):
- ✓ Practical code examples
- ✓ Modern forecasting methods
- ✓ Strong visualization
- ✗ Weak theoretical foundations
- ✗ Algorithm-focused without understanding diagnostics
- ✗ Limited coverage of when methods fail
- ✗ Minimal frequency-domain analysis

### What Makes This Book Different

This book bridges the gap by providing:

1. **Integrated workflow methodology**: Seamlessly moves between time domain, frequency domain, and time-frequency representations based on data characteristics
2. **Decision flowcharts as first-class citizens**: Three complementary flowcharts (general, purpose-based, representation-based) guide every analytical choice
3. **Test-driven decisions**: Every branch determined by explicit hypothesis tests (ADF, KPSS, Ljung-Box, etc.) with clear interpretation rules
4. **Both statistical and ML approaches**: Classical ARIMA/VAR alongside modern neural networks, with guidance on when to use each
5. **Frequency domain as essential, not optional**: Full treatment of FFT, spectral analysis, wavelets, and time-frequency methods
6. **Rigorous theory + modern code**: Mathematical foundations paired with production-ready Python implementations
7. **Diagnostic-focused**: Emphasis on residual analysis, model validation, and iterative refinement
8. **Deployment-ready**: Covers model monitoring, drift detection, and retraining strategies for production systems

## Who is This Book For?

**Primary audience:**
- Data scientists working with temporal data
- Economists and econometricians
- Quantitative analysts in finance
- Industrial data analysts and engineers
- Researchers in social sciences with time-series components

**Prerequisites:**
- Basic probability and statistics (mean, variance, hypothesis testing)
- Linear algebra fundamentals (vectors, matrices, eigenvalues)
- Python programming (numpy, pandas basics)
- Calculus (derivatives, integrals at undergraduate level)

**Not required:**
- Advanced measure theory or real analysis
- Prior time series experience
- Expertise in econometric software

## How to Use This Book

The book is structured in three layers:

### Layer 1: The Master Flowchart
Start here if you have data and want to know what to do next. The flowchart shows:
- Every decision point with explicit tests
- What to do if null hypothesis is rejected or not rejected
- Loops for iterative refinement

→ Go to [Master Flowchart](../01-master-flowchart/flowchart.md)

### Layer 2: Guided Walkthrough
Read this for a narrative explanation of each step in the flowchart, including:
- Why each test matters
- Common pitfalls
- When to deviate from the standard path

→ Go to [Guided Walkthrough](../01-master-flowchart/walkthrough.md)

### Layer 3: Deep Dive Chapters
Use these for rigorous understanding of each phase:
- Mathematical theory and proofs
- Test statistics and distributions
- Detailed Python implementations
- Worked examples with real data

**Chapter Structure:**
1. **Data Preparation** - Cleaning, sampling, and preprocessing
2. **Exploratory Analysis** - Distributions, stationarity, temporal structure
3. **Frequency Domain** - Spectral analysis, periodicities, filtering
4. **Modelling** - Statistical and ML models in time domain
5. **Feature Extraction** - Time, frequency, and nonlinear features for ML
6. **Validation & Deployment** - Testing, monitoring, and production deployment

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

## The Philosophy of This Book

1. **Test-driven decisions**: Every branch in the workflow is determined by hypothesis tests, not intuition
2. **Iterative refinement**: Models are improved through diagnostic testing and looping back
3. **Parsimony**: Start simple (ARIMA), only add complexity when diagnostics demand it
4. **Reproducibility**: All code is provided; all methods are algorithmically specified
5. **Theory + Practice**: Mathematical rigor paired with computational implementation

## Book Conventions

Throughout this book:

- **Mathematical notation** appears in collapsible blocks for clean reading
- **Python code** is provided inline with expected output
- **Hypothesis tests** always state H₀ (null hypothesis) and interpretation rules
- **Decision rules** explicitly state thresholds (e.g., p-value < 0.05)
- **Warnings** highlight common mistakes and edge cases

## Next Steps

Ready to start?

**If you're new to time series:**
1. Read this introduction
2. Skim the [Master Flowchart](../01-master-flowchart/flowchart.md) to see the big picture
3. Read [Guided Walkthrough](../01-master-flowchart/walkthrough.md) for context
4. Work through chapters 2-10 in order

**If you have specific questions:**
- Use the [Statistical Tests Reference](../appendices/B-statistical-tests-reference.md)
- Jump to relevant chapters via the [Table of Contents](../README.md)

**If you want to see code first:**
- Browse [code-examples/notebooks/](../code-examples/notebooks/)
- Check [Python Environment Setup](../appendices/C-python-environment-setup.md)

---

**[Next: Master Flowchart →](../01-master-flowchart/flowchart.md)**
