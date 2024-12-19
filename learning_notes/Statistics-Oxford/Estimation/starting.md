# 1.1 Starting Point: Introduction to Statistical Estimation

## Key Concepts

### Parametric Families

A parametric family is a collection of probability distributions that are characterized by a parameter θ (theta). This parameter can be:

- A scalar (single value)
- A vector (multiple values)
- Confined to a specific parameter space Θ (capital theta)

#### Examples:

1. **Poisson Distribution**

   - Parameter: $\theta = \lambda$
   - Parameter space: $\Theta = (0,\infty)$
   - Notation: $X \sim \text{Poisson}(\lambda)$

2. **Normal Distribution**
   - Parameters: $\theta = (\mu, \sigma^2)$
   - Parameter space: $\Theta = \mathbb{R} \times (0,\infty)$
   - Notation: $X \sim N(\mu, \sigma^2)$

### Random Samples

- Data: $x = (x_1, ..., x_n)$ are observed values
- These come from independent, identically distributed (iid) random variables $X_1, ..., X_n$
- The collection $X = (X_1, ..., X_n)$ is called a random sample

## Statistical Inference Goals

1. **Point Estimation**: Find $t(x)$ to estimate $\theta$
2. **Interval Estimation**: Construct confidence interval $(a(x), b(x))$ for $\theta$
3. **Hypothesis Testing**: Test hypotheses about $\theta$ (e.g., $H: \theta = 0$)

## Probability Functions

### For Discrete Random Variables

- Probability Mass Function (PMF): $f(x; \theta) = P(X = x)$
- Joint PMF for independent observations: $f(x; \theta) = \prod_{i=1}^n f(x_i; \theta)$

### For Continuous Random Variables

- Probability Density Function (PDF): $f(x; \theta)$
- Joint PDF for independent observations: $f(x; \theta) = \prod_{i=1}^n f(x_i; \theta)$

## Important Examples

### Example 1: Poisson Distribution (Discrete)

- PMF: $f(x; \theta) = \frac{e^{-\theta}\theta^x}{x!}$ for $x = 0,1,...$
- Joint PMF: $f(x; \theta) = \frac{e^{-n\theta}\theta^{\sum x_i}}{\prod x_i!}$

### Example 2: Exponential Distribution (Continuous)

- PDF: $f(x; \theta) = \theta e^{-\theta x}$ for $x \geq 0$
- Joint PDF: $f(x; \theta) = \theta^n e^{-\theta \sum x_i}$
- Mean: $E(X_i) = \frac{1}{\theta}$

## Properties of Random Variables

### Key Formulas

1. **Expectation of Sum**:

   - $E(\sum_{i=1}^n a_iX_i) = \sum_{i=1}^n a_iE(X_i)$
   - True whether or not $X_i$ are independent

2. **Variance of Sum (for independent RVs)**:
   - $\text{var}(\sum_{i=1}^n a_iX_i) = \sum_{i=1}^n a_i^2\text{var}(X_i)$

### Sample Mean Properties

For iid random variables with $E(X_i) = \mu$ and $\text{var}(X_i) = \sigma^2$:

- $E(\bar{X}) = \mu$
- $\text{var}(\bar{X}) = \frac{\sigma^2}{n}$

## Estimators

### Definition and Properties

- An estimator $t(X)$ is a function used to estimate $\theta$
- The function must not depend on $\theta$
- The estimate $t(x)$ is the numerical value for specific data
- An estimator $T = t(X)$ is unbiased if $E(T) = \theta$ for all $\theta$

### Examples of Estimators

1. **Sample Mean** ($\bar{X}$):

   - Unbiased estimator of population mean $\mu$
   - $T_1 = \frac{1}{n}\sum_{i=1}^n X_i$

2. **Sample Variance**:
   - Biased: $T_2 = \frac{1}{n}\sum_{i=1}^n(X_i - \bar{X})^2$
   - Unbiased: $S^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i - \bar{X})^2$

## Likelihood

### Definition

- Likelihood function: $L(\theta; x) = f(x; \theta)$
- Log-likelihood: $\ell(\theta) = \log L(\theta)$
- For iid observations: $L(\theta; x) = \prod_{i=1}^n f(x_i; \theta)$

### Maximum Likelihood Estimation (MLE)

- MLE $\hat{\theta}(x)$ maximizes $L(\theta)$ or $\ell(\theta)$
- Found by solving $\frac{\partial \ell}{\partial \theta} = 0$
- Verify it's a maximum using second derivative

### Example: Normal Distribution MLE

For $X_1,...,X_n \stackrel{iid}{\sim} N(\mu,\sigma^2)$:

- Log-likelihood: $\ell(\mu,\sigma^2) = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2$
- MLEs: $\hat{\mu} = \bar{X}$, $\hat{\sigma^2} = \frac{1}{n}\sum_{i=1}^n(X_i-\bar{X})^2$

## Intuition and Key Takeaways

1. Parameters define the shape/behavior of distributions
2. Estimators are rules for guessing parameters from data
3. Unbiased estimators get the right answer "on average"
4. Likelihood measures how well parameters explain data
5. MLE picks the parameter values that make the data most likely
