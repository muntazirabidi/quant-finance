# Statistical Estimation and Bias: A Comprehensive Guide

## 1. Fundamental Principle

> "Bias is a property of the estimator, not the data."

This principle is fundamental to understanding estimation in statistics. The bias, or systematic error, comes from how we construct our estimation method, not from the data we observe.

## 2. Core Statistical Concepts

### 2.1 Types of Estimators

1. **Maximum Likelihood Estimator (MLE)**

   - Maximizes the likelihood function
   - Often biased but asymptotically efficient
   - Bias typically decreases with sample size

2. **Unbiased Estimator**
   - $E(\hat{\theta}) = \theta$
   - May have higher variance
   - Doesn't necessarily maximize likelihood

### 2.2 Definition of Bias

For an estimator $\hat{\theta}$ of parameter $\theta$:

- Bias = $E(\hat{\theta}) - \theta$
- Unbiased: Bias = 0
- Biased: Bias ≠ 0

## 3. Deep Dive: Geometric Distribution

### 3.1 Distribution Properties

- Models number of trials until first success
- Parameter: $p$ (probability of success)
- Alternative parameter: $\theta = \frac{1}{p}$ (expected trials until success)
- Support: $X = 1, 2, 3, ...$
- PMF: $P(X = x) = (1-p)^{x-1}p$ for $x = 1, 2, ...$
- Mean: $E[X] = \frac{1}{p} = \theta$
- Variance: $Var(X) = \frac{1-p}{p^2}$

### 3.2 Maximum Likelihood Estimation

**Step 1: Likelihood Function**

- $L(p; X_1, ..., X_n) = \prod_{i=1}^n (1-p)^{x_i-1}p$

**Step 2: Log-Likelihood**

- $\ell(p) = (\sum_{i=1}^n x_i - n)\log(1-p) + n\log(p)$

**Step 3: MLE Derivation**

1. For $p$:

   - $\frac{d\ell}{dp} = -\frac{\sum_{i=1}^n x_i - n}{1-p} + \frac{n}{p} = 0$
   - Solving yields: $\hat{p} = \frac{n}{\sum_{i=1}^n x_i}$

2. For $\theta$:
   - Using invariance property: $\hat{\theta} = \frac{1}{\hat{p}} = \frac{\sum_{i=1}^n x_i}{n} = \bar{X}$

### 3.3 Properties of Estimators

**For $\hat{\theta}$ (Sample Mean)**:

1. Unbiased: $E[\hat{\theta}] = \theta$
2. Variance: $Var(\hat{\theta}) = \frac{1}{n} \cdot \frac{1-p}{p^2}$

**For $\hat{p}$ (MLE)**:

1. Biased: $E[\hat{p}] \neq p$
2. Bias = $-\frac{p}{n-1}$ (underestimates $p$)
3. Bias-corrected version: $\hat{p}_{corrected} = \frac{n-1}{\sum_{i=1}^n x_i}$

## 4. Other Common Distributions

### 4.1 Normal Distribution

**Parameters**: $\mu$ (mean), $\sigma^2$ (variance)

**Estimators**:

1. For mean:
   - $\hat{\mu} = \bar{X}$ (unbiased)
2. For variance:
   - MLE: $\hat{\sigma}^2_{MLE} = \frac{\sum(X_i - \bar{X})^2}{n}$ (biased)
   - Unbiased: $s^2 = \frac{\sum(X_i - \bar{X})^2}{n-1}$

### 4.2 Exponential Distribution

**Parameter**: $\lambda$ (rate)

- MLE: $\hat{\lambda} = \frac{n}{\sum X_i}$
- Similar bias pattern to geometric when estimating mean

## 5. Practical Guidelines for Estimator Choice

### 5.1 When to Use MLE

1. **Large Samples (n > 30)**

   - Bias becomes negligible
   - Efficiency is more important
   - Asymptotic properties dominate

2. **Applications**
   - Model building
   - Machine learning
   - Prediction tasks

### 5.2 When to Use Unbiased Estimators

1. **Small Samples (n < 30)**

   - Bias in MLE could be significant
   - Systematic errors more important

2. **Theoretical Work**
   - Mathematical proofs
   - Method comparison
   - Research contexts

## 6. Common Patterns in Bias

### 6.1 Typical Bias Scenarios

1. **Variance Estimation**

   - MLEs often biased
   - Need $n-1$ denominator correction

2. **Reciprocal Parameters**
   - Bias when estimating $\frac{1}{\theta}$
   - Examples: geometric, exponential distributions

### 6.2 Bias Correction Methods

1. **Denominator Adjustment**

   - Change $n$ to $n-1$
   - Common in variance estimation

2. **Multiplicative Correction**
   - Scale by correction factor
   - Example: $\frac{n}{n-1}$

## 7. Numerical Example: Geometric Distribution

Given data: $X = [2, 3, 4, 3, 2]$ (n = 5)

**Calculations**:

1. $\hat{\theta} = \frac{2 + 3 + 4 + 3 + 2}{5} = 2.8$
2. $\hat{p} = \frac{5}{14} \approx 0.357$
3. $\hat{p}_{corrected} = \frac{4}{14} \approx 0.286$

This shows:

- Sample mean estimates expected trials
- MLE of $p$ is larger than corrected version
- Bias correction reduces estimated probability

## 8. Conclusion

Key takeaways:

1. Bias is inherent in estimation method, not data
2. MLE and unbiased estimators serve different purposes
3. Sample size heavily influences estimator choice
4. Common patterns exist across distributions
5. Practical considerations often override theoretical concerns

Remember: The "best" estimator depends on context, sample size, and intended use. Sometimes a biased estimator with lower variance is preferable to an unbiased one with higher variance.
