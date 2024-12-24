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

The null hypothesis $H_0$ represents our skeptical stance:
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

Under \($H_0$\), our test statistic follows a $t$-distribution with n-1 degrees of freedom:
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

# P-Value

Imagine you're testing a new coin to see if it's fair. You flip it 100 times and get 60 heads. That seems like more heads than you'd expect from a fair coin, but could this happen just by chance with a fair coin? This is exactly what a p-value helps us determine.

## Core Concept

A p-value answers this question: If our null hypothesis (our default assumption) were true, how likely would we be to see results as extreme as what we actually observed?

In mathematical terms:

$$
\text{p-value} = P(\text{observing data as extreme or more extreme} | H_0 \text{ is true})
$$

## Real-World Example

Let's break this down with our sleep drug example:

1. We observed that patients slept an average of 0.75 hours more with the low dose drug
2. Our null hypothesis ($H_0$) was "the drug has no effect" ($\mu=0$)
3. The p-value of $0.109$ tells us: "If the drug truly had no effect, we would see results this extreme or more extreme about $10.9\%$ of the time"

## Interpreting P-values

The p-value represents a probability, ranging from 0 to 1. Here's how to think about different p-values:

- $p = 0.001:$ If H₀ were true, we'd see results this extreme only $0.1\%$ of the time
- $p = 0.05:$ If H₀ were true, we'd see results this extreme $5\%$ of the time
- $p = 0.50:$ If H₀ were true, we'd see results this extreme $50\%$ of the time

## Common Misconceptions

It's important to understand what a p-value is NOT:

1. It's NOT the probability that the null hypothesis is true
2. It's NOT the probability that your results occurred by chance
3. It's NOT the probability that your research hypothesis is true
4. It's NOT an indicator of the importance or size of an effect

## How to Use P-values

The p-value helps us make decisions by comparing it to a predetermined significance level $\alpha$, typically $0.05$:

- If $p < \alpha$: We reject the null hypothesis
- If $p ≥ \alpha:$ We fail to reject the null hypothesis

In our sleep drug example:

- Low dose: $p = 0.109 > 0.05$, so we fail to reject H₀
- Normal dose: $p = 0.0025 < 0.05$, so we reject H₀

## The Bigger Picture

Think of the p-value as just one piece of evidence in a larger scientific investigation. It should be considered alongside:

1. Effect size (how big is the difference?)
2. Practical significance (does the difference matter in real-world terms?)
3. Study design quality
4. Prior research and theoretical framework
5. Sample size and power

Remember: A small p-value tells us our result is unlikely under the null hypothesis, but it doesn't automatically make our finding important or meaningful in practical terms.

Would you like me to elaborate on any of these aspects or provide additional examples to clarify the concept further?
