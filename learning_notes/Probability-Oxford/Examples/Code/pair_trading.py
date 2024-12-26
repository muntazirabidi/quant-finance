import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class PairsTrader:
    def __init__(self, symbol_A, symbol_B, start_date, end_date, window=60, z_threshold=2.0):
        self.symbol_A = symbol_A
        self.symbol_B = symbol_B
        self.start_date = start_date
        self.end_date = end_date
        self.window = window
        self.z_threshold = z_threshold
        self.data = None
        self.results = None

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
      Calculate the spread between two price series using log prices.
      This approach has several statistical advantages:
      1. Log returns are more likely to be normally distributed
      2. Log differences are additive
      3. Prevents negative prices in theoretical modeling
      """
      price_A = self.data[f'{self.symbol_A}_price']
      price_B = self.data[f'{self.symbol_B}_price']
      
      # Calculate log prices
      log_price_A = np.log(price_A)
      log_price_B = np.log(price_B)
      
      # Calculate spread
      spread = log_price_A - log_price_B
      
      # Calculate rolling statistics with minimum periods requirement
      rolling_mean = spread.rolling(window=self.window, min_periods=self.window).mean()
      rolling_std = spread.rolling(window=self.window, min_periods=self.window).std()
      
      # Calculate z-score with protection against zero standard deviation
      zscore = np.where(
          rolling_std > 0,
          (spread - rolling_mean) / rolling_std,
          0  # Default value when std is zero
      )
      
      # Add some basic statistics
      print(f"\nSpread Statistics:")
      print(f"Mean: {spread.mean():.4f}")
      print(f"Std Dev: {spread.std():.4f}")
      print(f"Min: {spread.min():.4f}")
      print(f"Max: {spread.max():.4f}")
      
      return spread, pd.Series(zscore, index=spread.index)

    def generate_signals(self):
        spread, zscore = self.calculate_spread()
        signals = pd.DataFrame(index=self.data.index)

        signals['position'] = np.where(zscore > self.z_threshold, -1,
                            np.where(zscore < -self.z_threshold, 1, 0))
        signals['spread'] = spread
        signals['zscore'] = zscore

        return signals

    def calculate_returns(self, signals, initial_capital=100000):
        price_A = self.data[f'{self.symbol_A}_price']
        price_B = self.data[f'{self.symbol_B}_price']

        returns_A = price_A.pct_change().fillna(0)
        returns_B = price_B.pct_change().fillna(0)

        strategy_returns = signals['position'].shift(1).fillna(0) * (returns_A - returns_B)
        portfolio_value = (1 + strategy_returns).cumprod() * initial_capital

        sharpe_ratio = np.sqrt(252) * strategy_returns.mean() / strategy_returns.std() if strategy_returns.std() != 0 else 0
        max_drawdown = (portfolio_value / portfolio_value.cummax() - 1).min()

        self.results = {
            'returns': strategy_returns,
            'portfolio_value': portfolio_value,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'signals': signals
        }
        return self.results

    def plot_results(self):
        if self.results is None:
            raise ValueError("Run the strategy first using run_strategy()")
        
        signals = self.results['signals']
        fig, axes = plt.subplots(4, 1, figsize=(15, 20))
        
        self.data.plot(ax=axes[0])
        axes[0].set_title('Stock Prices')
        axes[0].set_ylabel('Price')
        axes[0].legend(loc="upper left")
        
        signals[['spread', 'zscore']].plot(ax=axes[1])
        axes[1].axhline(self.z_threshold, color='r', linestyle='--', label='Z Threshold')
        axes[1].axhline(-self.z_threshold, color='r', linestyle='--')
        axes[1].set_title('Spread and Z-Score')
        axes[1].legend()

        signals['position'].plot(ax=axes[2], color='blue')
        axes[2].set_title('Trading Positions')
        axes[2].set_ylabel('Position')

        self.results['portfolio_value'].plot(ax=axes[3], color='green')
        axes[3].set_title('Portfolio Value')
        axes[3].set_ylabel('Value')
        
        plt.tight_layout()
        plt.show()

    def run_strategy(self, initial_capital=100000):
        if self.data is None:
            self.fetch_data()

        signals = self.generate_signals()
        results = self.calculate_returns(signals, initial_capital)
        self.plot_results()

        return results

if __name__ == "__main__":
    pairs = [
        ('KO', 'PEP'),  # Coca-Cola vs Pepsi
        ('JPM', 'BAC'), # JPMorgan vs Bank of America
        ('CVX', 'XOM')  # Chevron vs Exxon Mobil
    ]
    
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    
    for symbol_A, symbol_B in pairs:
        try:
            print(f"\nAnalyzing pair: {symbol_A} - {symbol_B}")
            trader = PairsTrader(symbol_A, symbol_B, start_date, end_date)
            results = trader.run_strategy()
            
            print("\nStrategy Results:")
            print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
            print(f"Max Drawdown: {results['max_drawdown']:.2%}")
            print(f"Total Return: {(results['portfolio_value'][-1] / results['portfolio_value'][0] - 1):.2%}")
            
        except Exception as e:
            print(f"Error analyzing {symbol_A}-{symbol_B}: {str(e)}")
            continue
