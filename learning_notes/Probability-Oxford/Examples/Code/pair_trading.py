import yfinance as yf
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.tsa.stattools import coint
from datetime import datetime, timedelta

class PairsTrader:
    def __init__(self, symbol_A, symbol_B, start_date, end_date, window=60, z_threshold=2.0, stop_loss=0.1):
        """
        Initialize the pairs trading strategy with enhanced visualization settings.
        The visualization style is configured to create professional, easy-to-read plots
        using a combination of matplotlib and seaborn settings.
        """
        self.symbol_A = symbol_A
        self.symbol_B = symbol_B
        self.start_date = start_date
        self.end_date = end_date
        self.window = window
        self.z_threshold = z_threshold
        self.stop_loss = stop_loss
        self.data = None
        self.results = None
        
        # Configure plotting style for professional visualizations
        plt.style.use('default')  # Reset to default style
        
        # Set up custom style parameters
        plt.rcParams.update({
            'figure.facecolor': 'white',
            'axes.facecolor': 'white',
            'axes.grid': True,
            'grid.alpha': 0.3,
            'grid.linestyle': '--',
            'axes.labelsize': 10,
            'axes.titlesize': 12,
            'xtick.labelsize': 9,
            'ytick.labelsize': 9,
            'lines.linewidth': 1.5,
            'font.family': 'sans-serif'
        })
        
        # Configure seaborn for enhanced statistical visualizations
        sns.set_theme(style="whitegrid", palette="husl")
        sns.set_context("notebook", font_scale=1.1)

    def fetch_data(self):
        """
        Fetch historical price data for both stocks using Yahoo Finance API.
        This method implements careful data validation and preprocessing to ensure
        we have clean, aligned price data for our pairs trading strategy.
        """
        try:
            print(f"\nFetching data for {self.symbol_A} and {self.symbol_B}...")
            
            # First, let's download the data with proper error catching
            stock_A = yf.download(self.symbol_A, start=self.start_date, end=self.end_date)
            stock_B = yf.download(self.symbol_B, start=self.start_date, end=self.end_date)
            
            # Let's first check if we received any data
            if stock_A.empty or stock_B.empty:
                raise ValueError(f"No data received for {self.symbol_A} or {self.symbol_B}")
            
            # Let's check what columns we have available
            print(f"\nColumns available:")
            print(f"{self.symbol_A}: {stock_A.columns.tolist()}")
            print(f"{self.symbol_B}: {stock_B.columns.tolist()}")
            
            # Choose the appropriate price column (Close is more reliable for pairs trading)
            price_col = 'Close'
            
            # Here's the key fix: We need to maintain the index when creating the DataFrame
            self.data = pd.DataFrame(index=stock_A.index)
            self.data[f'{self.symbol_A}_price'] = stock_A[price_col]
            self.data[f'{self.symbol_B}_price'] = stock_B[price_col]
            
            # Handle any missing values
            missing_count = self.data.isnull().sum()
            if missing_count.any():
                print(f"\nWarning: Found missing values:\n{missing_count}")
                self.data = self.data.dropna()
                print("Missing values have been removed.")
            
            # Validate we have enough data for our analysis window
            if len(self.data) < self.window:
                raise ValueError(
                    f"Insufficient data points ({len(self.data)}) "
                    f"for analysis window ({self.window})"
                )
            
            # Print useful summary statistics
            print("\nData Summary:")
            print(f"Start Date: {self.data.index[0]}")
            print(f"End Date: {self.data.index[-1]}")
            print(f"Trading Days: {len(self.data)}")
            print(f"\nPrice Statistics:")
            print(self.data.describe())
            
            return self.data
            
        except Exception as e:
            print(f"\nDetailed error information:")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            raise RuntimeError(f"Error fetching data: {str(e)}")
            
        except Exception as e:
            raise RuntimeError(f"Error fetching data: {str(e)}")

    def calculate_spread(self):
        """
        Calculate the spread and z-score with enhanced statistical robustness.
        """
        price_A = self.data[f'{self.symbol_A}_price']
        price_B = self.data[f'{self.symbol_B}_price']
        
        # Perform cointegration test for pair validation
        try:
            # The coint function returns: test statistic, p-value, and critical values
            coint_stat, p_value, critical_values = coint(price_A, price_B)
            print(f"\nCointegration Analysis:")
            print(f"Test Statistic: {coint_stat:.4f}")
            print(f"P-value: {p_value:.4f}")
            print("Critical Values:")
            print(f"1%: {critical_values[0]:.4f}")
            print(f"5%: {critical_values[1]:.4f}")
            print(f"10%: {critical_values[2]:.4f}")
            
            if p_value > 0.05:
                print("\nWarning: Pair may not be cointegrated (p-value > 0.05)")
                print("This means the spread might not be mean-reverting")
            else:
                print("\nPair shows evidence of cointegration")
                
        except Exception as e:
            print(f"\nWarning: Could not perform cointegration test: {str(e)}")
            print("Proceeding with analysis, but results may be less reliable")
        
        # Calculate hedge ratio using rolling OLS
        rolling_hedge_ratio = (
            price_A.rolling(window=self.window)
            .cov(price_B) / price_B.rolling(window=self.window).var()
        )
        
        # Calculate spread using dynamic hedge ratio
        spread = price_A - rolling_hedge_ratio * price_B
        
        # Calculate z-score with enhanced robustness
        rolling_mean = spread.rolling(window=self.window, min_periods=self.window).mean()
        rolling_std = spread.rolling(window=self.window, min_periods=self.window).std()
        
        # Use robust statistics for outlier resistance
        zscore = stats.mstats.winsorize(
            (spread - rolling_mean) / rolling_std,
            limits=[0.05, 0.05]  # 5% winsorization
        )
        
        return spread, pd.Series(zscore, index=spread.index)

    def generate_signals(self):
        """
        Generate trading signals with position sizing and risk management.
        """
        spread, zscore = self.calculate_spread()
        signals = pd.DataFrame(index=self.data.index)
        
        # Generate basic position signals
        signals['position'] = np.where(zscore > self.z_threshold, -1,
                            np.where(zscore < -self.z_threshold, 1, 0))
        
        # Add stop-loss logic
        returns = spread.pct_change()
        cumulative_returns = (1 + returns).cumprod()
        drawdown = cumulative_returns / cumulative_returns.cummax() - 1
        
        # Apply stop-loss
        signals['position'] = np.where(
            drawdown < -self.stop_loss,
            0,  # Close position if stop-loss is hit
            signals['position']
        )
        
        # Position sizing based on z-score magnitude
        signals['position_size'] = np.minimum(
            np.abs(zscore) / self.z_threshold,
            1.0
        ) * np.sign(signals['position'])
        
        signals['spread'] = spread
        signals['zscore'] = zscore
        
        return signals

    def calculate_returns(self, signals, initial_capital=100000):
        """
        Calculate strategy returns with transaction costs and enhanced metrics.
        """
        price_A = self.data[f'{self.symbol_A}_price']
        price_B = self.data[f'{self.symbol_B}_price']
        
        # Include transaction costs
        transaction_cost = 0.001  # 10 bps per trade
        position_changes = signals['position'].diff().fillna(0)
        transaction_costs = abs(position_changes) * transaction_cost
        
        # Calculate returns with position sizing
        returns_A = price_A.pct_change().fillna(0)
        returns_B = price_B.pct_change().fillna(0)
        
        strategy_returns = (
            signals['position_size'].shift(1) * (returns_A - returns_B) -
            transaction_costs
        ).fillna(0)  # Fill NaN values with 0 for first day
        
        # Calculate portfolio value using cumulative product
        portfolio_value = initial_capital * (1 + strategy_returns).cumprod()
        
        # Calculate performance metrics
        trading_days = 252
        returns_mean = strategy_returns.mean()
        returns_std = strategy_returns.std()
        
        # Calculate Sharpe and Sortino ratios
        sharpe_ratio = np.sqrt(trading_days) * returns_mean / returns_std if returns_std != 0 else 0
        negative_returns = strategy_returns[strategy_returns < 0]
        sortino_ratio = (np.sqrt(trading_days) * returns_mean / negative_returns.std() 
                        if len(negative_returns) > 0 and negative_returns.std() != 0 else 0)
        
        # Calculate drawdown using proper indexing
        max_drawdown = (portfolio_value / portfolio_value.expanding().max() - 1).min()
        
        # Calculate win rate and other metrics
        winning_days = (strategy_returns > 0).sum()
        total_trading_days = (strategy_returns != 0).sum()
        win_rate = winning_days / total_trading_days if total_trading_days > 0 else 0
        
        # Store results using proper pandas indexing
        self.results = {
            'returns': strategy_returns,
            'portfolio_value': portfolio_value,
            'sharpe_ratio': sharpe_ratio,
            'sortino_ratio': sortino_ratio,
            'max_drawdown': max_drawdown,
            'signals': signals,
            'total_trades': abs(position_changes).sum() / 2,
            'win_rate': win_rate,
            'final_return': (portfolio_value.iloc[-1] / portfolio_value.iloc[0]) - 1  # Using proper indexing
        }
        
        return self.results

    def plot_results(self):
        """
        Create enhanced visualizations with improved styling and metrics display.
        """
        if self.results is None:
            raise ValueError("Run the strategy first using run_strategy()")
        
        signals = self.results['signals']
        
        # Create figure with custom style
        fig = plt.figure(figsize=(15, 25))
        gs = fig.add_gridspec(5, 1, height_ratios=[2, 1.5, 1, 1.5, 1.5])
        
        # Plot 1: Price Series
        ax1 = fig.add_subplot(gs[0])
        price_A = self.data[f'{self.symbol_A}_price'] / self.data[f'{self.symbol_A}_price'].iloc[0]
        price_B = self.data[f'{self.symbol_B}_price'] / self.data[f'{self.symbol_B}_price'].iloc[0]
        
        ax1.plot(price_A, label=f'{self.symbol_A} (Normalized)', linewidth=1.5)
        ax1.plot(price_B, label=f'{self.symbol_B} (Normalized)', linewidth=1.5)
        ax1.set_title('Normalized Stock Prices', fontsize=12, pad=15)
        ax1.legend(loc='upper left', frameon=True)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Spread and Z-score
        ax2 = fig.add_subplot(gs[1])
        ax2.plot(signals['spread'], label='Spread', color='blue', alpha=0.7)
        ax2.set_title('Price Spread', fontsize=12, pad=15)
        ax2.grid(True, alpha=0.3)
        
        ax2_twin = ax2.twinx()
        ax2_twin.plot(signals['zscore'], label='Z-Score', color='red', linestyle='--')
        ax2_twin.axhline(self.z_threshold, color='red', alpha=0.3)
        ax2_twin.axhline(-self.z_threshold, color='red', alpha=0.3)
        ax2_twin.set_ylabel('Z-Score', color='red')
        
        # Plot 3: Trading Positions
        ax3 = fig.add_subplot(gs[2])
        ax3.plot(signals['position_size'], color='green', label='Position Size')
        ax3.set_title('Trading Positions', fontsize=12, pad=15)
        ax3.set_ylabel('Position Size')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Cumulative Returns
        ax4 = fig.add_subplot(gs[3])
        cumulative_returns = (1 + self.results['returns']).cumprod()
        ax4.plot(cumulative_returns, color='blue', linewidth=1.5)
        ax4.set_title('Cumulative Returns', fontsize=12, pad=15)
        ax4.grid(True, alpha=0.3)
        
        # Plot 5: Drawdown
        ax5 = fig.add_subplot(gs[4])
        drawdown = cumulative_returns / cumulative_returns.cummax() - 1
        ax5.fill_between(drawdown.index, drawdown, 0, color='red', alpha=0.3)
        ax5.set_title('Drawdown', fontsize=12, pad=15)
        ax5.grid(True, alpha=0.3)
        
        # Add strategy metrics as text
        metrics_text = (
            f"Sharpe Ratio: {self.results['sharpe_ratio']:.2f}\n"
            f"Sortino Ratio: {self.results['sortino_ratio']:.2f}\n"
            f"Max Drawdown: {self.results['max_drawdown']:.2%}\n"
            f"Win Rate: {self.results['win_rate']:.2%}\n"
            f"Total Trades: {int(self.results['total_trades'])}"
        )
        
        fig.text(0.15, 0.02, metrics_text, fontsize=10, 
                bbox=dict(facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        # Create directory structure for figures
        figures_dir = "Figures"
        if not os.path.exists(figures_dir):
            os.makedirs(figures_dir)
            print(f"\nCreated main figures directory: {figures_dir}")

        # Create pair-specific directory with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        pair_dir = os.path.join(figures_dir, f"{self.symbol_A}_{self.symbol_B}")
        if not os.path.exists(pair_dir):
            os.makedirs(pair_dir)
            print(f"Created pair-specific directory: {pair_dir}")

        # Save the main strategy figure
        strategy_file = os.path.join(pair_dir, f"strategy_summary_{timestamp}.png")
        plt.savefig(strategy_file, dpi=300, bbox_inches='tight')
        print(f"Saved strategy summary: {strategy_file}")

        # Create and save correlation plot
        plt.figure(figsize=(8, 6))
        corr_data = pd.DataFrame({
            self.symbol_A: self.data[f'{self.symbol_A}_price'],
            self.symbol_B: self.data[f'{self.symbol_B}_price']
        })
        sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title(f'Correlation Matrix: {self.symbol_A} vs {self.symbol_B}')

        corr_file = os.path.join(pair_dir, f"correlation_{timestamp}.png")
        plt.savefig(corr_file, dpi=300, bbox_inches='tight')
        print(f"Saved correlation plot: {corr_file}")
        plt.close()

        # Create and save returns distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(self.results['returns'], kde=True, bins=50)
        plt.title('Strategy Returns Distribution')
        plt.xlabel('Return')
        plt.ylabel('Frequency')

        returns_file = os.path.join(pair_dir, f"returns_distribution_{timestamp}.png")
        plt.savefig(returns_file, dpi=300, bbox_inches='tight')
        print(f"Saved returns distribution: {returns_file}")
        plt.close()

        # Show the plots interactively
        plt.show()

        return pair_dir  # Return the directory path for reference
        

    def run_strategy(self, initial_capital=100000):
        """
        Run the complete trading strategy with enhanced reporting.
        """
        if self.data is None:
            self.fetch_data()
        
        signals = self.generate_signals()
        results = self.calculate_returns(signals, initial_capital)
        self.plot_results()
        
        # Print detailed performance report
        print("\nStrategy Performance Report")
        print("=" * 40)
        print(f"Total Return: {(results['portfolio_value'][-1] / results['portfolio_value'][0] - 1):.2%}")
        print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
        print(f"Sortino Ratio: {results['sortino_ratio']:.2f}")
        print(f"Max Drawdown: {results['max_drawdown']:.2%}")
        print(f"Win Rate: {results['win_rate']:.2%}")
        print(f"Total Trades: {int(results['total_trades'])}")
        print("=" * 40)
        
        return results

if __name__ == "__main__":
    # Define pairs with stronger theoretical relationships
    pairs = [
        ('XLE', 'USO'),    # Energy sector ETF vs Oil ETF
        ('GDX', 'GLD'),    # Gold miners vs Gold
        ('XLF', 'VFH'),    # Financial sector ETFs
        ('QQQ', 'SPY'),    # Tech vs S&P 500
        ('KO', 'PEP'),
        ('JPM', 'BAC'),
        ('CVX', 'XOM')
        
    ]
    
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    
    results_summary = []
    
    for symbol_A, symbol_B in pairs:
        try:
            print(f"\nAnalyzing pair: {symbol_A} - {symbol_B}")
            trader = PairsTrader(
                symbol_A,
                symbol_B,
                start_date,
                end_date,
                window=30,          # Shorter window for ETF pairs
                z_threshold=1.5,    # Lower threshold for more frequent trading
                stop_loss=0.05      # Tighter stop-loss for ETFs
            )
            
            # Run strategy and collect results
            results = trader.run_strategy(initial_capital=100000)
            
            # Calculate additional pair-specific metrics
            returns = results['returns']
            total_return = results['final_return']  # Using the new metric
            
            # Calculate annualized return properly
            total_days = len(returns)
            annualized_return = (1 + total_return) ** (252/total_days) - 1
            
            # Store results with proper numerical values
            pair_results = {
                'pair': f'{symbol_A}-{symbol_B}',
                'total_return': total_return,
                'annualized_return': annualized_return,
                'sharpe_ratio': results['sharpe_ratio'],
                'sortino_ratio': results['sortino_ratio'],
                'max_drawdown': results['max_drawdown'],
                'win_rate': results['win_rate'],
                'total_trades': int(results['total_trades']),
                'avg_trade_duration': total_days / results['total_trades'] if results['total_trades'] > 0 else 0,
                'profit_factor': abs(returns[returns > 0].sum() / returns[returns < 0].sum()) if len(returns[returns < 0]) > 0 else 0
            }
            
            results_summary.append(pair_results)
            
            # Format display values properly
            print(f"\nDetailed Results for {symbol_A}-{symbol_B}:")
            print("=" * 60)
            print(f"Total Return: {total_return:.2%}")
            print(f"Annualized Return: {annualized_return:.2%}")
            print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
            print(f"Sortino Ratio: {results['sortino_ratio']:.2f}")
            print(f"Max Drawdown: {results['max_drawdown']:.2%}")
            print(f"Win Rate: {results['win_rate']:.2%}")
            print(f"Total Trades: {int(results['total_trades'])}")
            print(f"Avg Trade Duration: {total_days / results['total_trades']:.1f} days" if results['total_trades'] > 0 else "Avg Trade Duration: N/A")
            print(f"Profit Factor: {abs(returns[returns > 0].sum() / returns[returns < 0].sum()):.2f}" if len(returns[returns < 0]) > 0 else "Profit Factor: N/A")
            print("=" * 60)
            
        except Exception as e:
            print(f"Error analyzing {symbol_A}-{symbol_B}: {str(e)}")
            continue
    
    # Create comprehensive summary DataFrame
    summary_df = pd.DataFrame(results_summary)
    
    # Calculate aggregate statistics
    print("\nAggregate Strategy Performance")
    print("=" * 80)
    print("Average Performance Metrics Across All Pairs:")
    
    metrics_to_analyze = [
        ('total_return', 'Total Return'),
        ('sharpe_ratio', 'Sharpe Ratio'),
        ('sortino_ratio', 'Sortino Ratio'),
        ('win_rate', 'Win Rate')
    ]
    
    for column, display_name in metrics_to_analyze:
        values = summary_df[column].values
        mean_value = np.mean(values)
        std_value = np.std(values)
        print(f"{display_name}:")
        print(f"  Mean: {mean_value:.2%}")
        print(f"  Std Dev: {std_value:.2%}")
    
    # Save detailed results with formatted columns
    summary_df_display = summary_df.copy()
    summary_df_display['total_return'] = summary_df_display['total_return'].map('{:.2%}'.format)
    summary_df_display['annualized_return'] = summary_df_display['annualized_return'].map('{:.2%}'.format)
    summary_df_display['sharpe_ratio'] = summary_df_display['sharpe_ratio'].map('{:.2f}'.format)
    summary_df_display['sortino_ratio'] = summary_df_display['sortino_ratio'].map('{:.2f}'.format)
    summary_df_display['max_drawdown'] = summary_df_display['max_drawdown'].map('{:.2%}'.format)
    summary_df_display['win_rate'] = summary_df_display['win_rate'].map('{:.2%}'.format)
    summary_df_display['avg_trade_duration'] = summary_df_display['avg_trade_duration'].map('{:.1f}'.format)
    summary_df_display['profit_factor'] = summary_df_display['profit_factor'].map('{:.2f}'.format)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_filename = f'pairs_trading_results_{timestamp}.csv'
    summary_df_display.to_csv(results_filename, index=False)
    
    print("\nDetailed Results Summary:")
    print("=" * 80)
    print(summary_df_display.to_string(index=False))
    print("\nResults have been saved to:", results_filename)
    
    # Plot aggregate performance comparison
    plt.figure(figsize=(12, 6))
    plt.bar(summary_df['pair'], summary_df['total_return'] * 100)
    plt.title('Total Returns by Pair')
    plt.xlabel('Pairs')
    plt.ylabel('Total Return (%)')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()