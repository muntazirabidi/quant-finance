# 1.4 Q-Q Plots

## Introduction

Q-Q plots (Quantile-Quantile plots) serve as powerful graphical tools in statistical analysis to assess whether data follows a specific probability distribution. The fundamental idea is to compare the quantiles of our data with the theoretical quantiles of a reference distribution. This comparison provides visual insights that numerical tests might miss.

## Theoretical Foundation

### Understanding Quantiles

A quantile represents a point in a distribution that divides the data into proportions. For a distribution with cumulative distribution function (CDF) $F$ and probability density function (PDF) $f$, the $p$-th quantile (where $0 \leq p \leq 1$) is defined as the value $x_p$ that satisfies:

$$
\int_{-\infty}^{x_p} f(u) \, du = p
$$

More concisely:

$$
x_p = F^{-1}(p)
$$

**Intuitive Understanding**: Think of quantiles as dividing points in your data. For example, the median (0.5 quantile) divides the data into two equal parts. The 0.25 quantile (first quartile) divides the lower half into two equal parts, and so on.

### The Probability Integral Transform

A cornerstone of Q-Q plot theory is the probability integral transform, formalized in the following Lemma:

**Lemma:** For a continuous random variable $X$ taking values in $(a,b)$ with strictly increasing CDF $F(x)$ for $x \in (a,b)$:

- If we define $Y = F(X)$
- Then $Y \sim U(0,1)$ (follows a uniform distribution on $[0,1]$)

This can be written symbolically as:

$$
F(X) \sim U(0,1)
$$

And consequently:

$$
X \sim F^{-1}(U)
$$

**Intuitive Understanding**: The probability integral transform tells us that applying the CDF to a random variable always gives us a uniform distribution on $[0,1]$, regardless of the original distribution. This is because the CDF "stretches" or "compresses" the probability density to make it uniform.

### Properties of Uniform Order Statistics

When we order a sample from a uniform distribution, the ordered values (order statistics) have specific properties described in below:

**Lemma:** For order statistics $U_{(1)}, ..., U_{(n)}$ from a $U(0,1)$ sample of size $n$:

1. Expected Value:

   $$
   E(U_{(r)}) = \frac{r}{n+1}
   $$

2. Variance:
   $$
   \text{var}(U_{(r)}) = \frac{r}{(n+1)(n+2)}\left(1 - \frac{r}{n+1}\right)
   $$

**Why This Matters**: These properties tell us where we expect the ordered uniform values to fall. The variance decreases with sample size, meaning larger samples give more reliable plots.

## The Delta Method and Its Role

When we say:

$$
E(X_{(k)}) \approx F^{-1}(E[U_{(k)}])
$$

We're using the delta method, which states that for a smooth function $g$ and a random variable $Y$:

$$
E[g(Y)] \approx g(E[Y])
$$

when the variance of $Y$ is small. In our case:

- $g = F^{-1}$
- $Y = U_{(k)}$

The approximation works well because:

$$
\text{var}(U_{(r)}) \leq \frac{1}{4(n+2)}
$$

This variance bound explains why Q-Q plots become more reliable with larger sample sizes.

## Construction and Interpretation

### The Construction Process

1. Order your data: $x_{(1)}, ..., x_{(n)}$
2. Calculate theoretical quantiles: $F^{-1}(\frac{k}{n+1})$ for $k = 1,...,n$
3. Plot points:
   $$
   (F^{-1}(\frac{k}{n+1}), x_{(k)})
   $$

### Reading Deviations

Different patterns in Q-Q plots indicate different types of departures from the theoretical distribution:

1. **S-shaped curve**: Indicates different skewness

   $$
   \text{Skewness} = E\left[\left(\frac{X-\mu}{\sigma}\right)^3\right]
   $$

2. **Concave/convex pattern**: Suggests different kurtosis
   $$
   \text{Kurtosis} = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right]
   $$

## Handling Unknown Parameters

When $F$ depends on unknown parameters $\theta$, we typically:

1. Estimate parameters:

   $$
   \hat{\theta} = \arg\max_{\theta} L(\theta; x_1,...,x_n)
   $$

   where $L$ is the likelihood function.

2. Use standardized residuals:
   $$
   z_i = \frac{x_i - \hat{\mu}}{\hat{\sigma}}
   $$

This transforms our problem to comparing with a standard form of the distribution.

## Statistical Distance and Q-Q Plots

The vertical distances in a Q-Q plot relate to the Kolmogorov-Smirnov statistic:

$$
D_n = \sup_x |F_n(x) - F(x)|
$$

where $F_n$ is the empirical CDF.

## Confidence Bands

We can construct confidence bands using:

$$
\pm c_{\alpha}\sqrt{\frac{p(1-p)}{n}}
$$

where $c_{\alpha}$ is based on the desired confidence level and $p$ is the theoretical quantile probability.

## Multivariate Extension

For multivariate data, we can use chi-square Q-Q plots based on:

$$
d_i^2 = (x_i - \mu)^T\Sigma^{-1}(x_i - \mu)
$$

These distances should follow a $\chi^2$ distribution with degrees of freedom equal to the dimension of the data.

## Practical Considerations

The effectiveness of Q-Q plots depends on:

1. Sample size ($n$): Larger samples provide more reliable plots as:

   $$
   \lim_{n \to \infty} \text{var}(U_{(r)}) = 0
   $$

2. Edge effects: The tails of the distribution have higher variance:

   $$
   \text{var}(U_{(1)}) = \text{var}(U_{(n)}) = \frac{n}{(n+1)^2(n+2)}
   $$

3. Robustness: The impact of outliers on the plot can be quantified through influence functions:
   $$
   IF(x; T, F) = \lim_{\epsilon \to 0} \frac{T((1-\epsilon)F + \epsilon\delta_x) - T(F)}{\epsilon}
   $$
   where $\delta_x$ is the point mass at $x$.

# Q-Q Plots with Unknown Parameters

## The Challenge of Unknown Parameters

In real-world applications, we rarely know the exact parameters of our theoretical distribution. This presents an interesting challenge: how can we create Q-Q plots when the very distribution we're comparing against has unknown parameters? Let's explore this question systematically.

### The Fundamental Approximation

We begin with our fundamental Q-Q plot relationship. For a sample $X_1, ..., X_n$ that we believe comes from a distribution with CDF $F$, we have:

$$
F(x_{(k)}) \approx \frac{k}{n+1}
$$

This relationship holds regardless of whether we know the parameters of $F$ or not. The challenge lies in how we use this relationship when $F$ depends on unknown parameters.

### The Normal Distribution Case: A Beautiful Solution

The normal distribution provides an elegant example of how we can handle unknown parameters. Let's work through this step by step.

#### Step 1: Setting Up the Problem

Suppose we have data $x_1, ..., x_n$ that we believe comes from a normal distribution $N(\mu, \sigma^2)$, but we don't know $\mu$ or $\sigma^2$. Our Q-Q plot approximation states:

$$
F(x_{(k)}) \approx \frac{k}{n+1}
$$

where $F$ is the CDF of $N(\mu, \sigma^2)$.

#### Step 2: The Key Transformation

Here's where the magic happens. For any normal random variable $Y \sim N(\mu, \sigma^2)$, we can express its CDF $F$ in terms of the standard normal CDF $\Phi$:

$$
F(y) = P(Y \leq y) = P\left(\frac{Y-\mu}{\sigma} \leq \frac{y-\mu}{\sigma}\right) = \Phi\left(\frac{y-\mu}{\sigma}\right)
$$

This transformation is crucial because it connects our unknown normal distribution to the standard normal distribution, whose CDF $\Phi$ we know and can compute.

#### Step 3: Applying the Transformation

Substituting this into our Q-Q plot approximation:

$$
\Phi\left(\frac{x_{(k)}-\mu}{\sigma}\right) \approx \frac{k}{n+1}
$$

#### Step 4: Solving for the Order Statistics

Now we can apply $\Phi^{-1}$ to both sides:

$$
\frac{x_{(k)}-\mu}{\sigma} \approx \Phi^{-1}\left(\frac{k}{n+1}\right)
$$

Therefore:

$$
x_{(k)} \approx \sigma\Phi^{-1}\left(\frac{k}{n+1}\right) + \mu
$$

### The Remarkable Result

This final equation reveals something beautiful: if we plot our ordered data $x_{(k)}$ against the theoretical quantiles $\Phi^{-1}(\frac{k}{n+1})$, we should see a straight line if our data is indeed normally distributed. Moreover:

- The slope of this line will be $\sigma$
- The intercept will be $\mu$

This means we can:

1. Create the Q-Q plot without knowing $\mu$ and $\sigma^2$
2. Actually estimate these parameters from the plot itself!

### Why This Works: The Deeper Understanding

The reason this approach works is that the normal distribution has a special property: any linear transformation of a standard normal random variable is still normal. When we standardize our data by subtracting $\mu$ and dividing by $\sigma$, we're essentially transforming it to match the standard normal distribution.

The unknown parameters $\mu$ and $\sigma$ simply determine how this transformation scales and shifts the data, which appears as the slope and intercept of our Q-Q plot line. This is why we can detect normality (by checking for linearity) without needing to know the specific parameters.

### Practical Implementation

To create a normal Q-Q plot in practice:

1. Order your data: $x_{(1)}, ..., x_{(n)}$
2. Calculate theoretical quantiles: $q_k = \Phi^{-1}(\frac{k}{n+1})$ for $k = 1,...,n$
3. Plot points: $(q_k, x_{(k)})$
4. Look for a straight line pattern

The beauty of this approach is that it separates the question "Is the data normally distributed?" from "What are the specific parameters of that normal distribution?" We can answer the first question just by checking for linearity, regardless of the actual parameter values.
