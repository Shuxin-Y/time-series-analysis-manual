# Introduction

---
## **What is Time Series Analysis?**

Time series analysis is the study of data points collected or recorded at successive time intervals. Unlike cross-sectional data (snapshots at a single point in time), time series data has inherent temporal structure that we must respect and leverage.

A time-series is simply a sequence of data points indexed in time order. What makes it fundamentally different from regular tabular data is **temporal dependence** — observations are not independent of each other. Yesterday's stock price influences today's. Last month's temperature influences this month's. That single fact changes almost everything about how we model it.


**Examples of time series data:**

- Stock prices recorded every second
- Monthly unemployment rates
- Daily temperature measurements
- Quarterly GDP figures
- Sensor readings from industrial equipment


## **Time Domain vs Frequency Domain**

Time series analysis operates in two complementary domains:

### Time Domain
- Analyze values as they change over time (observation by observation)
- Models describe how current values depend on past values
- **Use when:** questions are about predictability, causality, "what happens next"
- **Methods:** ARIMA, VAR, GARCH, state-space models, etc. 

### Frequency Domain
- Decompose signals into sine and cosine waves
- Reveals energy distribution across frequencies
- **Use when:** questions involve periodicity, cycles, spectral content
- **Methods:** Fourier transform, PSD, filtering, wavelets, ect.

**In practice**, skilled analysts move between domains:
1. Start in time domain (check trends, autocorrelation, etc.)
2. Move to frequency domain (find hidden cycles)
3. Return to time domain (build forecasting model with periodic components)


---

## **The 5 Classical OLS Assumptions and How Time Series Violates Them**


The simple linear regression model is:

$$y_t = \mathbf{x}_t^T \boldsymbol{\beta} + \epsilon_t, t = 1, \dots, T$$

(Read: y-sub-t equals x-sub-t-transpose times beta plus epsilon-sub-t, for t from 1 to T.)

where $\mathbf{x}_t$ is a vector of regressors and $\boldsymbol{\beta}$ is the coefficient vector we estimate via OLS:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

(Read: beta-hat equals X-transpose-X-inverse times X-transpose-y.)

The entire edifice of OLS (Ordinary Least Squares) estimation rests on a set of assumptions collectively known as the Gauss-Markov conditions. And it's **BLUE** — Best Linear Unbiased Estimator — only when those assumptions hold. Assumptions 1–4 are the **Gauss-Markov assumptions** — under these, the model is called the **Classical Regression Model** (CRM). Adding Assumption 5 (normality) yields the **Classical Normal Regression Model** (CNRM).


<div class="annotate" markdown>

!!! theorem "Assumption 1: Zero Mean"
    $$\mathbb{E}[\epsilon_t] = 0$$

    (Read: the expected value of epsilon-sub-t equals zero.)

The errors have zero mean — the model has no systematic bias. On average, it neither over-predicts nor under-predicts. (1)

</div>

1.  **Common alternative forms:**
    - $\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0$ — the conditional form, which is stronger and subsumes exogeneity (Assumption 4). Some texts (e.g., Wooldridge, 2020) combine A1 and A4 into this single condition
    - $\mu_\epsilon = 0$ — compact scalar notation in introductory texts
    - Note: A1 follows automatically from A4 (strict exogeneity) when the model includes an intercept $\beta_1$, by the law of iterated expectations: $\mathbb{E}[\epsilon_t] = \mathbb{E}[\mathbb{E}[\epsilon_t \mid \mathbf{X}]] = 0$

**How time series violates this:**

If $y_t$ has a **deterministic trend** — say, GDP growing over time — and we don't include time $t$ as a regressor, then:

$$\mathbb{E}[\epsilon_t] = f(t) \neq 0$$

(Read: the expected value of epsilon-sub-t equals f-of-t, not equal to zero.)

The errors are not mean-zero; they carry a systematic upward or downward drift depending on where we are in the sample. The mean of the error is a function of time itself, which our model hasn't accounted for.

More subtly, with **seasonal data** (monthly sales, quarterly earnings), the mean of $\epsilon_t$ shifts predictably every cycle. An OLS model with no seasonal terms will have errors whose conditional mean oscillates — violating this assumption periodically and predictably.

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

**How time series violates this:**

The variance of many time series is not constant — it **changes over time**. In financial data, large moves are followed by more large moves. This is **volatility clustering**, formalized by Engle (1982) as ARCH:

$$\text{Var}(\epsilon_t \mid \mathcal{F}_{t-1}) = \alpha_0 + \alpha_1 \epsilon_{t-1}^2$$

(Read: the variance of epsilon-sub-t, given the information set F-sub-t-minus-1, equals alpha-zero plus alpha-one times epsilon-sub-t-minus-1-squared.)

where $\mathcal{F}_{t-1}$ is all information up to $t-1$. *(Engle, R.F., Econometrica, 1982)*

Notice the variance now depends on the *past error*, so $\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] \neq \sigma^2$. OLS ignores this entirely — it estimates one pooled $\hat{\sigma}^2$ across the whole sample. The consequence is **inefficient estimates**: OLS is no longer BLUE because a GLS estimator that accounts for $\boldsymbol{\Omega}$ would use the changing variance to down-weight noisy periods and up-weight calm periods. OLS treats all observations equally when it shouldn't.

Moreover, the conventional OLS standard errors $\hat{\sigma}^2 (\mathbf{X}^T\mathbf{X})^{-1}$ are **inconsistent** for the true variance of $\hat{\boldsymbol{\beta}}$ under heteroskedasticity — they converge to the wrong quantity as $T \rightarrow \infty$. *(White, H., Econometrica, 1980)*

---

<div class="annotate" markdown>

!!! theorem "Assumption 3: No Serial Correlation"
    $$\mathbb{E}[\epsilon_t \epsilon_s \mid \mathbf{X}] = 0 \quad \forall \ t \neq s$$

    (Read: the expected value of epsilon-sub-t times epsilon-sub-s, given X, equals zero, for all t not equal to s.)

The error at time $t$ carries no information about the error at any other time $s$. Knowing we overpredicted yesterday tells us nothing about today's prediction error. (1)

</div>

1.  **Common alternative forms:**
    - $\text{Cov}(\epsilon_t, \epsilon_s) = 0$ — unconditional covariance form, seen widely in introductory econometrics
    - $\rho = 0$ where $\epsilon_t = \rho \epsilon_{t-1} + u_t$ — the AR(1) parameterization, common in applied papers testing for autocorrelation
    - The matrix form packaging Assumptions 2 and 3 together: $\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2\mathbf{I}$

**How time series violates this — and why it's the most dangerous violation:**

Time series observations are collected sequentially. Yesterday's GDP affects today's GDP. Last month's temperature affects this month's temperature. This produces **autocorrelation**: errors are correlated across time.

Define the autocovariance at lag $k$:

$$\gamma(k) = \mathbb{E}[\epsilon_t \epsilon_{t-k} \mid \mathbf{X}]$$

(Read: gamma-of-k equals the expected value of epsilon-sub-t times epsilon-sub-t-minus-k, given X.)

Assumption 3 requires $\gamma(k) = 0$ for all $k \neq 0$. In practice, $\gamma(1)$ is almost never zero in raw time series data.

When this is violated, the true error covariance matrix is no longer $\sigma^2 \mathbf{I}$ — it becomes:

$$\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T \mid \mathbf{X}] = \sigma^2 \boldsymbol{\Omega}, \quad \boldsymbol{\Omega} \neq \mathbf{I}$$

(Read: the expected value of epsilon-epsilon-transpose, given X, equals sigma-squared times Omega, where Omega is not the identity matrix.)

The true variance of $\hat{\boldsymbol{\beta}}$ is then:

$$\text{Var}(\hat{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2 (\mathbf{X}^T\mathbf{X})^{-1} \mathbf{X}^T \boldsymbol{\Omega} \mathbf{X} (\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the variance of beta-hat, given X, equals sigma-squared times X-transpose-X-inverse, times X-transpose-Omega-X, times X-transpose-X-inverse.)

But OLS reports:

$$\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = \hat{\sigma}^2 (\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the estimated variance of beta-hat equals sigma-hat-squared times X-transpose-X-inverse.)

These two expressions are different objects. Our reported standard errors are **wrong**. With positive autocorrelation (the common case), OLS **understates** the true standard errors, so t-statistics are inflated and we reject null hypotheses far too often. *(Wooldridge, J.M., Introductory Econometrics, 7th ed., 2020 — Chapter 12)*

Note: $\hat{\boldsymbol{\beta}}$ remains **unbiased** — the point estimate isn't wrong, but everything we use to judge its reliability is.

---

<div class="annotate" markdown>

!!! theorem "Assumption 4: Strict Exogeneity"
    $$\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0$$

    (Read: the expected value of epsilon-sub-t, given X, equals zero.)

The error at any time $t$ is uncorrelated with the regressors at *all* time periods — past, present, and future. No regressor in the entire design matrix $\mathbf{X}$ carries information about $\epsilon_t$. (1)

</div>

1.  **Common alternative forms:**
    - **Contemporaneous exogeneity**: $\mathbb{E}[\epsilon_t \mid \mathbf{x}_t] = 0$ — the error is uncorrelated with regressors at time $t$ only. Weaker than strict exogeneity; sufficient for consistency but not for finite-sample unbiasedness
    - **Weak exogeneity / Predetermined regressors**: $\mathbb{E}[\epsilon_t \mid \mathbf{x}_1, ..., \mathbf{x}_t] = 0$ — the error is uncorrelated with current and past regressors only, allowing future regressors to correlate with it. This is the relevant form for dynamic models
    - $\text{Cov}(\mathbf{x}_t, \epsilon_t) = 0$ — the covariance form, common in older literature. Note this is weaker than the conditional mean form
    - Note: A4 holds automatically when $\mathbf{x}_t$ is deterministic (non-random) — hence sometimes called the **nonstochastic regressor assumption**

**How time series violates this — uniquely and structurally:**

In time series, **strict exogeneity is almost always violated** by construction when we use lagged dependent variables. Consider the AR(1) model:

$$y_t = \beta y_{t-1} + \epsilon_t$$

(Read: y-sub-t equals beta times y-sub-t-minus-1 plus epsilon-sub-t.)

Here $\mathbf{x}_t = y_{t-1}$. Is $\mathbb{E}[\epsilon_t \mid y_1, y_2, ..., y_T] = 0$? No — because $\epsilon_t$ affects $y_t$, which affects $y_{t+1}$, which is a future value of the regressor. So $\text{Cov}(y_{t+1}, \epsilon_t) \neq 0$. Strict exogeneity fails.

What about weak exogeneity? $\mathbb{E}[\epsilon_t \mid y_{t-1}, y_{t-2}, ...] = 0$ — yes, this holds as long as $\epsilon_t$ is not autocorrelated. This is why time series econometrics **replaces strict exogeneity with predetermined/sequentially exogenous regressors** and relies on weak exogeneity plus large-sample ($T \rightarrow \infty$) asymptotics rather than finite-sample Gauss-Markov results. *(Hamilton, J.D., Time Series Analysis, Princeton University Press, 1994 — Chapter 8)*

The more catastrophic violation comes from **simultaneity** — when $y_t$ and $\mathbf{x}_t$ jointly determine each other. Supply and price in an economics model. OLS is **biased and inconsistent** in this case, not just inefficient.

---

<div class="annotate" markdown>

!!! theorem "Assumption 5: Normality"
    $$\epsilon_t \mid \mathbf{X} \sim \mathcal{N}(0, \sigma^2)$$

    (Read: epsilon-sub-t given X is distributed as Normal with mean zero and variance sigma-squared.)

The errors follow a normal distribution with mean zero and constant variance. This is what allows exact t-distributions and F-distributions for hypothesis tests in finite samples. (1)

</div>

1.  **Common alternative forms:**
    - $\boldsymbol{\epsilon} \mid \mathbf{X} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$ — the full vector form
    - Assumptions 1, 2, 3 and 5 together can be compactly expressed as $\epsilon_t \sim \text{i.i.d.} \ \mathcal{N}(0, \sigma^2)$ or $\text{n.i.d.}(0, \sigma^2)$ — the errors are independently and identically (normally) distributed with zero mean and constant variance
    - In large-sample work, normality is often dropped entirely and replaced by: $\sqrt{T}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{Q}^{-1})$ where $\mathbf{Q} = \text{plim}\frac{1}{T}\mathbf{X}^T\mathbf{X}$ — the asymptotic normality result

**When and how this fails in time series:**

Unlike the previous four assumptions, normality is not structurally tied to temporal ordering — many time series have approximately normal errors. The most common failures arise in high-frequency financial data and volatile processes: **fat tails** (leptokurtosis) and **asymmetry** (skewness). The normal distribution assigns near-zero probability to large deviations — but in daily stock returns and similar series, extreme observations ("black swans") occur far more frequently than a Gaussian model predicts.

Define excess kurtosis (recalling $\mathbb{E}[\epsilon_t] = 0$ from Assumption 1):

$$\kappa = \frac{\mathbb{E}[\epsilon_t^4]}{\sigma^4} - 3$$

(Read: kappa equals the expected value of epsilon-sub-t-to-the-fourth, divided by sigma-to-the-fourth, minus three.)

For a normal distribution, $\kappa = 0$. For daily stock returns, $\kappa$ is typically between 4 and 20. *(Cont, R., "Empirical Properties of Asset Returns," Quantitative Finance, 2001)*

Similarly, the skewness $\gamma_1 = \mathbb{E}[\epsilon_t^3]/\sigma^3$ is often non-zero — financial returns tend to be **left-skewed** (large losses are more common than large gains), while macroeconomic series can be right-skewed during expansions.

The practical consequences depend on sample size. By the **Central Limit Theorem**, the distribution of $\hat{\boldsymbol{\beta}}$ converges to normal asymptotically regardless of the error distribution — so normality matters most in **small samples**, where finite-sample t and F tests are not valid without it. However, convergence is slow when tails are heavy — precisely the time series setting where it matters most. For time series problems like volatility modeling, the non-normality itself *is* the phenomenon of interest, not just an inconvenient property to work around.

---

### Summary: What Breaks and What Doesn't

| Assumption | Requirement | Time Series Violation | What Breaks in OLS |
|---|---|---|---|
| **Zero Mean** | $\mathbb{E}[\epsilon_t] = 0$ | Trends, seasonality | Biased $\hat{\boldsymbol{\beta}}$ |
| **Homoskedasticity** | $\mathbb{E}[\epsilon_t^2 \mid \mathbf{X}] = \sigma^2$ | Volatility clustering (ARCH) | Inefficient $\hat{\boldsymbol{\beta}}$, biased $\hat{\sigma}^2$ |
| **No Serial Correlation** | $\mathbb{E}[\epsilon_t\epsilon_s \mid \mathbf{X}] = 0$ | Autocorrelation | Wrong standard errors, invalid inference |
| **Exogeneity** | $\mathbb{E}[\epsilon_t \mid \mathbf{X}] = 0$ | Lagged DVs, simultaneity | Biased and inconsistent $\hat{\boldsymbol{\beta}}$ |
| **Normality** | $\epsilon_t \mid \mathbf{X} \sim \mathcal{N}(0,\sigma^2)$ | Fat tails, skewness (domain-specific, not structural) | Invalid finite-sample t and F tests |

The critical distinction in that table: Assumptions 2 and 3 leave $\hat{\boldsymbol{\beta}}$ **unbiased but unreliable** (we have the right answer on average but can't trust our uncertainty estimates). Assumptions 1 and 4 make $\hat{\boldsymbol{\beta}}$ **biased or inconsistent** — the estimate itself is wrong. This hierarchy matters enormously when deciding which problems to prioritize fixing.




**[Next: General Flowchart →](../01-master-flowchart/01-general-flowchart.md)**
