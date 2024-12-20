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

$E[\bar{X}] = \lambda$
$\text{Var}(\bar{X}) = \frac{\lambda}{n}$

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
