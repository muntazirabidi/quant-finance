# Information Theory in Statistical Inference

## Introduction to Information in Statistics

The concept of information in statistics quantifies how much we can learn about parameters from data. This is formalized through two key concepts: observed information and Fisher information. These measures help us understand the precision of our parameter estimates and play a crucial role in statistical inference.

## Observed Information

### Definition and Mathematics

The observed information, denoted as $J(\theta)$, measures how quickly the log-likelihood function changes near its maximum. For a scalar parameter $\theta$, it is defined as:

$$J(\theta) = -\frac{d^2\ell}{d\theta^2}$$

where $\ell(\theta)$ is the log-likelihood function.

For a vector parameter $\boldsymbol{\theta} = (\theta_1, ..., \theta_p)$, it becomes a matrix with elements:

$$J(\theta)_{jk} = -\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}$$

### Geometric Interpretation

The observed information represents the curvature of the log-likelihood function at a point. A higher value of $J(\theta)$ indicates:

- Steeper curvature around the maximum likelihood estimate
- More concentrated likelihood function
- Greater precision in our parameter estimation

## Fisher (Expected) Information

### Definition

The Fisher information, denoted as $I(\theta)$, is the expected value of the observed information:

For scalar $\theta$:
$$I(\theta) = E\left[-\frac{d^2\ell}{d\theta^2}\right]$$

For vector $\boldsymbol{\theta}$:
$$I(\theta)_{jk} = E\left[-\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}\right]$$

### Key Properties

1. **Additivity for Independent Observations**: For i.i.d. samples:
   $$I(\theta) = n \times i(\theta)$$
   where $i(\theta)$ is the information from a single observation.

2. **Relationship to Score Function**: The Fisher information can also be expressed as:
   $$i(\theta) = E\left[\left(\frac{d}{d\theta}\log f(X;\theta)\right)^2\right]$$

## Practical Examples

### Example 1: Poisson Distribution

For $X_1, ..., X_n \stackrel{iid}{\sim} \text{Poisson}(\theta)$:

The log-likelihood is:
$$\ell(\theta) = -n\theta + \sum_{i} x_i\log\theta - \sum_{i}\log(x_i!)$$

The observed information is:
$$J(\theta) = \frac{\sum_{i} x_i}{\theta^2}$$

### Example 2: Normal Distribution

For $X_1, ..., X_n \stackrel{iid}{\sim} N(\mu, \sigma^2)$:

The Fisher information matrix is:

$$
I(\theta) = n\begin{pmatrix}
1/\sigma^2 & 0 \\
0 & 1/(2\sigma^4)
\end{pmatrix}
$$

## Applications in Statistical Inference

### 1. Asymptotic Theory

The Fisher information appears in the asymptotic distribution of MLEs:

$$\hat{\theta} \stackrel{D}{\approx} N(\theta, I(\theta)^{-1})$$

This approximation improves with larger sample sizes.

### 2. Confidence Intervals

We can construct approximate confidence intervals using:

$$\hat{\theta} \pm z_{\alpha/2}\sqrt{I(\theta)^{-1}}$$

where $z_{\alpha/2}$ is the appropriate quantile of the standard normal distribution.

### 3. Experimental Design

Fisher information helps in:

- Optimal design of experiments
- Sample size determination
- Comparing different sampling schemes

## Connection to Information Theory

The Fisher information connects to broader concepts in information theory:

- It measures the amount of information data carries about unknown parameters
- Relates to the Cramér-Rao bound for estimator efficiency
- Links to concepts of entropy and Kullback-Leibler divergence

## Information Inequality

The Fisher information sets a lower bound on the variance of any unbiased estimator through the Cramér-Rao inequality:

$$\text{Var}(\hat{\theta}) \geq \frac{1}{I(\theta)}$$

This fundamental result tells us:

- No unbiased estimator can have smaller variance than $1/I(\theta)$
- Maximum likelihood estimators often achieve this bound asymptotically
- The bound helps us evaluate estimator efficiency

## Additive Property

For independent observations, information adds linearly:

$$I_n(\theta) = nI_1(\theta)$$

This explains why:

- Precision improves with sample size
- Standard errors decrease with $\sqrt{n}$
- We can predict how much data we need for desired precision

## Practical Applications and Insights

### Connection to Likelihood Curvature

The observed information $J(\theta)$ provides:

- Local measure of likelihood curve steepness
- Indication of estimation precision
- Basis for numerical optimization methods

Example: In maximum likelihood estimation:
$$\hat{\theta}_{n+1} = \hat{\theta}_n + J(\hat{\theta}_n)^{-1}U(\hat{\theta}_n)$$
where $U(\theta)$ is the score function.

### Role in Hypothesis Testing

Information matrices help construct:

- Wald tests: $W = (\hat{\theta} - \theta_0)^T I(\hat{\theta})(\hat{\theta} - \theta_0)$
- Score tests: $S = U(\theta_0)^T I(\theta_0)^{-1}U(\theta_0)$
- Likelihood ratio tests: $\Lambda = 2[\ell(\hat{\theta}) - \ell(\theta_0)]$

### Model Selection and Design

Information helps in:

- Comparing model efficiency
- Optimal experimental design
- Sample size determination
  = Parameter identifiability assessment

## Advanced Topics Worth Understanding

### Missing Information

When dealing with incomplete data:

- Observed information < Complete information
- EM algorithm uses this concept
- Helps quantify information loss

### Expected vs. Observed Information

Choice between them considers:

- Computational convenience
- Robustness to model misspecification
- Availability of expectations in closed form

### Information in Transformed Parameters

For a transformation $\eta = g(\theta)$:

$$I_{\eta}(\eta) = I_{\theta}(\theta)(\frac{d\eta}{d\theta})^{-2}$$

This helps understand:

- Parameter reparameterization effects
- Variance stabilizing transformations
- Scale-invariant inference

## Interview Tips and Practice Problems

1. **Conceptual Understanding**

   - Explain the difference between observed and expected information
   - Describe why information increases with sample size
   - Discuss the role of information in precision of estimates

2. **Computational Skills**

   - Practice calculating Fisher information for common distributions
   - Understand how to use it in confidence interval construction
   - Be familiar with matrix calculations for multivariate cases

3. **Application Scenarios**
   - Financial modeling: Parameter estimation in asset pricing models
   - Risk management: Precision of risk estimates
   - Portfolio optimization: Efficiency of estimators
