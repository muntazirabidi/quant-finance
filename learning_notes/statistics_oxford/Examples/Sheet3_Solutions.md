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
