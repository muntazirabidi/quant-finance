# Question 1: Maximum Likelihood Estimation and Delta Method

## Part (a):

> Suppose $X_1, \ldots, X_n$ are independent $\text{Bernoulli}(p)$ random variables. Use the delta method to find the asymptotic distribution of $\hat{p}/(1-\hat{p})$ where $\hat{p}$ is the maximum likelihood estimator of $p$. (The quantity $p/(1-p)$ is the odds of a success.)

## Solution

**MLE for p**

The MLE for p is:

$$\hat{p} = \frac{\sum_{i=1}^n X_i}{n}$$

Since $X_i \sim \text{Bernoulli}(p)$, the sum $\sum_{i=1}^n X_i \sim \text{Binomial}(n,p)$.

The asymptotic distribution of $\hat{p}$ is:

$$\hat{p} \sim_{approx} N\left(p, \frac{p(1-p)}{n}\right)$$

for large $n$ (by the Central Limit Theorem).

**Function of Interest - Odds**

The odds of success is:

$$g(p) = \frac{p}{1-p}$$

We want the asymptotic distribution of $g(\hat{p}) = \frac{\hat{p}}{1-\hat{p}}$.

**Delta Method**

The **Delta Method** helps approximate the distribution of a function of an estimator. Specifically:

- Let $\hat{p} \sim N(p, \text{Var}(\hat{p}))$, where $\text{Var}(\hat{p}) = \frac{p(1-p)}{n}$
- For a smooth function $g(p)$, the asymptotic distribution of $g(\hat{p})$ is:
  $$g(\hat{p}) \sim N(g(p), (g'(p))^2 \cdot \text{Var}(\hat{p}))$$

**Compute $g'(p)$**

The derivative of $g(p) = \frac{p}{1-p}$ is:

$$g'(p) = \frac{1}{(1-p)^2}$$

**Apply the Delta Method**

The variance of $g(\hat{p})$ is:

$$\text{Var}(g(\hat{p})) \approx (g'(p))^2 \cdot \text{Var}(\hat{p})$$

Substitute $g'(p) = \frac{1}{(1-p)^2}$ and $\text{Var}(\hat{p}) = \frac{p(1-p)}{n}$:

$$\text{Var}(g(\hat{p})) \approx \left(\frac{1}{(1-p)^2}\right)^2 \cdot \frac{p(1-p)}{n}$$

Simplify:

$$\text{Var}(g(\hat{p})) \approx \frac{p}{n(1-p)^3}$$

**Asymptotic Distribution of $g(\hat{p})$**

The asymptotic distribution is:

$$g(\hat{p}) = \frac{\hat{p}}{1-\hat{p}} \sim N\left(\frac{p}{1-p}, \frac{p}{n(1-p)^3}\right)$$

**Conclusion**

Using the Delta Method, the odds $g(\hat{p}) = \frac{\hat{p}}{1-\hat{p}}$ has the following asymptotic distribution:

$$\frac{\hat{p}}{1-\hat{p}} \sim N\left(\frac{p}{1-p}, \frac{p}{n(1-p)^3}\right)$$

where:

- The mean $\frac{p}{1-p}$ is the true odds of success
- The variance $\frac{p}{n(1-p)^3}$ decreases with $n$, reflecting the increasing precision of $\hat{p}$ as $n \to \infty$

## Part (b):

> Suppose $X_1,\dots,X_n$ are independent Poisson(λ) random variables. Find a function $g(\bar{X})$ such that the asymptotic variance of $g(\bar{X})$ does not depend on $\lambda$.

## Solution:

**1. Properties of the Sample Mean $\bar{X}$**

For $X_i \sim \text{Poisson}(\lambda)$:

- $E[\bar{X}] = \lambda$
- $\text{Var}(\bar{X}) = \frac{\lambda}{n}$

where $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$

**2. Goal**

We need to find $g(\bar{X})$ such that its asymptotic variance does not depend on $\lambda$. Since $\text{Var}(\bar{X}) = \frac{\lambda}{n}$, we need $g(\bar{X})$ to normalize $\lambda$ appropriately.

**3. Define $g(\bar{X})$**

Let:
$$g(\bar{X}) = \sqrt{\bar{X}}$$

**4. Delta Method Application**

For large $n$, by the delta method:

$$\text{Var}(g(\bar{X})) \approx \left(\frac{\partial g(\bar{X})}{\partial \bar{X}}\right)^2 \text{Var}(\bar{X})$$

The derivative of $g(\bar{X}) = \sqrt{\bar{X}}$ is:

$$\frac{\partial g(\bar{X})}{\partial \bar{X}} = \frac{1}{2\sqrt{\bar{X}}}$$

As $n \to \infty$, $\bar{X} \to \lambda$ (by the Law of Large Numbers), so:

$$\text{Var}(g(\bar{X})) \approx \left(\frac{1}{2\sqrt{\lambda}}\right)^2 \cdot \frac{\lambda}{n} = \frac{1}{4n}$$

**5. Conclusion**
The function $g(\bar{X}) = \sqrt{\bar{X}}$ ensures that the asymptotic variance of $g(\bar{X})$ is $\frac{1}{4n}$, which does not depend on $\lambda$.

# Question 2:

> Let $X_1,...,X_n$ be a random sample from a uniform distribution with probability density function
>
> $$f(x) = \begin{cases} 1 & \text{if } 0 < x < 1 \\ 0 & \text{otherwise} \end{cases}$$
>
> Show that if $X_{(r)}$ is the $r$th order statistic, then
>
> $$E(X_{(r)}) = \frac{r}{n+1}, \quad \text{var}(X_{(r)}) = \frac{r(n+1-r)}{(n+1)^2(n+2)}$$
>
> Define the median of the random sample, distinguishing between the two cases $n$ odd and $n$ even. Show that the median has expected value $\frac{1}{2}$ if the random sample is drawn from a uniform distribution on $(0,1)$. Find its variance in the case when $n$ is odd. What is the expected value of the median if the random sample is drawn from a uniform distribution on $(a,b)$?
>
> [Hint: remember that pdfs integrate to 1, there's no need to actually do any integration in this question.]

## Solution Part a:

Let's solve this step by step for the first part of the question, showing that $E(X_{(r)}) = \frac{r}{n+1}$ and $\text{var}(X_{(r)}) = \frac{r(n+1-r)}{(n+1)^2(n+2)}$.

### 1. PDF of the r-th Order Statistic

For a sample of size $n$ from $U(0,1)$, the PDF of the $r$-th order statistic $X_{(r)}$ is:

$$f_{X_{(r)}}(x) = \frac{n!}{(r-1)!(n-r)!}x^{r-1}(1-x)^{n-r}, \quad 0 < x < 1$$

### 2. Expected Value $E[X_{(r)}]$

The expected value is given by:

$$E[X_{(r)}] = \int_0^1 x \cdot f_{X_{(r)}}(x) dx$$

Substituting the PDF:

$$E[X_{(r)}] = \int_0^1 x \cdot \frac{n!}{(r-1)!(n-r)!}x^{r-1}(1-x)^{n-r} dx$$

$$= \frac{n!}{(r-1)!(n-r)!}\int_0^1 x^r(1-x)^{n-r} dx$$

This integral is a Beta function $B(a,b)$ with $a=r+1$ and $b=n-r+1$:

$$\int_0^1 x^r(1-x)^{n-r} dx = B(r+1,n-r+1)$$

where:
$$B(a,b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$$

Using the relation between Beta and Gamma functions:

$$B(r+1,n-r+1) = \frac{\Gamma(r+1)\Gamma(n-r+1)}{\Gamma(n+2)}$$

Substituting back:

$$E[X_{(r)}] = \frac{n!}{(r-1)!(n-r)!} \cdot \frac{r!(n-r)!}{(n+1)!} = \frac{r}{n+1}$$

### 3. Variance $\text{Var}(X_{(r)})$

The variance is:

$$\text{Var}(X_{(r)}) = E[X_{(r)}^2] - (E[X_{(r)}])^2$$

Following similar steps for $E[X_{(r)}^2]$:

$$E[X_{(r)}^2] = \frac{n!}{(r-1)!(n-r)!}\int_0^1 x^{r+1}(1-x)^{n-r} dx$$

This gives:

$$E[X_{(r)}^2] = \frac{r(r+1)}{(n+1)(n+2)}$$

Therefore:

$$\text{Var}(X_{(r)}) = \frac{r(r+1)}{(n+1)(n+2)} - (\frac{r}{n+1})^2$$

After simplification:

$$\text{Var}(X_{(r)}) = \frac{r(n+1-r)}{(n+1)^2(n+2)}$$

Thus, we have proven both results:

- $E[X_{(r)}] = \frac{r}{n+1}$
- $\text{Var}(X_{(r)}) = \frac{r(n+1-r)}{(n+1)^2(n+2)}$

## Solution Part b: Median of Uniform Distribution Sample

Let's define the median for both cases:

**Case 1: n odd**
When $n$ is odd, let $n = 2k + 1$ for some $k \in \mathbb{N}$

- Median = $X_{(k+1)}$ (the $(k+1)$ th order statistic)

**Case 2: n even**
When $n$ is even, let $n = 2k$ for some $k \in \mathbb{N}$

- Median = $\frac{X_{(k)} + X_{(k+1)}}{2}$ (average of $k$ th and $(k+1)$ th order statistics)

### 2. Expected Value for U(0,1)

**Case 1: n odd $(n = 2k + 1)$**

Using the result from part 1, for the $(k+1)$ th order statistic:

$$E[X_{(k+1)}] = \frac{k+1}{n+1} = \frac{k+1}{2k+2} = \frac{1}{2}$$

**Case 2: n even $(n = 2k)$**
The median is the average of two order statistics:

$$E[\text{Median}] = E[\frac{X_{(k)} + X_{(k+1)}}{2}] = \frac{1}{2}(E[X_{(k)}] + E[X_{(k+1)}])$$

Using the previous result:
$$= \frac{1}{2}(\frac{k}{n+1} + \frac{k+1}{n+1}) = \frac{1}{2}(\frac{k + (k+1)}{2k+1}) = \frac{1}{2}$$

### 3. Variance for n odd

For $n = 2k + 1$, the median is $X_{(k+1)}$, so:

$$\text{Var}(X_{(k+1)}) = \frac{(k+1)(n+1-(k+1))}{(n+1)^2(n+2)}$$

Substituting $k = \frac{n-1}{2}$:

$$= \frac{(\frac{n+1}{2})(n+1-\frac{n+1}{2})}{(n+1)^2(n+2)}$$

$$= \frac{(\frac{n+1}{2})(\frac{n+1}{2})}{(n+1)^2(n+2)}$$

$$= \frac{1}{4(n+2)}$$

### 4. Expected Value for U(a,b)

For a uniform distribution on $(a,b)$, we can use the linear transformation property:

- If $X \sim U(0,1)$, then $Y = a + (b-a)X \sim U(a,b)$

Therefore:

- $E[Y_{(r)}] = a + (b-a)E[X_{(r)}]$

For the median (when $n$ is odd or even):
$$E[\text{Median}] = a + (b-a)\frac{1}{2} = \frac{a+b}{2}$$

This makes intuitive sense as it's the midpoint of the interval $(a,b)$.

Therefore:

- For $U(0,1)$: The median has expected value $\frac{1}{2}$
- For $U(a,b)$: The median has expected value $\frac{a+b}{2}$
- For odd $n$: The variance of the median is $\frac{1}{4(n+2)}$

# Question 3:

> Let $X$ be a continuous random variable with cumulative distribution function $F$ which is strictly increasing. If $Y = F(X)$, show that $Y$ is uniformly distributed on the interval $(0,1)$.
>
> The Weibull distribution with parameters $\alpha > 0$ and $\lambda > 0$ has cumulative distribution function:
>
> $$
> F(x) = \begin{cases}
> 0 & \text{if } x < 0 \\
> 1-\exp(-(x/\lambda)^\alpha) & \text{if } x > 0
> \end{cases}
> $$
>
> Explain why a probability plot for the Weibull distribution may be based on plotting the logarithm of the $r$th order statistic against $\log[-\log(1-\frac{r}{n+1})]$ and give the slope and intercept of such a plot.

## Solution: Weibull Distribution and Probability Plots

### Part 1: Uniform Distribution of $Y = F(X)$

- Since $F$ is a CDF, we know that $0 \leq F(x) \leq 1$ for all $x$
- Therefore, $Y = F(X)$ must be in $(0,1)$

For any $y \in (0,1)$:
$$P(Y \leq y) = P(F(X) \leq y)$$

Since $F$ is strictly increasing, it has an inverse $F^{-1}$:
$$P(F(X) \leq y) = P(X \leq F^{-1}(y))$$

By definition of CDF:
$$P(X \leq F^{-1}(y)) = F(F^{-1}(y)) = y$$

Therefore, $Y$ has CDF:
$$F_Y(y) = y \text{ for } y \in (0,1)$$

This is the CDF of $U(0,1)$, proving $Y \sim U(0,1)$

### Part 2: Weibull Probability Plot

For $x > 0$:
$$F(x) = 1-\exp(-(x/\lambda)^\alpha)$$

Take complement:
$$1-F(x) = \exp(-(x/\lambda)^\alpha)$$

Take log of both sides:
$$\log(1-F(x)) = -(x/\lambda)^\alpha$$

Take log again:
$$\log[-\log(1-F(x))] = \alpha\log(x) - \alpha\log(\lambda)$$

For the $r$ th order statistic:

- $E[X_{(r)}]$ represents expected value of the $r$th order statistic
- From previous results, $F(E[X_{(r)}]) \approx \frac{r}{n+1}$

Therefore:
$$\log[-\log(1-\frac{r}{n+1})] = \alpha\log(E[X_{(r)}]) - \alpha\log(\lambda)$$

Plotting $\log(X_{(r)})$ against $\log[-\log(1-\frac{r}{n+1})]$ gives:

- Slope = $\frac{1}{\alpha}$
- Intercept = $\log(\lambda)$

This creates a linear plot if the data follows a Weibull distribution, with:

- $y = \log(X_{(r)})$
- $x = \log[-\log(1-\frac{r}{n+1})]$

The resulting line has equation:
$$y = \frac{1}{\alpha}x + \log(\lambda)$$

This provides a graphical method to:

1. Verify if data follows Weibull distribution (check linearity)
2. Estimate parameters $\alpha$ and $\lambda$ from slope and intercept

<img src="../Estimation/Code/Figures/weibull.png" alt="alt text">

# Question 4:

> Find the expected information for $\theta$, where $0 < \theta < 1$, based on a random sample $X_1,...,X_n$ from:
>
> (a) the geometric distribution
> $$f(x;\theta) = \theta(1-\theta)^{x-1}, \quad x = 1,2,...$$
>
> (b) the Bernoulli distribution
> $$f(x;\theta) = \theta^x(1-\theta)^{1-x}, \quad x = 0,1$$
>
> A statistician has a choice between observing random samples from the geometric or Bernoulli distributions with the same $\theta$. Which will give the more precise inference about $\theta$?

## Solution: Expected Information for Geometric and Bernoulli Distributions

Let's solve this step by step for both distributions.

### Part (a): Geometric Distribution

The expected information is given by:
$$I(\theta) = -E\left[\frac{\partial^2}{\partial\theta^2}\log f(X;\theta)\right]$$

$$\log f(x;\theta) = \log\theta + (x-1)\log(1-\theta)$$

$$\frac{\partial}{\partial\theta}\log f(x;\theta) = \frac{1}{\theta} - \frac{x-1}{1-\theta}$$

$$\frac{\partial^2}{\partial\theta^2}\log f(x;\theta) = -\frac{1}{\theta^2} - \frac{x-1}{(1-\theta)^2}$$

We know $E[X] = \frac{1}{\theta}$ for geometric distribution

$$I_G(\theta) = \frac{1}{\theta^2} + \frac{E[X]-1}{(1-\theta)^2}$$
$$= \frac{1}{\theta^2} + \frac{\frac{1}{\theta}-1}{(1-\theta)^2}$$
$$= \frac{1}{\theta^2} + \frac{1}{\theta(1-\theta)^2}$$
$$= \frac{1}{\theta^2(1-\theta)}$$

For n observations, multiply by n:
$$I_G(\theta) = \frac{n}{\theta^2(1-\theta)}$$

### Part (b): Bernoulli Distribution

$$\log f(x;\theta) = x\log\theta + (1-x)\log(1-\theta)$$

$$\frac{\partial}{\partial\theta}\log f(x;\theta) = \frac{x}{\theta} - \frac{1-x}{1-\theta}$$

$$\frac{\partial^2}{\partial\theta^2}\log f(x;\theta) = -\frac{x}{\theta^2} - \frac{1-x}{(1-\theta)^2}$$

For Bernoulli, $E[X] = \theta$

$$I_B(\theta) = \frac{\theta}{\theta^2} + \frac{1-\theta}{(1-\theta)^2}$$
$$= \frac{1}{\theta} + \frac{1}{1-\theta}$$
$$= \frac{1}{\theta(1-\theta)}$$

For n observations:
$$I_B(\theta) = \frac{n}{\theta(1-\theta)}$$

### Comparison and Conclusion

Comparing the two expressions:

- Geometric: $I_G(\theta) = \frac{n}{\theta^2(1-\theta)}$
- Bernoulli: $I_B(\theta) = \frac{n}{\theta(1-\theta)}$

Since $0 < \theta < 1$, we have $\frac{1}{\theta} > 1$, therefore:
$$I_G(\theta) > I_B(\theta)$$

The geometric distribution provides more information about $\theta$ and will give more precise inference. This is because each geometric observation provides more information about $\theta$ than a single Bernoulli trial, as it captures the entire sequence of trials until success.

<img src="../Estimation/Code/Figures/fisher_geometric_bernoulli.png" alt="alt text">
