import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from numpy.linalg import cholesky
import yfinance as yf
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

def generate_synthetic_data(tickers, days=756):
    """
    Generate synthetic price data for testing when actual market data is unavailable.
    
    Parameters:
    tickers (list): List of ticker symbols
    days (int): Number of days to generate data for
    
    Returns:
    pandas.DataFrame: DataFrame with synthetic price data and dates as index
    """
    # Define asset parameters for different asset classes
    asset_params = {
        'SPY': {'mean': 0.0003, 'vol': 0.01},    # Stock index
        'IEF': {'mean': 0.0001, 'vol': 0.003},   # Treasury bonds
        'GLD': {'mean': 0.0002, 'vol': 0.008},   # Gold
        # Default parameters for other assets
        'DEFAULT': {'mean': 0.0002, 'vol': 0.007}
    }
    
    # Create date range for the past N days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date, freq='B')  # Business days
    
    # Initialize DataFrame for prices
    prices = pd.DataFrame(index=date_range)
    
    # Generate price data for each ticker
    for ticker in tickers:
        # Get parameters for this asset type
        params = asset_params.get(ticker, asset_params['DEFAULT'])
        
        # Start with initial price of 100
        price = 100
        price_series = [price]
        
        # Generate returns with specified mean and volatility
        returns = np.random.normal(
            loc=params['mean'], 
            scale=params['vol'], 
            size=len(date_range)-1
        )
        
        # Calculate price series
        for ret in returns:
            price = price * (1 + ret)
            price_series.append(price)
        
        # Add to DataFrame
        prices[ticker] = price_series
    
    return prices

def get_historical_data(tickers, start_date=None, end_date=None, use_synthetic=True):
    """
    Get historical price data and calculate returns.
    
    Parameters:
    tickers (list): List of ticker symbols
    start_date (str): Start date in 'YYYY-MM-DD' format
    end_date (str): End date in 'YYYY-MM-DD' format
    use_synthetic (bool): Whether to use synthetic data instead of downloading
    
    Returns:
    tuple: (returns DataFrame, means array, covariance matrix, correlation matrix)
    """
    try:
        if use_synthetic:
            print("Using synthetic data instead of downloading from external source")
            # Generate synthetic price data
            data = generate_synthetic_data(tickers)
        else:
            # This would be the original yfinance download code
            # We're replacing it with synthetic data due to the error
            print("Would attempt to download data here")
            # This line would be: 
            data = yf.download(tickers, start=start_date, end=end_date)['Close']

        
        # Verify we have data
        if data.empty:
            raise ValueError("No data was generated/downloaded")
            
        # Calculate daily returns
        returns = data.pct_change().dropna()
        
        # Verify we have returns
        if returns.empty:
            raise ValueError("No returns could be calculated")
            
        # Print data summary for verification
        print(f"Using {len(returns)} days of data")
        print("\nReturns Summary:")
        print(returns.describe())
        
        # Calculate statistical parameters
        means = returns.mean().values
        cov_matrix = returns.cov().values
        corr_matrix = returns.corr().values
        
        return returns, means, cov_matrix, corr_matrix
        
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        raise

# Define function to generate correlated random returns using Cholesky decomposition
def generate_correlated_returns(means, cov_matrix, n_scenarios=10000):
    """
    Generate correlated random returns using Cholesky decomposition.
    
    Parameters:
    means (array): Mean returns for each asset
    cov_matrix (array): Covariance matrix of returns
    n_scenarios (int): Number of scenarios to generate
    
    Returns:
    array: Matrix of simulated returns with shape (n_scenarios, n_assets)
    """
    # Get dimensions
    n_assets = len(means)
    
    # Compute Cholesky decomposition
    try:
        L = cholesky(cov_matrix)
    except np.linalg.LinAlgError:
        # If covariance matrix is not positive definite, apply a small adjustment
        print("Warning: Covariance matrix is not positive definite. Applying adjustment.")
        # Add a small value to the diagonal
        cov_matrix_adjusted = cov_matrix.copy()
        np.fill_diagonal(cov_matrix_adjusted, np.diag(cov_matrix) * 1.0001)
        L = cholesky(cov_matrix_adjusted)
    
    # Generate independent standard normal random variables
    Z = np.random.normal(0, 1, size=(n_scenarios, n_assets))
    
    # Transform to correlated random variables with correct means and covariances
    correlated_returns = means + np.dot(Z, L.T)
    
    return correlated_returns

# Define function to calculate VaR
def calculate_var(initial_values, simulated_values, confidence_level=0.99):
    """
    Calculate Value at Risk (VaR) as the difference between initial and simulated values.
    
    Parameters:
    initial_values (array-like): Initial portfolio value(s)
    simulated_values (array-like): Simulated portfolio values
    confidence_level (float): Confidence level for VaR calculation
    
    Returns:
    float: VaR value
    """
    # Ensure both are arrays
    initial_values = np.atleast_1d(initial_values)
    simulated_values = np.array(simulated_values)
    
    # Calculate changes
    if len(initial_values) == 1:
        # Single initial value case
        changes = initial_values[0] - simulated_values
    else:
        # Multiple initial values case (element-wise)
        changes = initial_values - simulated_values
    
    # Sort the changes
    sorted_changes = np.sort(changes)
    
    # Find the index corresponding to the confidence level
    index = int(np.round(confidence_level * len(sorted_changes)))
    
    # Get the VaR value
    var = sorted_changes[index]
    
    return var

def monte_carlo_var(tickers, portfolio_values, start_date=None, end_date=None, n_scenarios=10000, confidence_level=0.99, use_synthetic=True):
    """
    Perform Monte Carlo VaR calculation for a portfolio.
    
    Parameters:
    tickers (list): List of ticker symbols
    portfolio_values (list): Current value of each asset in the portfolio
    start_date (str): Start date for historical data in 'YYYY-MM-DD' format
    end_date (str): End date for historical data in 'YYYY-MM-DD' format
    n_scenarios (int): Number of scenarios to generate
    confidence_level (float): Confidence level for VaR calculation
    use_synthetic (bool): Whether to use synthetic data instead of downloading
    
    Returns:
    tuple: (VaR value, DataFrame of simulated returns, raw simulated returns, simulation results)
    """
    # Step 1: Get historical data and calculate statistical parameters
    returns_df, means, cov_matrix, corr_matrix = get_historical_data(tickers, start_date, end_date, use_synthetic)
    
    # Step 2: Generate correlated random returns
    simulated_returns = generate_correlated_returns(means, cov_matrix, n_scenarios)
    
    # Convert portfolio values to array
    portfolio_values = np.array(portfolio_values)
    total_portfolio_value = np.sum(portfolio_values)
    
    # Step 3: Calculate new portfolio value for each scenario
    new_portfolio_values = portfolio_values * (1 + simulated_returns)
    total_new_portfolio_values = np.sum(new_portfolio_values, axis=1)
    
    # Step 4: Calculate VaR
    var_value = calculate_var(total_portfolio_value, total_new_portfolio_values, confidence_level)
    
    # Create a DataFrame of simulated returns for analysis
    simulated_returns_df = pd.DataFrame(
        simulated_returns, 
        columns=[f"{ticker} Return" for ticker in tickers]
    )
    
    # Add portfolio values
    simulation_results = pd.DataFrame({
        'Initial Portfolio Value': total_portfolio_value,
        'Simulated Portfolio Value': total_new_portfolio_values,
        'Profit/Loss': total_new_portfolio_values - total_portfolio_value
    })
    
    return var_value, simulated_returns_df, simulated_returns, simulation_results

# Define a function to visualize the results
def calculate_var_contributions(portfolio_values, simulated_returns, total_portfolio_var, confidence_level=0.99):
    """
    Calculate the contribution of each asset to the total portfolio VaR.
    
    Parameters:
    portfolio_values (array-like): Values invested in each asset
    simulated_returns (array-like): Matrix of simulated returns with shape (n_scenarios, n_assets)
    total_portfolio_var (float): Total portfolio VaR value
    confidence_level (float): Confidence level for VaR calculation
    
    Returns:
    tuple: (Absolute VaR contributions, Percentage VaR contributions)
    """
    # Convert to numpy arrays
    portfolio_values = np.array(portfolio_values)
    simulated_returns = np.array(simulated_returns)
    
    # Calculate total portfolio value
    total_portfolio_value = np.sum(portfolio_values)
    
    # Calculate portfolio percentage for each scenario
    portfolio_pct_returns = np.sum(portfolio_values.reshape(1, -1) * simulated_returns, axis=1) / total_portfolio_value
    
    # Sort portfolio returns to find VaR scenario
    sorted_indices = np.argsort(portfolio_pct_returns)
    var_index = int(np.round((1 - confidence_level) * len(sorted_indices)))
    var_scenario_index = sorted_indices[var_index]
    
    # Get the returns for the VaR scenario
    var_scenario_returns = simulated_returns[var_scenario_index]
    
    # Calculate the dollar loss for each asset in the VaR scenario
    var_dollar_contributions = portfolio_values * var_scenario_returns
    
    # Calculate percentage contributions
    var_pct_contributions = var_dollar_contributions / np.sum(var_dollar_contributions)
    
    # Normalize to match total VaR
    var_dollar_contributions_normalized = var_pct_contributions * total_portfolio_var
    
    return var_dollar_contributions_normalized, var_pct_contributions

def visualize_var_results(returns_df, corr_matrix, simulated_returns_df, simulation_results, var_value, 
                         confidence_level, tickers, portfolio_values=None, var_dollar_contributions=None, 
                         var_pct_contributions=None):
    """
    Create visualizations of the VaR calculation results.
    
    Parameters:
    returns_df (DataFrame): Historical returns
    corr_matrix (array): Correlation matrix
    simulated_returns_df (DataFrame): Simulated returns
    simulation_results (DataFrame): Simulation results with portfolio values
    var_value (float): Calculated VaR value
    confidence_level (float): Confidence level used for VaR
    tickers (list): List of ticker symbols
    portfolio_values (list, optional): Values invested in each asset for VaR contribution analysis
    var_dollar_contributions (array, optional): Pre-calculated dollar contributions to VaR
    var_pct_contributions (array, optional): Pre-calculated percentage contributions to VaR
    """
    # Create a figure with subplots
    fig = plt.figure(figsize=(20, 18))  # Increased height for additional plot
    
    # 1. Historical Returns Distribution
    ax1 = fig.add_subplot(3, 3, 1)
    for ticker in returns_df.columns:
        sns.histplot(returns_df[ticker], kde=True, stat="density", label=ticker, ax=ax1)
    ax1.set_title("Historical Daily Returns Distribution")
    ax1.set_xlabel("Return")
    ax1.set_ylabel("Density")
    ax1.legend()
    
    # 2. Correlation Matrix Heatmap
    ax2 = fig.add_subplot(3, 3, 2)
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", 
                xticklabels=tickers, yticklabels=tickers, ax=ax2)
    ax2.set_title("Historical Correlation Matrix")
    
    # 3. Simulated Returns Distributions
    ax3 = fig.add_subplot(3, 3, 4)
    for col in simulated_returns_df.columns:
        sns.histplot(simulated_returns_df[col], kde=True, stat="density", label=col, ax=ax3)
    ax3.set_title("Simulated Daily Returns Distribution")
    ax3.set_xlabel("Return")
    ax3.set_ylabel("Density")
    ax3.legend()
    
    # 4. Simulated Portfolio Value Distribution
    ax4 = fig.add_subplot(3, 3, 5)
    sns.histplot(simulation_results['Simulated Portfolio Value'], kde=True, ax=ax4)
    ax4.axvline(x=simulation_results['Initial Portfolio Value'].iloc[0], color='r', linestyle='--',
                label=f"Initial Value: ${simulation_results['Initial Portfolio Value'].iloc[0]:,.2f}")
    # Calculate the VaR threshold
    var_threshold = simulation_results['Initial Portfolio Value'].iloc[0] - var_value
    ax4.axvline(x=var_threshold, color='g', linestyle='--',
                label=f"{confidence_level*100}% VaR Threshold: ${var_threshold:,.2f}")
    ax4.set_title("Distribution of Simulated Portfolio Values")
    ax4.set_xlabel("Portfolio Value ($)")
    ax4.set_ylabel("Frequency")
    ax4.legend()
    
    # 5. Portfolio Profit/Loss Distribution with VaR
    ax5 = fig.add_subplot(3, 3, 7)
    sns.histplot(simulation_results['Profit/Loss'], kde=True, ax=ax5)
    ax5.axvline(x=0, color='r', linestyle='--', label="No Change")
    ax5.axvline(x=-var_value, color='g', linestyle='--', 
                label=f"{confidence_level*100}% VaR: ${var_value:,.2f}")
    ax5.set_title("Distribution of Portfolio Profit/Loss")
    ax5.set_xlabel("Profit/Loss ($)")
    ax5.set_ylabel("Frequency")
    # Highlight the tail representing VaR
    ax5_xlim = ax5.get_xlim()
    ax5.fill_between(
        np.linspace(ax5_xlim[0], -var_value, 100),
        0, 
        1,
        transform=ax5.get_xaxis_transform(),
        alpha=0.3,
        color="red",
        label=f"{(1-confidence_level)*100}% Worst Outcomes"
    )
    ax5.legend()
    
    # 6. Scatter plot of returns for the first two assets
    if len(tickers) >= 2:
        ax6 = fig.add_subplot(3, 3, 8)
        ax6.scatter(
            simulated_returns_df.iloc[:, 0], 
            simulated_returns_df.iloc[:, 1], 
            alpha=0.3, s=10
        )
        ax6.set_title(f"Correlation Between {tickers[0]} and {tickers[1]} Returns")
        ax6.set_xlabel(f"{tickers[0]} Return")
        ax6.set_ylabel(f"{tickers[1]} Return")
        
        # Add a red "X" at the origin
        ax6.plot(0, 0, 'rx', ms=10, mew=3)
        
    # 7. VaR Contribution Analysis
    if portfolio_values is not None and var_dollar_contributions is not None and var_pct_contributions is not None:
        try:
            # Use pre-calculated VaR contributions instead of recalculating
            
            # Create VaR contribution pie chart
            ax7 = fig.add_subplot(3, 3, 3)
            labels = [f"{ticker}\n${abs(contrib):,.0f} ({abs(contrib/var_value)*100:.1f}%)" 
                     for ticker, contrib in zip(tickers, var_dollar_contributions)]
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
            explode = [0.1 if abs(pct) == max(abs(var_pct_contributions)) else 0 for pct in var_pct_contributions]
            
            ax7.pie(abs(var_dollar_contributions), labels=labels, autopct='%.1f%%', 
                   startangle=90, explode=explode, colors=colors[:len(tickers)], shadow=True)
            ax7.set_title(f"VaR Contribution by Asset (${var_value:,.0f} total)")
            
            # Create VaR vs Portfolio Allocation bar chart
            ax8 = fig.add_subplot(3, 3, 6)
            x = np.arange(len(tickers))
            width = 0.35
            
            # Portfolio allocation percentages
            total_portfolio = sum(portfolio_values)
            portfolio_pct = np.array(portfolio_values) / total_portfolio * 100
            # VaR contribution percentages (absolute values)
            var_contrib_pct = np.abs(var_pct_contributions) * 100
            
            ax8.bar(x - width/2, portfolio_pct, width, label='Portfolio Allocation')
            ax8.bar(x + width/2, var_contrib_pct, width, label='VaR Contribution')
            
            ax8.set_xticks(x)
            ax8.set_xticklabels(tickers)
            ax8.set_ylabel('Percentage (%)')
            ax8.set_title('Portfolio Allocation vs. VaR Contribution')
            ax8.legend()
            
            # Add text annotations for the ratio of VaR% to Portfolio%
            for i, ticker in enumerate(tickers):
                ratio = var_contrib_pct[i] / portfolio_pct[i]
                ax8.annotate(f'Ratio: {ratio:.2f}x', 
                            xy=(i, max(var_contrib_pct[i], portfolio_pct[i]) + 2),
                            ha='center', va='bottom')
        except Exception as e:
            print(f"Warning: Could not create VaR contribution visualizations: {str(e)}")
            # Create empty plots to maintain layout
            fig.add_subplot(3, 3, 3)
            fig.add_subplot(3, 3, 6)
    else:
        # Create empty plots to maintain layout if contributions aren't provided
        fig.add_subplot(3, 3, 3)
        fig.add_subplot(3, 3, 6)
    
    # Adjust spacing
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.suptitle(f"Monte Carlo Value at Risk ({confidence_level*100}%) Analysis", fontsize=16)
    
    return fig

# Main execution block
if __name__ == "__main__":
    # Define portfolio
    tickers = ['SPY', 'IEF', 'GLD']  # S&P 500 ETF, 10-Yr Treasury ETF, Gold ETF
    portfolio_values = [1000000, 500000, 200000]  # $1M in S&P, $500k in Treasuries, $200k in Gold
    
    # Define time period for historical data (typically 1-3 years for daily VaR)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=10*365)).strftime('%Y-%m-%d')  # 3 years of data
    
    # Set parameters
    n_scenarios = 10000
    confidence_level = 0.99
    
    # Calculate VaR using synthetic data since yfinance is not working
    var_value, simulated_returns_df, raw_simulated_returns, simulation_results = monte_carlo_var(
        tickers, portfolio_values, start_date, end_date, n_scenarios, confidence_level, use_synthetic=False
    )
    
    # Get the historical data for visualization
    returns_df, _, _, corr_matrix = get_historical_data(tickers, start_date, end_date, use_synthetic=False)
    
    # Calculate VaR contributions
    var_dollar_contributions, var_pct_contributions = calculate_var_contributions(
        portfolio_values, raw_simulated_returns, var_value, confidence_level
    )
    
    # Print VaR contribution analysis
    print("\nVaR Contribution Analysis:")
    total_portfolio_value = sum(portfolio_values)
    print(f"{'Asset':<8} {'Value ($)':<15} {'Portfolio %':<15} {'VaR Contribution ($)':<20} {'VaR Contribution %':<20}")
    print("-" * 80)
    for i, ticker in enumerate(tickers):
        print(f"{ticker:<8} ${portfolio_values[i]:,.2f} {portfolio_values[i]/total_portfolio_value*100:>13.1f}% ${abs(var_dollar_contributions[i]):>18,.2f} {abs(var_pct_contributions[i])*100:>18.2f}%")
    
    # Visualize results
    fig = visualize_var_results(
        returns_df, corr_matrix, simulated_returns_df, simulation_results, 
        var_value, confidence_level, tickers, portfolio_values,
        var_dollar_contributions, var_pct_contributions
    )
    
    # Print VaR information
    print(f"Portfolio Information:")
    print(f"Total Value: ${total_portfolio_value:,.2f}")
    for i, ticker in enumerate(tickers):
        print(f"  {ticker}: ${portfolio_values[i]:,.2f} ({portfolio_values[i]/total_portfolio_value*100:.1f}%)")
    
    print(f"\n{confidence_level*100}% 1-Day Value at Risk (VaR):")
    print(f"VaR Amount: ${var_value:,.2f}")
    print(f"VaR Percentage: {var_value/total_portfolio_value*100:.2f}%")
    print(f"This means there is a {(1-confidence_level)*100}% chance that the portfolio")
    print(f"will lose more than ${var_value:,.2f} in a single day.")
    
    # Save the plot instead of showing it (useful for non-interactive environments)
    plt.savefig('monte_carlo_var_analysis.png', dpi=300, bbox_inches='tight')
    print("Analysis plot saved as 'monte_carlo_var_analysis.png'")
    
    # Optionally show the plot if in an interactive environment
    plt.show()