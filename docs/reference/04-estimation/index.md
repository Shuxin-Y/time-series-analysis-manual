# 4. Estimation

Least squares and feasible GLS, moment and recursive estimators, cointegrating regression, the prediction-error decomposition, exact and conditional likelihood, quasi-likelihood, EM, GMM and Whittle estimation. Bayesian computation lives in area 12 and empirical-loss estimation in area 18. The page also hosts: Hannan-Rissanen estimation, Burg estimation, reduced-rank regression, conditional sum of squares.

The maximum-likelihood chain and the home of the term *Joint density* are on [Maximum likelihood](maximum-likelihood.md).

## OLS, GLS and feasible GLS

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_OLS_GLS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Yule-Walker and the method of moments

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_YULE_WALKER`). Write this section following the content rules in `.claude/rules/writing.md`.

## Durbin-Levinson and the innovations algorithm

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_DURBIN_LEVINSON`). Write this section following the content rules in `.claude/rules/writing.md`.

## Hannan-Rissanen estimation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_HANNAN_RISSANEN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Burg estimation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_BURG`). Write this section following the content rules in `.claude/rules/writing.md`.

## Cointegrating regression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_FMOLS_DOLS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Reduced-rank regression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_RRR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Prediction-error decomposition

Use the prediction-error decomposition to evaluate the likelihood of any model for dependent data. It writes the log-likelihood as a sum over time of one-step-ahead conditional log-densities, by the [chain rule of probability](../../00-foundations/stochastic-processes.md#chain-rule-of-probability):

\[\log L(\boldsymbol{\theta}) = \sum_{t=1}^{T} \log p(y_t \mid y_{t-1}, \ldots, y_1; \boldsymbol{\theta}).\]

(Read: the log-likelihood equals the sum over t of the log-density of y-sub-t given the earlier observations.)

For a Gaussian model each conditional density is normal, with mean the one-step forecast \(\hat{y}_{t \mid t-1}\) and variance \(F_t\). The log-likelihood then depends on the data only through the prediction errors \(v_t = y_t - \hat{y}_{t \mid t-1}\) and their variances:

\[\log L(\boldsymbol{\theta}) = -\frac{1}{2} \sum_{t=1}^{T} \left( \log 2\pi + \log F_t + \frac{v_t^2}{F_t} \right).\]

(Read: the Gaussian log-likelihood equals minus one half times the sum over t of log two pi, plus log F-sub-t, plus v-sub-t squared over F-sub-t.)

The [Kalman filter](../11-state-space/index.md#kalman-filter-and-smoother) computes \(v_t\) and \(F_t\) recursively for every linear Gaussian state-space model, so the exact likelihood of ARMA models, structural time-series models and regressions with ARMA errors is evaluated through it, including at missing and imputed time points, where the update step is skipped (Harvey 1989; Durbin and Koopman 2012). For a non-Gaussian or nonlinear model the same decomposition holds with the conditional densities computed by the model's own filter (a particle filter, the Hamilton filter for Markov switching, the variance recursion of GARCH). Dropping the first terms, whose conditional densities depend on unobserved pre-sample values, gives the conditional likelihood; the share of the dropped terms vanishes as \(T\) grows. The [maximum-likelihood](maximum-likelihood.md#likelihood) theory page states why maximising this sum is consistent.

## Maximum likelihood, exact and conditional

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_MLE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Quasi-maximum likelihood and sandwich standard errors

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_QMLE`). Write this section following the content rules in `.claude/rules/writing.md`.

## EM for state-space models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_EM`). Write this section following the content rules in `.claude/rules/writing.md`.

## Generalised method of moments

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_GMM`). Write this section following the content rules in `.claude/rules/writing.md`.

## Whittle and local Whittle estimation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_WHITTLE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Conditional sum of squares

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P8_CSS`). Write this section following the content rules in `.claude/rules/writing.md`.

## References

- Durbin, J., and S. J. Koopman. 2012. *Time Series Analysis by State Space Methods*. 2nd ed. Oxford: Oxford University Press.
- Harvey, A. C. 1989. *Forecasting, Structural Time Series Models and the Kalman Filter*. Cambridge: Cambridge University Press.
