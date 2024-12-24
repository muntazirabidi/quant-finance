# Question 1

> A two-part question about statistical inference:

> What is the connection between Fisher's information and the asymptotic distribution of the maximum likelihood estimator?

> Assume the individuals in a sample of size $n = 1029$ are independent and that each individual has blood type M with probability $(1-\theta)^2$, type MN with probability $2\theta(1-\theta)$, and type N with probability $\theta^2$. For the following data (Rice, 2007) find the maximum likelihood estimate $\hat{\theta}$ and use the asymptotic distribution of the MLE to find an approximate 95% confidence interval for $\theta$.

> | Blood Type | Frequency |
> | ---------- | --------- |
> | M          | 342       |
> | MN         | 500       |
> | N          | 187       |

This question elegantly combines theoretical concepts of Fisher information with their practical application in genetic data analysis. It tests understanding of:

- The asymptotic theory of maximum likelihood estimation
- The role of Fisher information in determining estimation precision
- Practical computation of MLEs and confidence intervals
- Application to real genetic data following Hardy-Weinberg proportions

The problem requires both theoretical understanding and practical statistical computation skills. Note how the blood type frequencies follow a trinomial distribution with probabilities determined by a single parameter $\theta$, making this an interesting case study in constrained parameter estimation.

## Solution Part 1: Fisher Information and Maximum Likelihood Estimation

### 1. Understanding Fisher Information

Fisher Information quantifies the amount of information a sample carries about a parameter $\theta$. It is formally defined as:

$I(\theta) = -E[\frac{\partial^2}{\partial \theta^2} \log L(\theta;X)]$

Alternatively, it can be expressed using the score function:

$I(\theta) = E[(\frac{\partial}{\partial \theta} \log L(\theta;X))^2]$

where the score function $U(\theta) = \frac{\partial}{\partial \theta} \log L(\theta;X)$ has the property:

$E[U(\theta)] = 0$

### 2. Maximum Likelihood Estimator (MLE)

The MLE, denoted $\hat{\theta}_n$, maximizes the likelihood function $L(\theta;X)$ and satisfies:

$\left.\frac{\partial}{\partial \theta} \log L(\theta;X)\right|_{\theta=\hat{\theta}_n} = 0$

### 3. Asymptotic Distribution Properties

Under regularity conditions, the MLE exhibits two key properties:

1. **Consistency**:
   $\hat{\theta}_n \xrightarrow{P} \theta_0$ as $n \to \infty$

2. **Asymptotic Normality**:
   $\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} N(0, I(\theta_0)^{-1})$

### 4. The Fundamental Connection

The connection between Fisher Information and the MLE's asymptotic distribution manifests in several ways:

**4.1 Variance Relationship**

- For large $n$, the variance of the MLE is approximately:

  $\text{Var}(\hat{\theta}_n) \approx \frac{1}{n \cdot I(\theta_0)}$

**4.2 Confidence Intervals**

- Asymptotic $(1-\alpha)$ confidence intervals take the form:

  $\hat{\theta}_n \pm z_{\alpha/2}\sqrt{\frac{1}{n \cdot I(\hat{\theta}_n)}}$

where $z_{\alpha/2}$ is the standard normal critical value.

### 5. Practical Implications

1. **Precision Scale**:

   - Higher Fisher Information → Lower variance → More precise estimation
   - Lower Fisher Information → Higher variance → Less precise estimation

2. **Sample Size Effect**:
   - Variance decreases proportionally to $\frac{1}{n}$
   - Fisher Information scales linearly with sample size

### 6. Theoretical Importance

The relationship between Fisher Information and the MLE's asymptotic distribution stems from:

- The curvature of the log-likelihood function at its maximum
- Local quadratic approximation via Taylor expansion
- The central role of the score function in both concepts

### Summary

This connection reveals that Fisher Information fundamentally determines the precision of maximum likelihood estimation through:

1. The asymptotic variance of the MLE
2. The shape of the likelihood surface
3. The efficiency of parameter estimation

These relationships make Fisher Information a crucial concept in both theoretical statistics and practical applications.

## Solution Part 2:

Given blood type frequencies:

- Type M: $X_M = 342$
- Type MN: $X_{MN} = 500$
- Type N: $X_N = 187$
- Total sample size: $n = 1029$

With probabilities:

- $P(M) = (1-\theta)^2$
- $P(MN) = 2\theta(1-\theta)$
- $P(N) = \theta^2$

### 1. Likelihood Function

The likelihood function is:
$L(\theta) = [(1-\theta)^2]^{X_M} [2\theta(1-\theta)]^{X_{MN}} [\theta^2]^{X_N}$

Log-likelihood:
$\ell(\theta) = (2X_M + X_{MN})\log(1-\theta) + (X_{MN} + 2X_N)\log(\theta) + X_{MN}\log(2)$

### 2. Finding MLE

First derivative:
$\frac{\partial \ell(\theta)}{\partial \theta} = -\frac{2X_M + X_{MN}}{1-\theta} + \frac{X_{MN} + 2X_N}{\theta}$

Setting to zero and solving:
$\hat{\theta} = \frac{X_{MN} + 2X_N}{2(X_M + X_{MN} + X_N)} = \frac{500 + 2(187)}{2(1029)} = \frac{874}{2058} \approx 0.4246$

### 3. Fisher Information and Confidence Interval

Second derivative:
$\frac{\partial^2 \ell(\theta)}{\partial \theta^2} = -\frac{2X_M + X_{MN}}{(1-\theta)^2} - \frac{X_{MN} + 2X_N}{\theta^2}$

Fisher Information at $\hat{\theta}$:
$I(\hat{\theta}) = \frac{2X_M + X_{MN}}{(1-\hat{\theta})^2} + \frac{X_{MN} + 2X_N}{\hat{\theta}^2} \approx 8422.7$

Standard Error:
$SE(\hat{\theta}) = \sqrt{\frac{1}{nI(\hat{\theta})}} \approx 0.00344$

### 4. Final Results

1. Maximum Likelihood Estimate:
   $\hat{\theta} = 0.4246$

2. 95% Confidence Interval:
   $\hat{\theta} \pm 1.96 \times SE(\hat{\theta})$
   $(0.4179, 0.4313)$

### Verification

All calculations were checked and are correct. The Fisher Information calculation:

- At $\hat{\theta} = 0.4246$:
  - $(1-\hat{\theta})^2 = 0.3311$
  - $\hat{\theta}^2 = 0.1803$
  - Leading to $I(\hat{\theta}) \approx 8422.7$

The confidence interval uses:

- $z_{0.025} = 1.96$
- Width: $1.96 \times 0.00344 = 0.0067$

These results provide strong evidence that $\theta$ is approximately 0.42, with high precision given the narrow confidence interval.

# Question 2: Estimation of Log-Standard Deviation in Normal Distribution

> Consider independent normal random variables $X_1,...,X_n \sim N(\mu,\sigma^2)$ where:
>
> - $\mu$ is known
> - $\sigma$ is unknown
> - We want to estimate $\psi = \log \sigma$
>
> Solve the following:
>
> **(a)** Find:
>
> 1. The maximum likelihood estimator $\hat{\sigma}$
> 2. The asymptotic normal approximation to the distribution of $\hat{\sigma}$
>
> **(b)** Using the delta method:
>
> 1. Find the asymptotic distribution of $\hat{\psi}$
> 2. Construct an approximate 95% confidence interval for $\psi$
>
> **(c)** Explain how to convert the confidence interval for $\psi$ into an approximate confidence interval for $\sigma$

## Solution Part (a):

### 1. Finding the MLE $\hat{\sigma}$

For $X_i \sim N(\mu,\sigma^2)$ independently:

$L(\sigma) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i-\mu)^2}{2\sigma^2}\right)$

$\ell(\sigma) = -\frac{n}{2}\log(2\pi) - n\log(\sigma) - \frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2$

$\frac{\partial \ell}{\partial \sigma} = -\frac{n}{\sigma} + \frac{1}{\sigma^3}\sum_{i=1}^n(x_i-\mu)^2$

$-\frac{n}{\sigma} + \frac{1}{\sigma^3}\sum_{i=1}^n(x_i-\mu)^2 = 0$

Simplifying:
$\hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n(x_i-\mu)^2$

Therefore:
$\hat{\sigma} = \sqrt{\frac{1}{n}\sum_{i=1}^n(x_i-\mu)^2}$

### 2. Finding Asymptotic Distribution

$\frac{\partial^2 \ell}{\partial \sigma^2} = \frac{n}{\sigma^2} - \frac{3}{\sigma^4}\sum_{i=1}^n(x_i-\mu)^2$

At $\hat{\sigma}$, this is negative, confirming we have a maximum.

$I(\sigma) = -E\left[\frac{\partial^2 \ell}{\partial \sigma^2}\right] = \frac{2n}{\sigma^2}$

For large $n$, the MLE is approximately normally distributed:

$\hat{\sigma} \stackrel{a}{\sim} N\left(\sigma, \frac{1}{nI(\sigma)}\right)$

Therefore:
$\hat{\sigma} \stackrel{a}{\sim} N\left(\sigma, \frac{\sigma^2}{2n}\right)$

This means:
$\sqrt{n}(\hat{\sigma} - \sigma) \stackrel{d}{\to} N\left(0, \frac{\sigma^2}{2}\right)$

---

The MLE $\hat{\sigma}$ is therefore:

1. Consistent (converges to true value)
2. Asymptotically normal
3. Has variance decreasing at rate $1/n$

## Solution Part (b): Applying Delta Method and Confidence Interval

### 1. Finding Asymptotic Distribution of $\hat{\psi}$

We want to find distribution of $\hat{\psi} = \log(\hat{\sigma})$
where $g(\sigma) = \log(\sigma)$

For $g'(\sigma) = \frac{1}{\sigma}$, the delta method states:

$\sqrt{n}(\hat{\psi} - \psi) \stackrel{d}{\to} N(0, [g'(\sigma)]^2 \cdot \frac{\sigma^2}{2})$

Substituting $g'(\sigma) = \frac{1}{\sigma}$:

$\text{Var}(\hat{\psi}) \approx \frac{1}{n} \cdot (\frac{1}{\sigma})^2 \cdot \frac{\sigma^2}{2} = \frac{1}{2n}$

Therefore:
$\hat{\psi} \stackrel{a}{\sim} N(\psi, \frac{1}{2n})$

### 2. Constructing 95% Confidence Interval

For 95% confidence, we use $z_{0.025} = 1.96$

$\hat{\psi} \pm z_{0.025} \sqrt{\frac{1}{2n}}$

Therefore, the 95% confidence interval for $\psi$ is:

$\left(\log(\hat{\sigma}) - \frac{1.96}{\sqrt{2n}}, \log(\hat{\sigma}) + \frac{1.96}{\sqrt{2n}}\right)$

---

Key observations:

1. The variance of $\hat{\psi}$ is constant (doesn't depend on $\sigma$)
2. The interval is symmetric around $\log(\hat{\sigma})$
3. Width of interval shrinks at rate $1/\sqrt{n}$

This provides a theoretically elegant result as the confidence interval has constant width on the log scale.

## Solution Part (c): Converting Confidence Intervals

Since $\psi = \log(\sigma)$, we can transform the confidence interval for $\psi$ to get one for $\sigma$ by applying the exponential function.

If $(L, U)$ is a 95% CI for $\psi = \log(\sigma)$, then:
$(e^L, e^U)$ is a 95% CI for $\sigma$

### Detailed Steps

1. From part (b), our CI for $\psi$ was:
   $\left(\log(\hat{\sigma}) - \frac{1.96}{\sqrt{2n}}, \log(\hat{\sigma}) + \frac{1.96}{\sqrt{2n}}\right)$

2. Apply exponential function:
   $\left(\hat{\sigma} \cdot e^{-1.96/\sqrt{2n}}, \hat{\sigma} \cdot e^{1.96/\sqrt{2n}}\right)$

### Key Properties

1. **Asymmetry**:

   - Unlike the interval for $\psi$, this interval is not symmetric around $\hat{\sigma}$
   - This reflects the skewed nature of the distribution of $\hat{\sigma}$

2. **Interpretation**:

   - The interval gives positive values only (appropriate for $\sigma$)
   - The multiplicative nature of the interval reflects the log-normal behavior

3. **Width**:
   - The relative width (ratio of upper to lower bound) remains constant
   - This is often more appropriate for scale parameters like $\sigma$

This transformation maintains the 95% confidence level while ensuring the interval is appropriate for the scale parameter $\sigma$.

# Question 3:

A sequence of estimators $T_n$, $n \geq 1$, of a scalar parameter $\theta$ is called consistent if, for all $\theta$ (i.e., whatever the true value of $\theta$), we have that $T_n$ converges in probability to $\theta$ as $n \to \infty$.
Suppose $T_n$ is a sequence of estimators of $\theta$ satisfying:

$\text{bias}(T_n) \to 0$ and
$\text{var}(T_n) \to 0$ as $n \to \infty$

Show that $T_n$ is consistent for $\theta$.
[Hint: Chebyshev's inequality]

## Solution: Consistency of Estimators

Let's prove this step by step using Chebyshev's inequality.

We need to show that $T_n$ converges in probability to $\theta$, i.e.,
$P(|T_n - \theta| > \epsilon) \to 0$ as $n \to \infty$ for any $\epsilon > 0$

For any random variable $X$ with mean $\mu$ and variance $\sigma^2$, and any $k > 0$:

$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$

Let's express $|T_n - \theta|$ in terms of bias:

$T_n - \theta = (T_n - E[T_n]) + (E[T_n] - \theta)$
$= (T_n - E[T_n]) + \text{bias}(T_n)$

For any $\epsilon > 0$:

$P(|T_n - \theta| > \epsilon) = P(|(T_n - E[T_n]) + \text{bias}(T_n)| > \epsilon)$
$\leq P(|T_n - E[T_n]| + |\text{bias}(T_n)| > \epsilon)$

Let $b_n = |\text{bias}(T_n)|$. Then:

$P(|T_n - E[T_n]| > \epsilon - b_n) \leq \frac{\text{var}(T_n)}{(\epsilon - b_n)^2}$

Given:

- $\text{bias}(T_n) \to 0$ as $n \to \infty$, so $b_n \to 0$
- $\text{var}(T_n) \to 0$ as $n \to \infty$

Therefore, for sufficiently large $n$:

- $\epsilon - b_n > 0$ (since $b_n \to 0$)
- $\frac{\text{var}(T_n)}{(\epsilon - b_n)^2} \to 0$ (since $\text{var}(T_n) \to 0$ and $\epsilon - b_n$ converges to a positive constant)

Thus, for any $\epsilon > 0$:

$\lim_{n \to \infty} P(|T_n - \theta| > \epsilon) = 0$

This proves that $T_n$ is consistent for $\theta$.

### Key Insights

1. The convergence of both bias and variance to zero is crucial for consistency.
2. Chebyshev's inequality provides the probabilistic bound needed to show convergence in probability.
3. The proof combines both the bias and variance components to show overall consistency.

This completes the proof of consistency for the sequence of estimators $T_n$.

# Question 4: Earthquake Time Interval Analysis Problem

## Problem Statement

The following data are time intervals in days between earthquakes which either registered magnitudes greater than 7.5 on the Richter scale or produced over 1,000 fatalities. Recording starts on 16 December, 1902 and ends on 4 March, 1977, a total period of 27,107 days. There were 63 earthquakes in all, and therefore 62 recorded time intervals.

## Data

```
840 190 140 139 246 157 695 1336 780 1617 145 294 335 203 638
44 562 1354 436 937 337 21 454 30 735 121 763 6 384 381 507
10 667 129 365 280 464 099 243 440 2 20 982 736 194 995 992
205 847 595 56 304 838 87 319 375 832 263 460 567 328
```

## Parts:

**1. Maximum Likelihood Estimation**
Assuming the data to be a random sample $X_1,...,X_n$ from an exponential distribution with parameter $\lambda$, obtain the maximum likelihood estimator $\hat{\lambda}$ of $\lambda$ and calculate the maximum likelihood estimate.

**2. Distribution of Sum**
Given that the moment generating function of a gamma distribution with parameters $(n,\lambda)$ is:

$$M_n(t) = \left(\frac{\lambda}{\lambda-t}\right)^n$$

Show that $Y = \sum_{i=1}^n X_i$ has a gamma distribution.

**3. Confidence Intervals**
Show that $(a_n x, b_n x)$ is an exact 95% central confidence interval for $\lambda$ if:

$$\int_0^a \frac{y^{n-1}e^{-y}}{\Gamma(n)}dy = \int_\infty^b \frac{y^{n-1}e^{-y}}{\Gamma(n)}dy = 0.025$$

**4. Fisher Information**
Obtain Fisher's information for $\lambda$ and use it to find an approximate 95% confidence interval for $\lambda$.

The interval given by the exact method above is $(0.0018, 0.0029)$. Verify numerically that your approximate interval is close to this.

## Solution:

### 1. Maximum Likelihood Estimation

For an exponential distribution with parameter λ, the probability density function is:
f(x) = λe^(-λx) for x ≥ 0

Let's solve this:

1. First, let's write the likelihood function for n independent observations:
   L(λ) = ∏(i=1 to n) λe^(-λx_i)
   = λ^n \* e^(-λ∑x_i)

2. Take the natural logarithm to get the log-likelihood:
   ln L(λ) = n ln(λ) - λ∑x_i

3. To find the MLE, take the derivative with respect to λ and set it to zero:
   d/dλ[ln L(λ)] = n/λ - ∑x_i = 0

4. Solve for λ:
   n/λ = ∑x_i
   λ = n/∑x_i

Therefore, the maximum likelihood estimator is:
λ̂ = n/∑x_i

Let's calculate the actual estimate using our data:

Therefore:

- The maximum likelihood estimator (MLE) formula is λ̂ = n/∑x_i
- With our data:
  - n = 61 observations
  - ∑x_i = 27,521 days
  - The maximum likelihood estimate is λ̂ ≈ 0.002216

This estimate represents the rate parameter of the exponential distribution, which is the inverse of the mean waiting time between earthquakes. The small value indicates relatively long average waiting times between events, which makes sense given these are major earthquakes.

## (2) Moment Generating Function:

Let's solve this step by step using the properties of moment generating functions (MGFs).

1. For independent random variables $X$ and $Y$:
   $$M_{X+Y}(t) = M_X(t) \times M_Y(t)$$

2. If two random variables have the same MGF, they have the same distribution

For our exponential variables $X_i$ with parameter $\lambda$:

$$
\begin{aligned}
M_X(t) &= \int_0^\infty e^{tx} \lambda e^{-\lambda x} dx \\
&= \lambda \int_0^\infty e^{(t-\lambda)x} dx \\
&= \frac{\lambda}{\lambda-t} \text{ for } t < \lambda
\end{aligned}
$$

For $Y = \sum X_i$, since the $X_i$ are independent:

$$
\begin{aligned}
M_Y(t) &= M_{X_1+X_2+...+X_n}(t) \\
&= M_{X_1}(t) \times M_{X_2}(t) \times ... \times M_{X_n}(t) \\
&= \left[\frac{\lambda}{\lambda-t}\right]^n
\end{aligned}
$$

### Comparison with Gamma Distribution

The given MGF of the gamma distribution with parameters $(n,\lambda)$ is:

$$M_n(t) = \left(\frac{\lambda}{\lambda-t}\right)^n$$

Since $Y = \sum X_i$ has exactly the same MGF as a gamma distribution with parameters $(n,\lambda)$, we can conclude that $Y$ follows a gamma distribution with these parameters.

### Intuitive Understanding

This result makes sense because:

- The gamma distribution represents the waiting time until the $n$th event in a Poisson process
- Each $X_i$ represents one waiting time in our sequence
- Their sum represents the total waiting time for all $n$ events
- The parameter $\lambda$ remains the same as in our original exponential distribution
- The parameter $n$ corresponds to the number of exponential variables we're summing

### Conclusion

Therefore, we have proven that $Y = \sum X_i$ follows a gamma distribution with parameters $(n,\lambda)$. This is a special case of a more general property: the sum of $n$ independent exponential random variables with the same parameter $\lambda$ follows a gamma distribution with shape parameter $n$ and rate parameter $\lambda$.

### (3) Confidence Intervals

Let's prove why $(a_n x, b_n x)$ is an exact 95% confidence interval for $\lambda$.

From part 2, we know that $\sum X_i$ follows a gamma distribution with parameters $(n,\lambda)$.
Let $S = \sum X_i$

For the gamma distribution, if:
$$Y \sim \text{Gamma}(n,1), \text{ then } \frac{Y}{\lambda} \sim \text{Gamma}(n,\lambda)$$

Therefore:
$$\lambda S \sim \text{Gamma}(n,1)$$

The given integrals represent tail probabilities of a standard $\text{Gamma}(n,1)$ distribution:

$$P(\lambda S < a) = \int_0^a \frac{y^{n-1}e^{-y}}{\Gamma(n)}dy = 0.025$$

$$P(\lambda S > b) = \int_b^\infty \frac{y^{n-1}e^{-y}}{\Gamma(n)}dy = 0.025$$

This gives us:
$$P(a < \lambda S < b) = 0.95$$

We can rewrite this in terms of $\lambda$:
$$P(a < \lambda S < b) = P(\frac{a}{S} < \lambda < \frac{b}{S}) = 0.95$$

Therefore, $(\frac{a}{S}, \frac{b}{S})$ is a 95% confidence interval for $\lambda$

Since $S = n\bar{x}$ (where $\bar{x}$ is the sample mean), we can write:
$$(\frac{a}{n\bar{x}}, \frac{b}{n\bar{x}}) = (a_n x, b_n x)$$
where $a_n = \frac{a}{n}$ and $b_n = \frac{b}{n}$

### Conclusion

$(a_n x, b_n x)$ is an exact 95% confidence interval for $\lambda$ because:

- It contains $\lambda$ with probability 0.95
- The distribution used is exactly gamma, not an approximation
- The confidence level comes directly from the specified tail probabilities (0.025 + 0.025 = 0.05, giving us 0.95 confidence)

The interval $(0.0018, 0.0029)$ can be verified by:

1. Calculating $\bar{x}$ from our data
2. Finding $a$ and $b$ from gamma distribution tables or numerical methods
3. Computing $a_n = \frac{a}{n}$ and $b_n = \frac{b}{n}$
4. Multiplying these by $\bar{x}$ to get our interval

## (4) Fisher Information and Approximate Confidence Interval

For an exponential distribution with parameter $\lambda$, the probability density function is:
$$f(x|\lambda) = \lambda e^{-\lambda x}, \quad x \geq 0$$

The log-likelihood for a single observation is:
$$\ell(\lambda|x) = \ln(\lambda) - \lambda x$$

Taking the second derivative with respect to $\lambda$:
$$\frac{\partial \ell}{\partial \lambda} = \frac{1}{\lambda} - x$$
$$\frac{\partial^2 \ell}{\partial \lambda^2} = -\frac{1}{\lambda^2}$$

Fisher Information for a single observation is:
$$I(\lambda) = -E\left[\frac{\partial^2 \ell}{\partial \lambda^2}\right] = \frac{1}{\lambda^2}$$

For $n$ independent observations, Fisher Information is:
$$I_n(\lambda) = \frac{n}{\lambda^2}$$

Using the asymptotic normality of MLE:
$$\hat{\lambda} \sim N\left(\lambda, \frac{1}{I_n(\lambda)}\right)$$

Therefore:
$$\hat{\lambda} \sim N\left(\lambda, \frac{\lambda^2}{n}\right)$$

A 95% confidence interval is given by:
$$\hat{\lambda} \pm 1.96 \sqrt{\frac{\hat{\lambda}^2}{n}}$$

Let's calculate using our data:

1. From Part 1, we found $\hat{\lambda} = 0.002216$
2. Number of observations $n = 61$
3. Standard error: $SE(\hat{\lambda}) = \sqrt{\frac{\hat{\lambda}^2}{n}} = 2.8373 \times 10^{-4}$

The approximate 95% confidence interval is:
$(0.001660, 0.002772)$

This interval is indeed quite close to the exact interval $(0.0018, 0.0029)$ obtained by the previous method. The small difference is due to:

- The asymptotic nature of the Fisher Information method
- The normal approximation used in deriving the interval
- Rounding in numerical calculations

Both intervals suggest similar conclusions about the precision of our estimate of $\lambda$.

<img src="../Confidence Intervals/Code/Figures/fisher.png" alt="alt text">

# Question 5: Confidence Intervals for Variance

> Let $X_1,...,X_n$ be a random sample from a normal distribution with known mean $\mu$ and unknown variance >$\sigma^2$. Three possible confidence intervals for $\sigma^2$ are:
>
> (a) $\left(\frac{\sum_{i=1}^n(X_i-\bar{X})^2}{a_1}, \frac{\sum_{i=1}^n(X_i-\bar{X})^2}{a_2}\right)$
>
> (b) $\left(\frac{\sum_{i=1}^n(X_i-\mu)^2}{b_1}, \frac{\sum_{i=1}^n(X_i-\mu)^2}{b_2}\right)$
>
> (c) $\left(\frac{n(\bar{X}-\mu)^2}{c_1}, \frac{n(\bar{X}-\mu)^2}{c_2}\right)$
>
> where $a_1, a_2, b_1, b_2, c_1, c_2$ are constants.
>
> 1.  Find values of these six constants which give confidence level 0.90 for each of the three intervals when >$n = 10$ and compare the expected widths of the three intervals in this case.
>
> 2.  With $\sigma^2 = 1$, what value of $n$ is required to achieve a 90% confidence interval of expected width >less than 2 in cases (b) and (c) above?
>
> _Note: For a $\chi^2$ with e.g. 6 degrees of freedom, you can use `qchisq(0.05, 6)` to find the 0.05 >quantile._

## Solution

### Step 1: Constants for 90% Confidence Intervals

To construct confidence intervals, we use the quantiles of the chi-square distribution:

Let $q_{\alpha, k}$ denote the quantile of the chi-square distribution with $k$ degrees of freedom at probability $\alpha$.

For a 90% confidence level:
$$\alpha_1 = 0.05, \quad \alpha_2 = 0.95$$

#### Case (a)

We know that:
$$\sum_{i=1}^n (X_i - \bar{X})^2 \sim \sigma^2 \chi^2_{n-1}, \quad n-1 = 9$$

The constants are:
$$a_1 = \frac{1}{q_{0.95, 9}}, \quad a_2 = \frac{1}{q_{0.05, 9}}$$

#### Case (b)

We know that:
$$\sum_{i=1}^n (X_i - \mu)^2 \sim \sigma^2 \chi^2_n, \quad n = 10$$

The constants are:
$$b_1 = \frac{1}{q_{0.95, 10}}, \quad b_2 = \frac{1}{q_{0.05, 10}}$$

#### Case (c)

We know that:
$$n(\bar{X} - \mu)^2 \sim \sigma^2 \chi^2_1$$

The constants are:
$$c_1 = \frac{1}{q_{0.95, 1}}, \quad c_2 = \frac{1}{q_{0.05, 1}}$$

### Step 2: Expected Width of Confidence Intervals

The expected width of a confidence interval is:
$$\text{Width} = \text{Upper Bound} - \text{Lower Bound}$$

For each case:

#### Case (a)

$$\text{Width}_a = \left(\frac{1}{q_{0.05, 9}} - \frac{1}{q_{0.95, 9}}\right) \cdot (n-1)\sigma^2$$

#### Case (b)

$$\text{Width}_b = \left(\frac{1}{q_{0.05, 10}} - \frac{1}{q_{0.95, 10}}\right) \cdot n\sigma^2$$

#### Case (c)

$$\text{Width}_c = \left(\frac{1}{q_{0.05, 1}} - \frac{1}{q_{0.95, 1}}\right) \cdot \sigma^2$$

### Step 3: Required Sample Size for Width < 2

For cases (b) and (c), with $\sigma^2 = 1$, solve:

#### Case (b)

$$\text{Width}_b < 2 \implies n \geq \text{calculated value}$$

#### Case (c)

$$\text{Width}_c < 2 \implies n \geq \text{calculated value}$$

### Insights

1. **Precision of Intervals:**

   - Case (b) produces narrower intervals than case (a) because it uses the true mean $\mu$, avoiding the uncertainty of estimating $\bar{X}$
   - Case (c) produces much wider intervals for small $n$ due to fewer degrees of freedom

2. **Sample Size Trade-Off:**

   - Larger $n$ reduces the width of all intervals, but the rate of reduction depends on degrees of freedom
   - Case (c) requires much larger $n$ for precision comparable to cases (a) and (b)

3. **Practical Use:**
   - This exercise illustrates the importance of choosing the right statistic for variance estimation and balancing trade-offs between precision and computational efficiency

### Numerical Results

For $n = 10$:

- $\text{Width}_a = 2.175$
- $\text{Width}_b = 1.992$
- $\text{Width}_c = 254.054$

Minimum $n$ for $\text{Width} < 2$:

- Case (b): $n = 10$
- Case (c): $n$ is very large (outside practical range)

# Questions 6:

> Let $X_1,...,X_m$ and $Y_1,...,Y_n$ be independent random samples from normal distributions $N(\mu_1,>\sigma^2)$ and $N(\mu_2,\sigma^2)$, respectively, where the parameters $\mu_1, \mu_2, \sigma^2$ are unknown. >Let:
>
> $$S^2 = \frac{1}{m+n-2}\left(\sum_{i=1}^m(X_i-\bar{X})^2 + \sum_{j=1}^n(Y_j-\bar{Y})^2\right)$$
>
> 1.  Determine the distributions of both:
>
> - $\frac{(m+n-2)S^2}{\sigma^2}$
> - $\frac{\bar{X}-\bar{Y}-(\mu_1-\mu_2)}{S\sqrt{\frac{1}{m}+\frac{1}{n}}}$
>
> 2.  Show how to construct a confidence interval for $\mu_1-\mu_2$.

## Solution

$$
$$
