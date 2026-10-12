# Appendix A: OLS Estimation — Derivation and Properties

This appendix develops the mathematical foundations of Ordinary Least Squares estimation. The results here underpin the discussion of assumption violations in [OLS Assumptions and How Time Series Violates Them](../00-foundations/ols-assumptions.md#the-classical-ols-assumptions-and-how-time-series-violates-them). Readers familiar with matrix calculus may proceed directly to [Section A.2](#a2-the-fundamental-decomposition).

---

## A.1 Minimizing the Sum of Squared Residuals

OLS selects the coefficient vector $\hat{\boldsymbol{\beta}}$ by minimizing the sum of squared residuals over all possible $\boldsymbol{\beta}$. The objective function is:

$$S(\boldsymbol{\beta}) = \sum_{t=1}^T \bigl(y_t - \mathbf{x}_t^T\boldsymbol{\beta}\bigr)^2 = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})$$

(Read: S of beta equals the sum, over t from 1 to T, of y-sub-t minus x-sub-t-transpose-beta, squared; equivalently in matrix form, y minus X-beta transposed, times y minus X-beta.)

Expanding the quadratic form using $(\mathbf{a} - \mathbf{b})^T(\mathbf{a} - \mathbf{b}) = \mathbf{a}^T\mathbf{a} - 2\mathbf{b}^T\mathbf{a} + \mathbf{b}^T\mathbf{b}$:

$$S(\boldsymbol{\beta}) = \mathbf{y}^T\mathbf{y} - 2\boldsymbol{\beta}^T\mathbf{X}^T\mathbf{y} + \boldsymbol{\beta}^T\mathbf{X}^T\mathbf{X}\boldsymbol{\beta}$$

(Read: S of beta equals y-transpose-y, minus two times beta-transpose-X-transpose-y, plus beta-transpose-X-transpose-X-beta.)

Taking the gradient with respect to $\boldsymbol{\beta}$ and applying the matrix calculus identities $\frac{\partial}{\partial \boldsymbol{\beta}}(\boldsymbol{\beta}^T\mathbf{a}) = \mathbf{a}$ and $\frac{\partial}{\partial \boldsymbol{\beta}}(\boldsymbol{\beta}^T\mathbf{A}\boldsymbol{\beta}) = 2\mathbf{A}\boldsymbol{\beta}$ for symmetric $\mathbf{A}$:

$$\frac{\partial S}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^T\mathbf{y} + 2\mathbf{X}^T\mathbf{X}\boldsymbol{\beta}$$

(Read: the gradient of S with respect to beta equals negative-two times X-transpose-y, plus two times X-transpose-X-beta.)

Setting this gradient to zero yields the **normal equations**:

$$\mathbf{X}^T\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^T\mathbf{y}$$

(Read: X-transpose-X times beta-hat equals X-transpose-y.)

When $\mathbf{X}$ has full column rank, $\mathbf{X}^T\mathbf{X}$ is invertible and the unique solution is:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

(Read: beta-hat equals X-transpose-X-inverse times X-transpose-y.)

The second-order condition confirms this is a global minimum. The Hessian $\frac{\partial^2 S}{\partial \boldsymbol{\beta}\,\partial \boldsymbol{\beta}^T} = 2\mathbf{X}^T\mathbf{X}$ is positive definite under full column rank, so $S$ is strictly convex and the critical point is a unique minimizer.

---

## A.2 The Fundamental Decomposition

Substituting the true data-generating process $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$ into the OLS formula:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T(\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}) = \boldsymbol{\beta} + (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\boldsymbol{\epsilon}$$

(Read: beta-hat equals beta plus X-transpose-X-inverse times X-transpose-epsilon.)

The estimator equals the true parameter plus a weighted sum of errors. The second term is the source of all bias and variance in OLS.

### Unbiasedness

Taking the conditional expectation given $\mathbf{X}$:

$$\mathbb{E}[\hat{\boldsymbol{\beta}} \mid \mathbf{X}] = \boldsymbol{\beta} + (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbb{E}[\boldsymbol{\epsilon} \mid \mathbf{X}]$$

(Read: the expected value of beta-hat given X equals beta, plus X-transpose-X-inverse times X-transpose, times the expected value of epsilon given X.)

The bias term $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbb{E}[\boldsymbol{\epsilon} \mid \mathbf{X}]$ vanishes if and only if $\mathbf{X}^T\mathbb{E}[\boldsymbol{\epsilon} \mid \mathbf{X}] = \mathbf{0}$; Assumption 4 (strict exogeneity, $\mathbb{E}[\boldsymbol{\epsilon} \mid \mathbf{X}] = \mathbf{0}$) is the usual sufficient condition. When it fails, $\hat{\boldsymbol{\beta}}$ is biased in finite samples. Whether the bias survives as $T$ grows depends on the orthogonality condition $\mathbb{E}[\mathbf{x}_t \epsilon_t] = \mathbf{0}$: a lagged dependent variable with martingale-difference errors satisfies it, and the bias is of order $1/T$; a lagged dependent variable with autocorrelated errors, or simultaneity, violates it, and $\hat{\boldsymbol{\beta}}$ is inconsistent.

### Variance

Using the identity $\text{Var}(\mathbf{A}\mathbf{v}) = \mathbf{A}\,\text{Var}(\mathbf{v})\,\mathbf{A}^T$:

$$\text{Var}(\hat{\boldsymbol{\beta}} \mid \mathbf{X}) = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\,\text{Var}(\boldsymbol{\epsilon} \mid \mathbf{X})\,\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the variance of beta-hat given X equals X-transpose-X-inverse times X-transpose, times the variance of epsilon given X, times X times X-transpose-X-inverse.)

Under Assumptions 2 and 3 jointly, $\text{Var}(\boldsymbol{\epsilon} \mid \mathbf{X}) = \sigma^2\mathbf{I}$, and the expression simplifies:

$$\text{Var}(\hat{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the variance of beta-hat given X equals sigma-squared times X-transpose-X-inverse.)

When A2 or A3 fails, $\text{Var}(\boldsymbol{\epsilon} \mid \mathbf{X}) = \sigma^2\boldsymbol{\Omega}$ with $\boldsymbol{\Omega} \neq \mathbf{I}$, and the true variance takes the **sandwich form**:

$$\text{Var}(\hat{\boldsymbol{\beta}} \mid \mathbf{X}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\boldsymbol{\Omega}\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}$$

(Read: the variance of beta-hat given X equals sigma-squared times X-transpose-X-inverse, times X-transpose-Omega-X, times X-transpose-X-inverse.)

OLS always reports $\hat{\sigma}^2(\mathbf{X}^T\mathbf{X})^{-1}$, ignoring $\boldsymbol{\Omega}$ entirely. When $\boldsymbol{\Omega} \neq \mathbf{I}$, this reported variance is the wrong quantity.

---

## A.3 t-Statistics and Their Validity Conditions

The t-statistic for the $k$-th coefficient tests $H_0\text{: }\beta_k = \beta_k^0$ (typically $\beta_k^0 = 0$):

$$t_k = \frac{\hat{\beta}_k - \beta_k^0}{\hat{\text{se}}(\hat{\beta}_k)}, \qquad \hat{\text{se}}(\hat{\beta}_k) = \sqrt{\hat{\sigma}^2\bigl[(\mathbf{X}^T\mathbf{X})^{-1}\bigr]_{kk}}$$

(Read: t-sub-k equals beta-hat-sub-k minus the hypothesized value, divided by the estimated standard error; the standard error equals the square root of sigma-hat-squared times the k-th diagonal element of X-transpose-X-inverse.)

Here $\bigl[(\mathbf{X}^T\mathbf{X})^{-1}\bigr]_{kk}$ denotes the $k$-th diagonal entry of $(\mathbf{X}^T\mathbf{X})^{-1}$, and $\hat{\sigma}^2 = \frac{1}{T-K}\sum_{t=1}^T \hat{\epsilon}_t^2$. The distribution of $t_k$ depends directly on which assumptions hold:

- **Under A1–A5:** $t_k \sim t_{T-K}$ exactly. A5 makes $\hat{\boldsymbol{\beta}}$ exactly normal; the ratio of a standard normal to the square root of an independent chi-squared variable is t-distributed.
- **Under A1–A4 without normality, plus large-sample conditions:** when $\frac{1}{T}\mathbf{X}^T\mathbf{X}$ converges to a positive definite matrix $\mathbf{Q}$ and a central limit theorem applies to $\mathbf{x}_t\epsilon_t$ (for example, an ergodic stationary martingale difference sequence with finite second moments), $t_k \xrightarrow{d} \mathcal{N}(0,1)$ as $T \to \infty$. Finite-sample critical values are approximate.
- **When A2 or A3 fails:** $\hat{\text{se}}(\hat{\beta}_k)$ is inconsistent for the true standard deviation of $\hat{\beta}_k$. The denominator converges to the wrong value, so $t_k$ is asymptotically $\mathcal{N}(0, v)$ with $v \neq 1$: the shape is normal and the scale is wrong. The actual size of the test differs from its nominal level at any sample size.
- **When A4 fails:** with a lagged dependent variable and martingale-difference errors, $\hat{\boldsymbol{\beta}}$ is consistent and the t-statistic is asymptotically $\mathcal{N}(0,1)$; finite-sample critical values are approximate. When the orthogonality condition $\mathbb{E}[\mathbf{x}_t \epsilon_t] = \mathbf{0}$ also fails, the numerator $\hat{\beta}_k - \beta_k^0$ does not center on zero under the null even in large samples, and the test rejects too often in a systematic direction, regardless of how accurately the standard error is estimated.

---

## A.4 The Gauss-Markov Theorem

*To be expanded.*

---

## A.5 Generalized Least Squares

*To be expanded.*

---

## A.6 Asymptotic Theory

*To be expanded.*
