# The Delta Method

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Core Concept](#core-concept)
4. [Mathematical Foundation](#mathematical-foundation)
5. [Examples](#examples)
6. [Applications](#applications)

## Introduction

The Delta method is a powerful statistical technique used to approximate the distribution of a function of an estimator, particularly useful in large sample scenarios.

## Prerequisites

### Central Limit Theorem (CLT)

- For iid random variables $X_1,...,X_n$ with:
  - $E(X_i) = \mu$
  - $var(X_i) = \sigma^2$
- The standardized sample mean follows:
  - $\frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \stackrel{D}{\approx} N(0,1)$
  - This approximation becomes exact as $n \to \infty$

### Laws of Large Numbers

- Weak/Strong law: $\bar{X}$ approaches $\mu$ as $n \to \infty$

## Core Concept

The Delta method helps find the asymptotic distribution of $g(\bar{X})$ for a function $g$.

### Key Steps:

1. Start with Taylor expansion of $g(\bar{X})$ around $g(\mu)$:

   - $g(\bar{X}) \approx g(\mu) + (\bar{X}-\mu)g'(\mu)$

2. Analysis of Terms:
   - $g(\mu)$: Constant term (order 1)
   - $(\bar{X}-\mu)g'(\mu)$: Order $n^{-1/2}$ term
   - Higher order terms are omitted as they become negligible

### Asymptotic Properties

1. **Expectation**:

   - $E[g(\bar{X})] \approx g(\mu) + g'(\mu)E[(\bar{X}-\mu)] = g(\mu)$

2. **Variance**:

   - $var[g(\bar{X})] \approx var[g'(\mu)(\bar{X}-\mu)] = g'(\mu)^2 \frac{\sigma^2}{n}$

3. **Distribution**:
   - $g(\bar{X}) \stackrel{D}{\approx} N(g(\mu), \frac{g'(\mu)^2\sigma^2}{n})$

## Examples

### Example 1: Ratio Estimation

Suppose we want to estimate the ratio $\theta = \mu_1/\mu_2$ from two samples.

**Setup:**

- Independent samples $X_1,...,X_n$ and $Y_1,...,Y_n$
- $\bar{X} \sim N(\mu_1, \sigma_1^2/n)$ and $\bar{Y} \sim N(\mu_2, \sigma_2^2/n)$ approximately
- $g(x,y) = x/y$

**Application of Delta Method:**

1. First derivatives:
   - $\frac{\partial g}{\partial x} = \frac{1}{y}$, $\frac{\partial g}{\partial y} = -\frac{x}{y^2}$
2. Asymptotic variance:
   - $Var(\hat{\theta}) \approx \frac{1}{\mu_2^2}\frac{\sigma_1^2}{n} + \frac{\mu_1^2}{\mu_2^4}\frac{\sigma_2^2}{n}$
3. Approximate distribution:
   - $\hat{\theta} \stackrel{D}{\approx} N(\frac{\mu_1}{\mu_2}, \frac{1}{\mu_2^2}\frac{\sigma_1^2}{n} + \frac{\mu_1^2}{\mu_2^4}\frac{\sigma_2^2}{n})$

### Example 2: Log Transformation

Consider estimating $\log(\mu)$ from a sample mean.

**Setup:**

- Sample mean $\bar{X} \sim N(\mu, \sigma^2/n)$ approximately
- $g(x) = \log(x)$

**Application:**

1. Derivative: $g'(x) = 1/x$
2. Asymptotic variance:
   - $Var(\log(\bar{X})) \approx \frac{1}{\mu^2}\frac{\sigma^2}{n}$
3. Distribution:
   - $\log(\bar{X}) \stackrel{D}{\approx} N(\log(\mu), \frac{\sigma^2}{n\mu^2})$

### Example 3: Variance Function

Estimating $\theta = \mu^2$ from a sample mean.

**Setup:**

- $\bar{X} \sim N(\mu, \sigma^2/n)$ approximately
- $g(x) = x^2$

**Application:**

1. Derivative: $g'(x) = 2x$
2. Asymptotic variance:
   - $Var(\bar{X}^2) \approx 4\mu^2\frac{\sigma^2}{n}$
3. Distribution:
   - $\bar{X}^2 \stackrel{D}{\approx} N(\mu^2, 4\mu^2\frac{\sigma^2}{n})$

## Applications

### 1. Financial Risk Analysis

#### Value at Risk (VaR) Estimation

- **Problem**: Estimate VaR from sample returns
- **Application**:
  - $g(x)$ transforms mean return to quantile
  - Delta method provides confidence intervals for VaR estimates

#### Portfolio Optimization

- **Problem**: Estimate optimal weights
- **Application**:
  - Transform covariance matrix estimates
  - Assess uncertainty in portfolio allocations

### 2. Medical Research

#### Odds Ratio Analysis

- **Problem**: Estimate odds ratios from proportions
- **Application**:
  - Transform proportion estimates to odds scale
  - Construct confidence intervals for odds ratios

#### Survival Analysis

- **Problem**: Estimate hazard ratios
- **Application**:
  - Transform survival time estimates
  - Assess uncertainty in hazard ratio estimates

### 3. Quality Control

#### Process Capability Indices

- **Problem**: Estimate $C_p$ and $C_{pk}$
- **Application**:
  - Transform mean and variance estimates
  - Provide confidence intervals for capability indices

#### Reliability Analysis

- **Problem**: Estimate mean time to failure
- **Application**:
  - Transform failure rate estimates
  - Assess uncertainty in reliability predictions

### 4. Environmental Science

#### Concentration Ratios

- **Problem**: Estimate pollutant concentration ratios
- **Application**:
  - Transform individual concentration measurements
  - Provide uncertainty estimates for ratio estimates

#### Exposure Assessment

- **Problem**: Estimate exposure levels
- **Application**:
  - Transform environmental measurements to exposure metrics
  - Assess uncertainty in exposure estimates

### 5. Practical Implementations

#### Confidence Interval Construction

```python
# Python implementation example
import numpy as np

def delta_ci(mean, var, g, g_prime, alpha=0.05):
    """
    Construct confidence interval using delta method
    """
    z = stats.norm.ppf(1 - alpha/2)
    g_mean = g(mean)
    g_var = (g_prime(mean))**2 * var
    margin = z * np.sqrt(g_var)
    return (g_mean - margin, g_mean + margin)
```

### Key Considerations in Applications

1. **Sample Size Requirements**

   - Rule of thumb: n > 30 for reliable approximations
   - Larger n needed for more complex transformations

2. **Function Smoothness**

   - First derivative should exist and be continuous
   - Function should be well-behaved near estimate

3. **Practical Limitations**
   - May not work well for highly nonlinear transformations
   - Care needed near boundaries or constraints

---

## Notes on Notation

- $\stackrel{D}{\approx}$ means "has approximately the same distribution as"
- Asymptotic refers to behavior as $n \to \infty$
- $g'(\mu)$ represents the derivative of function $g$ evaluated at $\mu$

---

## Key Takeaways

1. The Delta method uses Taylor expansion to approximate distributions
2. It's particularly useful for large sample scenarios
3. Relies on CLT and properties of normal distribution
4. Gives both mean and variance of the asymptotic distribution
