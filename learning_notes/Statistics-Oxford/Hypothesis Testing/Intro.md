# T-Test: A Statistical Guide

## Introductory Example: t-test (Sleep Data)

In this study, we examine the effectiveness of a drug on sleep duration. We begin with data from 10 patients who received a low dose of the drug, measuring their change in sleep hours:

\[
0.7, -1.6, -0.2, -1.2, -0.1, 3.4, 3.7, 0.8, 0.0, 2.0
\]

_Key observation: Notice that some values are negative, indicating that some patients actually slept less after taking the drug._

### Objective

Our goal is to determine whether the drug genuinely increases sleep duration. This is a perfect scenario for a t-test, as we're comparing a sample mean to a hypothesized population mean.

### Statistical Framework

#### 1. Hypothesis Setup

The null hypothesis \(H_0\) represents our skeptical stance:
\[
$H_0: \mu = \mu_0 \text{ (where } \mu_0 = 0\text{)}$
\]

The alternative hypothesis \($H_1$\) represents what we're trying to prove:
\[
$H_1: \mu > \mu_0$
\]

_Remember: We choose a one-sided test $(\mu > \mu_0)$ because we specifically want to know if the drug increases sleep duration._

#### 2. Key Assumptions

The validity of our t-test relies on these crucial assumptions:

\[
$X_1, X_2, \ldots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2)$
\]

_Important to remember:_

- The "iid" means independent and identically distributed
- The normality assumption becomes less critical with larger sample sizes $(n > 30)$ due to the Central Limit Theorem

### Test Mechanics

#### Test Statistic

The t-statistic measures how many standard errors the sample mean is from the hypothesized mean:

\[
$t\_{\text{obs}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$
\]

For our low-dose data:
\[
$\bar{x} = 0.75, \quad s^2 = 3.2, \quad n = 10, \quad \mu_0 = 0$
\]

Leading to:
\[
$t\_{\text{obs}} = \frac{0.75 - 0}{\sqrt{3.2} / \sqrt{10}} = 1.326$
\]

### Results Analysis

Under \($H*0$\), our test statistic follows a $t$-distribution with n-1 degrees of freedom:
\[
$t(X) \sim t*{n-1}$
\]

The $p$-value represents the probability of seeing our observed result (or more extreme) if $H*0$ is true:
\[
$p = P(t(X) > t*{\text{obs}}) = 0.109$
\]

### Normal Dose Comparison

When testing a normal dose, we observed:
\[
$1.9, 0.8, 1.1, 0.1, -0.1, 4.4, 5.5, 1.6, 4.6, 3.4$
\]

With statistics:
\[
$\bar{x} = 2.33, \quad s^2 = 4.0, \quad n = 10, \quad t\_{\text{obs}} = 3.68, \quad p = 0.0025$
\]

### P-value Interpretation Guide

| P-value Range     | Evidence Against $H_0$ | Typical Conclusion                |
| ----------------- | ---------------------- | --------------------------------- |
| $p < 0.01$        | Very strong evidence   | Reject $H_0$ with high confidence |
| $0.01 < p < 0.05$ | Strong evidence        | Reject $H_0$                      |
| $0.05 < p < 0.10$ | Weak evidence          | Fail to reject $H_0$              |
| $p > 0.10$        | Little to no evidence  | Fail to reject $H_0$              |

### Critical Points to Remember

1. The t-test assumes normality, but is robust to moderate violations when n is large enough.
2. Always check the assumptions before applying the test.
3. The $p$-value is not the probability that $H_0$ is true.
4. Larger sample sizes can detect smaller effects.
5. Clinical significance may differ from statistical significance.
