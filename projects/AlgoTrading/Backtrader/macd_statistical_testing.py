"""
MACD Strategy Statistical Testing Framework
This script implements various statistical tests to validate the MACD strategy.
It tests hypothesis about signal effectiveness, parameter robustness, and
compares performance against benchmarks with proper statistical rigor.
"""

import backtrader as bt
import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import os
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Import your existing MACD strategy
from macd_strategy import OptimizedMACDStrategy, run_backtest

# Set matplotlib to use Agg backend
import matplotlib
matplotlib.use('Agg')

# Create directory for test results
results_dir = "statistical_test_results"
os.makedirs(results_dir, exist_ok=True)


class BuyAndHoldStrategy(bt.Strategy):
    """Simple Buy and Hold strategy for benchmark comparison"""
    
    def __init__(self):
        self.order = None
        self.buy_price = None
        self.buy_comm = None
        
    def next(self):
        if not self.position:
            self.order = self.buy()


def run_buy_and_hold(ticker, start_date, end_date, initial_cash=10000.0):
    """Run a buy and hold backtest for comparison"""
    cerebro = bt.Cerebro()
    cerebro.addstrategy(BuyAndHoldStrategy)
    
    # Download data
    data_df = yf.download(ticker, start=start_date, end=end_date)
    
    # Handle multi-level columns that might come from yfinance
    if isinstance(data_df.columns, pd.MultiIndex):
        data_df.columns = [col[0].lower() for col in data_df.columns]
    else:
        data_df.columns = [col.lower() for col in data_df.columns]
    
    # Convert to Backtrader data feed
    data = bt.feeds.PandasData(dataname=data_df)
    cerebro.adddata(data)
    
    cerebro.broker.setcash(initial_cash)
    cerebro.broker.setcommission(commission=0.001)
    
    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    
    results = cerebro.run()
    strat = results[0]
    
    # Calculate metrics
    final_value = cerebro.broker.getvalue()
    
    try:
        sharpe_ratio = strat.analyzers.sharpe.get_analysis().get('sharperatio', 0)
        max_drawdown = strat.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0)
        annual_return = strat.analyzers.returns.get_analysis().get('rnorm100', 0)
        
        # Ensure all metrics are numeric values
        sharpe_ratio = 0.0 if sharpe_ratio is None else sharpe_ratio
        max_drawdown = 0.0 if max_drawdown is None else max_drawdown
        annual_return = 0.0 if annual_return is None else annual_return
    except:
        sharpe_ratio, max_drawdown, annual_return = 0.0, 0.0, 0.0
    
    return {
        'final_value': final_value,
        'total_return': (final_value/initial_cash - 1) * 100,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': max_drawdown,
        'annual_return': annual_return
    }


class RandomEntryStrategy(bt.Strategy):
    """Strategy that enters the market randomly but uses the same exit logic as MACD strategy"""
    
    params = (
        ('entry_prob', 0.05),  # Probability of entry on any given day
        ('atr_period', 14),    # ATR period for stops
        ('atr_multiplier', 3), # ATR multiplier for stop loss
        ('take_profit', 0.1),  # Take profit at 10% gain
    )
    
    def __init__(self):
        # Initialize tracking variables
        self.order = None
        self.stop_order = None
        self.buy_price = None
        self.stop_loss = None
        self.take_profit_level = None
        self.position_size = 0
        
        # ATR for stop losses
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)
    
    def next(self):
        # Skip if an order is pending
        if self.order:
            return
            
        if not self.position:
            # Random entry with specified probability
            if random.random() < self.params.entry_prob:
                cash = self.broker.getcash()
                size = int(cash * 0.2 / self.datas[0].close[0])  # Use 20% of cash
                
                if size > 0:
                    self.order = self.buy(size=size)
                    self.buy_price = self.datas[0].close[0]
                    self.position_size = size
                    
                    # Set stop loss based on ATR
                    self.stop_loss = self.buy_price - (self.atr[0] * self.params.atr_multiplier)
                    # Set take profit level
                    self.take_profit_level = self.buy_price * (1 + self.params.take_profit)
                    
                    # Create stop order
                    self.stop_order = self.sell(exectype=bt.Order.Stop, price=self.stop_loss, size=size)
        
        else:
            # Exit logic - same as MACD strategy
            
            # 1. Take profit hit?
            if self.take_profit_level and self.datas[0].close[0] >= self.take_profit_level:
                if self.stop_order:
                    self.cancel(self.stop_order)
                    self.stop_order = None
                self.order = self.sell()
                return
            
            # 2. Manual stop loss check
            if self.stop_loss and self.datas[0].close[0] <= self.stop_loss:
                if self.stop_order:
                    self.cancel(self.stop_order)
                    self.stop_order = None
                self.order = self.sell()
                return
                
            # 3. Time-based exit (exit after 20 bars/days)
            if len(self.position.history) > 20:
                if self.stop_order:
                    self.cancel(self.stop_order)
                    self.stop_order = None
                self.order = self.sell()
                return


def run_random_entry(ticker, start_date, end_date, initial_cash=10000.0, runs=30):
    """Run multiple random entry backtests and return the distribution of results"""
    random_results = []
    
    for i in range(runs):
        cerebro = bt.Cerebro()
        
        # Set a different random seed for each run
        random.seed(42 + i)
        
        cerebro.addstrategy(RandomEntryStrategy)
        
        # Download data
        data_df = yf.download(ticker, start=start_date, end=end_date)
        
        # Handle multi-level columns that might come from yfinance
        if isinstance(data_df.columns, pd.MultiIndex):
            data_df.columns = [col[0].lower() for col in data_df.columns]
        else:
            data_df.columns = [col.lower() for col in data_df.columns]
        
        # Convert to Backtrader data feed
        data = bt.feeds.PandasData(dataname=data_df)
        cerebro.adddata(data)
        
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=0.001)
        
        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
        
        results = cerebro.run()
        strat = results[0]
        
        final_value = cerebro.broker.getvalue()
        
        try:
            sharpe_ratio = strat.analyzers.sharpe.get_analysis().get('sharperatio', 0)
            max_drawdown = strat.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0)
            annual_return = strat.analyzers.returns.get_analysis().get('rnorm100', 0)
            
            sharpe_ratio = 0.0 if sharpe_ratio is None else sharpe_ratio
            max_drawdown = 0.0 if max_drawdown is None else max_drawdown
            annual_return = 0.0 if annual_return is None else annual_return
        except:
            sharpe_ratio, max_drawdown, annual_return = 0.0, 0.0, 0.0
        
        random_results.append({
            'run': i,
            'final_value': final_value,
            'total_return': (final_value/initial_cash - 1) * 100,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'annual_return': annual_return
        })
    
    return random_results


def generate_random_parameters():
    """Generate random MACD parameters within typical ranges"""
    fast = random.randint(8, 20)
    slow = random.randint(fast + 4, 34)  # Ensure slow > fast
    signal = random.randint(7, 13)
    atr_mult = round(random.uniform(2.0, 4.0), 1)
    
    return {
        'macd_fast': fast,
        'macd_slow': slow,
        'macd_signal': signal,
        'atr_multiplier': atr_mult
    }


def bootstrap_performance(returns, n_samples=1000):
    """
    Perform bootstrap resampling to generate confidence intervals for performance metrics
    
    Args:
        returns: pandas.Series of strategy returns
        n_samples: number of bootstrap samples
        
    Returns:
        dict: Confidence intervals for Sharpe ratio and annualized return
    """
    # Make sure returns is a numpy array
    returns_array = np.array(returns)
    
    # Initialize lists to store bootstrap statistics
    sharpe_ratios = []
    annual_returns = []
    
    # Create bootstrap samples
    for _ in range(n_samples):
        # Sample with replacement
        sample_idx = np.random.choice(len(returns_array), size=len(returns_array), replace=True)
        sample = returns_array[sample_idx]
        
        # Calculate statistics
        mean_return = np.mean(sample)
        std_return = np.std(sample)
        
        # Compute Sharpe ratio (annualized, assuming daily returns)
        sharpe = (mean_return / std_return) * np.sqrt(252) if std_return > 0 else 0
        
        # Compute annualized return
        annual_return = ((1 + mean_return) ** 252 - 1) * 100
        
        sharpe_ratios.append(sharpe)
        annual_returns.append(annual_return)
    
    # Compute confidence intervals (95%)
    sharpe_ci = (np.percentile(sharpe_ratios, 2.5), np.percentile(sharpe_ratios, 97.5))
    returns_ci = (np.percentile(annual_returns, 2.5), np.percentile(annual_returns, 97.5))
    
    return {
        'sharpe_ratio_ci': sharpe_ci,
        'annual_return_ci': returns_ci,
        'sharpe_mean': np.mean(sharpe_ratios),
        'annual_return_mean': np.mean(annual_returns)
    }


def test_significance_against_random(strategy_perf, random_perfs, metric='sharpe_ratio'):
    """
    Test if strategy performance is significantly better than random entries
    
    Args:
        strategy_perf: float, performance metric of the strategy
        random_perfs: list, performance metrics from random strategies
        metric: str, the metric to compare
        
    Returns:
        float: p-value of the test
        bool: True if strategy is significantly better
    """
    # Extract the specific metric from random performances
    random_metrics = [r[metric] for r in random_perfs]
    
    # Calculate the percentile rank of the strategy's performance
    percentile = stats.percentileofscore(random_metrics, strategy_perf)
    
    # Convert to p-value (one-tailed test)
    p_value = 1 - (percentile / 100)
    
    # Significant if p < 0.05 (95th percentile or higher)
    is_significant = p_value < 0.05
    
    return p_value, is_significant


def test_parameter_robustness(ticker, start_date, end_date, optimal_params, n_random=50):
    """
    Test if optimized parameters are significantly better than random parameters
    
    Args:
        ticker: str, the stock ticker
        start_date, end_date: str, date range for testing
        optimal_params: dict, optimized parameters
        n_random: int, number of random parameter sets to test
        
    Returns:
        dict: Test results including p-value and parameter stability metrics
    """
    # Run backtest with optimal parameters
    optimal_results = run_backtest(
        ticker=ticker,
        start_date=start_date,
        end_date=end_date,
        macd_fast=optimal_params['macd_fast'],
        macd_slow=optimal_params['macd_slow'],
        macd_signal=optimal_params['macd_signal'],
        atr_multiplier=optimal_params['atr_multiplier'],
        initial_cash=10000.0,
        verbose=False,
        plot=False
    )
    
    if not optimal_results:
        return {"error": "Could not run backtest with optimal parameters"}
    
    # Get performance with random parameters
    random_performances = []
    random_params_list = []
    
    for i in range(n_random):
        random_params = generate_random_parameters()
        random_params_list.append(random_params)
        
        results = run_backtest(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date,
            macd_fast=random_params['macd_fast'],
            macd_slow=random_params['macd_slow'],
            macd_signal=random_params['macd_signal'],
            atr_multiplier=random_params['atr_multiplier'],
            initial_cash=10000.0,
            verbose=False,
            plot=False
        )
        
        if results:
            random_performances.append({
                'params': random_params,
                'sharpe_ratio': results['sharpe_ratio'],
                'annual_return': results['annual_return'],
                'max_drawdown': results['max_drawdown']
            })
    
    # Extract the performance metrics
    random_sharpes = [p['sharpe_ratio'] for p in random_performances]
    random_returns = [p['annual_return'] for p in random_performances]
    
    # Calculate percentile rank and p-value for each metric
    sharpe_percentile = stats.percentileofscore(random_sharpes, optimal_results['sharpe_ratio'])
    returns_percentile = stats.percentileofscore(random_returns, optimal_results['annual_return'])
    
    sharpe_p_value = 1 - (sharpe_percentile / 100)
    returns_p_value = 1 - (returns_percentile / 100)
    
    # Plot the distribution of random parameters vs. optimal
    fig = Figure(figsize=(12, 8))
    canvas = FigureCanvas(fig)
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    
    # Sharpe ratio distribution
    ax1.hist(random_sharpes, bins=10, alpha=0.7)
    ax1.axvline(optimal_results['sharpe_ratio'], color='red', linestyle='dashed', 
                linewidth=2, label=f'Optimal: {optimal_results["sharpe_ratio"]:.3f}')
    ax1.set_title('Distribution of Sharpe Ratios with Random Parameters')
    ax1.set_xlabel('Sharpe Ratio')
    ax1.set_ylabel('Frequency')
    ax1.legend()
    
    # Annual return distribution
    ax2.hist(random_returns, bins=10, alpha=0.7)
    ax2.axvline(optimal_results['annual_return'], color='red', linestyle='dashed', 
                linewidth=2, label=f'Optimal: {optimal_results["annual_return"]:.2f}%')
    ax2.set_title('Distribution of Annual Returns with Random Parameters')
    ax2.set_xlabel('Annual Return (%)')
    ax2.set_ylabel('Frequency')
    ax2.legend()
    
    fig.tight_layout()
    fig.savefig(f"{results_dir}/parameter_robustness_{ticker}_{start_date}_{end_date}.png")
    
    return {
        'sharpe_percentile': sharpe_percentile,
        'sharpe_p_value': sharpe_p_value,
        'returns_percentile': returns_percentile,
        'returns_p_value': returns_p_value,
        'is_sharpe_significant': sharpe_p_value < 0.05,
        'is_returns_significant': returns_p_value < 0.05,
        'optimal_params': optimal_params,
        'random_params_count': len(random_performances),
        'plot_path': f"{results_dir}/parameter_robustness_{ticker}_{start_date}_{end_date}.png"
    }


def extract_strategy_returns(ticker, start_date, end_date, params):
    """Extract daily returns from strategy for further statistical analysis"""
    # Download price data
    data_df = yf.download(ticker, start=start_date, end=end_date)
    
    # Handle multi-level columns that might come from yfinance
    if isinstance(data_df.columns, pd.MultiIndex):
        data_df.columns = [col[0].lower() for col in data_df.columns]
    else:
        data_df.columns = [col.lower() for col in data_df.columns]
    
    # Create a Cerebro instance
    cerebro = bt.Cerebro(stdstats=False)  # Don't plot standard statistics
    
    # Add the MACD strategy
    cerebro.addstrategy(
        OptimizedMACDStrategy,
        macd_fast=params['macd_fast'],
        macd_slow=params['macd_slow'],
        macd_signal=params['macd_signal'],
        atr_multiplier=params['atr_multiplier'],
        verbose=False
    )
    
    # Add the data
    data = bt.feeds.PandasData(dataname=data_df)
    cerebro.adddata(data)
    
    # Set broker parameters
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.001)
    
    # Add analyzers to track daily returns
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='daily_returns', timeframe=bt.TimeFrame.Days)
    
    # Run the strategy
    results = cerebro.run()
    
    # Get the first strategy from results
    strategy = results[0]
    
    # Get daily returns as a Series
    try:
        daily_returns = pd.Series(strategy.analyzers.daily_returns.get_analysis())
        daily_returns = daily_returns.fillna(0)  # Fill any missing days with 0
        return daily_returns
    except Exception as e:
        print(f"Error extracting returns: {e}")
        return pd.Series()


def comparative_analysis(ticker, start_date, end_date, train_end_date, optimal_params):
    """
    Perform comparative analysis between MACD strategy, buy-and-hold, and random entry
    
    Args:
        ticker: str, the stock ticker
        start_date: str, start date for analysis
        end_date: str, end date for analysis
        train_end_date: str, end date of training period
        optimal_params: dict, optimized parameters from training period
    """
    print(f"\n{'='*60}")
    print(f"COMPARATIVE STATISTICAL ANALYSIS FOR {ticker}")
    print(f"{'='*60}")
    print(f"Training period: {start_date} to {train_end_date}")
    print(f"Testing period: {train_end_date} to {end_date}")
    print(f"Optimal parameters: {optimal_params}")
    print(f"{'-'*60}")
    
    # 1. Run the optimized MACD strategy on the testing period
    macd_results = run_backtest(
        ticker=ticker,
        start_date=train_end_date,
        end_date=end_date,
        macd_fast=optimal_params['macd_fast'],
        macd_slow=optimal_params['macd_slow'],
        macd_signal=optimal_params['macd_signal'],
        atr_multiplier=optimal_params['atr_multiplier'],
        initial_cash=10000.0,
        verbose=False,
        plot=False
    )
    
    if not macd_results:
        print("Error: Could not run MACD strategy backtest")
        return
    
    # 2. Run buy-and-hold for the same period
    buyhold_results = run_buy_and_hold(ticker, train_end_date, end_date)
    
    # 3. Run random entry strategy multiple times
    print("Running random entry tests (this might take a while)...")
    random_results = run_random_entry(ticker, train_end_date, end_date, runs=30)
    
    # 4. Extract daily returns for bootstrap analysis
    print("Extracting daily returns for bootstrap analysis...")
    daily_returns = extract_strategy_returns(ticker, train_end_date, end_date, optimal_params)
    
    if len(daily_returns) > 0:
        # 5. Perform bootstrap analysis
        bootstrap_results = bootstrap_performance(daily_returns)
        
        print(f"\nBOOTSTRAP ANALYSIS (95% Confidence Intervals):")
        print(f"Sharpe Ratio: {bootstrap_results['sharpe_ratio_ci'][0]:.3f} to {bootstrap_results['sharpe_ratio_ci'][1]:.3f}")
        print(f"Annual Return: {bootstrap_results['annual_return_ci'][0]:.2f}% to {bootstrap_results['annual_return_ci'][1]:.2f}%")
    else:
        print("Unable to perform bootstrap analysis due to missing return data")
    
    # 6. Test if MACD outperforms random entry
    print("\nCOMPARISON TO RANDOM ENTRY:")
    random_sharpes = [r['sharpe_ratio'] for r in random_results]
    sharpe_p_value, sharpe_significant = test_significance_against_random(
        macd_results['sharpe_ratio'], random_results
    )
    
    print(f"MACD Sharpe Ratio: {macd_results['sharpe_ratio']:.3f}")
    print(f"Random Entries Avg Sharpe: {np.mean(random_sharpes):.3f}")
    print(f"P-value: {sharpe_p_value:.4f} - {'Significant' if sharpe_significant else 'Not Significant'}")
    
    # 7. Compare to buy-and-hold
    print("\nCOMPARISON TO BUY-AND-HOLD:")
    print(f"MACD Total Return: {macd_results['total_return']:.2f}%")
    print(f"Buy & Hold Total Return: {buyhold_results['total_return']:.2f}%")
    print(f"MACD Sharpe Ratio: {macd_results['sharpe_ratio']:.3f}")
    print(f"Buy & Hold Sharpe Ratio: {buyhold_results['sharpe_ratio']:.3f}")
    
    # 8. Test parameter robustness
    print("\nPARAMETER ROBUSTNESS TESTING:")
    print("Testing if optimized parameters are significantly better than random parameters...")
    robustness_results = test_parameter_robustness(
        ticker, train_end_date, end_date, optimal_params, n_random=30
    )
    
    if 'error' not in robustness_results:
        print(f"Optimal parameters perform better than {robustness_results['sharpe_percentile']:.1f}% of random parameters")
        print(f"Sharpe ratio p-value: {robustness_results['sharpe_p_value']:.4f}")
        print(f"Statistical significance: {'Yes' if robustness_results['is_sharpe_significant'] else 'No'}")
        print(f"Parameter robustness plot saved to: {robustness_results['plot_path']}")
    else:
        print(f"Error in robustness testing: {robustness_results['error']}")
    
    # 9. Create a summary visualization
    performance_metrics = {
        'MACD Strategy': {
            'Total Return': macd_results['total_return'],
            'Sharpe Ratio': macd_results['sharpe_ratio'],
            'Max Drawdown': macd_results['max_drawdown']
        },
        'Buy and Hold': {
            'Total Return': buyhold_results['total_return'],
            'Sharpe Ratio': buyhold_results['sharpe_ratio'],
            'Max Drawdown': buyhold_results['max_drawdown']
        },
        'Random Entry (Avg)': {
            'Total Return': np.mean([r['total_return'] for r in random_results]),
            'Sharpe Ratio': np.mean([r['sharpe_ratio'] for r in random_results]),
            'Max Drawdown': np.mean([r['max_drawdown'] for r in random_results])
        }
    }
    
    # Create summary plot
    fig = Figure(figsize=(12, 10))
    canvas = FigureCanvas(fig)
    
    # Plot metrics comparison
    metrics = ['Total Return', 'Sharpe Ratio', 'Max Drawdown']
    strategies = list(performance_metrics.keys())
    
    for i, metric in enumerate(metrics):
        ax = fig.add_subplot(3, 1, i+1)
        values = [performance_metrics[strat][metric] for strat in strategies]
        
        bars = ax.bar(strategies, values)
        ax.set_title(f'Comparison of {metric}')
        ax.set_ylabel(metric)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            formatter = '{:.2f}%' if metric == 'Total Return' else '{:.3f}'
            ax.annotate(formatter.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    fig.tight_layout()
    summary_plot_path = f"{results_dir}/strategy_comparison_{ticker}_{train_end_date}_{end_date}.png"
    fig.savefig(summary_plot_path)
    print(f"\nSummary comparison plot saved to: {summary_plot_path}")
    
    # Save detailed results to CSV
    summary_df = pd.DataFrame({
        'Metric': [
            'Total Return (%)', 'Sharpe Ratio', 'Max Drawdown (%)',
            'Statistical Significance vs Random (p-value)',
            'Outperforms Buy & Hold', 'Parameter Robustness (percentile)'
        ],
        'Value': [
            f"{macd_results['total_return']:.2f}",
            f"{macd_results['sharpe_ratio']:.3f}",
            f"{macd_results['max_drawdown']:.2f}",
            f"{sharpe_p_value:.4f} ({'Significant' if sharpe_significant else 'Not Significant'})",
            f"{'Yes' if macd_results['sharpe_ratio'] > buyhold_results['sharpe_ratio'] else 'No'}",
            f"{robustness_results.get('sharpe_percentile', 'N/A'):.1f}%"
        ]
    })
    
    summary_csv_path = f"{results_dir}/statistical_summary_{ticker}_{train_end_date}_{end_date}.csv"
    summary_df.to_csv(summary_csv_path, index=False)
    print(f"Detailed statistical summary saved to: {summary_csv_path}")


def run_macd_hypothesis_testing():
    """Main function to run all statistical tests on the MACD strategy"""
    ticker = 'SPY'
    train_start_date = '2018-01-01'
    train_end_date = '2022-12-31'
    test_end_date = '2024-12-31'
    
    print(f"Running MACD Strategy Statistical Testing for {ticker}")
    print(f"Training period: {train_start_date} to {train_end_date}")
    print(f"Testing period: {train_end_date} to {test_end_date}")
    
    # 1. First, run optimization on the training data to get the best parameters
    print("\nOptimizing MACD parameters on training data...")
    
    # Run optimization on training period
    best_params, all_results = optimize_macd_strategy(
        ticker=ticker,
        start_date=train_start_date,
        end_date=train_end_date,
        fast_range=(8, 20),
        slow_range=(18, 32),
        signal_range=(7, 13),
        atr_mult_range=(2.0, 4.0),
        initial_cash=10000.0
    )
    
    # 2. Perform statistical analysis on the testing period
    print("\nPerforming statistical analysis on the test data...")
    comparative_analysis(
        ticker=ticker,
        start_date=train_start_date,
        end_date=test_end_date,
        train_end_date=train_end_date,
        optimal_params=best_params
    )
    
    print("\nMACD Strategy Statistical Testing Complete!")


if __name__ == "__main__":
    # Import the optimize_macd_strategy function - replace this with your import
    from macd_strategy import optimize_macd_strategy
    
    # Run all tests
    run_macd_hypothesis_testing()
