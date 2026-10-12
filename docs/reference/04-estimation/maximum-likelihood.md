---
kind: theory
---
# Maximum likelihood

Theory page for the maximum-likelihood chain: joint density, likelihood, maximum likelihood, identification, the uniform law of large numbers and the pseudo-true value. The chain runs from the joint density of the sample, through the [chain rule of probability](../../00-foundations/stochastic-processes.md#chain-rule-of-probability) and the [prediction-error decomposition](index.md#prediction-error-decomposition), to the limit of the average log-likelihood under [stationarity and ergodicity](../../00-foundations/stochastic-processes.md#ergodicity-and-mixing).

## Joint density

The joint density $p(y_1, \ldots, y_T; \boldsymbol{\theta})$ describes the $T$ observations as one point in $\mathbb{R}^T$: it is the [probability density](../../00-foundations/stochastic-processes.md#probability-density) of the whole sample under the parameter value $\boldsymbol{\theta}$. For i.i.d. data it is the product of the marginal densities. For dependent data the information about $\boldsymbol{\theta}$ often sits in the relations between observations. In a Gaussian AR(1), $y_t = \phi y_{t-1} + \epsilon_t$ with $|\phi| < 1$ and $\epsilon_t$ i.i.d. $\mathcal{N}(0, \sigma^2)$, every $y_t$ has the marginal distribution $\mathcal{N}(0, \sigma^2 / (1 - \phi^2))$. The marginal fixes only the ratio $\sigma^2 / (1 - \phi^2)$, and it never reveals the sign of $\phi$; the joint density of consecutive values does.

## Likelihood

The **likelihood** is the joint density read as a function of the parameters, with the data fixed at their observed values:

$$L(\boldsymbol{\theta}) = p(y_1, \ldots, y_T; \boldsymbol{\theta}).$$

(Read: the likelihood of theta equals the joint density of the observed sample evaluated at theta.)

It is not a probability distribution over $\boldsymbol{\theta}$: it need not integrate to one over the parameter space. Multiplying it by a prior and normalising gives a posterior, which is the link to Bayesian estimation. By the chain rule, the log-likelihood of a time series is a sum of one-step conditional log-densities,

$$\log L(\boldsymbol{\theta}) = \log p(y_1; \boldsymbol{\theta}) + \sum_{t=2}^{T} \log p(y_t \mid y_{t-1}, \ldots, y_1; \boldsymbol{\theta}),$$

(Read: the log-likelihood equals the log-density of the first observation plus, for each later t, the log-density of y-sub-t given the earlier observations.)

which is the [prediction-error decomposition](index.md#prediction-error-decomposition). The **conditional likelihood** drops the terms for the first few observations and conditions on them; it differs from the exact likelihood by a term whose share vanishes as $T$ grows.

## Maximum-likelihood estimator

The **maximum-likelihood estimator** is the parameter value that makes the observed sample most probable under the model:

$$\hat{\boldsymbol{\theta}} = \arg\max_{\boldsymbol{\theta} \in \Theta} \log L(\boldsymbol{\theta}).$$

(Read: theta-hat is the value of theta in the parameter space that maximises the log-likelihood.)

Its consistency rests on four conditions, each with its own section:

1. The average log-likelihood converges: under stationarity and ergodicity, $\frac{1}{T} \log L(\boldsymbol{\theta})$ converges to $\ell(\boldsymbol{\theta}) = \mathbb{E}[\log p(y_t \mid y_{t-1}, y_{t-2}, \ldots; \boldsymbol{\theta})]$, the expected conditional log-density; the initial-condition term vanishes in the average ([law of large numbers](../../00-foundations/asymptotics.md#law-of-large-numbers)).
2. The limit is maximised at the true value $\boldsymbol{\theta}_0$, because $\ell(\boldsymbol{\theta}_0) - \ell(\boldsymbol{\theta})$ is an expected [KL divergence](../../00-foundations/stochastic-processes.md#kl-divergence) between conditional densities and is non-negative.
3. The maximiser is unique ([identification](#identification)).
4. The convergence in step 1 is uniform over a compact parameter space, so the maximiser of the sample objective converges to the maximiser of the limit ([uniform law of large numbers](#uniform-law-of-large-numbers)).

Under further regularity conditions the score $\partial \log L / \partial \boldsymbol{\theta}$ at $\boldsymbol{\theta}_0$ is a sum of martingale differences, the [central limit theorem](../../00-foundations/asymptotics.md#central-limit-theorem) applies to it, and $\sqrt{T}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0) \xrightarrow{d} \mathcal{N}(\mathbf{0}, \mathcal{I}(\boldsymbol{\theta}_0)^{-1})$, where $\mathcal{I}$ is the per-observation Fisher information. When the model is misspecified, $\hat{\boldsymbol{\theta}}$ converges to the [pseudo-true value](#pseudo-true-value) instead.

## Identification

A parameter is **identified** when distinct parameter values imply distinct distributions of the data: $\boldsymbol{\theta} \neq \boldsymbol{\theta}'$ implies $p(\cdot\,; \boldsymbol{\theta}) \neq p(\cdot\,; \boldsymbol{\theta}')$. For time series the condition is stated on the conditional densities of $y_t$ given its past. Without it the limit $\ell(\boldsymbol{\theta})$ has several maximisers, and no amount of data selects among them. Three cases recur:

- The AR(1) parameter is not identified from the marginal distribution alone (see [joint density](#joint-density)).
- An ARMA model with a common factor in its autoregressive and moving-average polynomials is not identified: the cancelling roots can take any value.
- An MA(1) with coefficient $\theta$ and one with $1/\theta$ have the same autocovariances; restricting to invertible models, $|\theta| < 1$, identifies the Gaussian likelihood.

## Uniform law of large numbers

Pointwise convergence of the average log-likelihood at each $\boldsymbol{\theta}$ does not make its maximiser converge: the sample objective can stay large somewhere far from $\boldsymbol{\theta}_0$ for every $T$. A **uniform law of large numbers** closes the gap:

$$\sup_{\boldsymbol{\theta} \in \Theta} \left| \frac{1}{T} \log L(\boldsymbol{\theta}) - \ell(\boldsymbol{\theta}) \right| \xrightarrow{p} 0.$$

(Read: the largest gap, over the parameter space, between the average log-likelihood and its limit converges in probability to zero.)

It holds for a stationary ergodic process when the parameter space $\Theta$ is compact, the log-density is continuous in $\boldsymbol{\theta}$, and $\mathbb{E}[\sup_{\boldsymbol{\theta}} |\log p(y_t \mid y_{t-1}, \ldots; \boldsymbol{\theta})|] < \infty$. Together with identification it gives consistency of the maximiser (Newey and McFadden 1994, Theorem 2.1). A concave log-likelihood, as in many linear Gaussian models, gives the same conclusion without compactness.

## Pseudo-true value

When no parameter value reproduces the true process, the maximum-likelihood estimator still converges, to the **pseudo-true value**

$$\boldsymbol{\theta}^* = \arg\max_{\boldsymbol{\theta}} \mathbb{E}\big[\log p(y_t \mid y_{t-1}, y_{t-2}, \ldots; \boldsymbol{\theta})\big],$$

(Read: theta-star is the parameter value that maximises the expected conditional log-density under the true process.)

which minimises the expected KL divergence from the true conditional density to the model's (White 1982). Whether $\boldsymbol{\theta}^*$ is useful depends on which parts of the model are correct. In a GARCH model fitted by the Gaussian likelihood to non-Gaussian innovations, the conditional mean and variance parameters are still consistent when the mean and variance equations are correctly specified (quasi-maximum likelihood; Bollerslev and Wooldridge 1992), and the standard errors take the sandwich form.

## References

- Bollerslev, T., and J. M. Wooldridge. 1992. "Quasi-Maximum Likelihood Estimation and Inference in Dynamic Models with Time-Varying Covariances." *Econometric Reviews* 11 (2): 143–172.
- Newey, W. K., and D. McFadden. 1994. "Large Sample Estimation and Hypothesis Testing." In *Handbook of Econometrics*, vol. 4, edited by R. F. Engle and D. McFadden, 2111–2245. Amsterdam: North-Holland.
- White, H. 1982. "Maximum Likelihood Estimation of Misspecified Models." *Econometrica* 50 (1): 1–25.
