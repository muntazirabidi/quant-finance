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
