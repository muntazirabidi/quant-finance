# Ordered Statistics

## 1. Introduction

### What are Order Statistics?

Order statistics are the values of a sample arranged in ascending order. Think of it like:

- Lining up students by height
- Sorting test scores from lowest to highest
- Arranging temperatures throughout the day

### Notation

For data points $x_1,...,x_n$, we write the ordered values as:
$x_{(1)} \leq x_{(2)} \leq ... \leq x_{(n)}$

Where:

- $x_{(1)}$ is the minimum
- $x_{(n)}$ is the maximum
- $x_{(r)}$ is the $r$ th ordered value

## 2. Important Summary Statistics

### 2.1 Sample Median

The "middle" value that divides the data into two equal parts.

For sample size $n$:

- If $n$ is odd: $m = x_{(\frac{n+1}{2})}$
- If $n$ is even: $m = \frac{1}{2}(x_{(\frac{n}{2})} + x_{(\frac{n}{2}+1)})$

**Example:**

```
Data: 2, 5, 7, 8, 9
n = 5 (odd)
Median = x_{(3)} = 7

Data: 2, 5, 7, 8, 9, 10
n = 6 (even)
Median = (7 + 8)/2 = 7.5
```

### 2.2 Quartiles

- Lower quartile (Q1): 25th percentile
- Upper quartile (Q3): 75th percentile
- Interquartile Range (IQR) = Q3 - Q1

## 3. Probability Theory of Order Statistics

### 3.1 Distribution of Order Statistics

For iid continuous random variables $X_1,...,X_n$ with CDF $F$ and PDF $f$:

#### Maximum ($X_{(n)}$)

**CDF:**
$F_{(n)}(x) = P(X_{(n)} \leq x) = P(\text{all }X_i \leq x) = F(x)^n$

**PDF:**
$f_{(n)}(x) = nF(x)^{n-1}f(x)$

**Intuition:**

- All values must be ≤ x
- Probability multiplies due to independence

#### Minimum ($X_{(1)}$)

**CDF:**
$F_{(1)}(x) = 1 - P(X_{(1)} > x) = 1 - [1-F(x)]^n$

**PDF:**
$f_{(1)}(x) = n[1-F(x)]^{n-1}f(x)$

**Intuition:**

- Probability of minimum > x means all values > x
- Take complement for CDF

### 3.2 General Case: $r$ th Order Statistic

**PDF:**
$f_{(r)}(x) = \frac{n!}{(r-1)!(n-r)!}F(x)^{r-1}[1-F(x)]^{n-r}f(x)$

**Intuition behind the formula:**

1. Need $r-1$ observations < x
2. Need one observation at x
3. Need $n-r$ observations > x
4. Multiply probabilities and account for orderings

## 4. Examples

### Example 1: Uniform Distribution

Let $X_1,...,X_n \sim U(0,1)$
Then $f(x) = 1$ and $F(x) = x$ for $0 \leq x \leq 1$

For $r$th order statistic:
$f_{(r)}(x) = \frac{n!}{(r-1)!(n-r)!}x^{r-1}(1-x)^{n-r}$

### Example 2: Exponential Distribution

Let $X_1,...,X_n \sim Exp(\lambda)$
Then $f(x) = \lambda e^{-\lambda x}$ and $F(x) = 1-e^{-\lambda x}$ for $x \geq 0$

PDF of minimum:
$f_{(1)}(x) = n\lambda e^{-n\lambda x}$

## 5. Applications

### 5.1 Quality Control

- Using minimum/maximum for tolerance limits
- Monitoring extreme values in manufacturing

### 5.2 Environmental Science

- Analyzing extreme temperatures
- Studying pollution levels

### 5.3 Finance

- Value at Risk (VaR) calculations
- Portfolio risk assessment

### 5.4 Reliability Engineering

- System failure analysis
- Component lifetime studies

## 6. Computational Aspects

```python
import numpy as np

def order_statistic_sample(data, r):
    """
    Returns the r-th order statistic from data
    """
    sorted_data = np.sort(data)
    return sorted_data[r-1]
```

## 7. Key Takeaways

1. Order statistics organize random samples in ascending order
2. Special cases (min, max, median) have important applications
3. Distribution theory helps understand their probabilistic behavior
4. Applications span multiple fields from finance to engineering
