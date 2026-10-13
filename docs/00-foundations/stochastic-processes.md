# Stochastic Processes

A time series is one realisation of a stochastic process: a family of random variables indexed by time. Every error-process choice in [P7](../01-workflow/p07-error-process.md) names a stochastic process, and every diagnostic in [P3](../01-workflow/p03-exploratory-diagnostics.md) asks which properties that process has. This chapter collects the definitions and theorems those choices rest on, in the order they build on each other: densities and independence, the chain rule and conditional expectation, the law of a whole process, stationarity, the three levels of "unpredictable noise", ergodicity and mixing, the Wold decomposition, unit roots, and the KL divergence. Each section is the root of a derivation chain shown in the glossary drawer.

Sections still marked pending are created from the flowchart inventory and are written in later rounds.

## Probability density

A random vector \(Y\) in \(\mathbb{R}^n\) has a **probability density** \(p\) when its distribution is absolutely continuous:

\[P(Y \in A) = \int_A p(y)\, dy \quad \text{for every (measurable) set } A \subseteq \mathbb{R}^n.\]

(Read: the probability that Y falls in A equals the integral of the density p over A.)

At almost every point \(y\), the density equals the limit of the probability of a small ball around \(y\) divided by the ball's volume (Lebesgue differentiation). The density is therefore probability per unit volume. A continuous variable takes any exact value with probability zero, so only probabilities of neighbourhoods carry information, and the density is their limit.

A distribution with no atoms need not have a density: the Cantor distribution puts no mass on any point and has no density. A discrete variable, such as a count, has a probability mass function; it is a density with respect to counting measure, and the likelihoods of the count branch ([B1](../reference/16-count-categorical/index.md)) use it in place of \(p\).

## Independence

Random variables \(Y_1, \ldots, Y_n\) are **independent** when their joint distribution is the product of their marginal distributions:

\[P(Y_1 \in A_1, \ldots, Y_n \in A_n) = \prod_{i=1}^n P(Y_i \in A_i) \quad \text{for all sets } A_1, \ldots, A_n.\]

(Read: the probability that every Y-sub-i falls in its set A-sub-i equals the product of the separate probabilities.)

With densities, the joint density is the product of the marginal densities. Independence implies uncorrelatedness when the second moments are finite. The converse fails: for \(Y \sim \mathcal{N}(0, 1)\), the variables \(Y\) and \(Y^2\) are uncorrelated, because \(\text{Cov}(Y, Y^2) = \mathbb{E}[Y^3] = 0\), and they are dependent. For jointly Gaussian variables uncorrelatedness does imply independence, which is why Gaussian white noise is i.i.d.

## Chain rule of probability

Any joint density factorises into conditional densities taken in time order:

\[p(y_1, \ldots, y_T) = p(y_1) \prod_{t=2}^{T} p(y_t \mid y_{t-1}, \ldots, y_1).\]

(Read: the joint density of the sample equals the density of the first observation times, for each later t, the density of y-sub-t given all earlier observations.)

The identity holds for every joint distribution with a density; it needs no independence. Independence is the special case in which each conditional density equals the marginal density \(p(y_t)\). For time series the conditional form is the starting point of every likelihood: the [prediction-error decomposition](../reference/04-estimation/index.md#prediction-error-decomposition) is this identity applied to a model.

## Conditional expectation as the optimal forecast

Let \(\mathcal{F}_t\) denote the information available at time \(t\) (the past and present values of the series and of any other variables observed by then). The **conditional expectation** \(\mathbb{E}[y_{t+h} \mid \mathcal{F}_t]\) is the forecast that is a function of \(\mathcal{F}_t\) alone and matches \(y_{t+h}\) on average over every event in \(\mathcal{F}_t\). Its two working properties are the law of iterated expectations, \(\mathbb{E}[\mathbb{E}[y \mid \mathcal{F}_t]] = \mathbb{E}[y]\), and the orthogonality of the forecast error to every function of \(\mathcal{F}_t\).

Under squared-error loss the conditional expectation is the best forecast. For every forecast \(f\) that is a function of \(\mathcal{F}_t\) with a finite second moment,

\[\mathbb{E}\big[(y_{t+h} - f)^2\big] \ge \mathbb{E}\big[(y_{t+h} - \mathbb{E}[y_{t+h} \mid \mathcal{F}_t])^2\big].\]

(Read: the expected squared error of any forecast built from the information at time t is at least the expected squared error of the conditional expectation.)

The loss decides which functional of the predictive distribution is optimal (Gneiting 2011):

| Loss | Optimal forecast |
|---|---|
| Squared error | Conditional mean |
| Absolute error | Conditional median |
| Pinball loss at level \(\tau\) | Conditional \(\tau\)-quantile |
| A proper scoring rule for distributions (log score, CRPS) | The predictive distribution itself |

[P0](../01-workflow/p00-purpose/index.md) fixes the loss with the forecast task, and [P11](../01-workflow/p11-inference.md) issues the matching functional. The best *linear* forecast replaces \(\mathcal{F}_t\) by linear functions of past values ([projection theorem](#projection-theorem-and-best-linear-prediction)); it equals the conditional mean when the process is Gaussian.

## Kolmogorov extension theorem

A stochastic process \(\{y_t\}\) is an infinite sequence of random variables, and its law is a probability measure on the space of sequences. A model usually specifies only finite-dimensional distributions: the joint distribution of \((y_{t_1}, \ldots, y_{t_n})\) for every finite set of times. The **Kolmogorov extension theorem** gives existence and uniqueness. When these finite-dimensional distributions are consistent — each one marginalises to the distribution of any sub-vector, and permuting the times permutes the coordinates — there is exactly one probability measure on the product σ-field of sequences that has them as its finite-dimensional distributions (Billingsley 1995, sec. 36).

The likelihood of \(T\) observations needs only the joint distribution of the vector \((y_1, \ldots, y_T)\), which exists without the theorem. The theorem is needed for statements about the whole process: stationarity, ergodic theorems, and every limit as \(T \to \infty\).

## Strict and weak stationarity

A process is **strictly stationary** when shifting time does not change any of its finite-dimensional distributions: for every \(n\), all times \(t_1, \ldots, t_n\) and every shift \(h\),

\[(y_{t_1}, \ldots, y_{t_n}) \overset{d}{=} (y_{t_1 + h}, \ldots, y_{t_n + h}).\]

(Read: the vector of values at times t-1 to t-n has the same distribution as the vector at the same times shifted by h.)

A process is **weakly stationary** (covariance stationary) when it has finite second moments, a constant mean and an autocovariance that depends only on the lag:

\[\mathbb{E}[y_t^2] < \infty, \qquad \mathbb{E}[y_t] = \mu, \qquad \text{Cov}(y_t, y_{t-k}) = \gamma(k) \quad \text{for all } t.\]

(Read: y-sub-t has a finite second moment, a mean mu that does not depend on t, and a covariance with y-sub-t-minus-k that depends on the lag k but not on t.)

The two definitions relate as follows:

- Strict stationarity with finite second moments implies weak stationarity.
- Weak stationarity implies strict stationarity for Gaussian processes, because a Gaussian distribution is determined by its means and covariances.
- A strictly stationary process with infinite variance is not weakly stationary; IGARCH is an example ([P7](../01-workflow/p07-error-process.md)).
- A weakly stationary process need not be strictly stationary: independent variables that alternate between \(\mathcal{N}(0, 1)\) and a centred, scaled exponential with variance 1 have constant mean, variance and zero autocovariance, and their distribution changes with \(t\).

## White noise, martingale difference, independence

"Unpredictable noise" has three levels of strength, and the tests of this book check different ones.

- **White noise**, \(\text{WN}(0, \sigma^2)\): \(\mathbb{E}[\epsilon_t] = 0\), \(\text{Var}(\epsilon_t) = \sigma^2\), and \(\text{Cov}(\epsilon_t, \epsilon_s) = 0\) for \(t \neq s\). No *linear* forecast of \(\epsilon_t\) from its past beats zero.
- **Martingale difference sequence** (MDS): \(\mathbb{E}|\epsilon_t| < \infty\) and \(\mathbb{E}[\epsilon_t \mid \mathcal{F}_{t-1}] = 0\), where \(\mathcal{F}_{t-1}\) is the information up to \(t-1\). No forecast at all, linear or not, beats zero in mean.
- **i.i.d.** \((0, \sigma^2)\), also called strong white noise: the \(\epsilon_t\) are independent and identically distributed with mean 0 and variance \(\sigma^2\). Nothing about \(\epsilon_t\), not even its variance or its distribution, depends on the past.

The levels nest: i.i.d. \((0, \sigma^2)\) ⊂ stationary MDS with finite variance ⊂ white noise. Both inclusions are strict.

- ARCH errors are an MDS and not independent: their mean is unpredictable, and their squares are autocorrelated.
- \(\epsilon_t = \eta_t + \eta_{t-1}\eta_{t-2}\) with \(\eta_t\) i.i.d. \(\mathcal{N}(0, 1)\) is white noise and not an MDS: its autocovariances at every lag \(k \ge 1\) are zero, and its conditional mean given past \(\eta\) values is \(\eta_{t-1}\eta_{t-2} \neq 0\).

The residual ACF and the Ljung–Box test check white noise, and their usual null distributions are derived for i.i.d. noise; under ARCH they over-reject. A flat ACF therefore establishes uncorrelatedness only, and the squared-residual checks of [P7](../01-workflow/p07-error-process.md) look for dependence beyond it.

## Ergodicity and mixing

Stationarity says that the distribution does not change over time. It does not say that one long realisation reveals that distribution. Two properties add that.

A strictly stationary process is **ergodic** when every event that the time shift leaves unchanged has probability 0 or 1. Ergodicity is what makes time averages converge to expectations ([law of large numbers](asymptotics.md#law-of-large-numbers)). A stationary process that is not ergodic: \(y_t = Z + \epsilon_t\), with \(Z\) drawn once and \(\epsilon_t\) i.i.d.; its sample mean converges to the realised \(Z\), not to \(\mathbb{E}[Z]\).

A process is **mixing** when the dependence between its past and its distant future vanishes. The strong-mixing coefficient at gap \(k\) is

\[\alpha(k) = \sup \big| P(A \cap B) - P(A)\, P(B) \big|,\]

(Read: alpha of k is the largest gap between the probability of A-and-B and the product of their probabilities.)

where the supremum runs over events \(A\) determined by \((\ldots, y_{t-1}, y_t)\) and events \(B\) determined by \((y_{t+k}, y_{t+k+1}, \ldots)\). The process is strong mixing when \(\alpha(k) \to 0\) as \(k \to \infty\).

Independence implies mixing (\(\alpha(k) = 0\) for \(k \ge 1\)), and for a strictly stationary process mixing implies ergodicity. The law of large numbers needs ergodicity alone, with no rate. A central limit theorem needs more: mixing coefficients that decay fast enough, or a martingale-difference structure ([central limit theorem](asymptotics.md#central-limit-theorem)).

## Wold decomposition

Every weakly stationary process with mean zero can be written as a moving average of its one-step forecast errors plus a part that is perfectly predictable from its own past (Wold 1938):

\[y_t = \sum_{j=0}^{\infty} \psi_j\, \epsilon_{t-j} + V_t, \qquad \psi_0 = 1, \qquad \sum_{j=0}^{\infty} \psi_j^2 < \infty.\]

(Read: y-sub-t equals an infinite moving average of the innovations epsilon, with square-summable weights psi, plus a deterministic part V-sub-t.)

Here \(\epsilon_t\) is the error of the best linear forecast of \(y_t\) from \(y_{t-1}, y_{t-2}, \ldots\), and \(V_t\) is linearly deterministic and uncorrelated with every \(\epsilon_s\). A process with \(V_t = 0\) is purely non-deterministic. A sinusoid with a random phase is the opposite case: it is weakly stationary and entirely deterministic.

The innovations \(\epsilon_t\) are white noise. They need not be i.i.d. or an MDS, which is why a conditional-variance model can sit inside them ([P7](../01-workflow/p07-error-process.md)). An ARMA model approximates the infinite sequence \(\psi_j\) by a ratio of two finite polynomials.

## Random walks and unit-root asymptotics

A **random walk** adds white noise to its own previous value:

\[y_t = y_{t-1} + \epsilon_t, \qquad \epsilon_t \sim \text{WN}(0, \sigma^2), \qquad y_0 \text{ given}.\]

(Read: y-sub-t equals its previous value plus a white-noise shock.)

Its variance \(\text{Var}(y_t \mid y_0) = t\sigma^2\) grows with \(t\), so it is not stationary; every shock has a permanent effect. With a drift, \(y_t = \mu + y_{t-1} + \epsilon_t\) adds the deterministic trend \(\mu t\) to the stochastic trend \(\sum_{s \le t} \epsilon_s\).

A process is **I(0)** when it is stationary with a positive long-run variance (its Wold weights do not sum to zero). An **integrated process** of order \(d\), written I(\(d\)), is one whose \(d\)-th difference, after its deterministic part is removed, is I(0), where \(\Delta y_t = y_t - y_{t-1}\) (Johansen 1995, ch. 3). A random walk is I(1). An autoregression has a **unit root** when its autoregressive polynomial has a root at \(z = 1\); with a single unit root and all other roots outside the unit circle, it is I(1). A trend-stationary series, \(y_t = \alpha + \delta t + u_t\) with I(0) \(u_t\), is I(0) around a deterministic trend, and shocks do not persist; differencing it leaves \(\Delta u_t\), whose long-run variance is zero, which is why differencing it over-differences.

Estimators of a unit root have non-standard limits: the least-squares estimate of the autoregressive coefficient converges at rate \(T\) instead of \(\sqrt{T}\), and the Dickey–Fuller statistics converge to functionals of Brownian motion whose distributions depend on the deterministic terms in the test regression ([nonstationarity theory](../reference/28-nonstationarity-theory/index.md)). The deterministic terms (constant, or constant and trend) are therefore chosen with the test, not after it.

The ADF test has a unit root as its null; the KPSS test has stationarity (around a level or a trend) as its null. Read together they have four outcomes:

| ADF rejects a unit root | KPSS rejects stationarity | Reading |
|---|---|---|
| Yes | No | Stationary around the deterministic terms of the test regressions |
| No | Yes | Unit root |
| No | No | The data do not discriminate; both nulls remain compatible, typically because the sample is short |
| Yes | Yes | Conflict; check for breaks and for long memory, and estimate the fractional order \(d\) |

[P3](../01-workflow/p03-exploratory-diagnostics.md) applies this table, with the breaks and long-memory checks that resolve its last two rows.

## KL divergence

The **Kullback–Leibler divergence** from a true density \(f\) to a model density \(g\) is the expected log-ratio of the two under the truth:

\[\text{KL}(f \,\|\, g) = \mathbb{E}_f\left[\log \frac{f(Y)}{g(Y)}\right] = \int f(y) \log \frac{f(y)}{g(y)}\, dy.\]

(Read: the KL divergence from f to g is the expected value, under f, of the log of f over g.)

It is non-negative and equals zero only when \(f = g\) almost everywhere (Gibbs' inequality, a consequence of Jensen's inequality for the concave logarithm). It is not symmetric, so it is a divergence and not a distance. Maximising an expected log-likelihood is minimising a KL divergence to the truth; for time series the divergence is taken between conditional densities of \(y_t\) given its past ([pseudo-true value](../reference/04-estimation/maximum-likelihood.md#pseudo-true-value)).

## Long memory and hyperbolic decay

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_LONG_MEMORY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Stationarity conditions of GARCH

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_GARCH_STATIONARITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Latent processes and filtering

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_LATENT_FILTERING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Brownian motion, Poisson jumps, Levy processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_LEVY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Hidden Markov chains

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_HMM`). Write this section following the content rules in `.claude/rules/writing.md`.

## Sklar's theorem

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_SKLAR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Time-rescaling theorem

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_TIME_RESCALING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Lag operator, difference equations and characteristic roots

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_LAG_OPERATOR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Projection theorem and best linear prediction

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_PROJECTION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Markov chains

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `F_MARKOV`). Write this section following the content rules in `.claude/rules/writing.md`.

## References

- Billingsley, P. 1995. *Probability and Measure*. 3rd ed. New York: Wiley.
- Gneiting, T. 2011. "Making and Evaluating Point Forecasts." *Journal of the American Statistical Association* 106 (494): 746–762.
- Johansen, S. 1995. *Likelihood-Based Inference in Cointegrated Vector Autoregressive Models*. Oxford: Oxford University Press.
- Wold, H. 1938. *A Study in the Analysis of Stationary Time Series*. Uppsala: Almqvist and Wiksell.
