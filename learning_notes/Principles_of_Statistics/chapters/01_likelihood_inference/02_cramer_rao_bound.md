# The Cramér–Rao Lower Bound (CRLB)

The Cramér–Rao lower bound (CRLB) is a fundamental result in statistics that provides a theoretical lower limit on the variance of an unbiased estimator. It tells us how "good" an estimator can potentially be in terms of its variance, given a specific statistical model.

## Key Notations and Concepts

Let's understand the essential components that make up this theorem:

### Model $P_\theta$

This represents a family of probability distributions indexed by the parameter $\theta$, where $\theta$ is a vector in $\mathbb{R}^p$.

### Estimator $\hat{\phi}$

An estimator is a rule or function used to estimate a parameter (or a function of it). Here, $\hat{\phi}$ estimates a function of the parameter, $\phi(\theta)$.

### Variance of an Estimator $\text{Var}_\theta(\hat{\phi})$

This measures how much the estimates $\hat{\phi}$ vary around their expected value.

### Score Function $S(\theta)$

This is the gradient (vector of partial derivatives) of the log-likelihood function with respect to $\theta$. Mathematically:

$S(\theta) = \nabla_\theta \log L(\theta)$

where $L(\theta)$ is the likelihood.

### Fisher Information Matrix $I(\theta)$

This is a measure of how much information the data provides about the parameter $\theta$. It's defined as:

$I(\theta) = \mathbb{E}_\theta[S(\theta)S(\theta)^\top]$

## The Cramér–Rao Lower Bound (CRLB)

For an unbiased estimator $\hat{\phi}$ of $\phi(\theta)$, the variance is bounded as:

$\text{Var}_\theta(\hat{\phi}) \geq \nabla_\theta\phi(\theta)^\top I(\theta)^{-1}\nabla_\theta\phi(\theta)$

where:

- $\nabla_\theta\phi(\theta)$ is the gradient of $\phi(\theta)$ with respect to $\theta$
- $I(\theta)^{-1}$ is the inverse Fisher information matrix

## Remarks

### Univariate Case ($p=1$)

If $\phi(\theta)=\theta$ (identity function) and $\hat{\phi}=\hat{\theta}$ is an estimator of $\theta$, the bound simplifies to:

$\text{Var}_\theta(\hat{\theta}) \geq \frac{1}{I(\theta)}$

This indicates that the variance of any unbiased estimator of $\theta$ cannot be smaller than the reciprocal of the Fisher information.

### Linear Function of $\theta$

If $\phi(\theta)=v^\top\theta$ for a vector $v$, and $\hat{\phi}=v^\top\hat{\theta}$, then:

$\text{Var}_\theta(\hat{\phi}) \geq v^\top I(\theta)^{-1}v$

This applies to any linear combination of the components of $\theta$.

### Covariance Matrix Implications

The CRLB implies that the covariance matrix of an unbiased estimator, $\text{Cov}_\theta(\hat{\theta})$, satisfies:

$\text{Cov}_\theta(\hat{\theta})-I(\theta)^{-1}$ is positive semi-definite.

This means the diagonal elements (variances) of $\text{Cov}_\theta(\hat{\theta})$ are at least as large as the corresponding elements of $I(\theta)^{-1}$.

## Example: Poisson Distribution

Consider the following scenario:

- Let $X_1,\ldots,X_n$ be i.i.d. $\text{Poisson}(\theta)$
- The maximum likelihood estimator (MLE) is $\hat{\theta}=\bar{X}$ (the sample mean)
- The variance of MLE: $\text{Var}(\hat{\theta})=\theta/n$
- Fisher Information for a single observation: $I_1(\theta)=1/\theta$
- For $n$ observations: $I(\theta)=n/\theta$
- CRLB: $\text{Var}(\hat{\theta}) \geq 1/I(\theta)=\theta/n$

In this case, the variance of the MLE equals the CRLB, demonstrating that the MLE is the most efficient unbiased estimator of $\theta$.
