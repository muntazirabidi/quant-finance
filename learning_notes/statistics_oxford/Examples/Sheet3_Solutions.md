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

# Question: Statistical Analysis of Receptionist Performance

A telephone receptionist for a large partnership of financial advisers is responsible for determining the precise nature of each incoming enquiry and connecting the client with an appropriate adviser. The number of inappropriate connections on any given day may be modelled by a random variable $X$ which has a Poisson distribution with mean $\mu$.

Let us examine the following scenario:

If $Z$ is the number of inappropriate connections made over a period of $n$ days, we need to:

1. Determine the distribution of $Z$
2. Find its expected value

We are given that Uhura, who has been such a receptionist for many years, has been found to have a mean rate of $\mu_U = 0.47$ inappropriate connections per day. For several months she has been training Spock, a new receptionist, with corresponding mean rate $\mu_S$.

At a meeting of senior partners, it was conjectured that Spock was already as proficient as Uhura; accordingly they resolved to keep a daily record of the number of inappropriate connections made by him over his next 10 working days.

Tasks:

1. Find a critical region of size 5% for a test of the hypothesis that Spock is as proficient as Uhura versus the alternative that he is less proficient.
2. For what values of $\mu_S$ does the probability of type II error fall below 10%?

Note: If $\phi_\mu(k) = \sum_{x=0}^k \frac{\mu^x e^{-\mu}}{x!}$, then:

- $\phi_{4.7}(8) = 0.95$
- $\phi_{13}(8) = 0.1$

## Solution Part I: Analyzing Inappropriate Connections

Let's start by clearly understanding what we're given:

- Each day, we track inappropriate connections ($X$)
- $X$ follows a Poisson distribution with mean $\mu$
- We want to find the distribution and expected value of $Z$, where $Z$ represents inappropriate connections over $n$ days

### Part 1: Determining the Distribution of Z

To find the distribution of $Z$, let's think about what $Z$ represents mathematically:

$Z = X_1 + X_2 + ... + X_n$ where each $X_i$ is the number of inappropriate connections on day $i$

A key property of the Poisson distribution tells us that when we sum independent Poisson random variables, the result is also Poisson distributed. The mean of the sum equals the sum of the individual means.

In our case:

- Each day is independent
- Each $X_i \sim \text{Poisson}(\mu)$
- We sum over $n$ days

Therefore:
$Z \sim \text{Poisson}(n\mu)$

This means that over $n$ days, the number of inappropriate connections follows a Poisson distribution with mean $n\mu$.

### Part 2: Finding the Expected Value

The expected value of a Poisson distribution equals its parameter. Therefore:

$E(Z) = n\mu$

To understand this intuitively:

- If we expect $\mu$ inappropriate connections per day
- And we're looking at $n$ days
- Then we expect $n\mu$ inappropriate connections in total

This result also follows from the linearity of expectation:
$E(Z) = E(X_1 + X_2 + ... + X_n) = E(X_1) + E(X_2) + ... + E(X_n) = n\mu$

## Solution Part II: Hypothesis Testing for Receptionist Proficiency

Let's build on our understanding of the Poisson distribution to analyze Spock's performance compared to Uhura's.

### Given Information:

- Uhura's mean rate: $\mu_U = 0.47$ inappropriate connections per day
- Test period for Spock: $n = 10$ days
- Significance level: $\alpha = 0.05$
- We're told that $\phi_{4.7}(8) = 0.95$ and $\phi_{13}(8) = 0.1$

### Step 1: Setting Up the Hypothesis Test

Let's establish our hypotheses:

$H_0: \mu_S = \mu_U = 0.47$ (Spock is as proficient as Uhura)

$H_1: \mu_S > \mu_U$ (Spock is less proficient)

Under $H_0$, over 10 days:

- Total expected inappropriate connections follows Poisson(10 × 0.47)
- So $Z \sim \text{Poisson}(4.7)$

### Step 2: Finding the Critical Region

We need a critical region of size 5%. Using the given information:
$\phi_{4.7}(8) = 0.95$

For a Poisson distribution:
$P(Z > k) = 1 - P(Z \leq k) = 1 - \phi_\mu(k)$

Let's verify this is our critical value:

$P(Z > 8|\mu = 4.7) = 1 - \phi_{4.7}(8) = 1 - 0.95 = 0.05$

To double-check, let's calculate $\phi_{4.7}(8)$ explicitly:

$\phi_{4.7}(8) = \sum_{x=0}^8 \frac{4.7^x e^{-4.7}}{x!}$

The critical region is $\{Z > 8\}$

- We reject $H_0$ if Spock makes more than 8 inappropriate connections in 10 days
- This gives us exactly our desired significance level of 5%

To confirm 8 is the optimal critical value:

- If we used 7: $P(Z > 7) > 0.05$ (too large)
- If we used 9: $P(Z > 9) < 0.05$ (too small)

### Step 3: Type II Error Analysis

For the second part, we need to find values of $\mu_S$ where Type II error probability is below 10%.

Type II error occurs when we fail to reject $H_0$ when $H_1$ is true.

Given that $\phi_{13}(8) = 0.1$:

Let $\beta(\mu_S)$ be the probability of Type II error:

$\beta(\mu_S) = P(\text{fail to reject }H_0|\mu_S) = P(Z \leq 8|10\mu_S)$

We want:
$\beta(\mu_S) < 0.1$

Since $\phi_{13}(8) = 0.1$, and $\phi_{10\mu_S}(8)$ decreases as $\mu_S$ increases:

$10\mu_S \geq 13$ will give us $\beta(\mu_S) \leq 0.1$

Therefore:
$\mu_S \geq 1.3$ inappropriate connections per day

### Interpretation:

This means:

1. We reject the hypothesis that Spock is as proficient as Uhura if he makes more than 8 inappropriate connections in 10 days
2. If Spock's true mean rate is 1.3 or more inappropriate connections per day, we have at least a 90% chance of detecting this difference

# Question 4:

When studying the sex ratio in a population using a sample of size $n$, it is usually assumed that, indpendently, each child is male with probability $p$. Renkonen (1956) observed $19,711$ male births out of a total of $38,562$ births in American families withtwo children each. Use the likelihood ratio statistic $Λ$ to test the hypothesis $H0:p=1/2$ against a suitable alternative which you should specify.

Renkonen also found $17,703$ males out of $35,042$ similar births in Finland. Use the generalised likelihood ratio test to test the hypothesis thatphas the same value in eachcountry versus a suitable alternative.

## Solution Part 1: Testing if $p = 1/2$ for American Births

We have data from births in American families with:

- Total births: $n = 38,562$
- Male births: $x = 19,711$
- Each birth is independent with probability $p$ of being male
- Distribution: $X \sim \text{Binomial}(n,p)$

### Hypotheses

- $H_₀: p = 1/2$ (sex ratio is exactly balanced)
- $H_₁: p ≠ 1/2$ (two-sided alternative)

### Likelihood Ratio Calculation

The likelihood function for a binomial distribution is:
$L(p) = \binom{n}{x}p^x(1-p)^{n-x}$

Under H₀:

- $p_₀ = 1/2$
- $L(p_0) = \binom{38562}{19711}(0.5)^{19711}(0.5)^{18851}$

Under $H_₁:$

- MLE is $\hat{p} = \frac{x}{n} = \frac{19711}{38562} = 0.5111$
- $L(\hat{p}) = \binom{38562}{19711}(0.5111)^{19711}(0.4889)^{18851}$

The likelihood ratio statistic is:
$\Lambda = -2\log\left(\frac{L(p_0)}{L(\hat{p})}\right)$

$= -2[19711\log(0.5) + 18851\log(0.5) - (19711\log(0.5111) + 18851\log(0.4889))]$

$= 19.18$

Under $H_₀, Λ$ follows a $\chi^2_1$ distribution.

### Decision

- Critical value at $5\%$ level: $\chi^2_1(0.05) = 3.84$
- Since $19.18 > 3.84$, we reject $H_₀$
- The p-value is extremely small ($≈ 1.2 × 10^{⁻⁵}$)

## Solution Part 2: Testing Equal Proportions Between Countries

### Additional Data

Finnish births:

- Total births: $n_₂ = 35,042$
- Male births: $x_₂ = 17,703$

### Hypotheses

- $H_₀: p_₁ = p_₂$ (same proportion in both countries)
- $H_₁: p_₁ ≠ p_₂$ (different proportions)

### Likelihood Ratio Calculation

Under $H_₁$ (separate proportions):

- US MLE: $\hat{p}_1 = \frac{19711}{38562} = 0.5111$
- Finnish MLE: $\hat{p}_2 = \frac{17703}{35042} = 0.5052$
- $L(\hat{p}_1,\hat{p}_2) = \binom{38562}{19711}\hat{p}_1^{19711}(1-\hat{p}_1)^{18851} \times \binom{35042}{17703}\hat{p}_2^{17703}(1-\hat{p}_2)^{17339}$

Under $H_₀$ (common proportion):

- Pooled MLE: $\hat{p} = \frac{x_1 + x_2}{n_1 + n_2} = \frac{19711 + 17703}{38562 + 35042} = 0.5083$
- $L(\hat{p}) = \binom{38562}{19711}\hat{p}^{19711}(1-\hat{p})^{18851} \times \binom{35042}{17703}\hat{p}^{17703}(1-\hat{p})^{17339}$

The likelihood ratio statistic:
$\Lambda = -2\log\left(\frac{L(\hat{p})}{L(\hat{p}_1,\hat{p}_2)}\right) = 2.61$

Under $H_₀, Λ$ follows a $\chi^2_1$ distribution.

- Critical value at $5%$ level: $\chi^2_1(0.05) = 3.84$
- Since $2.61 < 3.84$, we fail to reject $H_₀$
- Therefore, we don't have sufficient evidence to conclude that the sex ratios differ between countries

### Conclusion

1. We have strong evidence that the sex ratio in the American population deviates from exactly $50-50$, with a slight excess of male births ($p ≈ 0.511$).
2. However, we cannot conclude that the sex ratios differ between the US and Finland. The estimated proportions (US: $0.511$, Finland: $0.505$) are not significantly different, with a pooled estimate of $0.508.$
3. The large sample sizes allow detection of even small deviations from $p = 1/2$, but the difference between countries is not statistically significant.

### Effect Size

For comparing a sample proportion to a hypothesized value (Part 1):

$z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$

Let's calculate this for Part 1:

$\hat{p} = \frac{19,711}{38,562} = 0.5111$ (sample proportion)

$p_0 = 0.5$ (hypothesized value)

$n = 38,562$ (sample size)

$z = \frac{0.5111 - 0.5}{\sqrt{\frac{0.5(1-0.5)}{38,562}}}$

$= \frac{0.0111}{\sqrt{\frac{0.25}{38,562}}}$

$= \frac{0.0111}{0.00254} = 4.37$

For comparing two proportions (Part 2):

$z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}}$

$\hat{p}_1 = \frac{19,711}{38,562} = 0.5111$ (US proportion)

$\hat{p}_2 = \frac{17,703}{35,042} = 0.5052$ (Finnish proportion)

$n_1 = 38,562$ (US sample size)

$n_2 = 35,042$ (Finnish sample size)

$z = \frac{0.5111 - 0.5052}{\sqrt{\frac{0.5111(1-0.5111)}{38,562} + \frac{0.5052(1-0.5052)}{35,042}}}$

$= \frac{0.0059}{\sqrt{0.000006494 + 0.000007225}}$

$= \frac{0.0059}{0.00366} = 1.61$

These z-scores tell us:

1. For Part 1: The observed proportion differs from 0.5 by 4.37 standard errors - a highly significant result
2. For Part 2: The difference between countries is only 1.61 standard errors - not significant at the 5% level

# Question 5:

### Part (a)

A random variable $X$ has a distribution given by

$$P(X=i) = \pi_i, \quad i = 1,...,k \quad \text{where} \quad \sum_{i=1}^k \pi_i = 1$$

. In a sample of size $n$ from a population with distribution $X$, the frequency of outcome $i$ is $n_i$, where $n_i > 0$ and $\sum_{i=1}^k n_i = n$. Find the maximum likelihood estimates of $\pi_1,...,\pi_k$.

### Part (b)

The leaves of the plant _Pharbitis nil_ can be variegated or unvariegated and, at the same time, faded or unfaded. In an experiment reported by Bailey (1961), of 290 plants which were observed:

- 31 had variegated faded leaves
- 37 had variegated unfaded leaves
- 35 had unvariegated faded leaves
- 187 had unvariegated unfaded leaves

If the properties of variegated appearance and faded appearance are assumed independent, then a model for the above observations has respective probabilities $\frac{1}{16}, \frac{3}{16}, \frac{3}{16}, \frac{9}{16}$. The general alternative is that the probabilities $\pi_i$, $i = 1,...,4$, are restricted only by the constraint $\sum \pi_i = 1$. Use a $\chi^2$ goodness-of-fit test to show that the data offer strong evidence that the independence model is inappropriate.

### Part (c)

A genetic theory which allows for an effect called _genetic linkage_ assumes a probability model for the above observations with respective probabilities:

$\frac{1}{16}+\theta, \frac{3}{16}-\theta, \frac{3}{16}-\theta, \frac{9}{16}+\theta$

(i) Find the equation satisfied by the maximum likelihood estimate $\hat{\theta}$ of $\theta$. You may assume that $\hat{\theta} = 0.058$.

(ii) Let $H_0$ be the null hypothesis that the genetic linkage model is appropriate, and let $H_1$ be the general alternative. If $L_0$ is the supremum of the likelihood under $H_0$ and if $L_1$ is the supremum of the likelihood under $H_1$, show that:

$\Lambda = 2\sum_{i=1}^4 n_i \log(\frac{n_i}{n\pi_i(\hat{\theta})}),$

where $\Lambda = -2(\log L_0 - \log L_1)$. Write down the approximate distribution of $\Lambda$.

(iii) What can you infer about the plausibility of the genetic linkage model?

## Solution

### Part (a)

Let's find the maximum likelihood estimates of π₁,...,πₖ.

The likelihood function is:

$L(\pi_1,...,\pi_k) = \frac{n!}{n_1!...n_k!}\pi_1^{n_1}...\pi_k^{n_k}$

Taking the log:

$\ell(\pi_1,...,\pi_k) = \text{constant} + \sum_{i=1}^k n_i\log(\pi_i)$

We need to maximize this subject to $\sum_{i=1}^k \pi_i = 1$. Using a Lagrange multiplier λ:

$\frac{\partial}{\partial \pi_i}(\ell + \lambda(\sum_{i=1}^k \pi_i - 1)) = \frac{n_i}{\pi_i} + \lambda = 0$

Therefore $\pi_i = -\frac{n_i}{\lambda}$ for all i.

Using $\sum_{i=1}^k \pi_i = 1$, we get $-\frac{1}{\lambda}\sum_{i=1}^k n_i = 1$

Since $\sum_{i=1}^k n_i = n$, we have $\lambda = -n$

Therefore, the MLEs are:

$\hat{\pi_i} = \frac{n_i}{n}$ for i = 1,...,k

### Part (b)

Let's organize the data:

|              | Faded | Unfaded |
| ------------ | ----- | ------- |
| Variegated   | 31    | 37      |
| Unvariegated | 35    | 187     |

Under independence model:

- Expected frequencies: E₁ = 290(1/16) = 18.125
- E₂ = E₃ = 290(3/16) = 54.375
- E₄ = 290(9/16) = 163.125

The χ² statistic is:
$\chi^2 = \sum\frac{(O_i - E_i)^2}{E_i}$

$\chi^2 = \frac{(31-18.125)^2}{18.125} + \frac{(37-54.375)^2}{54.375} + \frac{(35-54.375)^2}{54.375} + \frac{(187-163.125)^2}{163.125}$

This has 1 degree of freedom (4 cells - 2 parameters - 1).

The calculated χ² value is large, providing strong evidence against independence.

### Part (c)

For the genetic linkage model, the log-likelihood is:

$\ell(\theta) = \sum n_i\log(\pi_i(\theta))$

where π₁ = 1/16 + θ, π₂ = π₃ = 3/16 - θ, π₄ = 9/16 + θ

The MLE satisfies $\frac{d\ell}{d\theta} = 0$, giving:

$\frac{n_1}{1/16 + \theta} - \frac{n_2}{3/16 - \theta} - \frac{n_3}{3/16 - \theta} + \frac{n_4}{9/16 + \theta} = 0$

Given $\hat{\theta} = 0.058$

For the likelihood ratio test:
$\Lambda = -2(\log L_0 - \log L_1) = 2\sum n_i\log(\frac{n_i}{n\pi_i(\hat{\theta})})$

Under H₀, we have 3 probabilities specified by 1 parameter θ, so df = 4 - 1 - 1 = 2.

Therefore $\Lambda \sim \chi^2_2$ approximately.

The genetic linkage model provides a better fit than independence, but we'd need to calculate Λ and compare to χ²₂ critical values to assess its plausibility.

The genetic linkage model provides much better fit to observed data because:

- The expected frequencies are much closer to observed values
- The genetic linkage model has one parameter ($\theta$) to adjust for association between traits, while independence model assumes no association
- The large discrepancy between observed and expected values under independence suggests strong evidence against independence assumption

To formally compare models, we would calculate the likelihood ratio statistic $\Lambda$ and compare to $\chi^2_2$ distribution, but even without this calculation, we can see the genetic linkage model provides a substantially better fit to the data.

### degrees of freedom:

**Part b (Independence Model):**

- Total parameters needed = 2 (row probability and column probability)
- Total constraints = 1 (probabilities sum to 1)
- Degrees of freedom = (number of cells - 1) - number of independent parameters
  $df = (4 - 1) - 2 = 1$

Under independence, we only need to know:

- Probability of being variegated ($p₁$)
- Probability of being faded ($p₂$)
- Then all cell probabilities are determined by these two parameters $(p₁p₂, p₁(1-p₂), (1-p₁)p₂, (1-p₁)(1-p₂))$

**Part c (Genetic Linkage Model):**

- Total parameters needed = 1 (just $θ$)
- Total constraints = 1 (probabilities sum to 1)
- Degrees of freedom = (number of cells - 1) - number of independent parameters
  $df = (4 - 1) - 1 = 2$

**Why? Under genetic linkage:**

- We only need to estimate one parameter $θ$
- All cell probabilities are determined by this single parameter through the specified formula $(1/16+θ, 3/16-θ, 3/16-θ, 9/16+θ)$

This illustrates an important principle: the degrees of freedom depend not just on the number of cells, but also on how many independent parameters we need to estimate under each model

# Question 6: Statistical Test of Independence for Two Categorical Variables

Let ordered pairs of random variables $(X_k,Y_k)$, $k=1,...,n$, be independent with:

$P((X_k,Y_k) = (i,j)) = \pi_{ij}$, for $i=1,...,r$ and $j=1,...,c$

where $\sum_{i,j}\pi_{ij}=1$

Let $n_{ij}$ be the frequency of outcome $(i,j)$, where $n_{ij}>0$.

Find the maximum likelihood estimates of the $\pi_{ij}$ under two scenarios:

1. Under the assumption that $\pi_{ij}=\alpha_i\beta_j$ for $i=1,...,r$ and $j=1,...,c$, where $\sum_i\alpha_i=\sum_j\beta_j=1$

2. Without this assumption

Using these results, find test statistics for testing the null hypothesis that the $X_k$ and the $Y_k$ are independent using:

a) The likelihood ratio method
b) Pearson's $\chi^2$ statistic

What can you say about the distributions of these two statistics for large values of $n$?

## Application

The data below (Agresti, 2007) cross-classifies gender and political party identification in the USA: 2757 individuals indicated whether they identified more strongly with the Democratic or Republican party or as Independents. Is there an association between gender and political party identification?

### Data Table: Party Identification by Gender

| Gender | Democrat | Independent | Republican |
| ------ | -------- | ----------- | ---------- |
| Female | 762      | 327         | 468        |
| Male   | 484      | 239         | 477        |

## Solution

### 1. Maximum Likelihood Estimates (MLEs)

Let's start with the simpler case (2) where we don't assume independence, then build up to case (1).

**Case 2: No Independence Assumption**

Here we need to maximize the likelihood subject only to the constraint that probabilities sum to 1.

The likelihood function is:
$L(\pi) = \prod_{i=1}^r \prod_{j=1}^c \pi_{ij}^{n_{ij}}$

Taking the log:
$\ell(\pi) = \sum_{i=1}^r \sum_{j=1}^c n_{ij} \log \pi_{ij}$

We maximize this subject to $\sum_{i=1}^r \sum_{j=1}^c \pi_{ij} = 1$ using a Lagrange multiplier $\lambda$:

$\mathcal{L} = \sum_{i=1}^r \sum_{j=1}^c n_{ij} \log \pi_{ij} - \lambda(\sum_{i=1}^r \sum_{j=1}^c \pi_{ij} - 1)$

Taking derivatives with respect to each $\pi_{ij}$ and setting to zero:
$\frac{\partial \mathcal{L}}{\partial \pi_{ij}} = \frac{n_{ij}}{\pi_{ij}} - \lambda = 0$

This gives:
$\pi_{ij} = \frac{n_{ij}}{\lambda}$

Using the constraint $\sum_{i,j} \pi_{ij} = 1$:
$\sum_{i,j} \frac{n_{ij}}{\lambda} = 1$

Therefore $\lambda = \sum_{i,j} n_{ij} = n$ (total sample size)

So the MLEs without the independence assumption are:
$\hat{\pi}_{ij} = \frac{n_{ij}}{n}$

**Case 1: With Independence Assumption**

Now we assume $\pi_{ij} = \alpha_i\beta_j$ where $\sum_i \alpha_i = \sum_j \beta_j = 1$

The log-likelihood becomes:
$\ell(\alpha,\beta) = \sum_{i=1}^r \sum_{j=1}^c n_{ij} \log(\alpha_i\beta_j)$
$= \sum_{i=1}^r \sum_{j=1}^c n_{ij}(\log \alpha_i + \log \beta_j)$

Using two Lagrange multipliers $\lambda$ and $\mu$ for the two constraints:

$\mathcal{L} = \sum_{i,j} n_{ij}(\log \alpha_i + \log \beta_j) - \lambda(\sum_i \alpha_i - 1) - \mu(\sum_j \beta_j - 1)$

Taking derivatives and setting to zero:
$\frac{\partial \mathcal{L}}{\partial \alpha_i} = \sum_j \frac{n_{ij}}{\alpha_i} - \lambda = 0$
$\frac{\partial \mathcal{L}}{\partial \beta_j} = \sum_i \frac{n_{ij}}{\beta_j} - \mu = 0$

This gives:
$\alpha_i = \frac{n_{i+}}{\lambda}$ and $\beta_j = \frac{n_{+j}}{\mu}$

where $n_{i+} = \sum_j n_{ij}$ and $n_{+j} = \sum_i n_{ij}$ are the row and column totals.

Using the constraints, we find:
$\hat{\alpha}_i = \frac{n_{i+}}{n}$ and $\hat{\beta}_j = \frac{n_{+j}}{n}$

Therefore under independence:
$\hat{\pi}_{ij} = \hat{\alpha}_i\hat{\beta}_j = \frac{n_{i+}}{n} \cdot \frac{n_{+j}}{n}$

### 2. Test Statistics

**Likelihood Ratio Test**

The likelihood ratio statistic is:
$\Lambda = -2\log\left(\frac{\sup_{H_0} L}{\sup_{H_1} L}\right)$
$= -2\log\left(\frac{L(\hat{\alpha}\hat{\beta})}{L(\hat{\pi})}\right)$
$= 2\sum_{i,j} n_{ij}\log\left(\frac{n_{ij}n}{n_{i+}n_{+j}}\right)$

**Pearson's Chi-square Test**

$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$

where:

- $O_{ij} = n_{ij}$ (observed frequencies)
- $E_{ij} = \frac{n_{i+}n_{+j}}{n}$ (expected frequencies under independence)

### 3. Large Sample Distribution

Under $H_0$ (independence), both $\Lambda$ and $\chi^2$ follow approximately a $\chi^2$ distribution with $(r-1)(c-1)$ degrees of freedom for large $n$.

### 4. Testing Independence Between Gender and Party Identification

First, let's clearly state what we have:

- Two categorical variables (Gender and Party Identification)
- A 2×3 contingency table of observed frequencies:

$\begin{array}{l|ccc|c}
\text{Gender} & \text{Democrat} & \text{Independent} & \text{Republican} & \text{Total} \\
\hline
\text{Female} & 762 & 327 & 468 & 1557 \\
\text{Male} & 484 & 239 & 477 & 1200 \\
\hline
\text{Total} & 1246 & 566 & 945 & 2757
\end{array}$

Under the null hypothesis of independence, expected frequencies are calculated as:
$E_{ij} = \frac{(\text{row total})_i \times (\text{column total})_j}{\text{total sample size}}$

Let's calculate each expected frequency:

For Female row:

- Democrat: $E_{11} = \frac{1557 \times 1246}{2757} = 703.8$
- Independent: $E_{12} = \frac{1557 \times 566}{2757} = 319.7$
- Republican: $E_{13} = \frac{1557 \times 945}{2757} = 533.5$

For Male row:

- Democrat: $E_{21} = \frac{1200 \times 1246}{2757} = 542.2$
- Independent: $E_{22} = \frac{1200 \times 566}{2757} = 246.3$
- Republican: $E_{23} = \frac{1200 \times 945}{2757} = 411.5$

### A. Pearson's Chi-square Statistic

$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$

Let's calculate each term:

Female row:

- Democrat: $\frac{(762 - 703.8)^2}{703.8} = 4.80$
- Independent: $\frac{(327 - 319.7)^2}{319.7} = 0.17$
- Republican: $\frac{(468 - 533.5)^2}{533.5} = 8.12$

Male row:

- Democrat: $\frac{(484 - 542.2)^2}{542.2} = 6.23$
- Independent: $\frac{(239 - 246.3)^2}{246.3} = 0.22$
- Republican: $\frac{(477 - 411.5)^2}{411.5} = 10.53$

$\chi^2 = 30.07$

### B. Likelihood Ratio Statistic

$G^2 = 2\sum_{i,j} O_{ij}\log\left(\frac{O_{ij}}{E_{ij}}\right)$

Let me verify this calculation:

$G^2 = 30.02$

## Step 4: Interpretation

1. Degrees of Freedom:

   - For a 2×3 table: df = (r-1)(c-1) = (2-1)(3-1) = 2

2. Critical Values for $\chi^2_2$:

   - At 5% level: 5.99
   - At 1% level: 9.21
   - At 0.1% level: 13.82

3. Decision:
   Both test statistics (χ² = 30.07 and G² = 30.02) are much larger than the critical value even at the 0.1% level (13.82). Therefore, we have extremely strong evidence to reject the null hypothesis of independence.

4. Detailed Analysis:
   Looking at the contributions to the chi-square statistic, we see:

   - The largest contributions come from Republicans (18.65 total from both genders)
   - Democrats show the next largest departure from independence (11.03 total)
   - Independents show relatively small departures (0.39 total)

5. Substantive Conclusion:
   There is a clear association between gender and party identification:
   - Women are more likely to identify as Democrats (762 observed vs 703.8 expected)
   - Men are more likely to identify as Republicans (477 observed vs 411.5 expected)
   - Independent identification shows little gender difference

This thorough analysis demonstrates both the mathematical application of the independence tests and their practical interpretation in a social science context. The consistency between the two test statistics adds robustness to our conclusions.

# Key Statistical Concepts for Quant Finance - Study Notes

## 1. Hypothesis Testing Framework

### Core Intuition

- Always start with null hypothesis ($H_0$) as the "status quo" or "no effect" scenario
- Think of hypothesis testing like a legal trial: default is innocence ($H_0$) unless strong evidence suggests otherwise
- p-value = probability of seeing data this extreme or more extreme _assuming $H_0$ is true_

### Critical Formulas

- Test statistic (z-test): $z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$
- Test statistic (t-test): $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$
- Power of test = $1 - \beta$ = probability of correctly rejecting false $H_0$

### Interview Tips

- Know when to use z-test (known σ) vs t-test (unknown σ)
- Understand trade-off between Type I (α) and Type II (β) errors
- Sample size affects power - larger n means better ability to detect small effects

## 2. Maximum Likelihood Estimation (MLE)

### Core Intuition

- MLE finds parameter values that make observed data most likely
- Log-likelihood often easier to work with than likelihood
- For normal data, MLE often gives same result as "common sense" estimators

### Key Formulas

- Likelihood: $L(\theta) = \prod_{i=1}^n f(x_i|\theta)$
- Log-likelihood: $\ell(\theta) = \sum_{i=1}^n \log f(x_i|\theta)$
- MLE: $\hat{\theta} = \text{argmax}_\theta \ell(\theta)$

### Interview Tips

- Know that MLE is asymptotically unbiased and efficient
- For normal distribution: $\hat{\mu} = \bar{x}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(x_i-\bar{x})^2$
- Can handle censored/truncated data better than method of moments

## 3. Likelihood Ratio Tests

### Core Intuition

- Compare maximized likelihood under $H_0$ vs $H_1$
- If ratio is small, evidence against $H_0$
- Powerful for comparing nested models

### Key Formula

$\Lambda = -2\log\left(\frac{L(\theta_0)}{L(\hat{\theta})}\right) \sim \chi^2_k$

### Interview Tips

- Under $H_0$, $\Lambda$ follows $\chi^2$ with df = difference in parameters
- Can be used for model selection
- More powerful than Wald test in many cases

## 4. Statistical Independence

### Core Intuition

- Independence means $P(A\cap B) = P(A)P(B)$
- For contingency tables: expected frequency = $\frac{\text{row total} \times \text{column total}}{\text{grand total}}$
- Large deviations from expected frequencies suggest dependence

### Key Formulas

- Chi-square statistic: $\chi^2 = \sum \frac{(O-E)^2}{E}$
- Degrees of freedom = (rows-1)(columns-1)

### Interview Tips

- Know relationship between correlation and independence
- Independence important for portfolio theory and risk management
- Can test independence using either $\chi^2$ or likelihood ratio test

## 5. Advanced Topics for Interviews

### Bayesian vs Frequentist

- Frequentist: θ fixed, data random
- Bayesian: data fixed, θ random
- Bayesian updates prior beliefs with data

### Delta Method

$g(\bar{X}) \approx N(g(\mu), [g'(\mu)]^2\frac{\sigma^2}{n})$

- Important for transforming estimators
- Used in financial derivatives pricing

### Asymptotic Properties

- Consistency: $\hat{\theta}_n \xrightarrow{p} \theta$
- Asymptotic normality: $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0,\sigma^2)$
- Important for large sample inference
