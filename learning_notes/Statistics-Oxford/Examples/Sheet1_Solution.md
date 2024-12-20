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

## Solution

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
