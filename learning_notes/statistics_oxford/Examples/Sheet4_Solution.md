# Question 1: Posterior Distribution of $\theta$

Suppose $X_1,\dots,X_n$ are independent, each having a geometric distribution with probability mass function $f(x|θ) = (1−θ)^x θ$ for $x= 0,1,\dots$. Suppose that the prior for $θ$ is a $\text{Beta}(a,b)$ density. Find the posterior distribution of $θ$.

## Solution:

To find the posterior distribution of $\theta$, we use Bayes' theorem. The posterior is proportional to the product of the likelihood function and the prior density.

## Step 1: Likelihood Function

The probability mass function (PMF) of the geometric distribution is given as:

$$
f(x | \theta) = (1 - \theta)^x \theta, \quad x = 0, 1, 2, \dots
$$

For $n$ independent observations $X_1, X_2, \dots, X_n$, the likelihood function is:

$$
L(\theta | X_1, \dots, X_n) = \prod_{i=1}^n f(X_i | \theta) = \prod_{i=1}^n (1 - \theta)^{X_i} \theta.
$$

Simplifying:

$$
L(\theta | X_1, \dots, X_n) = \theta^n (1 - \theta)^{\sum_{i=1}^n X_i}.
$$

Let $S = \sum_{i=1}^n X_i$. Then:

$$
L(\theta | X_1, \dots, X_n) = \theta^n (1 - \theta)^S.
$$

## Step 2: Prior Density

The prior for $\theta$ is $\text{Beta}(a, b)$, with the density:

$$
\pi(\theta) = \frac{\theta^{a-1} (1 - \theta)^{b-1}}{B(a, b)}, \quad 0 < \theta < 1,
$$

where $B(a, b)$ is the Beta function.

## Step 3: Posterior Distribution

The posterior distribution is proportional to the product of the likelihood and the prior:

$$
\pi(\theta | X_1, \dots, X_n) \propto L(\theta | X_1, \dots, X_n) \pi(\theta).
$$

Substitute the likelihood and prior:

$$
\pi(\theta | X_1, \dots, X_n) \propto \theta^n (1 - \theta)^S \cdot \theta^{a-1} (1 - \theta)^{b-1}.
$$

Combine the powers of $\theta$ and $1 - \theta$:

$$
\pi(\theta | X_1, \dots, X_n) \propto \theta^{n + a - 1} (1 - \theta)^{S + b - 1}.
$$

This is the kernel of a Beta distribution. Specifically, the posterior distribution is:

$$
\pi(\theta | X_1, \dots, X_n) \sim \text{Beta}(n + a, S + b).
$$

## Final Answer:

The posterior distribution of $\theta$ is:

$$
\theta | X_1, \dots, X_n \sim \text{Beta}(n + a, S + b),
$$

where $S = \sum_{i=1}^n X_i$.
