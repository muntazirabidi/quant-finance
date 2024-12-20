# Multivariate Normal Distribution in Quantitative Finance

## Overview

The multivariate normal distribution extends the familiar univariate normal distribution to handle multiple correlated random variables. This extension is crucial in quantitative finance for modeling portfolio returns, risk factors, and multi-asset derivatives.

## Mathematical Foundation

### From Univariate to Multivariate

In the univariate case, we work with two parameters:

- $\mu$ (mean)
- $\sigma^2$ (variance)

The multivariate case generalizes these to:

- $\boldsymbol{\mu}$ (mean vector)
- $\boldsymbol{\Sigma}$ (covariance matrix)

### Standard Multivariate Normal Distribution

Let $\mathbf{Z} = (Z_1, \ldots, Z_p)$ where $Z_1, \ldots, Z_p \stackrel{iid}{\sim} N(0,1)$. The probability density function (PDF) is:

$$f(\mathbf{z}) = \frac{1}{(2\pi)^{p/2}} \exp\left(-\frac{1}{2}\mathbf{z}^T\mathbf{z}\right)$$

We denote this as $\mathbf{Z} \sim N(\mathbf{0}, \mathbf{I})$, where:

- $\mathbf{0}$ is a $p$-dimensional zero vector
- $\mathbf{I}$ is the $p \times p$ identity matrix

### General Multivariate Normal Distribution

For $\mathbf{X} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where $\boldsymbol{\Sigma}$ is positive definite, the PDF is:

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{p/2}|\boldsymbol{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$$

where $|\boldsymbol{\Sigma}|$ denotes the determinant of $\boldsymbol{\Sigma}$.

## Key Properties

### 1. Marginal Distributions

For $\mathbf{X} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$:

- Each component follows: $X_j \sim N(\mu_j, \Sigma_{jj})$

### 2. Linear Combinations

For any constant vector $\mathbf{a}$:

- $\mathbf{a}^T\mathbf{X} \sim N(\mathbf{a}^T\boldsymbol{\mu}, \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a})$

### 3. Moments

For components $j$ and $k$:

- $E(X_j) = \mu_j$
- $\text{var}(X_j) = \Sigma_{jj}$
- $\text{cov}(X_j,X_k) = \Sigma_{jk}$

## Practical Example: Bivariate Normal Distribution

Consider a two-dimensional case $(p=2)$ with parameters:

$$
\boldsymbol{\mu} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \quad
\boldsymbol{\Sigma} = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
$$

where $\rho$ is the correlation coefficient $(-1 < \rho < 1)$.

The PDF becomes:

$$f(x_1,x_2) = \frac{1}{2\pi\sqrt{1-\rho^2}} \exp\left(-\frac{1}{2(1-\rho^2)}(x_1^2 - 2\rho x_1x_2 + x_2^2)\right)$$

### Financial Interpretation

This setup could represent two financial assets where:

- Expected returns are zero ($\mu_1 = \mu_2 = 0$)
- Both assets have unit variance ($\Sigma_{11} = \Sigma_{22} = 1$)
- $\rho$ captures their correlation:
  - $\rho = 0$: Independent assets
  - $\rho \to 1$: Perfect positive correlation
  - $\rho \to -1$: Perfect negative correlation

## Applications in Quantitative Finance

### 1. Portfolio Theory

The linear combination property directly applies to portfolio returns:

- For portfolio weights $\mathbf{w}$, return $R_p = \mathbf{w}^T\mathbf{R}$ follows:
  $$R_p \sim N(\mathbf{w}^T\boldsymbol{\mu}, \mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w})$$

### 2. Risk Management

Value at Risk (VaR) calculations for normally distributed returns:

- For confidence level $\alpha$:
  $$\text{VaR}_\alpha = -(\boldsymbol{\mu}^T\mathbf{w} + \Phi^{-1}(\alpha)\sqrt{\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}})$$

### 3. Option Pricing

Multi-asset options can be priced using multivariate normal distributions:

- Black-Scholes extensions for basket options
- Correlation options
- Spread options

## Interview Tips

### 1. Core Concepts

Be prepared to explain:

- Why normality is assumed (Central Limit Theorem)
- Limitations of the assumption
- How to test for multivariate normality

### 2. Practical Applications

Know how to:

- Calculate portfolio moments
- Derive efficient frontiers
- Explain correlation effects on diversification

### 3. Extensions

Be familiar with:

- Student's t-distribution (heavier tails)
- Copulas (non-linear dependence)
- Time-varying correlations (GARCH models)

### 4. Common Questions

Practice explaining:

- Why correlations tend to increase in market stress
- How to account for non-normal features
- When normality is a reasonable assumption

This formulation provides a solid foundation for quant finance interviews while maintaining mathematical rigor and practical relevance.
