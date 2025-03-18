import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as sco
from scipy.stats import norm
import seaborn as sns
from numpy.linalg import cholesky

# Set seed for reproducibility
np.random.seed(42)

# Define our assets and current allocation
tickers = ['SPY', 'IEF', 'GLD']
current_weights = np.array([0.588, 0.294, 0.118])  # 58.8% SPY, 29.4% IEF, 11.8% GLD

# Asset parameters based on the real market data from your chart
# Adjusted to reflect the distributions shown in the visualization
expected_returns = np.array([0.00045, 0.00015, 0.00025])  # Daily expected returns
volatilities = np.array([0.0095, 0.0045, 0.0080])  # Daily volatilities

# Correlation matrix from your visualization
correlation = np.array([
    [1.00, 0.41, 0.21],  # SPY correlations
    [0.41, 1.00, 0.14],  # IEF correlations
    [0.21, 0.14, 1.00]   # GLD correlations
])

# Convert correlation to covariance matrix
covariance = np.diag(volatilities) @ correlation @ np.diag(volatilities)

# Function to calculate portfolio statistics
def calculate_portfolio_stats(weights, returns, cov):
    portfolio_return = np.sum(returns * weights)
    portfolio_volatility = np.sqrt(weights.T @ cov @ weights)
    sharpe_ratio = portfolio_return / portfolio_volatility  # Simplified Sharpe (no risk-free rate)
    return portfolio_return, portfolio_volatility, sharpe_ratio

# Function to calculate VaR using Monte Carlo simulation
def calculate_mc_var(weights, returns, cov, initial_investment=1_700_000, 
                     confidence_level=0.99, n_simulations=10000, time_horizon=1):
    # Generate correlated random returns
    L = cholesky(cov)
    Z = np.random.normal(0, 1, size=(n_simulations, len(returns)))
    correlated_returns = returns.reshape(1, -1) + Z @ L.T  # Reshape returns to (1, 3)
    
    # Calculate portfolio values
    portfolio_returns = np.sum(correlated_returns * weights, axis=1)
    portfolio_values = initial_investment * (1 + portfolio_returns)
    
    # Calculate VaR
    var_value = initial_investment - np.percentile(portfolio_values, (1-confidence_level)*100)
    var_pct = var_value / initial_investment
    
    return var_value, var_pct, portfolio_values

# Calculate VaR contributions
def calculate_var_contributions(weights, simulated_returns, var_level, initial_investment=1_700_000):
    # Calculate total portfolio returns for each simulation
    n_simulations = simulated_returns.shape[0]
    portfolio_returns = np.sum(weights * simulated_returns, axis=1)
    
    # Find the VaR scenario
    var_scenario_index = np.argsort(portfolio_returns)[int(n_simulations * (1-var_level))]
    var_scenario_returns = simulated_returns[var_scenario_index]
    
    # Calculate marginal VaR contributions
    var_contributions = weights * var_scenario_returns * initial_investment
    var_contribution_pct = var_contributions / np.sum(var_contributions)
    
    return var_contributions, var_contribution_pct

# Display current portfolio statistics
current_return, current_vol, current_sharpe = calculate_portfolio_stats(
    current_weights, expected_returns, covariance)

# Calculate current portfolio VaR
current_var, current_var_pct, _ = calculate_mc_var(
    current_weights, expected_returns, covariance)

print(f"Current Portfolio Statistics:")
print(f"Allocation: SPY={current_weights[0]*100:.1f}%, IEF={current_weights[1]*100:.1f}%, GLD={current_weights[2]*100:.1f}%")
print(f"Expected Return (daily): {current_return*100:.4f}%")
print(f"Volatility (daily): {current_vol*100:.4f}%")
print(f"Sharpe Ratio: {current_sharpe:.4f}")
print(f"1-Day 99% VaR: ${current_var:,.2f} ({current_var_pct*100:.2f}%)")

# 1. Mean-Variance Optimization (Efficient Frontier)
# Objective function to minimize negative Sharpe Ratio
def negative_sharpe(weights, returns, cov):
    portfolio_return, portfolio_volatility, sharpe = calculate_portfolio_stats(weights, returns, cov)
    return -sharpe  # We minimize the negative Sharpe ratio to maximize Sharpe

# Constraints and bounds for optimization
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights sum to 1
bounds = tuple((0, 1) for _ in range(len(tickers)))  # Weights between 0 and 1

# Optimize to maximize Sharpe ratio
initial_guess = np.array([1/3, 1/3, 1/3])  # Equal weights as starting point
optimized_sharpe_result = sco.minimize(
    negative_sharpe, 
    initial_guess, 
    args=(expected_returns, covariance),
    method='SLSQP', 
    bounds=bounds, 
    constraints=constraints
)

sharpe_weights = optimized_sharpe_result['x']
sharpe_return, sharpe_vol, sharpe_ratio = calculate_portfolio_stats(
    sharpe_weights, expected_returns, covariance)

# Calculate VaR for the Sharpe-optimized portfolio
sharpe_var, sharpe_var_pct, _ = calculate_mc_var(
    sharpe_weights, expected_returns, covariance)

print(f"\nMaximum Sharpe Ratio Portfolio:")
print(f"Allocation: SPY={sharpe_weights[0]*100:.1f}%, IEF={sharpe_weights[1]*100:.1f}%, GLD={sharpe_weights[2]*100:.1f}%")
print(f"Expected Return (daily): {sharpe_return*100:.4f}%")
print(f"Volatility (daily): {sharpe_vol*100:.4f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
print(f"1-Day 99% VaR: ${sharpe_var:,.2f} ({sharpe_var_pct*100:.2f}%)")

# 2. Risk Parity Portfolio
# Function to calculate risk contribution
def calculate_risk_contributions(weights, cov):
    portfolio_vol = np.sqrt(weights.T @ cov @ weights)
    marginal_contrib = cov @ weights
    risk_contrib = weights * marginal_contrib / portfolio_vol
    return risk_contrib

# Risk parity objective function
def risk_parity_objective(weights, cov):
    weights = np.array(weights)
    risk_contrib = calculate_risk_contributions(weights, cov)
    target_risk = 1.0 / len(weights)  # Equal risk contribution
    # Sum of squared differences between target and actual risk contributions
    return np.sum((risk_contrib - target_risk)**2)

# Optimize for risk parity
risk_parity_result = sco.minimize(
    risk_parity_objective, 
    initial_guess, 
    args=(covariance,),
    method='SLSQP', 
    bounds=bounds, 
    constraints=constraints
)

# Normalize weights to sum to 1
risk_parity_weights = risk_parity_result['x'] / np.sum(risk_parity_result['x'])
risk_parity_return, risk_parity_vol, risk_parity_sharpe = calculate_portfolio_stats(
    risk_parity_weights, expected_returns, covariance)

# Calculate VaR for risk parity portfolio
risk_parity_var, risk_parity_var_pct, _ = calculate_mc_var(
    risk_parity_weights, expected_returns, covariance)

print(f"\nRisk Parity Portfolio:")
print(f"Allocation: SPY={risk_parity_weights[0]*100:.1f}%, IEF={risk_parity_weights[1]*100:.1f}%, GLD={risk_parity_weights[2]*100:.1f}%")
print(f"Expected Return (daily): {risk_parity_return*100:.4f}%")
print(f"Volatility (daily): {risk_parity_vol*100:.4f}%")
print(f"Sharpe Ratio: {risk_parity_sharpe:.4f}")
print(f"1-Day 99% VaR: ${risk_parity_var:,.2f} ({risk_parity_var_pct*100:.2f}%)")

# 3. Minimum VaR Portfolio
# Objective function to minimize VaR directly
def var_objective(weights, returns, cov):
    weights = np.array(weights)
    var_value, var_pct, _ = calculate_mc_var(weights, returns, cov)
    return var_value

# Optimize to minimize VaR
min_var_result = sco.minimize(
    var_objective, 
    initial_guess, 
    args=(expected_returns, covariance),
    method='SLSQP', 
    bounds=bounds, 
    constraints=constraints
)

min_var_weights = min_var_result['x']
min_var_return, min_var_vol, min_var_sharpe = calculate_portfolio_stats(
    min_var_weights, expected_returns, covariance)

# Calculate VaR for minimum VaR portfolio
min_var_var, min_var_var_pct, _ = calculate_mc_var(
    min_var_weights, expected_returns, covariance)

print(f"\nMinimum VaR Portfolio:")
print(f"Allocation: SPY={min_var_weights[0]*100:.1f}%, IEF={min_var_weights[1]*100:.1f}%, GLD={min_var_weights[2]*100:.1f}%")
print(f"Expected Return (daily): {min_var_return*100:.4f}%")
print(f"Volatility (daily): {min_var_vol*100:.4f}%")
print(f"Sharpe Ratio: {min_var_sharpe:.4f}")
print(f"1-Day 99% VaR: ${min_var_var:,.2f} ({min_var_var_pct*100:.2f}%)")

# 4. Target Return Portfolio (with minimum risk)
# Target a specific return level
target_return = current_return * 1.1  # Target 10% higher return than current portfolio

# Objective function to minimize volatility subject to target return
def min_vol_objective(weights, returns, cov):
    return np.sqrt(weights.T @ cov @ weights)

# Additional constraint for target return
return_constraint = {'type': 'eq', 
                     'fun': lambda x: np.sum(x * expected_returns) - target_return}
all_constraints = [constraints, return_constraint]

# Optimize for minimum volatility with target return
target_return_result = sco.minimize(
    min_vol_objective, 
    initial_guess, 
    args=(expected_returns, covariance),
    method='SLSQP', 
    bounds=bounds, 
    constraints=all_constraints
)

# Check if optimization was successful
if target_return_result['success']:
    target_return_weights = target_return_result['x']
    target_return_return, target_return_vol, target_return_sharpe = calculate_portfolio_stats(
        target_return_weights, expected_returns, covariance)
    
    # Calculate VaR for target return portfolio
    target_return_var, target_return_var_pct, _ = calculate_mc_var(
        target_return_weights, expected_returns, covariance)
    
    print(f"\nTarget Return Portfolio (with minimum risk):")
    print(f"Allocation: SPY={target_return_weights[0]*100:.1f}%, IEF={target_return_weights[1]*100:.1f}%, GLD={target_return_weights[2]*100:.1f}%")
    print(f"Expected Return (daily): {target_return_return*100:.4f}%")
    print(f"Volatility (daily): {target_return_vol*100:.4f}%")
    print(f"Sharpe Ratio: {target_return_sharpe:.4f}")
    print(f"1-Day 99% VaR: ${target_return_var:,.2f} ({target_return_var_pct*100:.2f}%)")
else:
    print("\nTarget return optimization failed - target may be too high.")

# Create comparison table of all portfolios
portfolios = {
    'Current': current_weights,
    'Max Sharpe': sharpe_weights,
    'Risk Parity': risk_parity_weights,
    'Min VaR': min_var_weights
}

if 'target_return_weights' in locals():
    portfolios['Target Return'] = target_return_weights

# Generate comparative statistics
stats_table = pd.DataFrame({
    'SPY %': [weights[0] * 100 for weights in portfolios.values()],
    'IEF %': [weights[1] * 100 for weights in portfolios.values()],
    'GLD %': [weights[2] * 100 for weights in portfolios.values()],
    'Expected Return (%)': [calculate_portfolio_stats(weights, expected_returns, covariance)[0] * 100 
                           for weights in portfolios.values()],
    'Volatility (%)': [calculate_portfolio_stats(weights, expected_returns, covariance)[1] * 100 
                      for weights in portfolios.values()],
    'Sharpe Ratio': [calculate_portfolio_stats(weights, expected_returns, covariance)[2] 
                    for weights in portfolios.values()],
    'VaR ($)': [calculate_mc_var(weights, expected_returns, covariance)[0] 
               for weights in portfolios.values()],
    'VaR (%)': [calculate_mc_var(weights, expected_returns, covariance)[1] * 100 
               for weights in portfolios.values()]
}, index=portfolios.keys())

# Format the table
pd.set_option('display.float_format', '${:.2f}'.format)
print("\nPortfolio Comparison:")
print(stats_table.to_string(formatters={
    'SPY %': '{:.1f}%'.format,
    'IEF %': '{:.1f}%'.format,
    'GLD %': '{:.1f}%'.format,
    'Expected Return (%)': '{:.4f}%'.format,
    'Volatility (%)': '{:.4f}%'.format,
    'Sharpe Ratio': '{:.4f}'.format,
    'VaR ($)': '${:,.2f}'.format,
    'VaR (%)': '{:.2f}%'.format
}))

# Calculate and display risk contributions for each portfolio
print("\nRisk Contribution Analysis:")
for name, weights in portfolios.items():
    risk_contrib = calculate_risk_contributions(weights, covariance)
    risk_contrib_pct = risk_contrib / np.sum(risk_contrib) * 100
    
    print(f"\n{name} Portfolio Risk Contributions:")
    for i, ticker in enumerate(tickers):
        print(f"{ticker}: {risk_contrib_pct[i]:.1f}%")

# Generate efficient frontier
def efficient_frontier_data(returns, cov, points=100):
    # Generate a range of target returns
    target_returns = np.linspace(min(returns) * 0.8, max(returns) * 1.2, points)
    efficient_portfolios = []
    
    for target in target_returns:
        # Constraint for target return
        return_constraint = {'type': 'eq', 'fun': lambda x: np.sum(x * returns) - target}
        constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}, return_constraint]
        
        # Optimize
        result = sco.minimize(
            min_vol_objective, 
            initial_guess, 
            args=(returns, cov),
            method='SLSQP', 
            bounds=bounds, 
            constraints=constraints
        )
        
        if result['success']:
            weights = result['x']
            portfolio_return, portfolio_vol, _ = calculate_portfolio_stats(weights, returns, cov)
            efficient_portfolios.append((portfolio_return, portfolio_vol, weights))
    
    return efficient_portfolios

# Generate efficient frontier
ef_data = efficient_frontier_data(expected_returns, covariance)
ef_returns = [x[0] for x in ef_data]
ef_vols = [x[1] for x in ef_data]

# Create visualization
plt.figure(figsize=(12, 8))

# Plot efficient frontier
plt.plot(np.array(ef_vols) * 100, np.array(ef_returns) * 100, 'b-', label='Efficient Frontier')

# Plot current and optimized portfolios
portfolio_markers = {
    'Current': 'ro',
    'Max Sharpe': 'go',
    'Risk Parity': 'yo',
    'Min VaR': 'co'
}

for name, weights in portfolios.items():
    if name == 'Target Return' and 'target_return_weights' not in locals():
        continue
    return_val, vol_val, _ = calculate_portfolio_stats(weights, expected_returns, covariance)
    plt.plot(vol_val * 100, return_val * 100, portfolio_markers.get(name, 'mo'), markersize=10, label=name)

plt.title('Portfolio Optimization with Real Market Data: Risk-Return Tradeoff')
plt.xlabel('Expected Volatility (%)')
plt.ylabel('Expected Return (%)')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('real_market_efficient_frontier.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate risk contribution chart for each portfolio
plt.figure(figsize=(15, 10))

for i, (name, weights) in enumerate(portfolios.items()):
    plt.subplot(3, 2, i+1)
    
    risk_contributions = calculate_risk_contributions(weights, covariance)
    risk_contributions_pct = risk_contributions / np.sum(risk_contributions) * 100
    
    plt.bar(tickers, risk_contributions_pct)
    plt.title(f'Risk Contribution - {name} Portfolio')
    plt.ylabel('Risk Contribution (%)')
    plt.ylim(0, 100)
    
    # Add value labels
    for j, v in enumerate(risk_contributions_pct):
        plt.text(j, v + 1, f'{v:.1f}%', ha='center')

plt.tight_layout()
plt.savefig('real_market_risk_contributions.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nVisualizations saved as 'real_market_efficient_frontier.png' and 'real_market_risk_contributions.png'")

# Generate VaR contribution analysis
for name, weights in portfolios.items():
    # Generate Monte Carlo simulations for this portfolio
    _, _, portfolio_values = calculate_mc_var(weights, expected_returns, covariance, n_simulations=10000)
    
    # Find the VaR threshold and value
    var_threshold = np.percentile(portfolio_values, 1)
    var_value = 1_700_000 - var_threshold
    
    print(f"\n{name} Portfolio VaR Analysis:")
    print(f"99% 1-Day VaR: ${var_value:,.2f} ({var_value/1_700_000*100:.2f}%)")