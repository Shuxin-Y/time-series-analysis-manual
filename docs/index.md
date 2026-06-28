# Time Series Analysis Manual

!!! abstract "Preface"
    Time series analysis sits at the intersection of classical statistics, econometrics, signal processing, and modern machine learning. Each tradition has developed powerful tools, yet learners often encounter them in isolation — scattered across textbooks that emphasize one perspective at the expense of others.

    This manual is a modest attempt to bring these threads together in one place. It aims to offer a practical, test-driven workflow that respects the mathematical foundations while remaining accessible to practitioners. Where possible, we pair theory with working Python code, so that ideas can be tested and verified rather than taken on faith.

    No single reference can be comprehensive, and this one is no exception. We hope it serves as a useful starting point and companion for your work with temporal data — whether you are forecasting, diagnosing, or simply trying to understand the patterns hidden in a sequence of observations.

---

## Book Conventions

Throughout this book:

- **Mathematical notation** appears in collapsible blocks for clean reading
    - This book will use the conditional expectation form as the primary notation throughout, since it's the most general and is what modern econometrics papers default to.

- **Python code** is provided inline with expected output
- **Hypothesis tests** always state H₀ (null hypothesis) and interpretation rules
- **Decision rules** explicitly state thresholds (e.g., p-value < 0.05)
- **Warnings** highlight common mistakes and edge cases

---

## Book Structure

The manual is organized into focused chapters that build progressively:

### Core Content

<div class="annotate" markdown>

1. **[Introduction](00-introduction/logic-of-statistical-analysis.md)** - The model/estimator/test framework, when time series methods are needed, and how time series breaks the classical OLS assumptions
2. **[Flowcharts](01-master-flowchart/01-general-flowchart.md)** - Three comprehensive decision workflows (1)
3. **[Data Preparation](02-data-preparation/index.md)** - Cleaning, sampling, and quality checks
4. **[Exploratory Analysis](03-exploratory-analysis/index.md)** - Stationarity, distributions, temporal structure
5. **[Frequency Domain](04-frequency-domain/index.md)** - Spectral analysis, periodicities, filtering
6. **[Modelling](05-modelling/index.md)** - ARIMA, VAR, GARCH, state-space, and ML approaches
7. **[Feature Extraction](06-feature-extraction/index.md)** - Engineering features for machine learning
8. **[Validation & Deployment](07-validation-deployment/index.md)** - Testing, monitoring, and production systems

</div>

1.  The three flowcharts provide complementary views:
    - **General**: Complete econometric workflow from data to deployment
    - **Purpose-Based**: Organized by analytical goal (forecasting, causal analysis, etc.)
    - **Representation-Based**: Organized by mathematical domain (time, frequency, state-space, etc.)

### Reference Materials

- **[Appendices](appendices/index.md)** - Mathematical foundations, statistical tests reference, datasets, and resources

---

## Quick Start

=== "New to Time Series"
    
    1. Read the [Introduction](00-introduction/logic-of-statistical-analysis.md) to understand the framework
    2. Skim the [General Flowchart](01-master-flowchart/01-general-flowchart.md) for the big picture
    3. Follow the Guided Walkthrough (WIP) for detailed explanations
    4. Work through chapters 3-7 in order

=== "Have Specific Goals"

    - Forecasting → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#1-forecasting-workflow)
    - Causal Analysis → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#2-causal-analysis-structural-inference)
    - Anomaly Detection → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#5-anomaly-regime-detection)
    - Feature Engineering → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#7-feature-extraction-for-ml)

=== "Know Your Domain"

    - Finance → [Representation Workflow](01-master-flowchart/03-representation-workflow.md#1-time-domain-representation)
    - Signal Processing → [Representation Workflow](01-master-flowchart/03-representation-workflow.md#2-frequency-domain-representation)


=== "Want Examples"

    - Browse code examples in each chapter
    - Check [Python Setup](appendices/C-python-environment-setup.md) for environment configuration
    - Code directory (WIP)

---
## Techniques This Book Covers

=== "Theory & Inference"

    === "1. Math Foundations"

        Real analysis, measure theory, probability theory, stochastic processes, linear algebra, ergodicity, stationarity (strict vs. weak), mixing conditions, LLN, CLT for dependent data, delta method, functional analysis.

    === "4. Estimation"

        MOM, OLS, MLE (exact/conditional), QMLE, GMM, Bayesian estimation (MCMC, Gibbs, Metropolis-Hastings), Yule-Walker equations, Whittle likelihood.

    === "5. Hypothesis Testing"

        - **Unit Root:** ADF, KPSS, PP, DF-GLS, Zivot-Andrews (with structural breaks)
        - **Cointegration:** Engle-Granger, Johansen, ARDL bounds
        - **Causality:** Granger, Sims, Toda-Yamamoto
        - **Structural Breaks:** Chow test, CUSUM, Bai-Perron
        - **Serial Correlation:** Breusch-Godfrey, Ljung-Box, Durbin-Watson, White test
        - **Normality:** Jarque-Bera
        - **Bootstrap:** block, sieve

    === "6. Model Selection"

        - **Information criteria:** AIC, BIC, HQIC
        - **Cross-validation:** walk-forward, rolling
        - **Residual diagnostics:** ACF/PACF, Q-stats
        - **Forecast evaluation:** MAE, RMSE, MAPE, MASE
        - **Forecast comparison:** Diebold-Mariano test, reality check, model confidence sets (Hansen)

    === "25. Simulation"

        Monte Carlo, block/stationary/sieve bootstrap, simulation-based inference, numerical MLE, EM algorithm for state-space models, ABC for intractable likelihoods, variational inference.

=== "Core Models"

    === "2. Fundamentals"

        Trend, seasonality, cyclicality, residual noise. Stationarity testing (ADF, KPSS) and transformation (differencing, log). ACF/PACF diagnostics.

    === "3. Classical"

        - **AR/MA:** AR, MA, ARMA, ARIMA, SARIMA, ARIMAX/SARIMAX
        - **Exponential Smoothing:** SES, DES, TES, ETS
        - **Regression:** DLM, ADL, transfer function models, intervention analysis
        - **Decomposition:** Classical Decomposition, STL, X-11/X-13-ARIMA-SEATS
        - **Spectral:** FFT, periodogram, PSD

    === "7. Long Memory"

        ARFIMA, fractional Brownian motion, Hurst exponent, GPH estimator, local Whittle estimator.

    === "8. Nonlinear"

        - **Threshold:** TAR, SETAR, MTAR
        - **Smooth Transition:** STAR, LSTAR, ESTAR
        - **Regime-Switching:** Markov-Switching (Hamilton)
        - **Bilinear:** bilinear AR models
        - **Nonparametric/semiparametric:** kernel smoothing, local polynomial regression
        - **Chaos and nonlinear dynamics:** Lyapunov exponents, BDS test

    === "9. Multivariate"

        - **Core multivariate:** VAR, SVAR (short-run/long-run), VECM
        - **Factor models:** SFM, DFM, Approximate Factor Models
        - **Regularisation:** PCA, LASSO-VAR, Ridge-VAR, Elastic Net
        - **Graphical models:** sparse precision matrices
        - **Panel time series:** fixed/random effects, pooled estimators
        - **Tensor methods:** matrix/tensor autoregression

    === "10. Volatility"

        - **ARCH family:** ARCH, GARCH, IGARCH, FIGARCH, APARCH
        - **Asymmetric:** EGARCH, GJR-GARCH, TGARCH
        - **Multivariate GARCH:** DCC-GARCH, BEKK-GARCH, CCC-GARCH
        - **Stochastic volatility:** SV models
        - **High-frequency:** realised volatility, HF econometrics
        - **Jump models:** jump diffusion
        - **Risk measures:** VaR, Expected Shortfall
        - **Dependence:** copula-based modelling
        - **Extreme value theory:** GEV, GPD, peaks-over-threshold, extremal index
        - **Rough volatility:** rough Heston, fBM-driven models, rough Bergomi

=== "Specialized Models"

    === "11. State-Space"

        General linear Gaussian state-space models, Kalman filter/smoother, EKF, UKF, particle filters (SMC), HMM, DLM (West & Harrison framework), BSTS.

    === "12. Bayesian"

        BVAR (Minnesota prior, natural conjugate prior), Bayesian ARIMA, DBN, posterior predictive distributions, Bayesian model comparison (Bayes factors, WAIC, LOO-CV), TVP-VAR, sequential Bayesian updating, Bayesian forecasting with structural breaks.

    === "15. Continuous-Time"

        OU process, Ito diffusions, geometric Brownian motion, CARMA, Levy-driven processes, jump-diffusion models, numerical methods for SDEs (Euler-Maruyama, Milstein), likelihood inference for diffusions, signature methods (rough path theory).

    === "16. Count & Categorical"

        - **Integer-valued:** INAR, PAR, INGARCH, negative binomial autoregression
        - **Categorical/qualitative:** Markov chains for discrete states, autoregressive logit/probit, multinomial time series
        - **Compositional:** Dirichlet regression, log-ratio transforms for constrained series

    === "17. Point Processes"

        Poisson process, Cox process, Hawkes process (self-exciting), renewal processes, temporal point process models, neural point processes, intensity estimation, Marked point processes.

=== "Representations & Signals"

    === "13. Spectral Analysis"

        DFT, PSD (parametric/nonparametric), periodogram, smoothed periodogram, Welch's method, cross-spectral analysis, coherence, phase spectrum, Wavelet analysis (DWT, MODWT, wavelet decomposition), HHT, EMD, Bandpass filtering (HP/BK/CF filters).

    === "14. Functional & HF"

        Functional time series (Ramsay-Silverman framework), intraday seasonality modeling, irregularly spaced time series, Duration models (ACD), order book modelling, UHF data, survival analysis and reliability (Cox PH, hazard functions, censored time series).

    === "19. Classification & Anomaly"

        - **Classification:** DTW + k-NN, shapelets, ROCKET/MiniRocket, InceptionTime, time series kernels (GAK)
        - **Clustering:** k-means with DTW, kernel k-means, spectral clustering for time series
        - **Symbolic representations:** SAX, SFA, symbolic dynamics
        - **Anomaly detection algorithms:** BOCPD, PELT, matrix profile, isolation forests for time series, autoencoders, VAE
        - **Topological methods:** persistent homology, TDA for time series shape analysis
        - **Data augmentation:** window slicing, magnitude/time warping, synthetic oversampling

    === "20. Spatio-Temporal"

        - **Spatial econometrics:** spatial panel VAR, spatial error/lag models with temporal dependence
        - **Geostatistical:** spatio-temporal kriging, Gaussian process spatio-temporal models
        - **Graph-based:** graph signal processing, STGNN, DCRNN, spatio-temporal attention networks
        - **Network time series:** time series on dynamic/evolving graphs, network autoregression
        - **Point processes:** spatio-temporal point processes

=== "ML, Forecasting & Practice"

    === "18. ML & Deep Learning"

        - **Classical ML:** Random Forests, XGBoost, LightGBM
        - **Gaussian processes:** GP regression
        - **Reservoir computing:** Echo State Networks, Liquid State Machines
        - **Recurrent networks:** RNN, LSTM, GRU
        - **Convolutional:** TCN
        - **Transformers:** Informer, Autoformer, PatchTST, TimesFM
        - **State-space sequence models:** S4, S5, Mamba
        - **Foundation models:** Chronos, Lag-Llama, Moirai, TimeGPT, MOMENT
        - **Neural forecasters:** N-BEATS, N-HiTS, TiDE
        - **Generative:** diffusion models for time series
        - **Hybrid:** ARIMA + NN, residual modelling
        - **Uncertainty quantification:** conformal prediction
        - **Interpretability:** SHAP for temporal features, attention visualization, counterfactual explanations

    === "21. Causal Inference"

        Granger causality (linear/nonlinear), CCM, transfer entropy, structural causal models (PCMCI, DYNOTEARS), do-calculus and Pearl's framework for temporal data, causal discovery from interventions, interrupted time series, DiD, synthetic control.

    === "22. Forecasting"

        Point/interval/density forecasting, forecast combination (simple average, BMA, optimal combination), hierarchical and grouped time series forecasting (reconciliation -- MinT, BU, TD), probabilistic forecasting (quantile regression, conformal intervals, GAMLSS), distributional regression, long-horizon forecasting, nowcasting (mixed-frequency models, MIDAS), forecast rationality testing, M-competition benchmarks and lessons (M4/M5), zero-shot forecasting evaluation, communicating uncertainty to non-technical stakeholders.

    === "23. Online & Adaptive"

        Online gradient descent for forecasting, adaptive Kalman filters, exponentially weighted methods, concept drift detection, continual/incremental learning, multi-task and multi-output forecasting with shared representations, bandit algorithms for adaptive model selection.

    === "24. Robust & Nonparametric"

        M-estimators, nonparametric PSD, nonparametric regression, rank-based tests, QAR, optimal transport for time series (Wasserstein distance, Sliced Wasserstein).

    === "26. Applied Domains"

        - **Macroeconometrics:** business cycles, DSGE, monetary policy
        - **Financial econometrics:** asset pricing, risk, portfolio optimisation
        - **Climate/environmental:** climate modelling, anomaly detection
        - **Epidemiology:** surveillance, epidemic modelling (SIR/SEIR with time series)
        - **Neuroscience:** EEG/fMRI, spike trains, brain connectivity
        - **Signal processing:** control systems, communications
        - **Energy:** demand/price forecasting
        - **Supply chain/retail:** demand sensing, inventory optimisation
        - **IoT/sensor networks:** predictive maintenance, fault detection
        - **Audio/speech:** spectrogram analysis, WaveNet
        - **MLOps for time series:** model monitoring, retraining policies, drift detection in production
        - **Privacy-preserving methods:** federated learning for sequential data, differential privacy
        - **Ethics and fairness:** accountability in forecasting, bias in temporal predictions


---

## The Python Stack You'll Use

| Purpose | Library |
|---|---|
| Data handling | `pandas` |
| Classical models (ARIMA, ETS, VAR) | `statsmodels` |
| Prophet | `prophet` |
| ML-based forecasting | `sktime`, `darts` |
| Deep learning | `pytorch-forecasting`, `neuralforecast` |
| Visualization | `matplotlib`, `plotly` |

---
## Citation

If you use this manual in your research or work, please cite:

```bibtex
@book{timeseries2024,
  title={Time Series Analysis Manual: A Comprehensive Practical Guide},
  author={Yang Shuxin},
  year={2025},
  publisher={[Publisher]},
  url={https://Shuxin-Y.github.io/time-series-analysis-manual}
}
```

---

## License

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

<!-- Abbreviation definitions — ordered by "What This Book Covers" sections 1–26 -->

<!-- 1. Mathematical and Statistical Foundations -->
*[LLN]: Law of Large Numbers
*[CLT]: Central Limit Theorem

<!-- 2. Time Series Fundamentals -->
*[ADF]: Augmented Dickey-Fuller test
*[KPSS]: Kwiatkowski-Phillips-Schmidt-Shin test
*[ACF]: Autocorrelation Function
*[PACF]: Partial Autocorrelation Function

<!-- 3. Core Classical Models — AR/MA -->
*[AR]: Autoregressive
*[MA]: Moving Average
*[ARMA]: Autoregressive Moving Average
*[ARIMA]: Autoregressive Integrated Moving Average
*[SARIMA]: Seasonal ARIMA
*[ARIMAX]: ARIMA with exogenous variables
*[SARIMAX]: Seasonal ARIMA with exogenous variables
<!-- 3. Core Classical Models — Exponential Smoothing -->
*[SES]: Simple Exponential Smoothing
*[DES]: Double Exponential Smoothing (Holt's Linear Trend)
*[TES]: Triple Exponential Smoothing (Holt-Winters)
*[ETS]: Error, Trend, Seasonality framework
<!-- 3. Core Classical Models — Regression -->
*[DLM]: Distributed Lag Model
*[ADL]: Autoregressive Distributed Lag
<!-- 3. Core Classical Models — Decomposition -->
*[STL]: Seasonal-Trend decomposition using LOESS
<!-- 3. Core Classical Models — Spectral -->
*[FFT]: Fast Fourier Transform
*[PSD]: Power Spectral Density

<!-- 4. Estimation Theory -->
*[MOM]: Method of Moments
*[OLS]: Ordinary Least Squares
*[MLE]: Maximum Likelihood Estimation
*[QMLE]: Quasi-Maximum Likelihood Estimation
*[GMM]: Generalized Method of Moments
*[MCMC]: Markov Chain Monte Carlo
*[Whittle likelihood]: frequency domain estimation

<!-- 5. Inference and Hypothesis Testing — Unit Root -->
*[PP]: Phillips-Perron test
*[DF-GLS]: Dickey-Fuller Generalized Least Squares
<!-- 5. Inference and Hypothesis Testing — Cointegration -->
*[ARDL]: Autoregressive Distributed Lag
<!-- 5. Inference and Hypothesis Testing — Structural Breaks -->
*[CUSUM]: Cumulative Sum test

<!-- 6. Model Selection and Validation -->
*[AIC]: Akaike Information Criterion
*[BIC]: Bayesian Information Criterion
*[HQIC]: Hannan-Quinn Information Criterion
*[MAE]: Mean Absolute Error
*[RMSE]: Root Mean Squared Error
*[MAPE]: Mean Absolute Percentage Error
*[MASE]: Mean Absolute Scaled Error
*[MCS]: Model Confidence Set

<!-- 7. Long Memory and Fractional Integration -->
*[ARFIMA]: Autoregressive Fractionally Integrated Moving Average
*[GPH]: Geweke and Porter-Hudak estimator

<!-- 8. Nonlinear Models — Threshold -->
*[TAR]: Threshold Autoregressive
*[SETAR]: Self-Exciting Threshold Autoregressive
*[MTAR]: Momentum Threshold Autoregressive
<!-- 8. Nonlinear Models — Smooth Transition -->
*[STAR]: Smooth Transition Autoregressive
*[LSTAR]: Logistic STAR
*[ESTAR]: Exponential STAR
<!-- 8. Nonlinear Models — Chaos -->
*[BDS]: Brock-Dechert-Scheinkman test

<!-- 9. Multivariate and High-Dimensional -->
*[VAR]: Vector Autoregression
*[SVAR]: Structural Vector Autoregression
*[VECM]: Vector Error Correction Model
*[SFM]: Static Factor Model
*[DFM]: Dynamic Factor Model
*[PCA]: Principal Component Analysis
*[LASSO]: Least Absolute Shrinkage and Selection Operator

<!-- 10. Volatility and Financial Econometrics — ARCH Family -->
*[ARCH]: Autoregressive Conditional Heteroskedasticity
*[GARCH]: Generalized ARCH
*[IGARCH]: Integrated GARCH
*[FIGARCH]: Fractionally Integrated GARCH
*[APARCH]: Asymmetric Power ARCH
<!-- 10. Volatility and Financial Econometrics — Asymmetric -->
*[EGARCH]: Exponential GARCH
*[TGARCH]: Threshold GARCH
<!-- 10. Volatility and Financial Econometrics — Multivariate GARCH -->
*[DCC]: Dynamic Conditional Correlation
*[BEKK]: Baba-Engle-Kraft-Kroner model
*[CCC]: Constant Conditional Correlation
<!-- 10. Volatility and Financial Econometrics — Other -->
*[SV]: Stochastic Volatility
*[HF]: High-Frequency
*[VaR]: Value-at-Risk
<!-- 10. Volatility and Financial Econometrics — EVT -->
*[GEV]: Generalized Extreme Value distribution
*[GPD]: Generalized Pareto Distribution
<!-- 10. Volatility and Financial Econometrics — Rough Volatility -->
*[fBM]: fractional Brownian motion

<!-- 11. State-Space Models and Filtering -->
*[EKF]: Extended Kalman Filter
*[UKF]: Unscented Kalman Filter
*[SMC]: Sequential Monte Carlo
*[HMM]: Hidden Markov Model
*[DLM]: Dynamic Linear Model (West-Harrison)
*[BSTS]: Bayesian Structural Time Series

<!-- 12. Bayesian Time Series -->
*[BVAR]: Bayesian Vector Autoregression
*[DBN]: Dynamic Bayesian Network
*[WAIC]: Widely Applicable Information Criterion
*[LOO-CV]: Leave-One-Out Cross-Validation
*[TVP-VAR]: Time-Varying Parameter VAR

<!-- 13. Frequency Domain and Spectral Analysis -->
*[DFT]: Discrete Fourier Transform
*[DWT]: Discrete Wavelet Transform
*[MODWT]: Maximal Overlap Discrete Wavelet Transform
*[HHT]: Hilbert-Huang Transform
*[EMD]: Empirical Mode Decomposition
*[HP]: Hodrick-Prescott filter
*[BK]: Baxter-King filter
*[CF]: Christiano-Fitzgerald filter

<!-- 14. Functional and High-Frequency Time Series -->
*[ACD]: Autoregressive Conditional Duration
*[UHF]: Ultra-High-Frequency
*[Cox PH]: Cox Proportional Hazards model

<!-- 15. Continuous-Time Models and SDEs -->
*[OU]: Ornstein-Uhlenbeck process
*[CARMA]: Continuous-time Autoregressive Moving Average
*[SDE]: Stochastic Differential Equation

<!-- 16. Count and Categorical Time Series -->
*[INAR]: Integer-valued Autoregressive
*[PAR]: Poisson Autoregression
*[INGARCH]: Integer-valued Generalized ARCH

<!-- 17. Point Processes and Event-Time Series -->

<!-- 18. Machine Learning and Deep Learning -->
*[SSM]: State-Space sequence Model
*[GP]: Gaussian Process
*[RNN]: Recurrent Neural Network
*[LSTM]: Long Short-Term Memory
*[GRU]: Gated Recurrent Unit
*[TCN]: Temporal Convolutional Network
*[NN]: Neural Network
*[SHAP]: SHapley Additive exPlanations

<!-- 19. Time Series Classification, Clustering, and Anomaly Detection -->
*[DTW]: Dynamic Time Warping
*[GAK]: Global Alignment Kernel
*[ROCKET]: RandOm Convolutional KErnel Transform
*[SAX]: Symbolic Aggregate approXimation
*[SFA]: Symbolic Fourier Approximation
*[BOCPD]: Bayesian Online Change Point Detection
*[PELT]: Pruned Exact Linear Time
*[VAE]: Variational Autoencoder
*[TDA]: Topological Data Analysis

<!-- 20. Spatio-Temporal Models -->
*[STGNN]: Spatio-Temporal Graph Neural Network
*[DCRNN]: Diffusion Convolutional Recurrent Neural Network

<!-- 21. Causal Inference -->
*[CCM]: Convergent Cross Mapping
*[PCMCI]: Peter and Clark Momentary Conditional Independence
*[DiD]: Difference-in-Differences

<!-- 22. Forecasting Theory and Practice -->
*[BMA]: Bayesian Model Averaging
*[BU]: Bottom-Up reconciliation
*[TD]: Top-Down reconciliation
*[MIDAS]: Mixed Data Sampling
*[GAMLSS]: Generalized Additive Models for Location, Scale and Shape

<!-- 23. Online Learning and Adaptive Methods -->

<!-- 24. Robust and Nonparametric Methods -->
*[QAR]: Quantile Autoregression

<!-- 25. Simulation and Computational Methods -->
*[EM]: Expectation-Maximisation
*[ABC]: Approximate Bayesian Computation

<!-- 26. Applied Domains -->
*[DSGE]: Dynamic Stochastic General Equilibrium
*[EEG]: Electroencephalography
*[fMRI]: Functional Magnetic Resonance Imaging
*[IoT]: Internet of Things

