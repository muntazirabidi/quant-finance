# Linear Models Summary

## Key Concepts

### Basic Linear Model

- Models relationship between a response variable (Y) and explanatory variables (X)
- Assumes linear relationship in parameters
- Does not require normality assumption initially

Basic form for n observations and p covariates:

$$
Y_i = β_1x_{i1} + β_2x_{i2} + ... + β_px_{ip} + ε_i
$$

where:

- $β_1,...,β_p$ are unknown parameters
- $x_{i1},...,x_{ip}$ are known covariate values
- $ε_i$ are independent errors with mean 0 and variance $σ^2$

### Matrix Form

$$
Y = Xβ + ε
$$

where:

- $Y$ is $n×1$ response vector
- $X$ is $n×p$ design matrix
- $β$ is $p×1$ parameter vector
- $ε$ is $n×1$ error vector

Properties:

- $E(ε) = 0$
- $cov(Y) = σ²I$
- $X$ has full rank $p$
- Homoscedastic case: equal error variance

## Important Results

### Least Squares Estimator

The least squares estimator $\hat{β}$ minimizes:

$$
S(β) = ||Y - Xβ||² = (Y - Xβ)ᵀ(Y - Xβ)
$$

Solution:

$$
\hat{β} = (X^TX)^{-1}X^TY
$$

Properties:

- Unbiased: $E($\hat{β}$) = β$
- Covariance: $cov($\hat{β}$) = σ²(XᵀX)⁻¹$

### Simple Linear Regression

For model $Y_i = a + bx_i + ε_i:$

- Estimated slope: $\hat{b} = \frac{S_{xy}}{S_{xx}}$ where $S_{xy} = \sum(x_i - \bar{x})(y_i - \bar{y})$
- Estimated intercept: $\hat{a} = \bar{y} - \hat{b}\bar{x}$
- $\hat{b}$ = r × $\sqrt{\frac{S_{yy}}{S_{xx}}}$ where r is correlation coefficient

### Gauss-Markov Theorem

$\hat{β}$ is the Best Linear Unbiased Estimator (BLUE) - has minimum variance among all linear unbiased estimators.

### Under Normality Assumption

When $ε ~ N(0, σ²I)$:

1. $\hat{β} \sim N(β, σ²(XᵀX)⁻¹)$
2. $RSS \sim σ²χ²(n-p)$
3. $\hat{β}$ and $\hat{σ}²$ are independent

## Key Terms

- **Fitted Values**: $\hat{Y} = X\hat{β}$
- **Residuals**: $R = Y - \hat{Y}$
- **Residual Sum of Squares**: $RSS = ||R||² = RᵀR$

## Example: Simple Linear Regression

Oxygen uptake vs running time:

- Response ($Y$): Time to run 2 miles
- Predictor ($X$): Maximum oxygen uptake
- Results:
  - $\bar{y} = 826.5$
  - $S_{xx} = 783.5$
  - $S_{xy} = -10077$
  - Correlation r = -0.81
  - Estimated slope $\hat{b} = -12.9$

This shows strong negative correlation between oxygen uptake and running time, which makes intuitive sense - higher oxygen uptake capacity corresponds to faster running times.

### Projection Matrix Properties

- Projection matrix: $P = X(X^TX)^{-1}X^T$
- Properties:
  - Symmetric: $P^T = P$
  - Idempotent: $P^2 = P$
  - rank($P$) = tr($P$) = $p$
  - $I_n - P$ is also symmetric and idempotent
  - rank($I_n - P$) = $n - p$

## Hypothesis Testing

### General Framework

Tests about model parameters can be formulated as:

- $H_0: Cβ = d$ vs $H_1: Cβ \neq d$
  where $C$ is a $q × p$ matrix of rank $q$

### Test Statistics

Under normality, key test statistics:

1. **t-statistic** (for single parameter):
   $$t = \frac{\hat{β}_j - β_{j0}}{SE(\hat{β}_j)} \sim t_{n-p}$$
   where $SE(\hat{β}_j) = \sqrt{\hat{\sigma}^2(X^TX)^{-1}_{jj}}$

2. **F-statistic** (for multiple parameters):
   $$F = \frac{(Cβ - d)^T[C(X^TX)^{-1}C^T]^{-1}(Cβ - d)}{q\hat{\sigma}^2} \sim F_{q,n-p}$$

### Analysis of Variance (ANOVA)

- Total Sum of Squares: $TSS = \sum(y_i - \bar{y})^2$
- Regression Sum of Squares: $RSS_{reg} = \sum(\hat{y}_i - \bar{y})^2$
- Error Sum of Squares: $RSS = \sum(y_i - \hat{y}_i)^2$
- Decomposition: $TSS = RSS_{reg} + RSS$

### F-test for Overall Regression

- Tests if any predictors are significant
- $H_0: β_1 = β_2 = ... = β_{p-1} = 0$
- Test statistic:
  $$F = \frac{RSS_{reg}/(p-1)}{RSS/(n-p)} \sim F_{p-1,n-p}$$

### Model Comparison

For nested models $M_1 \subset M_2$:
$$F = \frac{(RSS_1 - RSS_2)/(p_2 - p_1)}{RSS_2/(n-p_2)} \sim F_{p_2-p_1,n-p_2}$$

### Key Results

- Under $H_0$, test statistics follow their stated distributions
- Confidence regions can be constructed using F-distribution
- Tests and confidence intervals are equivalent for single parameters
- Multiple testing requires adjustment of significance levels
