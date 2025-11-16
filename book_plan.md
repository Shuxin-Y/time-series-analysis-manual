## structure

1. Introduction
    - Who is this book for
    - How to use this book
    - Why is this book necessary (comparison with current textbooks in use)
1. Flowcharts
    
    These two flowcharts must serve as practical decision-making guides, not just conceptual diagrams. A reader should be able to follow the arrows and make concrete analytical choices based on their own data.

    1. General Requirements for All Flowcharts
        - Start explicitly with DATA as the first node.
        - Every branch must reflect actual diagnostic steps/tests (e.g. ADF test), not abstract categories (e.g. stationarity test).
        - Each path should end in appropriate transformations, domain choices, and final model families.
        - The flow must mirror the standard econometric workflow:
            1.	Data
            2.	Purpose
            3.	Diagnostic tests
            4.	Required transformations/actions based on test results
            5.  Following tests
            2.  Following transformations/actions
            5.	Domain selection (time / frequency / time–frequency)
            6.	Candidate model classes
            7.	Estimation / validation options
        - Keep visual complexity manageable by using:
            - high-level boxes for major steps,
            - collapsible sub-lists (if the platform supports them),
            - icons or colors to differentiate tests, transformations, and models.
            - link to places where each tests are mentioned first in the book

    1. General flowchart 
        (As the structure of the rest of this book)
    1.	Purpose-based workflow
        - Forecasting
        - Causal analysis / Structural inference
        - Signal extraction / Denoising
        - Change-point detection
        - Anomaly / regime detection
        - Decomposition (trend–cycle–seasonality)
        - Feature extraction for ML
        - Spectral analysis and system identification
	2.	Representation-based workflow (time / frequency / state-space).
        - Time domain
        - Frequency domain
        - Time–frequency domain
        - State-space representation
        - Functional domain (when series are curves)
        - Hilbert/phase domain (instantaneous frequency, analytic signal)

1. Data Preparation
    - Obtain and inspect raw signal
        - Sampling rate, resolution, missing intervals.
        - Align timestamps, handle time zones, resample
    - Cleaning and preprocessing
        - Handle missing values, spikes, or sensor errors
        - Detrend or normalize (z-score, min-max, log transform).
        - Convert cumulative to flow variables if needed (e.g., kWh to kW).
    - Ensure data consistency
        - Unit and metadata consistency
        - Synchronization and alignment
        - Anti-aliasing / resampling strategy when downsampling
1. Exploratory Analysis
    - Check distributional properties
        - Skewness, kurtosis, normality test — helps decide transformations.
        - Detect outliers
        - Check heteroskedasticity → possible GARCH behavior.
    - Assess temporal structure
        - Test stationarity (ADF, KPSS); difference or detrend if needed.
        - Examine ACF and PACF for memory structure (AR/MA order).
        - Decompose trend and seasonality (STL, additive/multiplicative).
        - Verify residuals are white noise.
3. Frequency, Multiscale, and Structure (frequency domain)
    - Analysis 
        - Detect periodicities invisible in time plots.
        - Quantify how much variance lies at low vs. high frequencies.
        - Diagnose noise: white, pink (1/f), or periodic components.
        - Design filters or transformations (band-pass, low-pass).
        - Identify dominant frequency bands (e.g., 8–12 Hz vibration energy).
    - Action
        - Re-enter the time domain and include seasonal terms or harmonic regressors.
        - Filter out unwanted frequencies (denoising).
        - Track how frequency content changes over time (non-stationarity indicator).
4. Modelling (time domain)
    - Select and fit models
        - Statistical models: (ARIMA, VAR, GARCH, etc.) — interpretable but parametric.
        - ML models: (RF, XGBoost, RNN, Transformers) — feature-driven, nonparametric.
    - Evaluate and forecast
        - In-sample fit, information criteria (AIC/BIC), residual diagnostics.
        - Out-of-sample prediction and error analysis (RMSE, MAPE).
    - Extend to complex dynamics
        - Multivariate and causal: cross-correlation, Granger causality, VAR.
        - Frequency-domain analogs: coherence, cross-spectrum.
        - Nonlinear or regime-switching: Threshold AR, Markov-switching, neural models.
5. Feature extraction for ML
    - Frequency-domain features
        - band power, spectral entropy, spectral centroid, dominant frequency, etc.
    - Time–frequency features
        - extracted from STFT or wavelet coefficients — these can capture transient bursts or modulations.
    - Nonlinear dynamics
        - Lyapunov exponents, recurrence quantification, if your signal shows chaos-like patterns.
    - Rolling statistics, spectral features, entropy, frequency-band power.
6. Validation and deployment
    - Out-of-sample testing, backtesting.
    - Rolling-origin evaluation
        - time-respecting cross-validation for non-iid data.
    - Model monitoring
        - drift detection using KL divergence or spectral shift (frequency-domain drift).
    - Recalibration / retraining policy

## Functional requirements

1.	Documentation Engine
    - Use MkDocs as the static site generator.
    - Use Material for MkDocs as the theme, since it supports a clean navigation structure, good typography, built-in search, and strong support for mathematical notation.
2.	Terminology System (Interactive Glossary)
    - All key technical terms should be recognised and rendered as clickable elements.
    - When a term is clicked, a drawer panel should slide in from the right side of the screen.
    - The drawer should display:
        - the definition of the term,
        - formal or mathematical expressions if applicable,
        - a short historical note or timeline of the relevant literature.
    - This feature can be implemented via a small custom JavaScript and CSS component on top of MkDocs Material.
3.	Code Examples
    - Code samples should appear immediately after the relevant paragraph as collapsible blocks.
    - All code must also be stored as standalone files in a code/ directory.
    - The documentation should include these files using --8<-- snippets, so the blocks always stay consistent with the source code.
4.	Mathematical Writing and Chapter Style
    - The layout should follow the clarity and structure of modern technical guides, similar to Google ML documentation or the Stan User’s Guide: clear headings, structured exposition, numbered equations where appropriate, and easy navigation.
    - The site should be fully compatible with MathJax for formulas, and with standard cross-referencing of concepts, sections, and figures.

5. Stylistic Benchmark for the Book
The overall presentation should follow the style of modern, technically rigorous online guides such as the Stan User’s Guide and Econometrics With R. That is, the writing should feature:
    - clear exposition with step-by-step derivations when appropriate;
    - well-structured sections and subsections;
    - consistent formatting of equations, definitions, and examples;
    - unobtrusive but accessible technical details.

6.	Deployment
    - The whole system should be deployable to GitHub Pages, so the book is publicly accessible and easy to update.


