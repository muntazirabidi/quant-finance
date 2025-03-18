# Optimizing a Portfolio for Better Risk-Reward

Let me show you how a hedge fund manager would optimize the portfolio we've been analyzing to achieve better risk-reward characteristics. I'll use Python to demonstrate several optimization approaches that are commonly used in quantitative finance.

## Understanding the Current Portfolio Issues

As we saw in our VaR analysis, our current portfolio has:
- Excessive risk concentration in equities (SPY)
- Underutilized diversification potential from treasuries (IEF)
- Suboptimal allocation to gold (GLD)

The goal of portfolio optimization is to find allocations that maximize expected return for a given level of risk, or minimize risk for a given level of expected return.

## Optimization Approaches

I'll demonstrate several portfolio optimization techniques:

1. **Mean-Variance Optimization**: The classic Markowitz approach
2. **Risk Parity**: Equalizing risk contribution across assets
3. **Minimum VaR Portfolio**: Directly minimizing portfolio VaR 
4. **Risk-Adjusted Return Maximization**: Optimizing for Sharpe ratio


## Understanding the Optimization Results

Let's analyze what each optimization approach tells us:

### 1. Mean-Variance Optimization (Maximum Sharpe Ratio)

The classic Markowitz approach optimizes for the highest risk-adjusted return (Sharpe ratio). The key insight is that this typically leads to:

- Lower allocation to SPY than our original portfolio
- Higher allocation to IEF to take advantage of its diversification benefits
- Adjusted allocation to GLD based on its expected risk-return profile

The Sharpe-optimized portfolio usually achieves a better risk-return tradeoff by properly balancing the expected return of equities against the diversification benefits of bonds.

### 2. Risk Parity Portfolio

The risk parity approach is philosophically different - it aims to equalize risk contribution across assets rather than optimizing for return. This typically results in:

- Dramatically lower allocation to SPY (often below 20%)
- Much higher allocation to IEF (typically 50-70%)
- Moderate allocation to GLD

Risk parity acknowledges that equities dominate portfolio risk, so it substantially reduces equity exposure to achieve balanced risk. This leads to lower expected returns but significantly lower volatility and VaR.

### 3. Minimum VaR Portfolio

This approach directly minimizes the Value at Risk of the portfolio. Since our VaR analysis showed extreme concentration in equities, the minimum VaR portfolio typically:

- Has the lowest allocation to SPY among all approaches
- Maximizes allocation to IEF
- Finds the optimal allocation to GLD that helps reduce tail risk

The minimum VaR portfolio provides the best protection against extreme market events but may sacrifice expected returns in normal market conditions.

### 4. Target Return Portfolio

This approach finds the minimum risk portfolio that achieves a target return. By setting a target slightly higher than our current portfolio, we can potentially improve risk-adjusted returns by:

- Finding a more efficient allocation that achieves the same or better return
- Reducing concentration risk without sacrificing expected performance
- Properly leveraging the diversification benefits of our assets

## Hedge Fund Manager's Interpretation and Decision Process

A hedge fund manager would interpret these results through both quantitative and qualitative lenses:

1. **Risk Adjustment**: The original portfolio is clearly inefficient from a risk perspective, with SPY contributing over 100% of VaR. All optimization approaches suggest reducing equity exposure.

2. **Fixed Income Utilization**: IEF is underutilized in the current portfolio. Its negative correlation with equities during stress events makes it a powerful diversifier that should have a larger allocation.

3. **Gold's Role**: Optimization results likely suggest a reduced allocation to gold, as it's not proving to be an effective diversifier during the specific scenarios that drive VaR.

4. **Implementation Considerations**: The manager would also consider:
   - Transaction costs of rebalancing
   - Tax implications of portfolio changes
   - Liquidity requirements and constraints
   - Forward-looking views that might differ from historical data

5. **Risk Budgeting**: The manager would likely set a risk budget that determines acceptable VaR levels, then select the portfolio that provides the best return within that constraint.

## Final Portfolio Selection

The hedge fund manager would likely choose one of the optimized portfolios based on:

1. **Risk Tolerance**: More conservative managers might select the Minimum VaR or Risk Parity portfolio.

2. **Return Objectives**: If higher returns are required, the Target Return or Maximum Sharpe portfolio would be preferred.

3. **Market Views**: If the manager has strong views on specific assets, they might make adjustments to the quantitative optimization results.

The results clearly show that our current portfolio is inefficient from a risk-return perspective, and significant improvement is possible through proper optimization techniques.

# Portfolio Optimization Analysis: Temporal Regime Shifts 

## 1. Introduction

This analysis examines the evolving dynamics between three major asset classes (SPY, IEF, and GLD) across different time horizons: 3-year, 5-year, and 10-year daily returns. We observe significant changes in correlation structures and risk contributions that challenge traditional portfolio construction assumptions and require adaptive management strategies.

## 2. Correlation Structure Evolution

The evolution of asset correlations reveals a fundamental regime shift in market dynamics:

| Time Horizon | SPY-IEF Correlation | SPY-GLD Correlation | IEF-GLD Correlation |
|--------------|---------------------|---------------------|---------------------|
| 10-Year      | +0.38               | +0.05               | -0.16               |
| 5-Year       | +0.36               | +0.18               | +0.02               |
| 3-Year       | +0.41               | +0.21               | +0.14               |

Most notably, the SPY-IEF correlation has remained persistently positive across all time frames, contradicting the traditional negative correlation assumption between stocks and bonds that formed the foundation of the 60/40 portfolio strategy for decades.

The mathematical implication for portfolio variance can be expressed as:

$$\sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_i \sigma_j \rho_{ij}$$

Where $\rho_{ij}$ represents the correlation between assets $i$ and $j$. As these correlations shift from negative to positive values, the diversification benefit (variance reduction) is substantially diminished.

## 3. Risk Contribution Analysis

Value at Risk (VaR) contributions have shifted significantly across time periods:

| Asset | 10-Year VaR Contribution | 5-Year VaR Contribution | 3-Year VaR Contribution |
|-------|--------------------------|--------------------------|--------------------------|
| SPY   | 76.3% ($17,424)          | 82.0% ($20,841)          | 71.3% ($20,245)          |
| IEF   | 21.7% ($4,959)           | 12.4% ($3,160)           | 22.7% ($6,438)           |
| GLD   | 2.0% ($457)              | 5.6% ($1,427)            | 6.0% ($1,694)            |

The risk concentration in equities (SPY) remains dominant across all periods but shows meaningful variability, particularly between the 5-year and 3-year horizons. This suggests that even with similar asset allocations, the risk profile of the portfolio has been evolving.

The total portfolio VaR has also changed:
- 10-Year: $22,840 (1.34% of portfolio)
- 5-Year: $25,428 (1.50% of portfolio)
- 3-Year: $24,990 (1.47% of portfolio)

## 4. Key Insights

### 4.1 Structural Regime Shift in Asset Relationships

The traditional negative correlation between stocks and bonds appears to have fundamentally changed. This represents a paradigm shift from the "Great Moderation" period (1985-2020) to a new regime with different macroeconomic dynamics.

The positive correlation between SPY and IEF can be mathematically expressed through their joint behavior:

$$\rho_{SPY,IEF} = \frac{Cov(SPY, IEF)}{\sigma_{SPY} \sigma_{IEF}} > 0$$

This positive value implies that these assets now tend to move in the same direction, reducing diversification benefits and increasing portfolio vulnerability to simultaneous drawdowns.

### 4.2 Gold's Evolving Role

The correlation between gold and equities has been steadily increasing:
- 10-year: +0.05 (nearly independent)
- 5-year: +0.18 (modest positive correlation)
- 3-year: +0.21 (stronger positive correlation)

This suggests gold's effectiveness as an equity hedge has diminished in recent periods. Simultaneously, gold's relationship with bonds has shifted from negative (-0.16) to positive (+0.14), further complicating its role in portfolio construction.

### 4.3 Implications for Risk Management

The changing correlation structure has profound implications for portfolio risk. Traditional mean-variance optimization may produce misleading results if based solely on long-term historical data that no longer reflects current market dynamics.

The Markowitz efficient frontier equation:

$$\min_w \sigma_p^2 = \min_w w^T \Sigma w$$

Subject to: $w^T \mu = \mu_p$ and $\sum w_i = 1$

Where $\Sigma$ represents the covariance matrix, is highly sensitive to changes in correlations. Using outdated correlation assumptions can lead to suboptimal or even dangerous allocations.

## 5. Underlying Causes of Regime Shifts

### 5.1 Inflation Regime Change

The post-2020 period has seen significantly higher inflation than the previous decade. The correlation between inflation and asset returns can be expressed as:

$$\rho_{asset,inflation} = \frac{Cov(r_{asset}, \pi)}{\sigma_{asset} \sigma_{\pi}}$$

During inflationary periods, this correlation tends to become more positive for both stocks and bonds, driving their correlation higher.

### 5.2 Monetary Policy Transition

The correlation between asset returns and interest rate changes:

$$\rho_{asset,\Delta r} = \frac{Cov(r_{asset}, \Delta r)}{\sigma_{asset} \sigma_{\Delta r}}$$

Has shifted as central banks transitioned from accommodative to restrictive policy. This impacts both the level and structure of correlations across asset classes.

### 5.3 Changing Market Microstructure

The proliferation of risk parity strategies, ETFs, and algorithmic trading has potentially altered market dynamics, leading to more synchronized behavior across traditionally distinct asset classes.

## 6. Strategic Recommendations

### 6.1 Dynamic Correlation Modeling

Implement an exponentially weighted moving average (EWMA) correlation model that gives greater weight to recent observations:

$$\hat{\rho}_{ij,t} = \lambda \hat{\rho}_{ij,t-1} + (1-\lambda) \frac{(r_{i,t} - \mu_i)(r_{j,t} - \mu_j)}{\sigma_i \sigma_j}$$

Where $\lambda$ is the decay factor (typically 0.94 for daily data).

### 6.2 Portfolio Construction Enhancements

1. **Expanded Asset Universe**
   - Include inflation-protected securities (TIPS)
   - Consider floating-rate instruments
   - Add alternative assets with more reliable negative correlations to equities

2. **Risk-Based Allocation**
   - Target maximum 60% risk contribution from equities
   - Implement risk parity approaches within asset classes
   - Set dynamic risk limits based on correlation regimes

3. **Tail Risk Hedging**
   - Implement option-based strategies to create positive convexity
   - Consider allocations to managed futures or trend-following strategies
   - Maintain higher cash reserves for liquidity during correlation spikes

### 6.3 Scenario Analysis Framework

Develop a robust scenario analysis framework that models portfolio performance under:
- Rising inflation with positive stock-bond correlation
- Recession with potentially reverting correlations
- Liquidity crises with correlation convergence toward 1.0

The expected portfolio return under different scenarios can be calculated as:

$$E[r_p | Scenario_i] = \sum_{j=1}^{n} w_j E[r_j | Scenario_i]$$

And the conditional portfolio variance:

$$Var[r_p | Scenario_i] = w^T \Sigma_i w$$

Where $\Sigma_i$ is the conditional covariance matrix in scenario $i$.

## 7. Implementation Considerations

### 7.1 Tactical Asset Allocation Framework

Implement a tactical allocation framework that adjusts weights based on correlation regimes:
- Reduce equity exposure when stock-bond correlation exceeds 0.3
- Increase alternative diversifiers when traditional correlations rise
- Adjust fixed income duration based on inflation expectations

### 7.2 Monitoring System

Establish a correlation monitoring system that:
- Tracks rolling correlations across multiple time frames
- Identifies statistically significant shifts
- Generates alerts when correlations exceed historical thresholds

### 7.3 Portfolio Stress Testing

Regularly stress-test the portfolio using:
- Historical scenarios (2008 GFC, 2020 COVID crash, 1970s stagflation)
- Hypothetical scenarios with extreme correlation assumptions
- Monte Carlo simulations with regime-switching correlation models

The expected shortfall under stress scenarios:

$$ES_{\alpha} = E[r_p | r_p \leq VaR_{\alpha}]$$

Provides a more comprehensive view of tail risk than standard VaR.

## 8. Conclusion

The temporal analysis reveals significant shifts in correlation structures and risk dynamics across different time horizons. These changes challenge traditional portfolio construction approaches and require more sophisticated, dynamic risk management strategies.

The persistently positive correlation between stocks and bonds represents a fundamental regime shift that demands careful reconsideration of portfolio allocations, diversification strategies, and risk management approaches. Implementing the recommended adaptive frameworks can help navigate this changing landscape and potentially exploit the opportunities it creates while managing the associated risks.


Article: https://www.schroders.com/en-lu/lu/professional/insights/regime-shift-what-it-means-for-strategic-asset-allocation/