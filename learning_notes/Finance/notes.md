# Understanding Volatility, Returns, and Portfolio Effects

## 1. The Core Concept: Arithmetic vs Geometric Returns

### Mathematical Foundation

Let's start with the fundamental relationship between arithmetic and geometric returns. For a single period, if we have returns $r_1, r_2, ..., r_n$:

Arithmetic Mean: $\mu_A = \frac{1}{n}\sum_{i=1}^n r_i$

Geometric Mean: $\mu_G = \left(\prod_{i=1}^n (1+r_i)\right)^{\frac{1}{n}} - 1$

The relationship between them involves volatility:
$\mu_G \approx \mu_A - \frac{\sigma^2}{2}$

This difference $\frac{\sigma^2}{2}$ is the volatility drag.

## 2. Leveraged ETF Decay

### Mathematical Analysis

For a leveraged ETF with leverage $L$, the value after $n$ periods follows:

$V_n = V_0\prod_{i=1}^n (1 + L r_i)$

Where $r_i$ are the returns of the underlying index. The expected value is:

$\mathbb{E}[V_n] = V_0(1 + L\mu - \frac{L^2\sigma^2}{2})^n$

This shows why leveraged ETFs don't provide $L$ times the long-term return.

### Example Calculation

```python
def leveraged_etf_path(initial_value, leverage, returns):
    """
    Calculate leveraged ETF value path

    Parameters:
    -----------
    initial_value: float
        Starting value of the investment
    leverage: float
        Leverage ratio (e.g., 2 for 2x leverage)
    returns: array-like
        Array of underlying index returns

    Returns:
    --------
    array-like: Path of leveraged ETF values
    """
    path = [initial_value]
    current_value = initial_value

    for r in returns:
        leveraged_return = leverage * r
        current_value *= (1 + leveraged_return)
        path.append(current_value)

    return np.array(path)
```

## 3. Sharpe Ratio Adjustments

### Time Scaling Framework

The Sharpe ratio for different time periods must account for both return and volatility scaling:

$SR(T) = \frac{R(T) - R_f(T)}{\sigma(T)}$

Where:

- $R(T)$ is the annualized return over period $T$
- $R_f(T)$ is the risk-free rate for period $T$
- $\sigma(T)$ is the annualized volatility

### Mathematical Adjustment

For a time period $T$ (in years), the adjustments are:

$R(T) = (1 + R_{daily})^{252T} - 1$

$\sigma(T) = \sigma_{daily}\sqrt{252T}$

```python
def adjusted_sharpe_ratio(returns, rf_rate, period_days):
    """
    Calculate time-adjusted Sharpe ratio

    Parameters:
    -----------
    returns: array-like
        Daily returns
    rf_rate: float
        Annual risk-free rate
    period_days: int
        Number of trading days in period

    Returns:
    --------
    float: Adjusted Sharpe ratio
    """
    annualization_factor = 252 / period_days

    # Adjust returns
    period_return = np.prod(1 + returns) ** annualization_factor - 1

    # Adjust volatility
    period_vol = returns.std() * np.sqrt(annualization_factor)

    return (period_return - rf_rate) / period_vol
```

## 4. Continuous vs Discrete Time Portfolio Optimization

### Key Differences

#### 1. Return Calculations

Discrete time: $R_t = \frac{S_t - S_{t-1}}{S_{t-1}}$

Continuous time: $dS_t = \mu S_t dt + \sigma S_t dW_t$

#### 2. Optimal Portfolio Weights

In continuous time, using Itô's lemma, the optimal portfolio weight for a risky asset is:

$w^* = \frac{\mu - r}{\gamma\sigma^2}$

Where:

- $\mu$ is the drift
- $r$ is the risk-free rate
- $\gamma$ is risk aversion
- $\sigma$ is volatility

### Kelly Criterion Example

```python
def kelly_criterion_comparison(mu, sigma, rf_rate):
    """
    Compare Kelly criterion in discrete vs continuous time

    Parameters:
    -----------
    mu: float
        Expected return
    sigma: float
        Volatility
    rf_rate: float
        Risk-free rate

    Returns:
    --------
    tuple: (discrete_kelly, continuous_kelly)
    """
    discrete_kelly = (mu - rf_rate) / sigma**2
    continuous_kelly = (mu - rf_rate - sigma**2/2) / sigma**2

    return discrete_kelly, continuous_kelly
```

## 5. Interview Tips

When discussing these concepts in interviews:

1. Start with the intuition before diving into mathematics
2. Use specific numerical examples to illustrate points
3. Be prepared to discuss practical implications and limitations
4. Connect concepts to real-world trading scenarios
5. Consider transaction costs and market frictions

### Common Interview Questions

1. "What happens to option Greeks when moving from discrete to continuous time?"
2. "How would you optimize a portfolio accounting for volatility drag?"
3. "Explain the relationship between Sharpe ratio and rebalancing frequency"

$$ \text{Note: Always remember that } \mathbb{E}[\prod_{i=1}^n (1+r_i)] \neq \prod\_{i=1}^n \mathbb{E}[1+r_i] $$

This inequality is at the heart of many quantitative finance phenomena.
