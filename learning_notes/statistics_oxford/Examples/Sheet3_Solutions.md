# Question 1: Statistical Analysis of Heart Rate Data

> The heart rate (beats per minute) of 10 children was measured in two situations:
>
> (i) at rest, and
> (ii) in anticipation of them doing a minute's exercise.
>
> The data are given below:
>
> Rest, $x$: 72, 116, 79, 97, 90, 67, 115, 82, 95, 82
>
> Anticipation, $y$: 76, 120, 84, 99, 93, 75, 116, 83, 98, 87
>
> The sample means and variances are:
>
> $\bar{x} = 89.5$, $s^2_x = 274.9$
>
> $\bar{y} = 93.1$, $s^2_y = 238.8$
>
> (a) Assuming the data are normally distributed, carry out a two-sample $t$-test of the null hypothesis that the mean heart rate for the two situations is the same, against the alternative that it is different. What further assumptions are required for the test to be valid?
>
> How would you modify the test if the alternative is that the mean heart rate is higher in situation (ii)? Explain which alternative you think is more appropriate here.
>
> (b) Suggest a more appropriate test than that in (a). Carry out this test and explain why you prefer it.

## Solutions:

## (a) Two-Sample t-test Analysis

### Step 1: Hypotheses

Let's begin by clearly stating our hypotheses:

- **Null Hypothesis** ($H_0$): $\mu_x = \mu_y$
  The mean heart rates in the two situations are equal.
- **Alternative Hypothesis** ($H_1$): $\mu_x \neq \mu_y$
  The mean heart rates in the two situations are different.

### Step 2: Required Assumptions

For this test to be valid, we require:

1. The data in both groups follow a normal distribution
2. The variances of both groups are equal (homogeneity of variances)

### Step 3: Calculating the Test Statistic

First, we compute the pooled variance using:

$s_p^2 = \frac{(n_x-1)s_x^2 + (n_y-1)s_y^2}{n_x + n_y - 2}$

Given:

- $n_x = n_y = 10$
- $s_x^2 = 274.9$
- $s_y^2 = 238.8$

Substituting:

$s_p^2 = \frac{(10-1)\cdot 274.9 + (10-1)\cdot 238.8}{10 + 10 - 2}$
$s_p^2 = \frac{2474.1 + 2149.2}{18} = 256.28$

Next, calculate the standard error:

$SE = \sqrt{s_p^2(\frac{1}{n_x} + \frac{1}{n_y})} = \sqrt{256.28 \cdot (\frac{1}{10} + \frac{1}{10})} \approx 7.16$

The t-statistic is:

$t = \frac{\bar{x} - \bar{y}}{SE} = \frac{89.5 - 93.1}{7.16} \approx -0.503$

### Step 4: Decision Making

Degrees of freedom: $df = n_x + n_y - 2 = 18$

At $\alpha = 0.05$ (two-tailed):

- Critical value: $t_{0.025, 18} = 2.101$
- Since $|t| = 0.503 < 2.101$, we fail to reject $H_0$

### One-tailed Alternative

For testing if anticipation increases heart rate:

- $H_0: \mu_y \leq \mu_x$
- $H_1: \mu_y > \mu_x$

Critical value at $\alpha = 0.05$ (one-tailed): $t_{0.05, 18} = 1.734$

Since $t = -0.503 < 1.734$, we fail to reject $H_0$.

## (b) Paired t-test Analysis

### Step 1: Computing Differences

Let $d_i = y_i - x_i$ for each pair. The differences are:
$d = [4, 4, 5, 2, 3, 8, 1, 1, 3, 5]$

Calculate mean difference:
$\bar{d} = \frac{\sum d}{n} = \frac{36}{10} = 3.6$

Calculate variance of differences:
$s_d^2 = \frac{\sum(d_i - \bar{d})^2}{n-1} = 3.16$

Standard error:
$SE_d = \sqrt{\frac{s_d^2}{n}} = \sqrt{\frac{3.16}{10}} \approx 0.562$

### Step 2: Test Statistic and Decision

Test statistic:
$t = \frac{\bar{d}}{SE_d} = \frac{3.6}{0.562} \approx 6.41$

With $df = n - 1 = 9$:

- Critical value: $t_{0.025,9} = 2.262$
- Since $|t| = 6.41 > 2.262$, we reject $H_0$

### Why Paired t-test is Superior

The paired t-test is more appropriate because:

1. It accounts for the natural pairing in the data (same subjects in both conditions)
2. This reduces the impact of individual variations between subjects
3. It provides greater statistical power by controlling for subject-specific differences

In the first test (two-sample t-test), we treated the "rest" and "anticipation" measurements as if they came from two completely separate groups of people. This test didn't consider that the same children were measured twice. When we do this, we're essentially throwing away valuable information about how each individual child's heart rate changed.

Let's look at the actual data more closely:

- Child 1: Rest = 72, Anticipation = 76 (Difference = +4)
- Child 2: Rest = 116, Anticipation = 120 (Difference = +4)
- Child 3: Rest = 79, Anticipation = 84 (Difference = +5)

And so on...

Notice something interesting? While the overall means aren't drastically different (89.5 vs 93.1), almost every single child showed an increase in heart rate during anticipation. This pattern is consistent, but the two-sample t-test missed it because it ignored these paired relationships.

Think of it like this: Imagine you're trying to detect if a coin is slightly weighted to land on heads. You could:

- Flip coin A 10 times, then flip coin B 10 times and compare the results (like the two-sample t-test)
- Flip the same coin twice 10 times and look at how often the second flip differs from the first (like the paired t-test)

The second method is much more powerful because it controls for variations between coins, just like the paired t-test controls for variations between children.

This is why the test statistics were so different:

- Two-sample t-test: t = -0.503 (not significant)
- Paired t-test: t = 6.41 (highly significant)

The paired t-test produced a much larger t-value because it focused specifically on the consistent pattern of increases within each child, rather than just comparing the overall group averages. Each child served as their own control, which made the small but consistent increase in heart rate much more detectable.

This is a classic example of why it's crucial to choose the right statistical test based on how the data was collected. When we have paired measurements (before/after, two conditions on the same subject, etc.), a paired t-test will almost always be more appropriate and powerful than a two-sample t-test

# Question 2: Most Powerful Test for Normal Distribution

Let $X_1,...,X_n$ be independent $N(\theta,\sigma_0^2)$ random variables, where $\sigma_0^2$ is known. Find the most powerful test of size $\alpha$ of

$H_0: \theta = \theta_0$ against $H_1: \theta = \theta_1$, where $\theta_1 > \theta_0$.

Show that the power function $w(\theta)$ of this test is given by:

$w(\theta) = 1 - \Phi(\frac{\sqrt{n}}{\sigma_0}(\theta_0-\theta) + z_\alpha)$

where $\Phi$ is the cumulative distribution function of the standard normal distribution and $\Phi(z_\alpha) = 1-\alpha$.

If $\theta_0 = 0$, $\theta_1 = 0.5$ and $\sigma_0 = 1$, how large must $n$ be if $\alpha = 0.05$ and the power at $\theta_1$ is to be 0.975?

[If $\Phi$ is the $N(0,1)$ cdf, then $\Phi(1.645) = 0.95$ and $\Phi(1.96) = 0.975$.]

## Solution:

Given that we have independent normal random variables $X_1, \ldots, X_n \sim N(\theta, \sigma_0^2)$, their sample mean $\bar{X}$ follows a normal distribution with:

$\bar{X} \sim N(\theta, \frac{\sigma_0^2}{n})$

This is a key result from sampling theory - the sample mean is normally distributed with the same center as the individual observations but with reduced variance (by a factor of n). This reduction in variance illustrates why larger sample sizes lead to more precise estimates.

Our hypotheses are:
$H_0: \theta = \theta_0$ versus $H_1: \theta = \theta_1$ where $\theta_1 > \theta_0$

### Deriving the Most Powerful Test

The Neyman-Pearson lemma tells us that the most powerful test is based on the likelihood ratio. In our case, because of the monotone likelihood ratio property of the normal distribution, this elegant result simplifies to rejecting $H_0$ when $\bar{X}$ exceeds some critical value $c$.

When $\bar{X}$ follows $N(\theta_0, \frac{\sigma_0^2}{n})$ under $H_0$, we can standardize it:

$Z = \frac{\bar{X} - \theta_0}{\sigma_0/\sqrt{n}} \sim N(0,1)$

For a test of size $\alpha$, we need:

$P(\text{Reject } H_0|H_0 \text{ is true}) = \alpha$

This means:
$P(Z > \frac{c-\theta_0}{\sigma_0/\sqrt{n}}) = \alpha$

### Finding the Critical Value

Let $z_\alpha$ be the $(1-\alpha)$ quantile of the standard normal distribution, meaning $\Phi(z_\alpha) = 1-\alpha$. Then:

$\frac{c-\theta_0}{\sigma_0/\sqrt{n}} = z_\alpha$

Solving for the critical value:
$c = \theta_0 + \frac{\sigma_0}{\sqrt{n}}z_\alpha$

### Deriving the Power Function

The power function $w(\theta)$ gives the probability of rejecting $H_0$ when the true parameter is $\theta$. Under any $\theta$, $\bar{X} \sim N(\theta, \frac{\sigma_0^2}{n})$, so:

$w(\theta) = P(\bar{X} > c|\theta) = P(Z > \frac{c-\theta}{\sigma_0/\sqrt{n}})$

Substituting the critical value:

$w(\theta) = 1 - \Phi(\frac{\sqrt{n}}{\sigma_0}(\theta_0-\theta) + z_\alpha)$

### Solving for Required Sample Size

For the specific values:

- $\theta_0 = 0$
- $\theta_1 = 0.5$
- $\sigma_0 = 1$
- $\alpha = 0.05$ (so $z_\alpha = 1.645$)
- Desired power at $\theta_1$ is 0.975

We solve:
$0.975 = 1 - \Phi(-0.5\sqrt{n} + 1.645)$

Since $\Phi(1.96) = 0.975$:
$-0.5\sqrt{n} + 1.645 = -1.96$

Solving:
$\sqrt{n} = 7.21$
$n = 52$

### Conclusion

The required sample size is 52 observations. This means we need 52 independent measurements to achieve 97.5% power for detecting a difference of 0.5 units from the null hypothesis value, while maintaining a 5% significance level. The relatively large sample size is needed because we want both a high power (0.975) and are testing for a moderate effect size (0.5 units).

This solution demonstrates how statistical theory can guide practical experimental design decisions, particularly in determining appropriate sample sizes to achieve desired levels of statistical power.

---
