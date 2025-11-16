# General Flowchart: Complete Econometric Workflow

This flowchart provides a comprehensive, step-by-step guide from raw data to validated model, following standard econometric practice.

---

## Quick Navigation

- **Phase 1** → [Data Acquisition & Inspection](#phase-1-data-acquisition--inspection)
- **Phase 2** → [Purpose Definition](#phase-2-purpose-definition)
- **Phase 3** → [Diagnostic Testing](#phase-3-diagnostic-testing)
- **Phase 4** → [Transformations & Actions](#phase-4-transformations--actions)
- **Phase 5** → [Further Diagnostics](#phase-5-further-diagnostics)
- **Phase 6** → [Domain Selection](#phase-6-domain-selection)
- **Phase 7** → [Model Selection](#phase-7-model-selection)
- **Phase 8** → [Estimation & Validation](#phase-8-estimation--validation)

---

## Complete Workflow Diagram

```mermaid
graph TD
    START([📊 RAW DATA]) --> INSPECT

    %% ===== PHASE 1: DATA =====
    INSPECT{Data Quality Check<br/>Missing? Irregular sampling?}
    INSPECT -->|Issues detected| CLEAN[🔧 Data Preparation<br/>Ch 3]
    INSPECT -->|Clean| PURPOSE

    CLEAN --> MISSING{Missing values?}
    MISSING -->|Yes: >5%| IMPUTE[Impute or Segment<br/>Ch 3.2]
    MISSING -->|No or <5%| SAMPLING

    IMPUTE --> SAMPLING{Sampling regular?}
    SAMPLING -->|Irregular| RESAMPLE[Resample/Align<br/>Ch 3.1]
    SAMPLING -->|Regular| OUTLIERS
    RESAMPLE --> OUTLIERS

    OUTLIERS{Outliers detected?<br/>|z| > 3?}
    OUTLIERS -->|Yes| FILTER[Filter/Replace<br/>Ch 3.2]
    OUTLIERS -->|No| PURPOSE
    FILTER --> PURPOSE

    %% ===== PHASE 2: PURPOSE =====
    PURPOSE{🎯 Analysis Purpose?}
    PURPOSE -->|Forecasting| DIST_CHECK
    PURPOSE -->|Causal inference| DIST_CHECK
    PURPOSE -->|Signal extraction| DIST_CHECK
    PURPOSE -->|Change detection| SPECIAL_CD[Change Point Detection<br/>Ch 4]
    PURPOSE -->|Anomaly detection| SPECIAL_AD[Anomaly Detection<br/>Ch 4]
    PURPOSE -->|Decomposition| SPECIAL_DC[Decomposition Methods<br/>Ch 4]
    PURPOSE -->|Feature extraction| SPECIAL_FE[Feature Engineering<br/>Ch 7]
    PURPOSE -->|Spectral analysis| FREQ_DIRECT[Frequency Domain<br/>Ch 5]

    SPECIAL_CD --> END_SPECIAL
    SPECIAL_AD --> END_SPECIAL
    SPECIAL_DC --> END_SPECIAL
    SPECIAL_FE --> END_SPECIAL
    FREQ_DIRECT --> END_SPECIAL
    END_SPECIAL([Specialized Workflow])

    %% ===== PHASE 3: DIAGNOSTIC TESTS =====
    DIST_CHECK[📈 Distributional Analysis<br/>Ch 4]
    DIST_CHECK --> NORMALITY

    NORMALITY{Shapiro-Wilk Test<br/>p < 0.05?}
    NORMALITY -->|Reject: Non-normal| CHECK_SKEW
    NORMALITY -->|Fail to reject: Normal| VAR_CHECK

    CHECK_SKEW{High skewness?<br/>|skew| > 1}
    CHECK_SKEW -->|Yes| TRANS_NEEDED[Flag: Transform needed]
    CHECK_SKEW -->|No: Heavy tails| TRANS_NEEDED
    TRANS_NEEDED --> VAR_CHECK

    VAR_CHECK{Rolling variance<br/>constant?}
    VAR_CHECK -->|No: Heteroskedastic| GARCH_FLAG[🚩 Flag: GARCH effects]
    VAR_CHECK -->|Yes: Homoskedastic| STATION_CHECK
    GARCH_FLAG --> STATION_CHECK

    STATION_CHECK[🔍 Stationarity Testing<br/>Ch 4]
    STATION_CHECK --> ADF_TEST

    ADF_TEST{ADF Test<br/>H₀: Unit root<br/>p < 0.05?}
    ADF_TEST -->|Reject H₀: Stationary| KPSS_TEST
    ADF_TEST -->|Fail to reject: Non-stat| KPSS_TEST

    KPSS_TEST{KPSS Test<br/>H₀: Stationary<br/>p < 0.05?}
    KPSS_TEST -->|Reject: Non-stat| DIFF_NEEDED
    KPSS_TEST -->|Fail to reject: Stat| CHECK_AGREEMENT

    CHECK_AGREEMENT{Both tests<br/>agree?}
    CHECK_AGREEMENT -->|Yes: Stationary| ACF_CHECK
    CHECK_AGREEMENT -->|Yes: Non-stationary| DIFF_NEEDED
    CHECK_AGREEMENT -->|No: Conflicting| VISUAL_TREND

    VISUAL_TREND{Visual trend<br/>present?}
    VISUAL_TREND -->|Yes| DIFF_NEEDED
    VISUAL_TREND -->|No| ACF_CHECK

    %% ===== PHASE 4: TRANSFORMATIONS =====
    DIFF_NEEDED[⚙️ Transformation Phase]
    DIFF_NEEDED --> APPLY_TRANS

    APPLY_TRANS{Type of<br/>non-stationarity?}
    APPLY_TRANS -->|Variance grows| LOG_TRANS[Log/Box-Cox<br/>Transform]
    APPLY_TRANS -->|Linear trend| DIFF_1[First Difference<br/>d=1]
    APPLY_TRANS -->|Seasonal pattern| SEAS_DIFF[Seasonal Difference<br/>D=1]
    APPLY_TRANS -->|Both| COMBINED_DIFF[Combined<br/>Transform + Diff]

    LOG_TRANS --> RETEST1
    DIFF_1 --> RETEST1
    SEAS_DIFF --> RETEST1
    COMBINED_DIFF --> RETEST1

    RETEST1{Retest ADF & KPSS}
    RETEST1 -->|Now stationary| ACF_CHECK
    RETEST1 -->|Still non-stationary| DIFF_2[Second difference<br/>or alternative]
    DIFF_2 --> ACF_CHECK

    %% ===== PHASE 5: FURTHER DIAGNOSTICS =====
    ACF_CHECK[📊 Autocorrelation Analysis<br/>Ch 4]
    ACF_CHECK --> LJUNG_BOX

    LJUNG_BOX{Ljung-Box Test<br/>H₀: No autocorr<br/>p < 0.05?}
    LJUNG_BOX -->|Fail to reject| WHITE_NOISE[✓ White Noise<br/>No model needed]
    LJUNG_BOX -->|Reject: Autocorr exists| ACF_PATTERN

    WHITE_NOISE --> END_SUCCESS

    ACF_PATTERN{ACF/PACF<br/>Pattern?}
    ACF_PATTERN -->|ACF cuts, PACF decays| MA_FLAG[MA(q) process]
    ACF_PATTERN -->|PACF cuts, ACF decays| AR_FLAG[AR(p) process]
    ACF_PATTERN -->|Both decay slowly| ARMA_FLAG[ARMA(p,q) process]
    ACF_PATTERN -->|Seasonal spikes| SEASONAL_FLAG[Seasonal ARIMA]

    MA_FLAG --> FREQ_QUESTION
    AR_FLAG --> FREQ_QUESTION
    ARMA_FLAG --> FREQ_QUESTION
    SEASONAL_FLAG --> FREQ_QUESTION

    %% ===== PHASE 6: DOMAIN SELECTION =====
    FREQ_QUESTION{Periodicity<br/>suspected?}
    FREQ_QUESTION -->|Yes: Check spectrum| FREQ_ANALYSIS
    FREQ_QUESTION -->|No: Time domain| TIME_DOMAIN
    FREQ_QUESTION -->|Unsure: Check both| FREQ_ANALYSIS

    FREQ_ANALYSIS[🌊 Frequency Domain<br/>Ch 5]
    FREQ_ANALYSIS --> FFT_COMPUTE

    FFT_COMPUTE[Compute FFT & PSD]
    FFT_COMPUTE --> PEAKS

    PEAKS{Significant peaks<br/>in PSD?}
    PEAKS -->|Yes| RECORD_FREQ[Record frequencies<br/>Add to model]
    PEAKS -->|No: Flat spectrum| TIME_DOMAIN

    RECORD_FREQ --> SPECTRAL_SHAPE

    SPECTRAL_SHAPE{Spectral shape?}
    SPECTRAL_SHAPE -->|1/f decay| LONG_MEM[Long memory<br/>Consider ARFIMA]
    SPECTRAL_SHAPE -->|Band-limited| FILTER_DESIGN[Design filter]
    SPECTRAL_SHAPE -->|Peaks only| TIME_DOMAIN

    LONG_MEM --> TIME_DOMAIN
    FILTER_DESIGN --> TIME_DOMAIN

    %% ===== PHASE 7: MODEL SELECTION =====
    TIME_DOMAIN[🎲 Model Selection<br/>Ch 6]
    TIME_DOMAIN --> MULTIVAR

    MULTIVAR{Multiple<br/>series?}
    MULTIVAR -->|No: Univariate| UNI_SELECT
    MULTIVAR -->|Yes: Multivariate| MULTI_SELECT

    UNI_SELECT{Model type?}
    UNI_SELECT -->|ARIMA family| ARIMA_ORDER
    UNI_SELECT -->|Nonlinear| NONLIN_MODEL
    UNI_SELECT -->|Machine Learning| ML_MODEL

    ARIMA_ORDER{Seasonal?}
    ARIMA_ORDER -->|Yes| SARIMA[SARIMA(p,d,q)(P,D,Q)s]
    ARIMA_ORDER -->|No| ARIMA[ARIMA(p,d,q)]

    SARIMA --> CHECK_GARCH
    ARIMA --> CHECK_GARCH

    CHECK_GARCH{GARCH effects<br/>flagged?}
    CHECK_GARCH -->|Yes| ADD_GARCH[Add GARCH(m,n)]
    CHECK_GARCH -->|No| ESTIMATE
    ADD_GARCH --> ESTIMATE

    NONLIN_MODEL[TAR, Markov-switching]
    ML_MODEL[LSTM, Transformer, GBM]

    NONLIN_MODEL --> ESTIMATE
    ML_MODEL --> ESTIMATE

    MULTI_SELECT{Cointegration?}
    MULTI_SELECT -->|Test first| JOHANSEN

    JOHANSEN{Johansen Test<br/>p < 0.05?}
    JOHANSEN -->|Reject: Cointegrated| VECM[VECM]
    JOHANSEN -->|Fail to reject| VAR[VAR(k)]

    VECM --> ESTIMATE
    VAR --> ESTIMATE

    %% ===== PHASE 8: ESTIMATION & VALIDATION =====
    ESTIMATE[⚡ Parameter Estimation<br/>Ch 6]
    ESTIMATE --> FIT_METHOD

    FIT_METHOD{Estimation<br/>method?}
    FIT_METHOD -->|Maximum Likelihood| MLE[MLE via optim]
    FIT_METHOD -->|Least Squares| OLS[OLS/GLS]
    FIT_METHOD -->|Gradient Descent| SGD[Backprop for NN]

    MLE --> CONVERGE
    OLS --> CONVERGE
    SGD --> CONVERGE

    CONVERGE{Convergence<br/>successful?}
    CONVERGE -->|No| ADJUST[Adjust initial values<br/>or simplify]
    CONVERGE -->|Yes| COMPARE_IC
    ADJUST --> FIT_METHOD

    COMPARE_IC[Compare models<br/>AIC, BIC, HQIC]
    COMPARE_IC --> SELECT_BEST

    SELECT_BEST[Select best model]
    SELECT_BEST --> RESIDUALS

    RESIDUALS[🔬 Residual Diagnostics<br/>Ch 6]
    RESIDUALS --> RESID_ACF

    RESID_ACF{Ljung-Box<br/>on residuals<br/>p < 0.05?}
    RESID_ACF -->|Reject: Still autocorr| INC_ORDER[Increase AR/MA order]
    RESID_ACF -->|Fail to reject| RESID_ARCH

    INC_ORDER --> ESTIMATE

    RESID_ARCH{ARCH-LM Test<br/>p < 0.05?}
    RESID_ARCH -->|Reject: ARCH effects| ADD_GARCH_NOW[Add GARCH now]
    RESID_ARCH -->|Fail to reject| RESID_NORM

    ADD_GARCH_NOW --> ESTIMATE

    RESID_NORM{Normality test<br/>on residuals?}
    RESID_NORM -->|Reject: Non-normal| ROBUST_SE[Use robust SE]
    RESID_NORM -->|Fail to reject| DIAG_PASS

    ROBUST_SE --> DIAG_PASS

    DIAG_PASS{All diagnostics<br/>passed?}
    DIAG_PASS -->|No| RESPEC[Respecify model]
    DIAG_PASS -->|Yes| FORECAST

    RESPEC --> TIME_DOMAIN

    FORECAST[📈 Forecasting<br/>Ch 8]
    FORECAST --> GEN_FORECAST

    GEN_FORECAST[Generate h-step forecasts<br/>with intervals]
    GEN_FORECAST --> OOS_TEST

    OOS_TEST[Out-of-sample testing<br/>Rolling origin CV]
    OOS_TEST --> EVAL_METRICS

    EVAL_METRICS[Compute RMSE, MAE, MAPE]
    EVAL_METRICS --> ACCEPTABLE

    ACCEPTABLE{Forecast accuracy<br/>acceptable?}
    ACCEPTABLE -->|No| TRY_DIFF[Try different model]
    ACCEPTABLE -->|Yes| DEPLOY

    TRY_DIFF --> TIME_DOMAIN

    DEPLOY[🚀 Deployment<br/>Ch 8]
    DEPLOY --> DOCUMENT

    DOCUMENT[Document model<br/>specification]
    DOCUMENT --> MONITOR_SETUP

    MONITOR_SETUP[Set up drift monitoring<br/>KL divergence, spectral shift]
    MONITOR_SETUP --> RETRAIN_POLICY

    RETRAIN_POLICY[Define retraining policy]
    RETRAIN_POLICY --> END_SUCCESS

    END_SUCCESS([✅ VALIDATED MODEL<br/>DEPLOYED])

    %% Styling
    style START fill:#e1f5e1
    style END_SUCCESS fill:#e1ffe1
    style END_SPECIAL fill:#ffe1e1
    style WHITE_NOISE fill:#fff4e1
    style GARCH_FLAG fill:#ffe4cc
    style TRANS_NEEDED fill:#ffe4cc
```

</details>

---

## Phase-by-Phase Guide

### Phase 1: Data Acquisition & Inspection

**Start Node**: Raw time series data (CSV, database, API)

**Critical Checks**:
1. **Missing values**: Use `df.isna().sum()` to detect gaps
   - Action: [Data Preparation Chapter 3.2](#)
2. **Sampling regularity**: Check `df.index.diff().describe()`
   - Irregular → Resample or interpolate [Chapter 3.1](#)
3. **Outliers**: Compute z-scores, modified z-scores
   - |z| > 3 → [Outlier treatment Chapter 3.2](#)

**Output**: Clean, regularly-sampled time series ready for analysis

---

### Phase 2: Purpose Definition

**Decision Node**: What is your analytical goal?

| Purpose | Next Step | Reference |
|---------|-----------|-----------|
| **Forecasting** | → Distributional checks | Ch 4 |
| **Causal inference** | → Distributional checks | Ch 4 |
| **Signal extraction** | → Distributional checks | Ch 4 |
| **Change detection** | → Specialized methods | Ch 4 |
| **Anomaly detection** | → Specialized methods | Ch 4 |
| **Decomposition** | → STL/seasonal methods | Ch 4 |
| **Feature extraction** | → Feature engineering | Ch 7 |
| **Spectral analysis** | → Frequency domain directly | Ch 5 |

**Why this matters**: Purpose determines which tests and models are relevant.

---

### Phase 3: Diagnostic Testing

#### 3.1 Distributional Analysis

**Normality Test (Shapiro-Wilk)**:
```python
from scipy.stats import shapiro
stat, p_value = shapiro(data)
if p_value < 0.05:
    print("Reject H₀: Data is not normal → Consider transformation")
```

**Variance Stability**:
```python
rolling_std = data.rolling(window=20).std()
if rolling_std.std() / rolling_std.mean() > 0.2:
    print("Heteroskedastic → Flag for GARCH")
```

#### 3.2 Stationarity Testing

**ADF Test** (H₀: Unit root exists, non-stationary):
```python
from statsmodels.tsa.stattools import adfuller
result = adfuller(data)
if result[1] < 0.05:
    print("Reject H₀: Series is stationary")
```

**KPSS Test** (H₀: Series is stationary):
```python
from statsmodels.tsa.stattools import kpss
result = kpss(data, regression='c')
if result[1] < 0.05:
    print("Reject H₀: Series is non-stationary")
```

**Decision Matrix**:
| ADF Result | KPSS Result | Conclusion | Action |
|------------|-------------|------------|--------|
| Reject H₀ | Fail to reject | **Stationary** | Proceed to ACF |
| Fail to reject | Reject | **Non-stationary** | Difference |
| Both reject | Both reject | **Conflicting** | Visual check + difference |

---

### Phase 4: Transformations & Actions

**If non-stationary**, apply appropriate transformation:

1. **Variance grows with level** → Log or Box-Cox
2. **Linear trend** → First difference (d=1)
3. **Seasonal pattern** → Seasonal difference (D=1, s=period)
4. **Both trend + seasonality** → Combined transformation

**Always retest** after transformation using ADF and KPSS.

---

### Phase 5: Further Diagnostics

**Ljung-Box Test** (H₀: No autocorrelation):
```python
from statsmodels.stats.diagnostic import acorr_ljungbox
result = acorr_ljungbox(data, lags=[10], return_df=True)
if result['lb_pvalue'][10] < 0.05:
    print("Reject H₀: Autocorrelation present → Model needed")
else:
    print("White noise → No model needed")
```

**ACF/PACF Pattern Recognition**:
- **ACF cuts, PACF decays** → MA(q)
- **PACF cuts, ACF decays** → AR(p)
- **Both decay** → ARMA(p,q)
- **Seasonal spikes** → Seasonal ARIMA

---

### Phase 6: Domain Selection

**Question**: Are there hidden periodicities?

**Frequency Domain Analysis**:
```python
from scipy.fft import fft, fftfreq
import numpy as np

N = len(data)
yf = fft(data)
xf = fftfreq(N, 1/sampling_rate)

# Find peaks
peaks = np.where(np.abs(yf) > threshold)[0]
dominant_freqs = xf[peaks]
```

**Decision**:
- **Significant peaks** → Record frequencies, add harmonic regressors
- **1/f decay** → Long memory (ARFIMA)
- **Flat spectrum** → Proceed in time domain

---

### Phase 7: Model Selection

#### Univariate Models

**ARIMA Family**:
- Orders p, d, q determined by ACF/PACF
- Seasonal: SARIMA(p,d,q)(P,D,Q)ₛ
- With GARCH: ARIMA-GARCH if heteroskedastic

**Nonlinear**:
- Threshold AR (TAR)
- Markov-switching

**Machine Learning**:
- LSTM for long sequences
- Transformers for attention mechanisms
- Gradient Boosting (XGBoost, LightGBM)

#### Multivariate Models

**Test for cointegration** (Johansen test):
- If cointegrated → **VECM** (captures long-run equilibrium)
- If not → **VAR** (short-run dynamics only)

---

### Phase 8: Estimation & Validation

#### Estimation Methods

**Maximum Likelihood Estimation (MLE)**:
- Most efficient under normality
- Standard for ARIMA

**Ordinary/Generalized Least Squares (OLS/GLS)**:
- Computationally simpler
- GLS for heteroskedastic errors

**Gradient Descent**:
- Required for neural networks

#### Model Comparison

Use information criteria:
- **AIC** = -2 log(L) + 2k (penalizes lightly)
- **BIC** = -2 log(L) + k log(n) (penalizes heavily)
- Lower is better

#### Residual Diagnostics (Critical!)

**Must pass all three tests**:

1. **Ljung-Box on residuals** (p > 0.05) → No remaining autocorrelation
2. **ARCH-LM test** (p > 0.05) → No ARCH effects
3. **Normality test** (p > 0.05) → Residuals are normal

**If any test fails** → Loop back to model selection or increase order

#### Out-of-Sample Validation

**Rolling-origin cross-validation**:
```
Train: [1 ... 100] → Test [101]
Train: [1 ... 101] → Test [102]
Train: [1 ... 102] → Test [103]
...
```

**Metrics**:
- RMSE: Root Mean Squared Error
- MAE: Mean Absolute Error
- MAPE: Mean Absolute Percentage Error

**Acceptance criteria** defined by domain (e.g., MAPE < 5% for demand forecasting)

---

## Summary: Critical Decision Points

1. **Missing data > 15%?** → Segment rather than impute
2. **Non-stationary?** → Difference or detrend
3. **White noise?** → Stop (no model needed)
4. **Periodic components?** → Frequency domain analysis
5. **Residuals autocorrelated?** → Increase model order
6. **ARCH effects?** → Add GARCH component
7. **Forecast accuracy poor?** → Try different model class

---

**[Next: Purpose-Based Workflow →](02-purpose-workflow.md)** | **[Next: Representation-Based Workflow →](03-representation-workflow.md)** | **[Contents](../README.md)**
