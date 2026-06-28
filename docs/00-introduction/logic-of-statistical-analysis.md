# Recall on The Logic of Statistical Analysis

Every statistical analysis rests on three components: a **model class**, an **estimator**, and a **statistical test**.

## Model Class

!!! definition "Model Class"
    A **model class** is a family of probability distributions or functional forms indexed by unknown parameters. It encodes the analyst's assumptions about how the data are generated — what depends on what, and through which channels.

A model class is a *form*, not a set of numbers. It says, for example, that the conditional mean of $y_t$ depends linearly on a feature vector, or that the conditional variance follows a particular recursion. Filling in numbers is the job of the estimator; choosing the form is a substantive decision about the data-generating process.

Three model classes used in this manual illustrate the breadth of the concept:

- **Linear regression**: $y_t = \mathbf{x}_t^T \boldsymbol{\beta} + \epsilon_t$, with $\epsilon_t$ iid. The unknown parameters are the coefficient vector $\boldsymbol{\beta}$ and the error variance $\sigma^2$.
- **ARMA(p, q)**: $y_t = \sum_{j=1}^p \phi_j y_{t-j} + \sum_{k=1}^q \theta_k \epsilon_{t-k} + \epsilon_t$. The unknowns are the autoregressive coefficients $\{\phi_j\}$, the moving-average coefficients $\{\theta_k\}$, and $\sigma^2$.
- **GARCH(1, 1)**: $\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$. The unknowns are $\omega$, $\alpha$, and $\beta$.

These three describe different aspects of the data: the conditional mean given features, the temporal dependence of a univariate series, and the conditional variance. A complete specification often combines several — for example, a regression on features for the mean, an ARMA structure for the residual serial correlation, and a GARCH structure for the residual volatility.

## Estimator

!!! definition "Estimator"
    An **estimator** is a procedure that maps observed data to parameter values within a chosen model class.

Different estimators reflect different optimality criteria: minimizing prediction error, maximizing the probability of the data, matching theoretical and sample moments, fitting a frequency-domain criterion, or minimizing an empirical loss. The same model class can usually be fit by more than one estimator, and the choice affects efficiency, bias, and which assumptions must hold for valid inference.

### Ordinary Least Squares (OLS)

OLS chooses parameters that minimize the sum of squared residuals:

$$\hat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta}} \sum_{t=1}^T \left( y_t - \mathbf{x}_t^T \boldsymbol{\beta} \right)^2.$$

(Read: beta-hat is the argmin over beta of the sum over $t$ of the squared residual.)

For linear models with iid errors satisfying the Gauss–Markov conditions, OLS is the best linear unbiased estimator (BLUE). It admits a closed-form solution, requires no distributional assumption beyond second moments, and applies to any model whose errors are iid white noise — including linear regression on exogenous features, pure autoregression AR($p$), and vector autoregression (VAR).

### Maximum Likelihood (MLE)

MLE chooses parameters that maximize the likelihood of the observed data under the model:

$$\hat{\boldsymbol{\theta}} = \arg\max_{\boldsymbol{\theta}} L(\boldsymbol{\theta}; y_1, \dots, y_T).$$

(Read: theta-hat is the argmax over theta of the likelihood of theta given the observed data.)

MLE is the standard estimator when the model contains components that are not directly observable from the data — moving-average innovations, latent states, conditional variances. ARMA, ARIMA, ARIMAX, state-space models, and the GARCH family are all fit by MLE. Under regularity conditions, MLE attains the Cramér–Rao lower bound asymptotically and is therefore efficient.

### Generalized Method of Moments (GMM)

GMM chooses parameters that make sample moment conditions match their theoretical counterparts. Given a vector of moment conditions $\mathbb{E}[g(y_t, \boldsymbol{\theta})] = 0$ implied by the model, GMM minimizes a weighted quadratic form in the sample analogue:

$$\hat{\boldsymbol{\theta}} = \arg\min_{\boldsymbol{\theta}} \left( \frac{1}{T}\sum_t g(y_t, \boldsymbol{\theta}) \right)^T W \left( \frac{1}{T}\sum_t g(y_t, \boldsymbol{\theta}) \right),$$

(Read: theta-hat is the argmin over theta of the sample moment condition transposed times $W$ times the sample moment condition.)

where $W$ is a positive-definite weighting matrix. GMM is the natural choice when the full likelihood is intractable or when the analyst is willing to specify only a subset of the data-generating process. It underpins instrumental variable estimation, dynamic panel models (Arellano and Bond, 1991), and many macroeconomic Euler-equation analyses.

### Spectral / Whittle Estimation

Spectral estimators work in the frequency domain rather than the time domain. The Whittle (1953) likelihood approximates the Gaussian likelihood using the periodogram $I(\omega_j)$ and the model's spectral density $f(\omega_j; \boldsymbol{\theta})$:

$$\hat{\boldsymbol{\theta}} = \arg\min_{\boldsymbol{\theta}} \sum_j \left[ \log f(\omega_j; \boldsymbol{\theta}) + \frac{I(\omega_j)}{f(\omega_j; \boldsymbol{\theta})} \right].$$

(Read: theta-hat is the argmin over theta of the sum over frequencies of log spectral density plus the periodogram divided by the spectral density.)

Spectral methods are the natural choice for long-memory models (ARFIMA), for analyses where cyclical structure is the object of interest, and for cases where time-domain likelihood evaluation is computationally prohibitive.

### Empirical Loss Minimization (Machine Learning)

Modern machine learning estimators minimize an empirical loss by gradient descent or boosting:

$$\hat{\boldsymbol{\theta}} = \arg\min_{\boldsymbol{\theta}} \frac{1}{T} \sum_{t=1}^T \ell\left(y_t, \hat{y}_t(\boldsymbol{\theta})\right) + \lambda R(\boldsymbol{\theta}).$$

(Read: theta-hat is the argmin over theta of the average loss plus a regularization penalty.)

The loss $\ell$ is typically squared error or cross-entropy; $R$ is a regularization term such as an $L_2$ norm. This is the estimator used for recurrent and convolutional networks, transformers, and gradient-boosted trees applied to lagged features. It is neither closed-form nor likelihood-based, and the classical inference tools (t-statistics, Hessian-based confidence intervals) generally do not apply. Uncertainty is instead quantified through resampling (the bootstrap), distribution-free coverage guarantees (conformal prediction; Vovk, Gammerman, and Shafer, 2005), or model ensembles. Overall validity is assessed by out-of-sample performance rather than asymptotic theory.

### Choice of Estimator

A single model class can often be reached by more than one estimator. AR($p$) can be estimated by OLS on lagged values, by MLE under a Gaussian innovation assumption, by Whittle approximation in the frequency domain, or by an empirical-loss estimator with lag features. The choice is governed by which assumptions one is willing to make and by what efficiency or robustness is required. The dividing line between OLS and MLE in particular is sharp: OLS suffices when errors are iid white noise; MLE is required whenever the model contains unobservable error components such as moving-average innovations, latent states, or conditional variances.

## Statistical Test

!!! definition "Statistical Test"
    A **statistical test** is a procedure that, given a sample, returns a binary decision about a hypothesis concerning the parameters or the model itself.

A test has four components:

1. **Null hypothesis** $H_0$ — the statement to be challenged (for example, "the coefficient is zero," or "the series has a unit root").
2. **Alternative hypothesis** $H_1$ — what is concluded if $H_0$ is rejected.
3. **Test statistic** — a function of the data whose sampling distribution under $H_0$ is known or can be approximated.
4. **Decision rule** — reject $H_0$ when the test statistic exceeds a critical value, or equivalently when the p-value falls below the significance level $\alpha$.

Tests sit downstream of the estimator. A test statistic is built from a parameter estimate, and its sampling distribution depends on both the model class and the estimation procedure. Testing $H_0: \beta_j = 0$ via a t-statistic, for instance, requires that the OLS standard error is consistent — which in turn requires assumptions about the error structure that may or may not hold for time series data.

Tests in this manual fall into two groups:

- **Coefficient and restriction tests** — t-tests, F-tests, and the likelihood-ratio, Wald, and score (Lagrange-multiplier) tests. These interrogate parameter values within an already-fitted model.
- **Specification and diagnostic tests** — Augmented Dickey–Fuller (Dickey and Fuller, 1979) and KPSS (Kwiatkowski et al., 1992) for unit roots, Ljung–Box (1978) for residual autocorrelation, ARCH-LM (Engle, 1982) for conditional heteroskedasticity. These probe whether the assumed model class is itself adequate.

A failed diagnostic test typically points back to the model-class layer. Mild violations can sometimes be patched at the estimator layer instead — for example, heteroskedasticity or short-range autocorrelation in OLS residuals admit White (1980) or Newey–West (1987) robust standard errors without changing the model. A failed coefficient test refines the parameter set within the current class.


## References

- Arellano, M., and S. Bond. 1991. "Some Tests of Specification for Panel Data: Monte Carlo Evidence and an Application to Employment Equations." *Review of Economic Studies* 58 (2): 277–297.
- Dickey, D. A., and W. A. Fuller. 1979. "Distribution of the Estimators for Autoregressive Time Series with a Unit Root." *Journal of the American Statistical Association* 74 (366): 427–431.
- Engle, R. F. 1982. "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation." *Econometrica* 50 (4): 987–1007.
- Kwiatkowski, D., P. C. B. Phillips, P. Schmidt, and Y. Shin. 1992. "Testing the Null Hypothesis of Stationarity against the Alternative of a Unit Root." *Journal of Econometrics* 54 (1–3): 159–178.
- Ljung, G. M., and G. E. P. Box. 1978. "On a Measure of Lack of Fit in Time Series Models." *Biometrika* 65 (2): 297–303.
- Newey, W. K., and K. D. West. 1987. "A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix." *Econometrica* 55 (3): 703–708.
- Vovk, V., A. Gammerman, and G. Shafer. 2005. *Algorithmic Learning in a Random World*. New York: Springer.
- White, H. 1980. "A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct Test for Heteroskedasticity." *Econometrica* 48 (4): 817–838.
- Whittle, P. 1953. "Estimation and Information in Stationary Time Series." *Arkiv för Matematik* 2 (5): 423–434.
