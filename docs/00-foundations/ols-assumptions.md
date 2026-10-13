# OLS Assumptions and How Time Series Violates Them

Time series analysis is the study of data points collected or recorded at successive time intervals. Unlike cross-sectional data, which represents a snapshot at a single point in time, time series data has inherent temporal structure that must be respected in modelling.

A time series is a sequence of observations indexed in time order. The defining characteristic that separates it from cross-sectional data is **temporal dependence** — observations are not independent of each other. Yesterday's stock price influences today's price. Last month's temperature influences this month's reading. This dependence invalidates the independence assumption that underlies standard statistical inference.


**Common examples of time series data:**

- Stock prices recorded every second
- Monthly unemployment rates
- Daily temperature measurements
- Quarterly GDP figures
- Sensor readings from industrial equipment


## Time Domain vs Frequency Domain

Time series analysis operates in two complementary domains.

### Time Domain

- Values are examined as they evolve over time, observation by observation.
- Models describe how current values depend on past values.
- **Use when** questions concern predictability, causality, or forecasting.
- **Common methods:** ARIMA, VAR, GARCH, and state-space models.

### Frequency Domain

- Signals decompose into sine and cosine waves of varying amplitude and phase.
- The decomposition reveals the energy distribution across frequencies.
- **Use when** questions involve periodicity, cycles, or spectral content.
- **Common methods:** Fourier transform, power spectral density, filtering, and wavelets.

**In practice**, skilled analysts move between domains:

1. Begin in the time domain to examine trends and autocorrelation.
2. Move to the frequency domain to identify hidden cycles.
3. Return to the time domain to build a forecasting model that incorporates periodic components.


---

## The Classical OLS Assumptions and How Time Series Violates Them

The linear regression model takes the form:

\[y_i = \mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i, \quad i = 1, \dots, N\]

(Read: y-sub-i equals x-sub-i-transpose times beta plus epsilon-sub-i, for i from 1 to N.)

where \(y_i\) is the scalar outcome for observation \(i\), \(\mathbf{x}_i\) is a \(K \times 1\) vector of regressors, \(\boldsymbol{\beta}\) is the \(K \times 1\) coefficient vector, and \(\epsilon_i\) is the error term. OLS estimates \(\boldsymbol{\beta}\) by minimizing the sum of squared residuals:

\[\min_{\boldsymbol{\beta}} \sum_{i=1}^N \left(y_i - \mathbf{x}_i^T \boldsymbol{\beta}\right)^2\]

(Read: minimize over beta the sum of y-sub-i minus x-sub-i-transpose-beta, squared, for i from 1 to N.)

When \(\mathbf{X}\) has full column rank ([Assumption 0](#assumption-0) below) — so that \(\mathbf{X}^T\mathbf{X}\) is invertible — this minimization has a unique closed-form solution (also called the OLS estimator):

\[\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}\]

(Read: beta-hat equals X-transpose-X-inverse times X-transpose-y.)

The finite-sample properties of OLS rest on a set of assumptions collectively known as the Gauss-Markov conditions. OLS is **BLUE** — the Best Linear Unbiased Estimator — when these assumptions hold; they are sufficient, not necessary (OLS also coincides with GLS for some error covariance matrices that violate them; Zyskind 1967). Assumptions 1–4 constitute the **Gauss-Markov assumptions**; under these, the model is called the **Classical Regression Model** (CRM). Adding Assumption 5 (normality) yields the **Classical Normal Regression Model** (CNRM). Preceding all five is **Assumption 0** (the rank condition), which determines whether the OLS estimator exists at all — a separate tier from A1–A5, treated below.

The matrix calculus derivation of \(\hat{\boldsymbol{\beta}}\), the fundamental decomposition, and the conditions under which t-statistics are valid are developed in full in [Appendix A](../appendices/A-ols-derivation.md).

For the remainder of this section we adopt the time-series convention: observations are indexed by \(t = 1, \ldots, T\) rather than \(i = 1, \ldots, N\), and \(\epsilon_t\) denotes the error at time \(t\). The model becomes \(y_t = \mathbf{x}_t^T \boldsymbol{\beta} + \epsilon_t\) with the same OLS estimator \(\hat{\boldsymbol{\beta}}\).

!!! note "Remark: Assumption 4 implies Assumption 1"
    Strict exogeneity \(\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0\) implies the zero mean \(\mathbb{E}[\epsilon_t] = \mathbb{E}[\mathbb{E}[\epsilon_t \mid \mathbf{X}]] = 0\) by the law of iterated expectations; the step needs no intercept. Many treatments therefore state only the conditional form. The intercept plays a different role: a constant non-zero error mean \(\mathbb{E}[\epsilon_t] = c\) is absorbed into the intercept and changes only \(\hat{\beta}_1\).

    In time series, \(\mathbb{E}[\epsilon_t \mid \mathbf{X}] \neq 0\) arises from two sources: omitted *deterministic* terms (trend, seasonal terms) and *stochastic* dependence between errors and regressors (feedback from past errors into lagged regressors, simultaneity). The page lists A1 separately because the first source leaves a time-varying error mean that is visible in residual plots; its consequences are those of an A4 failure.

---

<a id="assumption-0"></a>

<div class="annotate" markdown>

!!! theorem "Assumption 0: No Perfect Multicollinearity (Rank Condition)"
    \[\text{rank}(\mathbf{X}) = K\]

    (Read: the rank of X equals K, the number of regressors.)

The design matrix \(\mathbf{X}\) has full column rank: no regressor is an exact linear combination of the others. Equivalently, \(\mathbf{X}^T\mathbf{X}\) is invertible, which is what makes the OLS estimator \(\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}\) well-defined. (1)

</div>

1.  **Common alternative forms:**
    - \(\det(\mathbf{X}^T\mathbf{X}) \neq 0\) — the determinant form
    - \(\mathbf{X}^T\mathbf{X}\) is positive definite — the spectral form
    - For a single restriction: no \(\mathbf{x}_j\) can be written as \(\sum_{k \neq j} c_k \mathbf{x}_k\) for constants \(c_k\)
    - Sometimes called the **identification condition**, because it ensures \(\boldsymbol{\beta}\) is uniquely determined by the data

#### Existence vs quality

Assumption 0 differs from A1–A5 in kind. The five Gauss-Markov assumptions concern the *quality* of the estimator — bias, efficiency, valid inference. Assumption 0 concerns whether the estimator *exists at all*. If A0 fails, \(\mathbf{X}^T\mathbf{X}\) is singular, the inverse does not exist, and OLS produces no estimate. There is no notion of "biased" or "inefficient" because there is no number to begin with.

This distinction also affects how problems are detected. A failure of A0 is a structural failure of the design matrix and surfaces at computation time — software returns a singular-matrix error or silently drops a redundant column. Failures of A2, A3 and A5, and omitted structure that leaves a pattern in the residuals, surface after estimation by examining residuals. Correlation between the errors and the included regressors (simultaneity) leaves no trace in the OLS residuals, because \(\mathbf{X}^T\hat{\boldsymbol{\epsilon}} = \mathbf{0}\) by construction; detecting it needs instruments (the Durbin–Wu–Hausman test) or theory.

#### Perfect vs imperfect multicollinearity

Two cases are commonly conflated under the label "multicollinearity":

- **Perfect multicollinearity** — exact linear dependence among regressors. Violates A0. OLS cannot be computed. The textbook example is the **dummy variable trap**: including dummies for all categories alongside an intercept makes the dummy columns sum to the intercept column.

- **Imperfect (high) multicollinearity** — strong but not exact correlation among regressors. **No assumption is violated.** The estimator \(\hat{\boldsymbol{\beta}}\) remains BLUE under the Gauss-Markov conditions. The only consequence is that \(\text{Var}(\hat{\boldsymbol{\beta}})\) is inflated, producing wide confidence intervals and coefficients that swing under small data perturbations. Diagnose with the variance inflation factor (VIF); remedy by dropping redundant regressors, combining them, or using regularized methods such as ridge regression (Hoerl and Kennard 1970).

Imperfect multicollinearity is a **modelling nuisance, not an assumption violation**. It changes nothing about the validity of the OLS framework; it only affects the precision of individual coefficient estimates.

#### In time series

Two contexts produce multicollinearity in time series. **Including many lags** of the same persistent variable yields a near-singular \(\mathbf{X}^T\mathbf{X}\) when the series is highly autocorrelated, since successive lags carry redundant information. **Including a deterministic trend \(t\) alongside a near-unit-root regressor** also produces high collinearity, because both are nearly linear in time. Both are imperfect-multicollinearity cases — they inflate standard errors but do not invalidate OLS itself. The remedy is parsimony in lag selection (informed by AIC, BIC, and the PACF) and care when combining trends with persistent regressors.

---

<a id="assumption-1"></a>

<div class="annotate" markdown>

!!! theorem "Assumption 1: Zero Mean"
    \[\mathbb{E}[\epsilon_t] = 0\]

    (Read: the expected value of epsilon-sub-t equals zero.)

The errors have zero mean — the model has no systematic bias. On average, it neither over-predicts nor under-predicts. (1)

</div>

1.  **Common alternative forms:**
    - \(\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0\) — the conditional form, which is stronger and subsumes exogeneity (Assumption 4). Some texts (e.g., Wooldridge 2020) combine A1 and A4 into this single condition
    - \(\mu_\epsilon = 0\) — compact scalar notation in introductory texts
    - Note: A1 follows from A4 (strict exogeneity) by the law of iterated expectations, \(\mathbb{E}[\epsilon_t] = \mathbb{E}[\mathbb{E}[\epsilon_t \mid \mathbf{X}]] = 0\), with or without an intercept. With an intercept \(\beta_1\), a constant error mean is absorbed into \(\hat{\beta}_1\)

#### Violation in time series

When \(y_t\) contains a **deterministic trend** — for example, GDP growing over time — and time \(t\) is omitted as a regressor, the marginal mean of the error varies systematically across \(t\) rather than being a single constant. Concretely, if the data-generating process is \(y_t = \alpha + \delta t + u_t\) with \(\mathbb{E}[u_t] = 0\) but the fitted model is \(y_t = \alpha + \epsilon_t\), then \(\epsilon_t = \delta t + u_t\) has

\[\mathbb{E}[\epsilon_t] = \delta t,\]

(Read: the expected value of epsilon-sub-t equals delta times t.)

so the unconditional error mean is non-zero and grows with \(t\). Equivalently, if \(t\) is treated as a covariate, the conditional mean \(\mathbb{E}[\epsilon_t \mid t]\) is a non-constant function of time. The errors carry a systematic upward or downward drift that varies with position in the sample. This is an omitted-variable failure of \(\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0\): when the omitted trend is correlated with a trending included regressor, the slope estimates are biased, and the bias does not shrink as \(T\) grows.

A subtler violation arises with **seasonal data** (monthly sales, quarterly earnings): the mean of \(\epsilon_t\) shifts predictably every cycle. An OLS model that omits seasonal terms produces errors whose conditional mean oscillates, violating this assumption on a regular schedule.

---

<a id="assumption-2"></a>

<div class="annotate" markdown>

!!! theorem "Assumption 2: Homoskedasticity"
    \[\text{Var}(\epsilon_t \mid \mathbf{X}) = \sigma^2 \quad \forall \ t\]

    (Read: the variance of epsilon-sub-t, given X, equals sigma-squared, for all t.)

The variance of the error is constant across all observations and does not depend on the regressors or on time. (1)

</div>

1.  **Common alternative forms:**
    - \(\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] = \sigma^2\) — equals \(\text{Var}(\epsilon_t \mid \mathbf{X})\) only when \(\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0\) (i.e., A4 holds). Many treatments fold A4 in by default and write A2 in this form
    - \(\text{Var}(\epsilon_t) = \sigma^2\) — unconditional form, common in introductory texts
    - \(\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2 \mathbf{I}\) — the matrix form, seen in Greene (2018) and Wooldridge (2010), which packages both Assumption 2 and 3 together

#### Violation in time series

Two different things are called heteroskedasticity, and they have different consequences, because they condition on different information.

**Heteroskedasticity given the regressors.** The error variance is a function of the regressors or of the level of the series, \(\text{Var}(\epsilon_t \mid \mathbf{X}) = \sigma_t^2\) with \(\sigma_t^2\) varying across \(t\) — for example, errors that grow with the scale of a trending series. A2 fails. OLS stays unbiased but is no longer BLUE: a GLS estimator that uses the error covariance \(\boldsymbol{\Omega}\) — formally introduced under Assumption 3 below; for pure heteroskedasticity \(\boldsymbol{\Omega}\) is diagonal with non-constant entries — down-weights high-variance observations and has smaller variance. The conventional OLS variance estimator

\[\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = \hat{\sigma}^2 (\mathbf{X}^T\mathbf{X})^{-1}\]

(Read: the estimated variance of beta-hat equals sigma-hat-squared times X-transpose-X-inverse.)

is inconsistent for the true variance of \(\hat{\boldsymbol{\beta}}\) — it converges to the wrong quantity as \(T \rightarrow \infty\) — and White (1980) standard errors replace it.

**Conditional heteroskedasticity given the past.** In financial data, large price moves cluster together — **volatility clustering**, formalized by Engle (1982) as ARCH:

\[\text{Var}(\epsilon_t \mid \mathcal{F}_{t-1}) = \alpha_0 + \alpha_1 \epsilon_{t-1}^2\]

(Read: the variance of epsilon-sub-t, given the information set F-sub-t-minus-1, equals alpha-zero plus alpha-one times epsilon-sub-t-minus-1-squared.)

where \(\mathcal{F}_{t-1}\) denotes all information available up to \(t-1\). With \(0 \le \alpha_1 < 1\) this error is covariance stationary, serially uncorrelated, and has the constant unconditional variance \(\alpha_0 / (1 - \alpha_1)\). Conditioning on \(\mathcal{F}_{t-1}\) and conditioning on \(\mathbf{X}\) are different. When the regressors are strictly exogenous and independent of the error process, \(\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2 \mathbf{I}\): A2 and A3 hold, OLS is BLUE, and the conventional standard errors are valid (Engle 1982). Maximum likelihood with the ARCH variance equation is more efficient, because it is nonlinear in \(y\) and lies outside the class of linear unbiased estimators that the Gauss–Markov theorem covers. When the regressors carry information about past errors — lags of \(y\), or regressors correlated with volatility — \(\mathbb{E}[\mathbf{x}_t \mathbf{x}_t^T \epsilon_t^2] \neq \sigma^2\, \mathbb{E}[\mathbf{x}_t \mathbf{x}_t^T]\), and White or quasi-maximum-likelihood standard errors are needed (Hamilton 1994, ch. 8 and ch. 21).

---

<a id="assumption-3"></a>

<div class="annotate" markdown>

!!! theorem "Assumption 3: No Serial Correlation"
    \[\mathbb{E}[\epsilon_t \epsilon_s \mid \mathbf{X}] = 0 \quad \forall \ t \neq s\]

    (Read: the expected value of epsilon-sub-t times epsilon-sub-s, given X, equals zero, for all t not equal to s.)

The error at time \(t\) carries no information about the error at any other time \(s\). Knowing that the model over-predicted yesterday provides no information about today's prediction error. (1)

</div>

1.  **Common alternative forms:**
    - \(\text{Cov}(\epsilon_t, \epsilon_s) = 0\) — unconditional covariance form, seen widely in introductory econometrics
    - \(\rho = 0\) where \(\epsilon_t = \rho \epsilon_{t-1} + u_t\) — the AR(1) parameterization, common in applied papers testing for autocorrelation
    - The matrix form packaging Assumptions 2 and 3 together: \(\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2\mathbf{I}\)

#### Violation in time series — the most consequential failure

Time series observations are collected sequentially, so each observation is structurally linked to those that precede it. Yesterday's GDP affects today's GDP. Last month's temperature affects this month's temperature. This sequential dependence produces **autocorrelation**: errors are correlated across time.

Define the autocovariance at lag \(k\) (using the zero-mean property from Assumption 1):

\[\gamma(k) = \text{Cov}(\epsilon_t, \epsilon_{t-k}) = \mathbb{E}[\epsilon_t \epsilon_{t-k}]\]

(Read: gamma-of-k equals the covariance between epsilon-sub-t and epsilon-sub-t-minus-k, which equals the expected value of their product when the errors have zero mean.)

Assumption 3 requires \(\gamma(k) = 0\) for all \(k \neq 0\). In practice, \(\gamma(1)\) is almost never zero in raw time series data.

When this assumption fails, the true error covariance matrix is no longer \(\sigma^2 \mathbf{I}\); it becomes:

\[\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2 \boldsymbol{\Omega}, \quad \boldsymbol{\Omega} \neq \mathbf{I}\]

(Read: the expected value of epsilon-epsilon-transpose, given X, equals sigma-squared times Omega, where Omega is not the identity matrix.)

Here:

- \(\mathbf{I}\) is the \(T \times T\) **identity matrix** — a square matrix with ones on the main diagonal and zeros everywhere else. In the error covariance context, the diagonal ones mean every error has the same variance \(\sigma^2\), and the off-diagonal zeros mean no two errors are correlated. For \(T = 3\):

\[\mathbf{I}_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\]

- \(\boldsymbol{\Omega}\) is a \(T \times T\) **symmetric positive-definite matrix**. Symmetric means the matrix equals its own transpose (\(\boldsymbol{\Omega} = \boldsymbol{\Omega}^T\)), which reflects the fact that \(\text{Cov}(\epsilon_t, \epsilon_s) = \text{Cov}(\epsilon_s, \epsilon_t)\). Positive-definite ensures all variances are strictly positive and the matrix is invertible. The diagonal entries encode heteroskedasticity (time-varying variance); the off-diagonal entries encode serial correlation.

For concreteness, take \(T = 3\) errors following a stationary AR(1) process \(\epsilon_t = \rho \epsilon_{t-1} + u_t\) with white-noise innovations \(u_t\) of variance \(\sigma_u^2\). Then \(\sigma^2\) in the decomposition \(\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T] = \sigma^2 \boldsymbol{\Omega}\) is the **marginal (stationary) variance** of \(\epsilon_t\),

\[\sigma^2 = \text{Var}(\epsilon_t) = \frac{\sigma_u^2}{1 - \rho^2},\]

(Read: sigma-squared equals sigma-u-squared divided by one minus rho-squared.)

and \(\boldsymbol{\Omega}\) is the resulting **autocorrelation matrix**, with ones on the diagonal and \(\rho^{|t-s|}\) off-diagonal:

\[\boldsymbol{\Omega} = \begin{pmatrix} 1 & \rho & \rho^2 \\ \rho & 1 & \rho \\ \rho^2 & \rho & 1 \end{pmatrix}\]

When \(\rho = 0\), \(\boldsymbol{\Omega}\) collapses to \(\mathbf{I}\), recovering Assumption 3.

The true variance of \(\hat{\boldsymbol{\beta}}\) is then:

\[\text{Var}(\hat{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2 (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \boldsymbol{\Omega} \mathbf{X} (\mathbf{X}^T\mathbf{X})^{-1}\]

(Read: the variance of beta-hat, given X, equals sigma-squared times X-transpose-X-inverse, times X-transpose-Omega-X, times X-transpose-X-inverse.)

OLS, however, reports the conventional variance estimator \(\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = \hat{\sigma}^2 (\mathbf{X}^T\mathbf{X})^{-1}\) introduced under Assumption 2. The two expressions — the true sandwich form above and the OLS-reported form — are different objects. The reported standard errors are **wrong**. Their direction depends on the regressors as well as the errors: with AR(1) errors (coefficient \(\rho\)) and an AR(1) regressor (coefficient \(\lambda\)), the ratio of the true to the conventional variance is approximately \((1 + \rho\lambda)/(1 - \rho\lambda)\). When both the errors and the regressors are positively autocorrelated — the usual case — OLS **understates** the true standard errors, so t-statistics are inflated and null hypotheses are rejected too often (Wooldridge 2020, chap. 12). With serially uncorrelated regressors the conventional standard error is consistent; with negatively autocorrelated regressors it overstates.

The point estimate \(\hat{\boldsymbol{\beta}}\) remains **unbiased** — the estimate is correct on average — but the standard errors used to assess its reliability are not.

---

<a id="assumption-4"></a>

<div class="annotate" markdown>

!!! theorem "Assumption 4: Strict Exogeneity"
    \[\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0\]

    (Read: the expected value of epsilon-sub-t, given X, equals zero.)

The error at any time \(t\) is uncorrelated with the regressors at *all* time periods — past, present, and future. No regressor in the entire design matrix \(\mathbf{X}\) carries information about \(\epsilon_t\). (1)

</div>

1.  **Common alternative forms:**
    - **Contemporaneous exogeneity**: \(\mathbb{E}[\epsilon_t \mid \mathbf{x}_t] = 0\) — the error is uncorrelated with regressors at time \(t\) only. Weaker than strict exogeneity; sufficient for consistency in the cross-sectional case and in stationary time series under standard regularity conditions, but not for finite-sample unbiasedness. In time series with serially correlated regressors, the law of large numbers that consistency needs holds for a strictly stationary and *ergodic* process: sample averages converge to population means without any rate condition ([law of large numbers](asymptotics.md#law-of-large-numbers)). The standard errors need more: a central limit theorem, which requires the dependence to decay fast enough (summable mixing coefficients) or a martingale difference structure. Without ergodicity the OLS estimator \(\hat{\boldsymbol{\beta}}\) may fail to be *consistent* — meaning it does not converge to the true \(\boldsymbol{\beta}\) as the sample size \(T \to \infty\) — even when \(\mathbb{E}[\epsilon_t \mid \mathbf{x}_t] = 0\) holds
    - **Predetermined regressors** (Hamilton 1994, ch. 8): \(\mathbb{E}[\epsilon_t \mid \mathbf{x}_1, \ldots, \mathbf{x}_t] = 0\) — the error is uncorrelated with current and past regressors but future regressors may be correlated with it. This is the standard moment condition for dynamic time-series models with lagged dependent variables. It is sufficient for *consistency* of OLS under stationarity and weak dependence, even though strict exogeneity fails
    - **Weak exogeneity** (Engle, Hendry, and Richard 1983): a *parametric* concept distinct from predeterminedness. Formally, the density of \((y_t, \mathbf{x}_t)\) given the past \(\mathcal{F}_{t-1}\) factorises as \(D(y_t, \mathbf{x}_t \mid \mathcal{F}_{t-1}; \boldsymbol{\lambda}) = D(y_t \mid \mathbf{x}_t, \mathcal{F}_{t-1}; \boldsymbol{\lambda}_1)\, D(\mathbf{x}_t \mid \mathcal{F}_{t-1}; \boldsymbol{\lambda}_2)\), with \(\boldsymbol{\lambda}_1\) and \(\boldsymbol{\lambda}_2\) variation free and the parameters of interest functions of \(\boldsymbol{\lambda}_1\) alone — so that conditioning on \(\mathbf{x}_t\) entails no loss of information for inference on \(\boldsymbol{\beta}\). Weak exogeneity is about *what to condition on* for inference; predeterminedness is about *moment conditions on the error*. The two often coincide in applied work but are not equivalent. This text uses "predetermined" for the conditional-mean condition above
    - \(\text{Cov}(\mathbf{x}_t, \epsilon_t) = 0\) — the covariance form, common in older literature. Note this is weaker than the conditional mean form
    - Note: A4 holds automatically when \(\mathbf{x}_t\) is deterministic (non-random) — hence sometimes called the **nonstochastic regressor assumption**

#### Violation in time series — structural and unavoidable with lagged regressors

In time series, **strict exogeneity is violated by construction** whenever a lagged dependent variable appears as a regressor. Consider the AR(1) model:

\[y_t = \beta y_{t-1} + \epsilon_t\]

(Read: y-sub-t equals beta times y-sub-t-minus-1 plus epsilon-sub-t.)

Here \(\mathbf{x}_t = y_{t-1}\), so for a sample of \(T\) observations the design matrix consists of \(y_0, y_1, \ldots, y_{T-1}\). The condition \(\mathbb{E}[\epsilon_t \mid y_0, y_1, \ldots, y_{T-1}] = 0\) fails because \(\epsilon_t\) affects \(y_t\), and \(y_t\) itself enters the design matrix as the regressor at time \(t+1\) (i.e., \(y_t = \mathbf{x}_{t+1}\)). Therefore \(\text{Cov}(\mathbf{x}_{t+1}, \epsilon_t) = \text{Cov}(y_t, \epsilon_t) \neq 0\), and strict exogeneity fails.

The predetermined-regressor condition \(\mathbb{E}[\epsilon_t \mid y_{t-1}, y_{t-2}, \ldots] = 0\) holds when \(\epsilon_t\) is a martingale difference sequence with respect to the past of \(y\) (for example, i.i.d.). Uncorrelatedness alone is weaker: it gives \(\mathbb{E}[y_{t-1}\epsilon_t] = 0\), because \(y_{t-1}\) is linear in past errors, which suffices for consistency but not for the usual standard errors. Critically, although strict exogeneity fails for AR(1), OLS in this model with \(|\beta| < 1\) and martingale-difference errors is **biased in finite samples but consistent**: \(\hat{\beta} \xrightarrow{p} \beta\) as \(T \to \infty\). This is the classical Hurwicz (1950) bias result — the bias is of order \(1/T\) and vanishes asymptotically. Time-series econometrics therefore **replaces strict exogeneity with predetermined regressors** and relies on this combination together with large-sample (\(T \rightarrow \infty\)) asymptotics, rather than finite-sample Gauss-Markov results (Hamilton 1994, chap. 8).

A more severe violation arises from **simultaneity** — when \(y_t\) and \(\mathbf{x}_t\) jointly determine each other, as in the simultaneous determination of supply and price in a market equilibrium model. Unlike the AR(1) case, where bias vanishes asymptotically, OLS under simultaneity is **biased *and* inconsistent**: the bias does not shrink with sample size, and consistent estimation requires instrumental variables or system methods (Hamilton 1994, chap. 9).

---

<a id="assumption-5"></a>

<div class="annotate" markdown>

!!! theorem "Assumption 5: Normality"
    \[\boldsymbol{\epsilon} \mid \mathbf{X} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})\]

    (Read: the error vector given X is distributed as multivariate Normal with mean zero and covariance sigma-squared times the identity.)

The error vector is jointly normal with mean zero and covariance \(\sigma^2\mathbf{I}\). Joint normality is what allows exact t-distributions and F-distributions for hypothesis tests in finite samples; normality of each \(\epsilon_t\) separately is not enough, because uncorrelated normal variables need not be independent unless they are jointly normal. (1)

</div>

1.  **Common alternative forms:**
    - \(\epsilon_t \mid \mathbf{X} \sim \mathcal{N}(0, \sigma^2)\) for each \(t\) — the per-observation form, which gives exact tests only together with joint normality
    - The vector form contains Assumptions 1, 2 and 3 and can be written \(\epsilon_t \sim \text{i.i.d.} \ \mathcal{N}(0, \sigma^2)\) or \(\text{n.i.d.}(0, \sigma^2)\) given \(\mathbf{X}\) — the errors are independently and identically normally distributed with zero mean and constant variance
    - In large-sample work, normality is dropped as an assumption and replaced by conditions under which a central limit theorem applies to \(\mathbf{x}_t\epsilon_t\). The theorem then gives \(\sqrt{T}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \mathbf{Q}^{-1} \mathbf{S} \mathbf{Q}^{-1})\), where \(\mathbf{Q} = \text{plim}\frac{1}{T}\mathbf{X}^T\mathbf{X}\) and \(\mathbf{S} = \sum_{j=-\infty}^{\infty} \boldsymbol{\Gamma}_j\), \(\boldsymbol{\Gamma}_j = \mathbb{E}[\mathbf{x}_t \epsilon_t \epsilon_{t-j} \mathbf{x}_{t-j}^T]\), is the long-run variance of \(\mathbf{x}_t\epsilon_t\) — the **sandwich form**. Under homoskedastic martingale-difference errors \(\mathbf{S} = \sigma^2\mathbf{Q}\) and the variance reduces to \(\sigma^2\mathbf{Q}^{-1}\). Heteroskedasticity-and-autocorrelation-consistent (HAC) estimators (e.g., Newey-West 1987) estimate \(\mathbf{S}\); they cover predetermined regressors as well as strictly exogenous ones (Hayashi 2000, ch. 6)

#### When and how this fails in time series

Unlike the previous four assumptions, normality is not structurally tied to temporal ordering — many time series have approximately normal errors. The common failures arise in specific domains. High-frequency financial data and volatile processes exhibit **fat tails** (leptokurtosis) and **asymmetry** (skewness): the normal distribution assigns near-zero probability to extreme deviations, yet in daily stock returns such deviations occur far more often than a Gaussian model predicts.

Define excess kurtosis (with \(\mathbb{E}[\epsilon_t] = 0\) from Assumption 1):

\[\kappa = \frac{\mathbb{E}[\epsilon_t^4]}{\sigma^4} - 3\]

(Read: kappa equals the expected value of epsilon-sub-t-to-the-fourth, divided by sigma-to-the-fourth, minus three.)

For a normal distribution, \(\kappa = 0\). For daily stock returns, \(\kappa\) typically lies between 4 and 20 (Cont 2001).

The skewness \(\gamma_1 = \mathbb{E}[\epsilon_t^3]/\sigma^3\) is also often non-zero. Financial returns tend to be **left-skewed** — large losses occur more often than large gains — while certain macroeconomic series are right-skewed during expansions.

The practical consequences depend on sample size. By the [central limit theorem](asymptotics.md#central-limit-theorem) — under regularity conditions on \(\mathbf{x}_t\epsilon_t\), particularly finite \(\mathbb{E}[\mathbf{x}_t\mathbf{x}_t^T\epsilon_t^2]\) (usually fourth moments) and dependence that decays fast enough — the distribution of \(\sqrt{T}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})\) converges to a normal distribution regardless of the error distribution; \(\hat{\boldsymbol{\beta}}\) itself converges to the point \(\boldsymbol{\beta}\). Normality therefore matters most in **small samples**, where finite-sample t and F tests require it for validity. Convergence is slow when tails are heavy, which is the time series setting where this matters most.

When the regularity conditions themselves fail, asymptotic normality breaks down. If the errors have **infinite variance** — for example, \(\alpha\)-stable distributions with index \(\alpha < 2\), occasionally entertained for extreme financial returns or high-frequency tick data — the CLT does not apply, and \(\hat{\boldsymbol{\beta}}\) has a non-Gaussian limiting distribution. Likewise, processes with long memory or unit roots violate the weak-dependence requirement and require separate asymptotic theory. For problems such as volatility modelling, non-normality is the phenomenon of interest, not merely an inconvenient property to work around.

---

### How Each Violation Propagates

OLS produces three distinct outputs — the point estimate \(\hat{\boldsymbol{\beta}}\), the standard errors \(\hat{\text{se}}(\hat{\boldsymbol{\beta}})\), and the test statistics — and each is vulnerable to different assumptions. The table below maps each violation to the specific component it corrupts.

| Assumption | Violation | Point estimate \(\hat{\boldsymbol{\beta}}\) | Standard errors | t / F tests |
|---|---|---|---|---|
| [A1 Zero mean](#assumption-1) | Omitted trend or seasonality correlated with included regressors | Biased; the bias does not vanish as \(T\) grows | Wrong | Invalid |
| [A2 Homoskedasticity](#assumption-2) | Variance depending on the regressors or the level | Unbiased, not efficient | Inconsistent | Invalid |
| [A2 Homoskedasticity](#assumption-2) | Volatility clustering (ARCH) with strictly exogenous regressors | Unbiased; BLUE; ML more efficient | Valid | Valid |
| [A2 Homoskedasticity](#assumption-2) | Volatility clustering (ARCH) with lagged \(y\) among the regressors | Consistent | Inconsistent | Invalid |
| [A3 No serial correlation](#assumption-3) | Autocorrelated errors | Unbiased | Inconsistent; understated when errors and regressors are positively autocorrelated | Invalid |
| [A4 Exogeneity](#assumption-4) | Lagged \(y\) with conditionally homoskedastic martingale-difference errors | Biased of order \(1/T\); consistent | Valid asymptotically | Valid asymptotically |
| [A4 Exogeneity](#assumption-4) | Lagged \(y\) with autocorrelated errors, or simultaneity | Biased and inconsistent | Wrong | Invalid |
| [A5 Normality](#assumption-5) | Fat tails, skewness | Unbiased | Correct asymptotically | Approximately valid in large samples; exact only under A5 |

Three patterns emerge. Violations of A2 and A3 leave \(\hat{\boldsymbol{\beta}}\) unbiased but, except for ARCH with strictly exogenous regressors, corrupt the standard errors and all downstream tests — a deceptive situation in which point estimates look reasonable while inference is invalid. Whether \(\hat{\boldsymbol{\beta}}\) itself is consistent turns on the orthogonality condition \(\mathbb{E}[\mathbf{x}_t \epsilon_t] = \mathbf{0}\): a lagged dependent variable with martingale-difference errors satisfies it, so OLS is biased in finite samples but consistent; an omitted correlated trend, a lagged dependent variable with autocorrelated errors, or simultaneity violates it, and no correction to standard errors can fix the resulting inconsistent estimator. Three rows leave both \(\hat{\boldsymbol{\beta}}\) and the conventional standard errors asymptotically correct: A5, ARCH with strictly exogenous regressors, and a lagged dependent variable with conditionally homoskedastic martingale-difference errors; they affect only finite-sample claims, such as the exact t and F critical values that A5 provides.

**A note on the A1 row.** The A1 entry reflects the *omitted-variable* mechanism: when a deterministic regressor (a trend, a seasonal dummy) that is correlated with included regressors is omitted, the omitted-variable bias is transmitted to \(\hat{\boldsymbol{\beta}}\). If the omitted regressor is uncorrelated with all included regressors, only the intercept is biased while the slope coefficients remain unbiased. A constant error mean is absorbed by the intercept and biases nothing else.

---

### Summary: What Breaks and What Doesn't

| Assumption | Requirement | Time Series Violation | What Breaks in OLS |
|---|---|---|---|
| [**Zero Mean**](#assumption-1) | \(\mathbb{E}[\epsilon_t] = 0\) | Trends, seasonality | Biased \(\hat{\boldsymbol{\beta}}\) when the omitted term correlates with included regressors |
| [**Homoskedasticity**](#assumption-2) | \(\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] = \sigma^2\) | Variance depending on regressors or level; ARCH with lagged regressors | Inefficient \(\hat{\boldsymbol{\beta}}\) (first case), wrong conventional standard errors |
| [**No Serial Correlation**](#assumption-3) | \(\mathbb{E}[\epsilon_t\epsilon_s \mid \mathbf{X}] = 0\) | Autocorrelation | Wrong standard errors, invalid inference |
| [**Exogeneity**](#assumption-4) | \(\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0\) | Lagged \(y\); simultaneity | Finite-sample bias with lagged \(y\) and martingale-difference errors; inconsistency with autocorrelated errors or simultaneity |
| [**Normality**](#assumption-5) | \(\boldsymbol{\epsilon} \mid \mathbf{X} \sim \mathcal{N}(\mathbf{0},\sigma^2\mathbf{I})\) | Fat tails, skewness (domain-specific, not structural) | Exact finite-sample t and F tests |

The table reveals a hierarchy. Violations of Assumptions 2 and 3 leave \(\hat{\boldsymbol{\beta}}\) **unbiased but unreliable**: the estimate is correct on average, but the standard errors and test statistics are not. Violations of the orthogonality condition \(\mathbb{E}[\mathbf{x}_t \epsilon_t] = \mathbf{0}\) render \(\hat{\boldsymbol{\beta}}\) **inconsistent** — the estimate itself is wrong. This hierarchy determines which violations to address first.


**[Next: Do You Need Time Series Analysis? →](do-you-need-time-series-analysis.md)**
