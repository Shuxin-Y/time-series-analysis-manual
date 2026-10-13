# Asymptotics for Dependent Data

Estimators in this book are justified by large-sample arguments: a law of large numbers makes a sample average converge to an expectation, and a central limit theorem gives the limiting distribution that standard errors and tests rely on. For time series the two results rest on different conditions. The law of large numbers needs stationarity and ergodicity, with no rate at which dependence dies out. The central limit theorem needs a rate, or a martingale-difference structure, and it replaces the variance by the long-run variance. This chapter states both theorems for dependent data and the delta method that carries them to functions of the estimates; the conditions themselves are defined in [Stochastic Processes](stochastic-processes.md).

## Law of large numbers

A sequence of estimators \(\hat{\theta}_T\) **converges in probability** to \(\theta\), written \(\hat{\theta}_T \xrightarrow{p} \theta\), when for every \(\varepsilon > 0\) the probability \(P(|\hat{\theta}_T - \theta| > \varepsilon)\) tends to zero as \(T \to \infty\). An estimator with this property is **consistent**. Almost-sure convergence is stronger: the realised sequence itself converges with probability one.

The law of large numbers for a stationary time series is the ergodic theorem (Birkhoff 1931). If \(\{y_t\}\) is strictly stationary and ergodic with \(\mathbb{E}|y_1| < \infty\), then

\[\bar{y}_T = \frac{1}{T} \sum_{t=1}^{T} y_t \xrightarrow{\text{a.s.}} \mathbb{E}[y_1].\]

(Read: the sample mean of the first T observations converges almost surely to the expected value of y.)

No rate condition is needed. Two cases mark the boundary:

- For a stationary process that is not ergodic, the sample mean still converges, but to a random variable (the conditional expectation of \(y_1\) given the shift-invariant events), not to \(\mathbb{E}[y_1]\).
- A long-memory process such as ARFIMA(0, \(d\), 0) with \(0 < d < 1/2\) is ergodic and obeys the law of large numbers, yet its autocovariances are not summable and \(\text{Var}(\bar{y}_T)\) shrinks like \(T^{2d-1}\) instead of \(T^{-1}\).

Heterogeneous processes, whose distribution changes over time, have laws of large numbers under mixing and moment conditions instead of stationarity (Davidson 1994). Because a function of a stationary ergodic process is again stationary and ergodic, the theorem applies to sample autocovariances, to \(\frac{1}{T}\mathbf{X}^T\mathbf{X}\) in a regression with stationary regressors, and to average log-likelihoods.

## Central limit theorem

The **long-run variance** of a weakly stationary process with absolutely summable autocovariances is the limit of \(T\) times the variance of its sample mean:

\[\omega^2 = \lim_{T \to \infty} T\, \text{Var}(\bar{y}_T) = \sum_{k=-\infty}^{\infty} \gamma(k) = 2\pi f(0),\]

(Read: omega-squared equals the limit of T times the variance of the sample mean, which equals the sum of all autocovariances, and equals two pi times the spectral density at frequency zero.)

where \(f\) is the spectral density. For uncorrelated data \(\omega^2 = \gamma(0)\); positive autocorrelation makes \(\omega^2\) larger than the variance.

A sequence \(Z_T\) **converges in distribution** to a law \(D\), written \(Z_T \xrightarrow{d} D\), when its distribution function converges to that of \(D\) at every continuity point. The central limit theorem gives such a limit for the standardised sample mean. Two sets of conditions are used in this book:

- **Martingale differences** (Billingsley 1961; Ibragimov 1963): if \(\{\epsilon_t\}\) is a strictly stationary and ergodic martingale difference sequence with \(\mathbb{E}[\epsilon_t^2] = \sigma^2 < \infty\), then \(\sqrt{T}\, \bar{\epsilon}_T \xrightarrow{d} \mathcal{N}(0, \sigma^2)\). Scores of correctly specified likelihoods and the products \(\mathbf{x}_t \epsilon_t\) of a regression with predetermined regressors and MDS errors have this form.
- **Mixing** (Ibragimov 1962; White 2001, ch. 5): if \(\{y_t\}\) is strictly stationary with \(\mathbb{E}|y_t|^r < \infty\) for some \(r > 2\) and strong-mixing coefficients satisfying \(\sum_k \alpha(k)^{1 - 2/r} < \infty\), then \(\sqrt{T}(\bar{y}_T - \mu) \xrightarrow{d} \mathcal{N}(0, \omega^2)\) with \(\omega^2 > 0\).

Here the rate matters: the mixing coefficients must decay fast enough, and moments beyond the second must exist. A long-memory process violates the summability, \(\omega^2\) is infinite, and the sample mean needs the normalisation \(T^{1/2 - d}\). Heteroskedasticity-and-autocorrelation-consistent (HAC) standard errors estimate \(\omega^2\) (or its matrix version) by a kernel-weighted sum of sample autocovariances (Newey and West 1987).

## Delta method

Standard errors are often needed for functions of estimated parameters: a long-run multiplier, the persistence \(\alpha_1 + \beta_1\) of a GARCH model, an impulse response, a half-life. If \(\sqrt{T}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})\) and \(g\) is differentiable at \(\boldsymbol{\theta}\) with gradient \(\nabla g(\boldsymbol{\theta}) \neq \mathbf{0}\), then

\[\sqrt{T}\big(g(\hat{\boldsymbol{\theta}}) - g(\boldsymbol{\theta})\big) \xrightarrow{d} \mathcal{N}\big(0,\ \nabla g(\boldsymbol{\theta})^T\, \boldsymbol{\Sigma}\, \nabla g(\boldsymbol{\theta})\big).\]

(Read: root T times the difference between g of theta-hat and g of theta converges in distribution to a normal with variance equal to the gradient of g, transposed, times Sigma, times the gradient of g.)

The approximation is poor where \(g\) is strongly nonlinear over the range of plausible estimates, for example a half-life \(\log(0.5)/\log(\hat{\phi})\) with \(\hat{\phi}\) near 1; the bootstrap or a confidence interval for \(\phi\) mapped through \(g\) is then used instead.

## References

- Billingsley, P. 1961. "The Lindeberg-Lévy Theorem for Martingales." *Proceedings of the American Mathematical Society* 12 (5): 788–792.
- Birkhoff, G. D. 1931. "Proof of the Ergodic Theorem." *Proceedings of the National Academy of Sciences* 17 (12): 656–660.
- Davidson, J. 1994. *Stochastic Limit Theory*. Oxford: Oxford University Press.
- Ibragimov, I. A. 1962. "Some Limit Theorems for Stationary Processes." *Theory of Probability and Its Applications* 7 (4): 349–382.
- Ibragimov, I. A. 1963. "A Central Limit Theorem for a Class of Dependent Random Variables." *Theory of Probability and Its Applications* 8 (1): 83–89.
- Newey, W. K., and K. D. West. 1987. "A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix." *Econometrica* 55 (3): 703–708.
- White, H. 2001. *Asymptotic Theory for Econometricians*. Revised ed. San Diego: Academic Press.
