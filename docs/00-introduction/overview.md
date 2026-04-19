# Introduction

---
## **What is Time Series Analysis?**

Time series analysis is the study of data points collected or recorded at successive time intervals. Unlike cross-sectional data, which represents a snapshot at a single point in time, time series data has inherent temporal structure that must be respected in modeling.

A time series is a sequence of observations indexed in time order. The defining characteristic that separates it from cross-sectional data is **temporal dependence** — observations are not independent of each other. Yesterday's stock price influences today's price. Last month's temperature influences this month's reading. This dependence invalidates the independence assumption that underlies standard statistical inference.


**Common examples of time series data:**

- Stock prices recorded every second
- Monthly unemployment rates
- Daily temperature measurements
- Quarterly GDP figures
- Sensor readings from industrial equipment


## **Time Domain vs Frequency Domain**

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

## **The 5 Classical OLS Assumptions and How Time Series Violates Them**

The linear regression model takes the form:

$$y_i = \mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i, \quad i = 1, \dots, N$$

(Read: y-sub-i equals x-sub-i-transpose times beta plus epsilon-sub-i, for i from 1 to N.)

where $y_i$ is the scalar outcome for observation $i$, $\mathbf{x}_i$ is a $K \times 1$ vector of regressors, $\boldsymbol{\beta}$ is the $K \times 1$ coefficient vector, and $\epsilon_i$ is the error term. OLS estimates $\boldsymbol{\beta}$ by minimizing the sum of squared residuals:

$$\min_{\boldsymbol{\beta}} \sum_{i=1}^N \left(y_i - \mathbf{x}_i^T \boldsymbol{\beta}\right)^2$$

(Read: minimize over beta the sum of y-sub-i minus x-sub-i-transpose-beta, squared, for i from 1 to N.)

When $\mathbf{X}$ has full column rank (invertible), this minimization has a unique closed-form solution (also called OLS estimator):

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

(Read: beta-hat equals X-transpose-X-inverse times X-transpose-y.)

The entire edifice of OLS estimation rests on a set of assumptions collectively known as the Gauss-Markov conditions. OLS achieves the **BLUE** property — Best Linear Unbiased Estimator — only when those assumptions hold. Assumptions 1–4 constitute the **Gauss-Markov assumptions**; under these, the model is called the **Classical Regression Model** (CRM). Adding Assumption 5 (normality) yields the **Classical Normal Regression Model** (CNRM).

The matrix calculus derivation of $\hat{\boldsymbol{\beta}}$, the fundamental decomposition, and the conditions under which t-statistics are valid are developed in full in [Appendix A](../appendices/A-ols-derivation.md).

---

<div class="annotate" markdown>

!!! theorem "Assumption 1: Zero Mean"
    $$\mathbb{E}[\epsilon_t] = 0$$

    (Read: the expected value of epsilon-sub-t equals zero.)

The errors have zero mean — the model has no systematic bias. On average, it neither over-predicts nor under-predicts. (1)

</div>

1.  **Common alternative forms:**
    - $\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0$ — the conditional form, which is stronger and subsumes exogeneity (Assumption 4). Some texts (e.g., Wooldridge 2020) combine A1 and A4 into this single condition
    - $\mu_\epsilon = 0$ — compact scalar notation in introductory texts
    - Note: A1 follows automatically from A4 (strict exogeneity) when the model includes an intercept $\beta_1$, by the law of iterated expectations: $\mathbb{E}[\epsilon_t] = \mathbb{E}[\mathbb{E}[\epsilon_t \mid \mathbf{X}]] = 0$

#### Violation in time series

When $y_t$ contains a **deterministic trend** — for example, GDP growing over time — and time $t$ is omitted as a regressor, the conditional mean of the error becomes a function of time:

$$\mathbb{E}[\epsilon_t] = f(t) \neq 0$$

(Read: the expected value of epsilon-sub-t equals f-of-t, not equal to zero.)

The errors carry a systematic upward or downward drift that varies with position in the sample. The model has not accounted for this time-varying mean.

A subtler violation arises with **seasonal data** (monthly sales, quarterly earnings): the mean of $\epsilon_t$ shifts predictably every cycle. An OLS model that omits seasonal terms produces errors whose conditional mean oscillates, violating this assumption on a regular schedule.

---

<div class="annotate" markdown>

!!! theorem "Assumption 2: Homoskedasticity"
    $$\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] = \sigma^2 \quad \forall \ t$$

    (Read: the expected value of epsilon-sub-t-squared, given X, equals sigma-squared, for all t.)

The variance of the error is constant across all observations and does not depend on the regressors or on time. (1)

</div>

1.  **Common alternative forms:**
    - $\text{Var}(\epsilon_t) = \sigma^2$ — unconditional form, common in introductory texts
    - $\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2 \mathbf{I}$ — the matrix form, seen in Greene (2018) and Wooldridge (2010), which packages both Assumption 2 and 3 together

#### Violation in time series

The variance of many time series changes over time rather than remaining constant. In financial data, large price moves cluster together — this is **volatility clustering**, formalized by Engle (1982) as ARCH:

$$\text{Var}(\epsilon_t \mid \mathcal{F}_{t-1}) = \alpha_0 + \alpha_1 \epsilon_{t-1}^2$$

(Read: the variance of epsilon-sub-t, given the information set F-sub-t-minus-1, equals alpha-zero plus alpha-one times epsilon-sub-t-minus-1-squared.)

where $\mathcal{F}_{t-1}$ denotes all information available up to $t-1$ (Engle 1982). The variance now depends on the past error, so $\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] \neq \sigma^2$. OLS ignores this structure and estimates a single pooled $\hat{\sigma}^2$ across the entire sample. The consequence is **inefficient estimation**: OLS is no longer BLUE because a GLS estimator that accounts for $\boldsymbol{\Omega}$ would down-weight high-variance periods and up-weight low-variance periods.

Furthermore, the conventional OLS standard errors $\hat{\sigma}^2 (\mathbf{X}^T\mathbf{X})^{-1}$ are **inconsistent** for the true variance of $\hat{\boldsymbol{\beta}}$ under heteroskedasticity — they converge to the wrong quantity as $T \rightarrow \infty$ (White 1980).

---

<div class="annotate" markdown>

!!! theorem "Assumption 3: No Serial Correlation"
    $$\mathbb{E}[\epsilon_t \epsilon_s \mid \mathbf{X}] = 0 \quad \forall \ t \neq s$$

    (Read: the expected value of epsilon-sub-t times epsilon-sub-s, given X, equals zero, for all t not equal to s.)

The error at time $t$ carries no information about the error at any other time $s$. Knowing that the model over-predicted yesterday provides no information about today's prediction error. (1)

</div>

1.  **Common alternative forms:**
    - $\text{Cov}(\epsilon_t, \epsilon_s) = 0$ — unconditional covariance form, seen widely in introductory econometrics
    - $\rho = 0$ where $\epsilon_t = \rho \epsilon_{t-1} + u_t$ — the AR(1) parameterization, common in applied papers testing for autocorrelation
    - The matrix form packaging Assumptions 2 and 3 together: $\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2\mathbf{I}$

#### Violation in time series — the most consequential failure

Time series observations are collected sequentially, so each observation is structurally linked to those that precede it. Yesterday's GDP affects today's GDP. Last month's temperature affects this month's temperature. This sequential dependence produces **autocorrelation**: errors are correlated across time.

Define the autocovariance at lag $k$:

$$\gamma(k) = \mathbb{E}[\epsilon_t \epsilon_{t-k} \mid \mathbf{X}]$$

(Read: gamma-of-k equals the expected value of epsilon-sub-t times epsilon-sub-t-minus-k, given X.)

Assumption 3 requires $\gamma(k) = 0$ for all $k \neq 0$. In practice, $\gamma(1)$ is almost never zero in raw time series data.

When this assumption fails, the true error covariance matrix is no longer $\sigma^2 \mathbf{I}$; it becomes:

$$\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2 \boldsymbol{\Omega}, \quad \boldsymbol{\Omega} \neq \mathbf{I}$$

(Read: the expected value of epsilon-epsilon-transpose, given X, equals sigma-squared times Omega, where Omega is not the identity matrix.)

Here:

- $\mathbf{I}$ is the $T \times T$ **identity matrix** — a square matrix with ones on the main diagonal and zeros everywhere else. In the error covariance context, the diagonal ones mean every error has the same variance $\sigma^2$, and the off-diagonal zeros mean no two errors are correlated. For $T = 3$:

$$\mathbf{I}_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

- $\boldsymbol{\Omega}$ is a $T \times T$ **symmetric positive-definite matrix**. Symmetric means the matrix equals its own transpose ($\boldsymbol{\Omega} = \boldsymbol{\Omega}^T$), which reflects the fact that $\text{Cov}(\epsilon_t, \epsilon_s) = \text{Cov}(\epsilon_s, \epsilon_t)$. Positive-definite ensures all variances are strictly positive and the matrix is invertible. The diagonal entries encode heteroskedasticity (time-varying variance); the off-diagonal entries encode serial correlation. For $T = 3$ errors following an AR(1) process with correlation $\rho$:

$$\boldsymbol{\Omega} = \begin{pmatrix} 1 & \rho & \rho^2 \\ \rho & 1 & \rho \\ \rho^2 & \rho & 1 \end{pmatrix}$$

When $\rho = 0$, $\boldsymbol{\Omega}$ collapses to $\mathbf{I}$, recovering Assumption 3.

The true variance of $\hat{\boldsymbol{\beta}}$ is then:

$$\text{Var}(\hat{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2 (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \boldsymbol{\Omega} \mathbf{X} (\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the variance of beta-hat, given X, equals sigma-squared times X-transpose-X-inverse, times X-transpose-Omega-X, times X-transpose-X-inverse.)

OLS, however, reports:

$$\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = \hat{\sigma}^2 (\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the estimated variance of beta-hat equals sigma-hat-squared times X-transpose-X-inverse.)

These two expressions are different objects. The reported standard errors are **wrong**. With positive autocorrelation — the common case — OLS **understates** the true standard errors, so t-statistics are inflated and null hypotheses are rejected too often (Wooldridge 2020, chap. 12).

The point estimate $\hat{\boldsymbol{\beta}}$ remains **unbiased** — the estimate is correct on average — but the standard errors used to assess its reliability are not.

---

<div class="annotate" markdown>

!!! theorem "Assumption 4: Strict Exogeneity"
    $$\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0$$

    (Read: the expected value of epsilon-sub-t, given X, equals zero.)

The error at any time $t$ is uncorrelated with the regressors at *all* time periods — past, present, and future. No regressor in the entire design matrix $\mathbf{X}$ carries information about $\epsilon_t$. (1)

</div>

1.  **Common alternative forms:**
    - **Contemporaneous exogeneity**: $\mathbb{E}[\epsilon_t \mid \mathbf{x}_t] = 0$ — the error is uncorrelated with regressors at time $t$ only. Weaker than strict exogeneity; sufficient for consistency in the cross-sectional case and in stationary time series under standard regularity conditions (law of large numbers, bounded moments), but not for finite-sample unbiasedness. In time series with serially correlated regressors, the law of large numbers requires that the dependence between observations decay fast enough as the time gap grows — formally, the process must be *weakly dependent* (sometimes called *mixing*): the influence of $\mathbf{x}_t$ on $\mathbf{x}_{t+k}$ must shrink to zero as $k \to \infty$. Without this decay, sample averages may not converge to population means, and the OLS estimator $\hat{\boldsymbol{\beta}}$ may fail to be *consistent* — meaning it does not converge to the true $\boldsymbol{\beta}$ as the sample size $T \to \infty$ — even when $\mathbb{E}[\epsilon_t \mid \mathbf{x}_t] = 0$ holds
    - **Weak exogeneity / Predetermined regressors**: $\mathbb{E}[\epsilon_t \mid \mathbf{x}_1, ..., \mathbf{x}_t] = 0$ — the error is uncorrelated with current and past regressors only, allowing future regressors to correlate with it. This is the relevant form for dynamic models
    - $\text{Cov}(\mathbf{x}_t, \epsilon_t) = 0$ — the covariance form, common in older literature. Note this is weaker than the conditional mean form
    - Note: A4 holds automatically when $\mathbf{x}_t$ is deterministic (non-random) — hence sometimes called the **nonstochastic regressor assumption**

#### Violation in time series — structural and unavoidable with lagged regressors

In time series, **strict exogeneity is violated by construction** whenever a lagged dependent variable appears as a regressor. Consider the AR(1) model:

$$y_t = \beta y_{t-1} + \epsilon_t$$

(Read: y-sub-t equals beta times y-sub-t-minus-1 plus epsilon-sub-t.)

Here $\mathbf{x}_t = y_{t-1}$. The condition $\mathbb{E}[\epsilon_t \mid y_1, y_2, \ldots, y_T] = 0$ fails because $\epsilon_t$ affects $y_t$, which affects $y_{t+1}$, which is a future value of the regressor. Therefore $\text{Cov}(y_{t+1}, \epsilon_t) \neq 0$, and strict exogeneity fails.

Weak exogeneity, defined as $\mathbb{E}[\epsilon_t \mid y_{t-1}, y_{t-2}, \ldots] = 0$, holds as long as $\epsilon_t$ is not autocorrelated. For this reason, time series econometrics **replaces strict exogeneity with predetermined regressors** and relies on weak exogeneity together with large-sample ($T \rightarrow \infty$) asymptotics, rather than finite-sample Gauss-Markov results (Hamilton 1994, chap. 8).

A more severe violation arises from **simultaneity** — when $y_t$ and $\mathbf{x}_t$ jointly determine each other, as in the simultaneous determination of supply and price in a market equilibrium model. OLS is **biased and inconsistent** under simultaneity, not merely inefficient.

---

<div class="annotate" markdown>

!!! theorem "Assumption 5: Normality"
    $$\epsilon_t \mid \mathbf{X} \sim \mathcal{N}(0, \sigma^2)$$

    (Read: epsilon-sub-t given X is distributed as Normal with mean zero and variance sigma-squared.)

The errors follow a normal distribution with mean zero and constant variance. Normality is what allows exact t-distributions and F-distributions for hypothesis tests in finite samples. (1)

</div>

1.  **Common alternative forms:**
    - $\boldsymbol{\epsilon} \mid \mathbf{X} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$ — the full vector form
    - Assumptions 1, 2, 3 and 5 together can be compactly expressed as $\epsilon_t \sim \text{i.i.d.} \ \mathcal{N}(0, \sigma^2)$ or $\text{n.i.d.}(0, \sigma^2)$ — the errors are independently and identically (normally) distributed with zero mean and constant variance
    - In large-sample work, normality is often dropped entirely and replaced by: $\sqrt{T}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{Q}^{-1})$ where $\mathbf{Q} = \text{plim}\frac{1}{T}\mathbf{X}^T\mathbf{X}$ — the asymptotic normality result

#### When and how this fails in time series

Unlike the previous four assumptions, normality is not structurally tied to temporal ordering — many time series have approximately normal errors. The common failures arise in specific domains. High-frequency financial data and volatile processes exhibit **fat tails** (leptokurtosis) and **asymmetry** (skewness): the normal distribution assigns near-zero probability to extreme deviations, yet in daily stock returns such deviations occur far more often than a Gaussian model predicts.

Define excess kurtosis (with $\mathbb{E}[\epsilon_t] = 0$ from Assumption 1):

$$\kappa = \frac{\mathbb{E}[\epsilon_t^4]}{\sigma^4} - 3$$

(Read: kappa equals the expected value of epsilon-sub-t-to-the-fourth, divided by sigma-to-the-fourth, minus three.)

For a normal distribution, $\kappa = 0$. For daily stock returns, $\kappa$ typically lies between 4 and 20 (Cont 2001).

The skewness $\gamma_1 = \mathbb{E}[\epsilon_t^3]/\sigma^3$ is also often non-zero. Financial returns tend to be **left-skewed** — large losses occur more often than large gains — while certain macroeconomic series are right-skewed during expansions.

The practical consequences depend on sample size. By the Central Limit Theorem, the distribution of $\hat{\boldsymbol{\beta}}$ converges to normal asymptotically regardless of the error distribution. Normality therefore matters most in **small samples**, where finite-sample t and F tests require it for validity. Convergence is slow when tails are heavy, which is the time series setting where this matters most. For problems such as volatility modeling, non-normality is the phenomenon of interest, not merely an inconvenient property to work around.

---

### How Each Violation Propagates

OLS produces three distinct outputs — the point estimate $\hat{\boldsymbol{\beta}}$, the standard errors $\hat{\text{se}}(\hat{\boldsymbol{\beta}})$, and the test statistics — and each is vulnerable to different assumptions. The table below maps each violation to the specific component it corrupts.

| Assumption | Violation | Point estimate $\hat{\boldsymbol{\beta}}$ | Standard errors | t / F tests |
|---|---|---|---|---|
| A1 Zero mean | Omitted trend, seasonality | Biased | Wrong | Invalid |
| A2 Homoskedasticity | Volatility clustering (ARCH) | Unbiased | Inconsistent | Invalid |
| A3 No serial correlation | Autocorrelated errors | Unbiased | Inconsistent | Invalid |
| A4 Exogeneity | Lagged DVs, simultaneity | Biased and inconsistent | Wrong | Invalid |
| A5 Normality | Fat tails, skewness | Unbiased | Correct asymptotically | Exact only in large samples |

Three patterns emerge. Violations of A2 and A3 leave $\hat{\boldsymbol{\beta}}$ unbiased but corrupt the standard errors and all downstream tests — a deceptive situation in which point estimates look reasonable while inference is invalid. Violations of A1 and A4 corrupt $\hat{\boldsymbol{\beta}}$ itself; no correction to standard errors can fix a biased or inconsistent estimator. A5 is the only violation that leaves both $\hat{\boldsymbol{\beta}}$ and standard errors asymptotically correct; it affects only the finite-sample distributional claim that makes exact t and F critical values valid.

---

### Summary: What Breaks and What Doesn't

| Assumption | Requirement | Time Series Violation | What Breaks in OLS |
|---|---|---|---|
| **Zero Mean** | $\mathbb{E}[\epsilon_t] = 0$ | Trends, seasonality | Biased $\hat{\boldsymbol{\beta}}$ |
| **Homoskedasticity** | $\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] = \sigma^2$ | Volatility clustering (ARCH) | Inefficient $\hat{\boldsymbol{\beta}}$, biased $\hat{\sigma}^2$ |
| **No Serial Correlation** | $\mathbb{E}[\epsilon_t\epsilon_s \mid \mathbf{X}] = 0$ | Autocorrelation | Wrong standard errors, invalid inference |
| **Exogeneity** | $\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0$ | Lagged DVs, simultaneity | Biased and inconsistent $\hat{\boldsymbol{\beta}}$ |
| **Normality** | $\epsilon_t \mid \mathbf{X} \sim \mathcal{N}(0,\sigma^2)$ | Fat tails, skewness (domain-specific, not structural) | Invalid finite-sample t and F tests |

The table reveals a critical hierarchy. Violations of Assumptions 2 and 3 leave $\hat{\boldsymbol{\beta}}$ **unbiased but unreliable**: the estimate is correct on average, but the standard errors and test statistics are not. Violations of Assumptions 1 and 4 render $\hat{\boldsymbol{\beta}}$ **biased or inconsistent** — the estimate itself is wrong. This hierarchy determines which violations to address first.


**[Next: General Flowchart →](../01-master-flowchart/01-general-flowchart.md)**
