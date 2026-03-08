# Purpose-Based Workflow

This flowchart helps you navigate time series analysis based on your **analytical purpose**. Different objectives require different emphasis in the methodology.

---

## Quick Navigation


---


## 1. Forecasting Workflow

**Goal**: Predict future values with quantified uncertainty

### Workflow Diagram

```mermaid
graph TD
    START([DATA: Time Series]) --> HORIZON

    HORIZON{Forecast Horizon?}
    HORIZON -->|Short: 1-7 steps| SHORT_PREP
    HORIZON -->|Medium: weeks-months| MED_PREP
    HORIZON -->|Long: > 1 year| LONG_PREP

    SHORT_PREP[Emphasis: Recent dynamics<br/>High-order models]
    MED_PREP[Emphasis: Cycles + trends<br/>Seasonal models]
    LONG_PREP[Emphasis: Long-run trends<br/>Structural/causal models]

    SHORT_PREP --> DATA_PREP
    MED_PREP --> DATA_PREP
    LONG_PREP --> DATA_PREP

    DATA_PREP[Clean data: missing, outliers]
    DATA_PREP --> STATION

    STATION{ADF + KPSS<br/>Stationary?}
    STATION -->|No| DIFF[Difference until stationary]
    STATION -->|Yes| EXOG

    DIFF --> RETEST{Retest}
    RETEST -->|Still non-stat| DIFF
    RETEST -->|Stationary| EXOG

    EXOG{Known future<br/>covariates?}
    EXOG -->|Yes: calendar, weather| SARIMAX[SARIMAX model]
    EXOG -->|No| PURE_TS[Pure time series]

    SARIMAX --> MODEL_FIT
    PURE_TS --> ACF_CHECK

    ACF_CHECK[ACF/PACF analysis]
    ACF_CHECK --> MODEL_SELECT{Model type?}

    MODEL_SELECT -->|Simple| ARIMA[ARIMA/SARIMA]
    MODEL_SELECT -->|Complex nonlinear| ML[LSTM/Transformer]
    MODEL_SELECT -->|Ensemble| HYBRID[Hybrid: ARIMA + ML]

    ARIMA --> MODEL_FIT
    ML --> MODEL_FIT
    HYBRID --> MODEL_FIT

    MODEL_FIT[Fit model via MLE/GD]
    MODEL_FIT --> RESID_DIAG

    RESID_DIAG{Residuals white noise?<br/>Ljung-Box p > 0.05}
    RESID_DIAG -->|No: Autocorr remains| INC_ORDER[Increase order]
    RESID_DIAG -->|Yes| INTERVALS

    INC_ORDER --> MODEL_FIT

    INTERVALS[Generate prediction intervals<br/>Bootstrap or analytical]
    INTERVALS --> OOS

    OOS[Out-of-sample validation<br/>Rolling origin CV]
    OOS --> METRICS[RMSE, MAE, MAPE<br/>Coverage of intervals]

    METRICS --> ACCEPT{Performance<br/>acceptable?}
    ACCEPT -->|No| REMODEL[Try different model]
    ACCEPT -->|Yes| DEPLOY

    REMODEL --> MODEL_SELECT

    DEPLOY([Deploy with monitoring])
```

### Key Emphasis
- **Residual diagnostics**: Critical for valid prediction intervals
- **Out-of-sample testing**: In-sample fit is misleading
- **Interval coverage**: 95% CI should cover 95% of actuals
- **Parsimony**: Simpler models often forecast better

### Model Recommendations by Horizon
| Horizon | Recommended Approach |
|---------|---------------------|
| 1-7 steps | ARIMA, ETS, TBATS |
| 1-3 months | SARIMA, Prophet |
| 3-12 months | SARIMAX with exogenous |
| > 1 year | Structural models, causal |

---

## 2. Causal Analysis / Structural Inference

**Goal**: Determine if X causes Y, quantify effect size

### Workflow Diagram

```mermaid
graph TD
    START([DATA]) --> EXPERIMENT

    EXPERIMENT{Experimental data?<br/>Randomization?}
    EXPERIMENT -->|Yes: RCT| INTERV_ANALYSIS
    EXPERIMENT -->|No: Observational| MULTI_CHECK

    INTERV_ANALYSIS[Intervention Analysis<br/>Before/after comparison]
    INTERV_ANALYSIS --> AUTOCORR_ADJ

    AUTOCORR_ADJ[Adjust for autocorrelation<br/>Newey-West SE]
    AUTOCORR_ADJ --> EFFECT_SIZE

    EFFECT_SIZE[Estimate effect + CI]
    EFFECT_SIZE --> SENSITIVITY

    MULTI_CHECK{Multiple time series?}
    MULTI_CHECK -->|Yes| GRANGER
    MULTI_CHECK -->|No: Single series| SYNTHETIC

    GRANGER[Granger Causality Test<br/>Ch 6]
    GRANGER --> VAR_MODEL

    VAR_MODEL{Cointegrated?<br/>Johansen test}
    VAR_MODEL -->|Yes| VECM[VECM: Long-run equilibrium]
    VAR_MODEL -->|No| VAR[VAR: Short-run dynamics]

    VECM --> IRF
    VAR --> IRF

    IRF[Impulse Response Functions<br/>Trace shock propagation]
    IRF --> INSTANT{Instantaneous<br/>effects?}

    INSTANT -->|Yes| SVAR[SVAR: Identify structural shocks<br/>Ch 6]
    INSTANT -->|No| SENSITIVITY

    SVAR --> SENSITIVITY

    SYNTHETIC[Synthetic Control Method<br/>Construct counterfactual]
    SYNTHETIC --> PLACEBO

    PLACEBO[Placebo tests<br/>Falsification checks]
    PLACEBO --> SENSITIVITY

    SENSITIVITY[Sensitivity Analysis<br/>Alternative specifications]
    SENSITIVITY --> INTERPRET

    INTERPRET{Strong identification?<br/>Robust across specs?}
    INTERPRET -->|Yes| CAUSAL_CLAIM
    INTERPRET -->|No: Weak| ASSOC_ONLY

    CAUSAL_CLAIM([Report CAUSAL effect])
    ASSOC_ONLY([Report ASSOCIATION only])
```

### Critical Requirements
1. **Identification**: Exogeneity assumption must hold
2. **Stationarity**: Test cointegration for multivariate
3. **Robustness**: Results must hold across specifications
4. **Falsification**: Placebo tests, pre-trends parallel

### Common Pitfalls
- **Granger ≠ causation**: Prediction doesn't imply causation
- **Omitted variables**: Confounders bias estimates
- **Spurious regression**: Non-stationary series can show false correlations

---

## 3. Signal Extraction / Denoising

**Goal**: Separate true signal from noise

### Workflow Diagram

```mermaid
graph TD
    START([DATA: Noisy signal]) --> NOISE_TYPE

    NOISE_TYPE{Noise characteristics?}
    NOISE_TYPE -->|White noise| FREQ_FILTER
    NOISE_TYPE -->|Colored noise| ADAPT_FILTER
    NOISE_TYPE -->|Outliers + noise| ROBUST_FIRST

    ROBUST_FIRST[Robust filtering<br/>Median filter, Hampel]
    ROBUST_FIRST --> FREQ_FILTER

    FREQ_FILTER[FFT Analysis<br/>Identify signal band]
    FREQ_FILTER --> DESIGN_FILTER

    DESIGN_FILTER{Filter type?}
    DESIGN_FILTER -->|Known signal freq| BANDPASS[Band-pass filter]
    DESIGN_FILTER -->|Low-freq signal| LOWPASS[Low-pass filter]
    DESIGN_FILTER -->|Remove specific freq| NOTCH[Notch filter]

    BANDPASS --> APPLY_FILTER
    LOWPASS --> APPLY_FILTER
    NOTCH --> APPLY_FILTER

    ADAPT_FILTER[Adaptive filtering<br/>Wiener, Kalman]
    ADAPT_FILTER --> STATE_SPACE

    STATE_SPACE[State-Space Model<br/>Kalman Filter]
    STATE_SPACE --> APPLY_FILTER

    APPLY_FILTER[Apply filter to data]
    APPLY_FILTER --> CHECK_SNR

    CHECK_SNR{SNR improved?<br/>Compare spectra}
    CHECK_SNR -->|No| ADJUST[Adjust filter params]
    CHECK_SNR -->|Yes| VALIDATE

    ADJUST --> DESIGN_FILTER

    VALIDATE[Visual + quantitative check<br/>Preserve signal features?]
    VALIDATE --> DEPLOY_FILTER

    DEPLOY_FILTER([Filtered signal])
```

### Filter Selection Guide
| Noise Type | Recommended Method |
|------------|-------------------|
| White noise, known signal freq | Butterworth band-pass |
| Unknown signal freq | Wiener filter |
| Non-stationary noise | Kalman filter |
| Outliers + noise | Median → Band-pass |
| 1/f noise | Wavelet denoising |

---

## 4. Change-Point Detection

**Goal**: Identify times when statistical properties change

### Workflow Diagram

```mermaid
graph TD
    START([DATA]) --> MODE

    MODE{Online or offline?}
    MODE -->|Online: Real-time| SEQUENTIAL
    MODE -->|Offline: Retrospective| BATCH

    SEQUENTIAL[Sequential Detection<br/>CUSUM, Page-Hinkley]
    SEQUENTIAL --> THRESHOLD_SEQ

    THRESHOLD_SEQ{Set threshold<br/>Trade-off: False alarm vs delay}
    THRESHOLD_SEQ --> MONITOR

    MONITOR[Monitor statistic]
    MONITOR --> DETECT_SEQ{Threshold<br/>exceeded?}
    DETECT_SEQ -->|Yes| ALARM[Raise alarm]
    DETECT_SEQ -->|No| MONITOR

    ALARM --> VALIDATE_CHANGE

    BATCH[Batch Methods<br/>PELT, Binary Segmentation]
    BATCH --> PENALTY

    PENALTY{Number of<br/>change points?}
    PENALTY -->|Known| FIT_MODEL
    PENALTY -->|Unknown| SELECT_PEN[Select penalty via BIC]

    SELECT_PEN --> FIT_MODEL

    FIT_MODEL[Fit change point model]
    FIT_MODEL --> DETECT_BATCH[Detect change points]

    DETECT_BATCH --> VALIDATE_CHANGE

    VALIDATE_CHANGE[Visual inspection<br/>Domain knowledge check]
    VALIDATE_CHANGE --> TYPE_CHANGE

    TYPE_CHANGE{Type of change?}
    TYPE_CHANGE -->|Mean shift| SEGMENT_MEAN
    TYPE_CHANGE -->|Variance shift| SEGMENT_VAR
    TYPE_CHANGE -->|Regime change| SEGMENT_DIST

    SEGMENT_MEAN[Model each segment<br/>separately]
    SEGMENT_VAR[Heteroskedastic model]
    SEGMENT_DIST[Markov-switching model]

    SEGMENT_MEAN --> DEPLOY_CPD
    SEGMENT_VAR --> DEPLOY_CPD
    SEGMENT_DIST --> DEPLOY_CPD

    DEPLOY_CPD([Change points identified])
```

### Method Selection
| Context | Method |
|---------|--------|
| Online detection | CUSUM, EWMA charts |
| Offline, single change | CUSUM on full data |
| Offline, multiple changes | PELT, Binary Segmentation |
| Multivariate | E-divisive, Bayesian |

---

## 5. Anomaly / Regime Detection

**Goal**: Identify unusual patterns or state switches

### Workflow Diagram

```mermaid
graph TD
    START([DATA]) --> ANOMALY_TYPE

    ANOMALY_TYPE{Type of anomaly?}
    ANOMALY_TYPE -->|Point: Single outlier| POINT_METHOD
    ANOMALY_TYPE -->|Contextual: Unusual in context| CONTEXTUAL_METHOD
    ANOMALY_TYPE -->|Collective: Unusual pattern| COLLECTIVE_METHOD

    POINT_METHOD[Statistical outlier detection<br/>Modified z-score]
    POINT_METHOD --> THRESHOLD_POINT

    THRESHOLD_POINT[Set threshold: |z| > 3 or 4]
    THRESHOLD_POINT --> DETECT_POINT

    DETECT_POINT[Flag outliers]
    DETECT_POINT --> VALIDATE_ANOM

    CONTEXTUAL_METHOD[Model normal behavior]
    CONTEXTUAL_METHOD --> FIT_MODEL_CONTEXT

    FIT_MODEL_CONTEXT{Model type?}
    FIT_MODEL_CONTEXT -->|Statistical| ARIMA_RESID[ARIMA residuals]
    FIT_MODEL_CONTEXT -->|ML| AUTOENCODER[LSTM Autoencoder]

    ARIMA_RESID --> RESID_THRESHOLD
    AUTOENCODER --> RESID_THRESHOLD

    RESID_THRESHOLD[Set threshold on reconstruction error]
    RESID_THRESHOLD --> DETECT_CONTEXT

    DETECT_CONTEXT[Flag deviations]
    DETECT_CONTEXT --> VALIDATE_ANOM

    COLLECTIVE_METHOD[Pattern-based detection<br/>Matrix Profile]
    COLLECTIVE_METHOD --> DISCORD

    DISCORD[Find discords<br/>Most unusual subsequences]
    DISCORD --> VALIDATE_ANOM

    VALIDATE_ANOM{Labeled data<br/>available?}
    VALIDATE_ANOM -->|Yes| SUPERVISED[Supervised learning<br/>Improve detection]
    VALIDATE_ANOM -->|No| UNSUPERVISED[Unsupervised<br/>Monitor false positives]

    SUPERVISED --> RETRAIN
    UNSUPERVISED --> RETRAIN

    RETRAIN[Periodic retraining<br/>Concept drift]
    RETRAIN --> DEPLOY_AD

    DEPLOY_AD([Anomaly detection deployed])
```

### Threshold Selection
Balance false positives vs false negatives based on cost:
- **High cost of missing anomaly** → Lower threshold (more sensitive)
- **High cost of false alarm** → Higher threshold (more specific)

---

## 6. Decomposition (Trend-Cycle-Seasonality)

**Goal**: Separate time series into interpretable components

### Workflow Diagram

```mermaid
graph TD
    START([DATA]) --> SEASONAL_CHECK

    SEASONAL_CHECK{Seasonality present?}
    SEASONAL_CHECK -->|Yes| PERIOD_KNOWN
    SEASONAL_CHECK -->|No| TREND_ONLY

    PERIOD_KNOWN{Period known?}
    PERIOD_KNOWN -->|Yes: s = 12, 52, etc.| METHOD_SELECT
    PERIOD_KNOWN -->|No| FFT_PERIOD

    FFT_PERIOD[FFT to detect period<br/>Ch 5]
    FFT_PERIOD --> METHOD_SELECT

    METHOD_SELECT{Decomposition method?}
    METHOD_SELECT -->|Additive| STL_ADD[STL decomposition<br/>Additive]
    METHOD_SELECT -->|Multiplicative| STL_MULT[STL decomposition<br/>Multiplicative]
    METHOD_SELECT -->|Both| X13[X-13ARIMA-SEATS]

    STL_ADD --> EXTRACT_COMPONENTS
    STL_MULT --> EXTRACT_COMPONENTS
    X13 --> EXTRACT_COMPONENTS

    TREND_ONLY[Trend extraction only<br/>HP filter, LOESS]
    TREND_ONLY --> EXTRACT_COMPONENTS

    EXTRACT_COMPONENTS[Extract: Trend, Seasonal, Residual]
    EXTRACT_COMPONENTS --> CHECK_RESID

    CHECK_RESID{Residuals<br/>white noise?}
    CHECK_RESID -->|No: Structure remains| REFINE[Refine decomposition]
    CHECK_RESID -->|Yes| ANALYZE

    REFINE --> METHOD_SELECT

    ANALYZE[Analyze each component<br/>separately]
    ANALYZE --> INTERPRET

    INTERPRET{Purpose of<br/>decomposition?}
    INTERPRET -->|Understand patterns| REPORT_DESC
    INTERPRET -->|Deseasonalize| RETURN_DESEAS
    INTERPRET -->|Forecast each| FORECAST_COMP

    REPORT_DESC([Report descriptive analysis])
    RETURN_DESEAS([Return deseasonalized series])
    FORECAST_COMP[Forecast components<br/>then recombine]
    FORECAST_COMP --> DEPLOY_DECOMP

    DEPLOY_DECOMP([Decomposition complete])
```

### Method Selection
| Characteristic | Method |
|----------------|--------|
| Additive (constant seasonal amplitude) | STL additive |
| Multiplicative (seasonal amp ∝ level) | STL multiplicative or log + additive |
| Multiple seasonalities | TBATS, Prophet |
| Non-stationary trend | STL (robust) |
| Official statistics | X-13ARIMA-SEATS |

---

## 7. Feature Extraction for ML

**Goal**: Transform time series into feature vectors for classification/clustering

### Workflow Diagram

```mermaid
graph TD
    START([DATA: Time series]) --> TASK

    TASK{ML Task?}
    TASK -->|Classification| CLASS_FEATURES
    TASK -->|Clustering| CLUSTER_FEATURES
    TASK -->|Regression| REGR_FEATURES

    CLASS_FEATURES[Need discriminative features]
    CLUSTER_FEATURES[Need representative features]
    REGR_FEATURES[Need predictive features]

    CLASS_FEATURES --> FEATURE_TYPES
    CLUSTER_FEATURES --> FEATURE_TYPES
    REGR_FEATURES --> FEATURE_TYPES

    FEATURE_TYPES[Feature categories]
    FEATURE_TYPES --> TIME_FEAT

    TIME_FEAT[Time domain features<br/>Mean, std, skew, kurtosis]
    TIME_FEAT --> FREQ_FEAT

    FREQ_FEAT[Frequency domain features<br/>FFT peaks, spectral entropy]
    FREQ_FEAT --> AUTOCORR_FEAT

    AUTOCORR_FEAT[Autocorrelation features<br/>ACF values at lags]
    AUTOCORR_FEAT --> SHAPE_FEAT

    SHAPE_FEAT[Shape features<br/>Peaks, zero-crossings, slopes]
    SHAPE_FEAT --> COMPLEXITY_FEAT

    COMPLEXITY_FEAT[Complexity features<br/>Entropy, Lyapunov, DFA]
    COMPLEXITY_FEAT --> AUTO_VS_MANUAL

    AUTO_VS_MANUAL{Feature selection<br/>approach?}
    AUTO_VS_MANUAL -->|Automated| TSFRESH[tsfresh: 700+ features]
    AUTO_VS_MANUAL -->|Curated| CATCH22[Catch22: 22 canonical features]
    AUTO_VS_MANUAL -->|Domain-specific| MANUAL[Manual engineering]

    TSFRESH --> FEATURE_MATRIX
    CATCH22 --> FEATURE_MATRIX
    MANUAL --> FEATURE_MATRIX

    FEATURE_MATRIX[Feature matrix: N x M]
    FEATURE_MATRIX --> HIGH_DIM

    HIGH_DIM{Too many features?<br/>M > N/10?}
    HIGH_DIM -->|Yes| FEATURE_SELECT
    HIGH_DIM -->|No| TRAIN_MODEL

    FEATURE_SELECT{Selection method?}
    FEATURE_SELECT -->|Statistical| BORUTA[Boruta]
    FEATURE_SELECT -->|L1 regularization| LASSO[Lasso]
    FEATURE_SELECT -->|Dimensionality reduction| PCA_TS[PCA or fPCA]

    BORUTA --> TRAIN_MODEL
    LASSO --> TRAIN_MODEL
    PCA_TS --> TRAIN_MODEL

    TRAIN_MODEL[Train ML model<br/>RF, XGBoost, SVM, NN]
    TRAIN_MODEL --> EVAL

    EVAL[Cross-validation<br/>Time-respecting splits]
    EVAL --> PERFORMANCE

    PERFORMANCE{Performance<br/>acceptable?}
    PERFORMANCE -->|No| REFINE_FEAT[Refine features<br/>or add domain knowledge]
    PERFORMANCE -->|Yes| DEPLOY_ML

    REFINE_FEAT --> FEATURE_TYPES

    DEPLOY_ML([ML model deployed])
```

### Feature Libraries
- **tsfresh**: 700+ features, automated extraction
- **Catch22**: 22 canonical features, computationally efficient
- **tsfeatures** (R): Interpretable summary features

---

## 8. Spectral Analysis and System Identification

**Goal**: Characterize frequency content and identify system dynamics

### Workflow Diagram

```mermaid
graph TD
    START([DATA: Signal]) --> DETREND_FIRST

    DETREND_FIRST[Remove trend<br/>Trends obscure spectrum]
    DETREND_FIRST --> WINDOWING

    WINDOWING[Apply window function<br/>Hanning, Hamming]
    WINDOWING --> FFT_COMPUTE

    FFT_COMPUTE[Compute FFT + PSD]
    FFT_COMPUTE --> SPECTRUM_TYPE

    SPECTRUM_TYPE{Spectrum type?}
    SPECTRUM_TYPE -->|Single series| UNIVAR_SPEC
    SPECTRUM_TYPE -->|Two series| BIVAR_SPEC

    UNIVAR_SPEC[Power Spectral Density]
    UNIVAR_SPEC --> INTERPRET_PSD

    INTERPRET_PSD{Spectral shape?}
    INTERPRET_PSD -->|Flat| WHITE_NOISE_SPEC[White noise]
    INTERPRET_PSD -->|1/f decay| PINK_NOISE[Pink/red noise]
    INTERPRET_PSD -->|Peaks| PERIODIC[Periodic components]
    INTERPRET_PSD -->|Band-limited| RESONANCE[Resonance/filtering]

    WHITE_NOISE_SPEC --> REPORT_SPEC
    PINK_NOISE --> REPORT_SPEC
    PERIODIC --> PEAK_ANALYSIS
    RESONANCE --> REPORT_SPEC

    PEAK_ANALYSIS[Peak detection<br/>Fisher's g-test]
    PEAK_ANALYSIS --> SIGNIFICANT_PEAKS

    SIGNIFICANT_PEAKS{Peaks<br/>significant?}
    SIGNIFICANT_PEAKS -->|Yes| RECORD_FREQS[Record frequencies<br/>Convert to periods]
    SIGNIFICANT_PEAKS -->|No| REPORT_SPEC

    RECORD_FREQS --> HARMONIC[Add harmonic regressors<br/>to time-domain model]
    HARMONIC --> REPORT_SPEC

    BIVAR_SPEC[Cross-spectrum analysis]
    BIVAR_SPEC --> COHERENCE

    COHERENCE[Coherence function<br/>Frequency-domain correlation]
    COHERENCE --> PHASE

    PHASE[Phase spectrum<br/>Lead-lag relationships]
    PHASE --> GRANGER_FREQ[Frequency-domain<br/>Granger causality]

    GRANGER_FREQ --> SYSTEM_ID

    SYSTEM_ID{System identification<br/>needed?}
    SYSTEM_ID -->|Yes| TRANSFER_FUNC[Estimate transfer function<br/>H(f) = Y(f)/X(f)]
    SYSTEM_ID -->|No| REPORT_SPEC

    TRANSFER_FUNC --> POLES_ZEROS[Poles and zeros<br/>Stability analysis]
    POLES_ZEROS --> REPORT_SPEC

    REPORT_SPEC([Spectral analysis complete])
```

### Applications
- **Signal processing**: Filter design, noise characterization
- **Control systems**: Stability analysis, transfer functions
- **Economics**: Business cycle frequencies, co-movements
- **Geophysics**: Seismic analysis, tidal harmonics

---

## Summary: Purpose-Based Decision Matrix

| Purpose | Primary Domain | Key Test | Model Family |
|---------|---------------|----------|-------------|
| **Forecasting** | Time | Ljung-Box, AIC/BIC | ARIMA, SARIMA, ML |
| **Causal inference** | Time | Granger, Johansen | VAR, VECM, SVAR |
| **Signal extraction** | Frequency | SNR, spectral comparison | Filters, Kalman |
| **Change detection** | Time | CUSUM, BIC | PELT, CUSUM |
| **Anomaly detection** | Both | Threshold tuning | Residuals, autoencoders |
| **Decomposition** | Time | White noise test | STL, X-13 |
| **Feature extraction** | Both | CV accuracy | tsfresh, Catch22 |
| **Spectral analysis** | Frequency | Fisher's g-test | FFT, coherence |

---

**[Previous: General Flowchart →](01-general-flowchart.md)** | **[Next: Representation-Based Workflow →](03-representation-workflow.md)** | **[Contents](../README.md)**
