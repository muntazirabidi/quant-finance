# Statistical Concepts for Quant Finance Interviews

## 1. Maximum Likelihood Estimation (MLE)

### Key Concepts

The MLE is a fundamental method in statistics for parameter estimation. In finance, it's crucial for:

- Estimating parameters of return distributions
- Calibrating financial models
- Risk parameter estimation

### Important Properties

- MLE is asymptotically unbiased: $\lim_{n \to \infty} E[\hat{\theta}] = \theta$
- MLE achieves the Cramér-Rao lower bound asymptotically
- MLE is asymptotically normal: $\sqrt{n}(\hat{\theta} - \theta) \stackrel{d}{\to} N(0, I(\theta)^{-1})$

### Common MLEs in Finance

1. **Normal Distribution**:

   - Mean: $\hat{\mu} = \bar{x}$
   - Variance: $\hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2$

2. **Exponential Distribution**:
   - Rate parameter: $\hat{\lambda} = \frac{1}{\bar{x}}$

## 2. Fisher Information

### Definition

Fisher Information quantifies the amount of information about an unknown parameter:
$I(\theta) = E\left[\left(\frac{\partial}{\partial \theta} \log L(\theta;X)\right)^2\right]$

### Key Applications

- Determining estimation precision
- Constructing confidence intervals
- Optimal sample size determination

### Important Properties

For exponential distribution:
$I(\lambda) = \frac{n}{\lambda^2}$

For normal distribution:
$I(\sigma^2) = \frac{n}{2(\sigma^2)^2}$

## 3. Confidence Intervals

### Methods of Construction

1. **Exact Method**:
   Using pivotal quantities
   $P(a \leq T(X,\theta) \leq b) = 1-\alpha$

2. **Asymptotic Method**:
   Using Fisher Information
   $\hat{\theta} \pm z_{\alpha/2}\sqrt{\frac{1}{nI(\hat{\theta})}}$

3. **Delta Method**:
   For transformed parameters
   $g(\hat{\theta}) \approx N(g(\theta), [g'(\theta)]^2\text{Var}(\hat{\theta}))$

### Financial Applications

- VaR estimation intervals
- Option pricing model parameter confidence bounds
- Risk metric uncertainty quantification

## 4. Hypothesis Testing

### Two-Sample Tests

For comparing two populations (e.g., strategies, portfolios):

$t = \frac{\bar{X} - \bar{Y}}{S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}$

where $S_p^2$ is the pooled variance:
$S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$

### Power Analysis

Power = $P(\text{reject }H_0|H_1\text{ true})$

- Critical for determining sample sizes in backtesting
- Important for strategy validation

## 5. Distribution Theory

### Important Relationships

1. **Chi-square and Normal**:
   If $Z_i \sim N(0,1)$, then $\sum_{i=1}^n Z_i^2 \sim \chi^2_n$

2. **Exponential and Gamma**:
   Sum of exponentials follows gamma distribution:
   $\sum_{i=1}^n \text{Exp}(\lambda) \sim \text{Gamma}(n,\lambda)$

### Applications in Finance

- Return distribution modeling
- Risk decomposition
- Extreme value analysis

## 6. Time Series Concepts

### Key Properties

- Stationarity
- Autocorrelation
- Mean reversion

### Testing Methods

1. **Stationarity**:

   - Augmented Dickey-Fuller test
   - KPSS test

2. **Serial Correlation**:
   - Ljung-Box test
   - Durbin-Watson test

## 7. Practical Tips for Interviews

### When Asked About Distributions

1. Start with assumptions:

   - Independence
   - Stationarity
   - Normality (if applicable)

2. Discuss limitations:
   - Fat tails in financial returns
   - Time-varying volatility
   - Regime changes

### Model Validation

1. **Visual Methods**:

   - Q-Q plots
   - Residual analysis
   - ACF/PACF plots

2. **Statistical Tests**:
   - Goodness of fit tests
   - Likelihood ratio tests
   - Information criteria (AIC, BIC)

### Sample Size Considerations

1. For confidence intervals:
   Width $\propto \frac{1}{\sqrt{n}}$

2. For hypothesis tests:
   Power increases with $\sqrt{n}$

## 8. Common Interview Questions

1. **MLE Properties**:
   "Why is MLE asymptotically efficient?"
   Answer: It achieves the Cramér-Rao lower bound asymptotically.

2. **Confidence Intervals**:
   "What happens to CI width as n increases?"
   Answer: Decreases proportionally to $\frac{1}{\sqrt{n}}$

3. **Distribution Selection**:
   "Why use t-distribution instead of normal?"
   Answer: Better for small samples and handles uncertainty in variance estimation.

## 9. Mathematical Tools to Remember

### Key Inequalities

1. Chebyshev's Inequality:
   $P(|X-\mu| \geq k\sigma) \leq \frac{1}{k^2}$

2. Jensen's Inequality:
   For convex $f$: $E[f(X)] \geq f(E[X])$

### Useful Limits

1. Law of Large Numbers:
   $\bar{X}_n \xrightarrow{p} \mu$

2. Central Limit Theorem:
   $\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0,\sigma^2)$

## 10. Risk and Portfolio Theory

### Key Metrics

1. Sharpe Ratio:
   $SR = \frac{R_p - R_f}{\sigma_p}$

2. Information Ratio:
   $IR = \frac{\alpha}{\omega}$

### Statistical Properties

- Estimation error in covariance matrices
- Impact of sample size on portfolio optimization
- Shrinkage estimators and regularization

Remember: In quant interviews, they're often more interested in your reasoning process than the final answer. Be prepared to:

- State and justify assumptions
- Discuss limitations of methods
- Suggest alternative approaches
- Connect statistical theory to practical applications
