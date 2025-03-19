import backtrader as bt
import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import csv
import os

# Set matplotlib to use Agg backend to avoid display issues
import matplotlib
matplotlib.use('Agg')


class OptimizedMACDStrategy(bt.Strategy):
    """
    Ultimate MACD Trading Strategy
    Features:
    - MACD signal for entry/exit with flexible signal interpretation
    - Long-term trend filter using 200-day moving average
    - Advanced volume analysis for trend confirmation
    - Adaptive ATR-based stop loss with trailing mechanism
    - Dynamic position sizing based on volatility
    - RSI filter to avoid overbought/oversold conditions
    - Take-profit targets for disciplined profit-taking
    - Emergency position handling for risk management
    - Bollinger Bands for market context
    """
    params = (
        ('macd_fast', 12),       # Fast EMA period for MACD
        ('macd_slow', 26),       # Slow EMA period for MACD
        ('macd_signal', 9),      # Signal period for MACD
        ('rsi_period', 14),      # RSI period
        ('rsi_overbought', 70),  # RSI overbought level
        ('rsi_oversold', 30),    # RSI oversold level
        ('atr_period', 14),      # ATR period
        ('atr_multiplier', 3),   # ATR multiplier for stop loss (increased for SPY)
        ('risk_pct', 0.02),      # Risk percentage per trade (2%)
        ('volume_factor', 1.5),  # Volume factor for volume filter
        ('trend_period', 200),   # Long-term trend filter period
        ('take_profit', 0.1),    # Take profit at 10% gain
        ('bb_period', 20),       # Bollinger Band period
        ('bb_dev', 2),           # Bollinger Band standard deviation
        ('trail_percent', 0.05), # Trailing stop percentage (reduced)
        ('verbose', False),      # Logging flag
    )

    def log(self, txt, dt=None):
        """Logging function"""
        if self.params.verbose:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
        
    def __init__(self):
        # Data references
        self.data_close = self.datas[0].close
        self.data_open = self.datas[0].open
        self.data_high = self.datas[0].high
        self.data_low = self.datas[0].low
        self.data_volume = self.datas[0].volume
        
        # MACD indicator
        self.macd = bt.indicators.MACD(
            self.data_close,
            period_me1=self.params.macd_fast,
            period_me2=self.params.macd_slow,
            period_signal=self.params.macd_signal
        )
        
        # Crossover signal
        self.macd_crossover = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
        
        # RSI for additional filter
        self.rsi = bt.indicators.RSI(self.data_close, period=self.params.rsi_period)
        
        # ATR for stop loss calculation
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)
        
        # Volume indicators
        self.volume_ma = bt.indicators.SMA(self.data_volume, period=20)
        self.volume_change = bt.indicators.PercentChange(self.data_volume, period=1)
        
        # Trend indicators
        self.sma200 = bt.indicators.SMA(self.data_close, period=self.params.trend_period)
        self.sma50 = bt.indicators.SMA(self.data_close, period=50)  # Medium-term trend
        
        # Bollinger Bands for volatility context
        self.bbands = bt.indicators.BollingerBands(
            self.data_close, 
            period=self.params.bb_period,
            devfactor=self.params.bb_dev
        )
        
        # Order and trade tracking
        self.order = None
        self.stop_order = None  # To track stop orders
        self.trade_count = 0
        self.profitable_trades = 0
        self.buy_price = None
        self.stop_loss = None
        self.take_profit_level = None
        self.position_size = 0
        self.in_trade = False   # Flag to track if we're in a trade

    def notify_order(self, order):
        """Called when order status changes"""
        if order.status in [order.Submitted, order.Accepted]:
            return  # Nothing to do
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.buy_price = order.executed.price
                self.position_size = order.executed.size
                self.in_trade = True
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}, Size: {order.executed.size}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                
                # Set stop loss based on ATR
                self.stop_loss = self.buy_price - (self.atr[0] * self.params.atr_multiplier)
                # Set take profit level
                self.take_profit_level = self.buy_price * (1 + self.params.take_profit)
                
                self.log(f'STOP LOSS SET AT {self.stop_loss:.2f}, TAKE PROFIT AT {self.take_profit_level:.2f}')
                
                # Create stop order
                self.stop_order = self.sell(exectype=bt.Order.Stop, price=self.stop_loss, size=self.position_size)
                
            else:
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}, Size: {order.executed.size}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                
                if self.buy_price:
                    profit_pct = (order.executed.price / self.buy_price - 1) * 100
                    self.log(f'Trade Profit: {profit_pct:.2f}%')
                
                # Reset trade tracking variables
                self.buy_price = None
                self.stop_loss = None
                self.take_profit_level = None
                self.stop_order = None
                self.in_trade = False
                self.position_size = 0
        
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Canceled/Margin/Rejected: {order.status}')
            
            # If a stop order is rejected, try to close the position immediately
            if order.exectype == bt.Order.Stop:
                self.log(f'STOP ORDER REJECTED - EMERGENCY CLOSING POSITION')
                self.close()

        # Reset main order reference if this is the main order (not stop order)
        if self.order == order:
            self.order = None

    def notify_trade(self, trade):
        """Called when a trade is closed"""
        if not trade.isclosed:
            return
            
        self.trade_count += 1
        if trade.pnl > 0:
            self.profitable_trades += 1
            
        self.log(f'TRADE COMPLETED, PROFIT: {trade.pnl:.2f}, NET: {trade.pnlcomm:.2f}')

    def is_volume_significant(self):
        """Check if current volume is significantly higher than average"""
        return self.data_volume[0] > (self.volume_ma[0] * self.params.volume_factor)

    def is_bull_trend(self):
        """Check if we're in a bullish trend"""
        # Primary trend filter
        primary_trend = self.data_close[0] > self.sma200[0]
        
        # Secondary filters for stronger confirmation
        price_above_50 = self.data_close[0] > self.sma50[0]
        medium_term_rising = self.sma50[0] > self.sma50[-1]
        
        # For SPY, we want strong confirmation of trend
        return primary_trend and price_above_50

    def get_volatility_factor(self):
        """Calculate a volatility factor for position sizing"""
        # Use Bollinger Band width as a proxy for volatility
        bb_width = (self.bbands.lines.top[0] - self.bbands.lines.bot[0]) / self.bbands.lines.mid[0]
        
        # Normalize: Lower value for high volatility, higher value for low volatility
        # Range will typically be between 0.5 (high vol) and 1.5 (low vol)
        norm_factor = 1.0 / (bb_width * 10)
        
        return max(0.5, min(1.5, norm_factor))

    def next(self):
        """Called for each market bar"""
        # Debug information
        if self.params.verbose and len(self.datas[0]) % 20 == 0:  # Print every 20 bars
            print(f'Bar: {len(self.datas[0])}, Date: {self.datas[0].datetime.date(0)}, '
                  f'Close: {self.data_close[0]:.2f}, MACD: {self.macd.macd[0]:.4f}, '
                  f'Signal: {self.macd.signal[0]:.4f}, RSI: {self.rsi[0]:.2f}, '
                  f'In Trade: {self.in_trade}, Position: {self.position.size}')
        
        # SAFETY CHECKS
        
        # 1. Check for account protection - stop trading if drawdown exceeds threshold
        current_value = self.broker.getvalue()
        if current_value < self.broker.startingcash * 0.85:  # 15% max drawdown
            # Cancel all open orders and close positions
            for order in self.broker.get_orders_open():
                self.broker.cancel(order)
            if self.position:
                self.close()
            return  # Stop trading completely
        
        # 2. Check for misaligned state (safeguard)
        if self.position.size > 0 and not self.in_trade:
            self.log("EMERGENCY: Position detected but not tracked. Closing.")
            self.close()
            self.in_trade = False
            self.stop_order = None
            return
            
        # 3. Check for unexpected positions (another safeguard)
        if self.position.size < 0:  # We shouldn't have short positions
            self.log("EMERGENCY: Unexpected short position detected. Closing.")
            self.close()
            return
        
        # Skip if an order is pending
        if self.order:
            return
            
        # TRADING LOGIC
        if not self.position:
            # --- BUY LOGIC ---
            
            # 1. MACD bullish signals (either crossover or positive spread)
            macd_crossover_bullish = self.macd_crossover > 0
            macd_positive_spread = self.macd.macd[0] > self.macd.signal[0]
            
            # For SPY, we're more strategic about entries
            if self.data_close[0] > 300:  # SPY price check
                # For SPY or high-value indices, use crossover for precision
                macd_buy_signal = macd_crossover_bullish
            else:
                # For other assets, either signal works
                macd_buy_signal = macd_positive_spread or macd_crossover_bullish
            
            # 2. RSI is not overbought (more lenient now)
            rsi_ok = self.rsi[0] < 75
            
            # 3. Trend filter - Most important for SPY
            trend_ok = self.is_bull_trend()
            
            # 4. Volatility check - avoid extremely high volatility periods
            vol_ok = self.bbands.lines.top[0] / self.bbands.lines.bot[0] < 1.1
            
            # 5. Buy Signal Logic - adapted for SPY
            if macd_buy_signal and trend_ok and rsi_ok:
                # Dynamic position sizing based on volatility
                cash = self.broker.getcash()
                vol_factor = self.get_volatility_factor()
                
                # Base position size on available capital
                position_pct = 0.2 * vol_factor  # Adjust position size by volatility (0.1-0.3 range)
                size = int((cash * position_pct) / self.data_close[0])
                
                if size > 0:
                    self.log(f'BUY CREATE, Close: {self.data_close[0]:.2f}, Size: {size}, Vol Factor: {vol_factor:.2f}')
                    self.order = self.buy(size=size)
        
        else:
            # --- SELL LOGIC ---
            
            # 1. Take profit hit?
            if self.take_profit_level and self.data_close[0] >= self.take_profit_level:
                self.log(f'TAKE PROFIT TRIGGERED, Close: {self.data_close[0]:.2f}, Target: {self.take_profit_level:.2f}')
                if self.stop_order:
                    self.cancel(self.stop_order)
                    self.stop_order = None
                self.order = self.sell()
                return
            
            # 2. Stop loss hit? (Manual check as backup to stop order)
            if self.stop_loss and self.data_close[0] <= self.stop_loss:
                self.log(f'STOP LOSS TRIGGERED MANUALLY, Close: {self.data_close[0]:.2f}, Stop: {self.stop_loss:.2f}')
                if self.stop_order:
                    self.cancel(self.stop_order)
                    self.stop_order = None
                self.order = self.sell()
                return
            
            # 3. Technical exit signals
            macd_crossover_bearish = self.macd_crossover < 0
            macd_negative_spread = self.macd.macd[0] < self.macd.signal[0]
            rsi_overbought = self.rsi[0] > self.params.rsi_overbought
            trend_turning = self.data_close[0] < self.sma50[0]  # Price below medium-term avg
            
            # Exit on strong bearish signals
            if (macd_crossover_bearish and trend_turning) or (rsi_overbought and macd_negative_spread):
                self.log(f'SELL CREATE FROM SIGNALS, Close: {self.data_close[0]:.2f}')
                if self.stop_order:
                    self.cancel(self.stop_order)
                    self.stop_order = None
                self.order = self.sell()
                return
            
            # 4. Update trailing stop if in profit
            if self.buy_price and self.stop_order:
                current_profit_pct = (self.data_close[0] / self.buy_price - 1) * 100
                
                # Start trailing when profit > 5%
                if current_profit_pct > 5:
                    # Set new stop based on ATR or percentage, whichever is tighter
                    atr_stop = self.data_close[0] - (self.atr[0] * 2)
                    pct_stop = self.data_close[0] * (1.0 - self.params.trail_percent)
                    new_stop = max(atr_stop, pct_stop, self.stop_loss)  # Never lower the stop
                    
                    if new_stop > self.stop_loss:
                        self.stop_loss = new_stop
                        self.log(f'TRAILING STOP UPDATED TO {self.stop_loss:.2f}')
                        
                        # Cancel and replace stop order
                        self.cancel(self.stop_order)
                        self.stop_order = self.sell(exectype=bt.Order.Stop, price=self.stop_loss, size=self.position.size)
    
    def stop(self):
        """Called at the end of the backtest"""
        win_rate = self.profitable_trades / self.trade_count * 100 if self.trade_count > 0 else 0
        print('-' * 50)
        print('STRATEGY PERFORMANCE SUMMARY:')
        print(f'Win rate: {win_rate:.2f}%')
        print(f'Profitable trades: {self.profitable_trades}/{self.trade_count}')
        print('-' * 50)


def run_backtest(ticker='SPY', start_date='2018-01-01', end_date='2023-12-31', 
                 macd_fast=12, macd_slow=26, macd_signal=9, rsi_period=14, 
                 risk_pct=0.02, atr_period=14, atr_multiplier=3, initial_cash=10000.0, 
                 commission=0.001, verbose=False, plot=True):
    """
    Run a backtest with the optimized MACD strategy
    """
    # Create Cerebro engine
    cerebro = bt.Cerebro(stdstats=True)
    
    # Set broker parameters more appropriately (fix conflicting settings)
    cerebro.broker.set_checksubmit(False)  # Needed for stop orders
    cerebro.broker.set_coc(True)  # Use close-of-candle for orders
    # Removed conflicting set_coo setting
    
    # Add strategy
    cerebro.addstrategy(OptimizedMACDStrategy, 
                         macd_fast=macd_fast, 
                         macd_slow=macd_slow,
                         macd_signal=macd_signal,
                         rsi_period=rsi_period,
                         risk_pct=risk_pct,
                         atr_period=atr_period,
                         atr_multiplier=atr_multiplier,
                         verbose=verbose)
    
    # Download data
    extended_start = pd.to_datetime(start_date) - pd.Timedelta(days=100)  # Extra data for indicators
    extended_start_str = extended_start.strftime('%Y-%m-%d')
    
    print(f"Downloading data for {ticker} from {extended_start_str} to {end_date}...")
    
    try:
        data_df = yf.download(ticker, start=extended_start_str, end=end_date)
        
        # Display data info
        print(f"Downloaded {len(data_df)} bars of data")
        print(f"Data range: {data_df.index.min()} to {data_df.index.max()}")
        
        if len(data_df) < 100:
            print("WARNING: Not enough data downloaded. Check date range and ticker symbol.")
            return None
            
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None
    
    # Handle multi-level columns that might come from yfinance
    if isinstance(data_df.columns, pd.MultiIndex):
        data_df.columns = [col[0].lower() for col in data_df.columns]
    else:
        data_df.columns = [col.lower() for col in data_df.columns]
    
    # Convert to Backtrader data feed
    data = bt.feeds.PandasData(dataname=data_df)
    cerebro.adddata(data)
    
    # Set broker parameters
    cerebro.broker.setcash(initial_cash)
    cerebro.broker.setcommission(commission=commission)
    
    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe', riskfreerate=0.01) 
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    cerebro.addanalyzer(bt.analyzers.SQN, _name='sqn')
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='time_return')
    
    # Print starting portfolio value
    print(f'Starting Portfolio Value: ${initial_cash:.2f}')
    
    # Run backtest
    try:
        results = cerebro.run()
        strat = results[0]
    except Exception as e:
        print(f"Error running backtest: {e}")
        return None
    
    # Get trade analyzer results
    try:
        trade_analysis = strat.analyzers.trades.get_analysis()
    except:
        trade_analysis = {}
    
    # Calculate final portfolio value
    final_value = cerebro.broker.getvalue()
    
    # Get performance metrics with error handling
    try:
        sharpe_ratio = strat.analyzers.sharpe.get_analysis().get('sharperatio', 0)
        max_drawdown = strat.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0)
        annual_return = strat.analyzers.returns.get_analysis().get('rnorm100', 0)
        sqn = strat.analyzers.sqn.get_analysis().get('sqn', 0)
        
        # Ensure all metrics are numeric values
        sharpe_ratio = 0.0 if sharpe_ratio is None else sharpe_ratio
        max_drawdown = 0.0 if max_drawdown is None else max_drawdown
        annual_return = 0.0 if annual_return is None else annual_return
        sqn = 0.0 if sqn is None else sqn
    except:
        sharpe_ratio, max_drawdown, annual_return, sqn = 0.0, 0.0, 0.0, 0.0
    
    # Print performance summary
    print('-' * 50)
    print('BACKTEST RESULTS:')
    print(f'Final Portfolio Value: ${final_value:.2f}')
    print(f'Total Return: {(final_value/initial_cash - 1) * 100:.2f}%')
    print(f'Sharpe Ratio: {sharpe_ratio:.3f}')
    print(f'SQN (System Quality Number): {sqn:.3f}')
    print(f'Max Drawdown: {max_drawdown:.2f}%')
    print(f'Annual Return: {annual_return:.2f}%')
    
    # Trade statistics if there were any trades
    if trade_analysis.get('total', {}).get('total', 0) > 0:
        print('\nTRADE STATISTICS:')
        print(f'Total Trades: {trade_analysis["total"]["total"]}')
        print(f'Winning Trades: {trade_analysis.get("won", {}).get("total", 0)}')
        print(f'Losing Trades: {trade_analysis.get("lost", {}).get("total", 0)}')
        
        win_trades = trade_analysis.get("won", {}).get("total", 0)
        total_trades = trade_analysis["total"]["total"]
        win_rate = (win_trades / total_trades * 100) if total_trades > 0 else 0
        print(f'Win Rate: {win_rate:.2f}%')
        
        if win_trades > 0:
            print(f'Average Profit: ${trade_analysis["won"]["pnl"]["average"]:.2f}')
            print(f'Max Profit: ${trade_analysis["won"]["pnl"]["max"]:.2f}')
        
        if trade_analysis.get("lost", {}).get("total", 0) > 0:
            print(f'Average Loss: ${trade_analysis["lost"]["pnl"]["average"]:.2f}')
            print(f'Max Loss: ${trade_analysis["lost"]["pnl"]["max"]:.2f}')
    
    print('-' * 50)
    
    # Plot results
    if plot:
        try:
            plt.rcParams['figure.figsize'] = [15, 10]
            figs = cerebro.plot(style='candlestick', barup='green', bardown='red', 
                               plotdist=0.5, volume=True)
            
            # Save plot as file
            plot_filename = f"Figure/{ticker}_macd_strategy_{start_date}_{end_date}.png"
            for fig in figs[0]:
                fig.savefig(plot_filename)
                print(f"Plot saved as {plot_filename}")
        except Exception as e:
            print(f"Error plotting results: {e}")
    
    # Return results as a dictionary
    return {
        'final_value': final_value,
        'total_return': (final_value/initial_cash - 1) * 100,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': max_drawdown,
        'annual_return': annual_return,
        'sqn': sqn,
        'trade_analysis': trade_analysis
    }


def optimize_macd_strategy(ticker='SPY', start_date='2018-01-01', end_date='2023-12-31',
                         fast_range=(8, 20), slow_range=(18, 32), signal_range=(7, 13),
                         atr_mult_range=(2.0, 4.0), initial_cash=10000.0):
    """
    Optimize MACD strategy parameters using a grid search
    """
    best_sharpe = -999
    best_sqn = -999
    best_params = {}
    
    # Create a list to store all parameter results
    all_results = []
    
    print(f"Optimizing MACD strategy for {ticker} from {start_date} to {end_date}...")
    
    # Grid search through parameter combinations
    for fast in range(fast_range[0], fast_range[1] + 1, 2):
        for slow in range(slow_range[0], slow_range[1] + 1, 2):
            # Skip invalid combinations
            if fast >= slow:
                continue
                
            for signal in range(signal_range[0], signal_range[1] + 1, 1):
                for atr_mult in [round(x * 0.5, 1) for x in range(int(atr_mult_range[0] * 2), int(atr_mult_range[1] * 2) + 1)]:
                    print(f"Testing: Fast={fast}, Slow={slow}, Signal={signal}, ATR Mult={atr_mult}")
                    
                    # Run backtest with current parameters
                    results = run_backtest(
                        ticker=ticker,
                        start_date=start_date,
                        end_date=end_date,
                        macd_fast=fast,
                        macd_slow=slow,
                        macd_signal=signal,
                        atr_multiplier=atr_mult,
                        initial_cash=initial_cash,
                        verbose=False,
                        plot=False
                    )
                    
                    if not results:
                        print("Skipping invalid parameter combination")
                        continue
                    
                    # Store this parameter combination and its results
                    param_results = {
                        'macd_fast': fast,
                        'macd_slow': slow,
                        'macd_signal': signal,
                        'atr_multiplier': atr_mult,
                        'sharpe_ratio': results['sharpe_ratio'],
                        'sqn': results['sqn'],
                        'annual_return': results['annual_return'],
                        'max_drawdown': results['max_drawdown'],
                        'total_return': results['total_return'],
                        'final_value': results['final_value']
                    }
                    
                    # Add trade statistics if available
                    trade_analysis = results.get('trade_analysis', {})
                    if trade_analysis:
                        total_trades = trade_analysis.get('total', {}).get('total', 0)
                        win_trades = trade_analysis.get('won', {}).get('total', 0)
                        win_rate = (win_trades / total_trades * 100) if total_trades > 0 else 0
                        
                        param_results.update({
                            'total_trades': total_trades,
                            'win_trades': win_trades,
                            'win_rate': win_rate
                        })
                    
                    all_results.append(param_results)
                    
                    # Use sharpe ratio as primary metric for optimization - better for SPY
                    if results['sharpe_ratio'] > best_sharpe:
                        best_sharpe = results['sharpe_ratio']
                        best_sqn = results['sqn']
                        best_params = {
                            'macd_fast': fast,
                            'macd_slow': slow,
                            'macd_signal': signal,
                            'atr_multiplier': atr_mult,
                            'annual_return': results['annual_return'],
                            'sharpe_ratio': best_sharpe,
                            'sqn': best_sqn,
                            'max_drawdown': results['max_drawdown']
                        }
                        
                        print(f"New best parameters found! Sharpe: {best_sharpe:.3f}, SQN: {best_sqn:.3f}, Annual Return: {results['annual_return']:.2f}%")

    # Save all results to CSV
    results_dir = "optimization_results"
    os.makedirs(results_dir, exist_ok=True)
    csv_file = f"{results_dir}/{ticker}_macd_optimization_{start_date}_{end_date}.csv"
    
    with open(csv_file, 'w', newline='') as file:
        if all_results:
            fieldnames = all_results[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_results)
            print(f"All optimization results saved to {csv_file}")
    
    print("\nOPTIMIZATION RESULTS:")
    print(f"Best Parameters: Fast={best_params.get('macd_fast')}, Slow={best_params.get('macd_slow')}, " 
          f"Signal={best_params.get('macd_signal')}, ATR Mult={best_params.get('atr_multiplier')}")
    print(f"Sharpe Ratio: {best_params.get('sharpe_ratio', 0):.3f}")
    print(f"SQN: {best_params.get('sqn', 0):.3f}")
    print(f"Annual Return: {best_params.get('annual_return', 0):.2f}%")
    print(f"Max Drawdown: {best_params.get('max_drawdown', 0):.2f}%")
    
    return best_params, all_results


if __name__ == "__main__":
    # Initial backtest with default parameters
    results = run_backtest(
        ticker='SPY',
        start_date='2018-01-01',
        end_date='2024-12-31',    # Update to use all available historical data
        macd_fast=12,
        macd_slow=26,
        macd_signal=9,
        risk_pct=0.02,
        atr_multiplier=3.0,
        initial_cash=10000.0,
        verbose=True,
        plot=True
    )
    
    # Run optimization on in-sample period only
    best_params, all_results = optimize_macd_strategy(
        ticker='SPY',
        start_date='2018-01-01',
        end_date='2022-12-31'  # In-sample period
    )

    # Validate on out-of-sample period
    if best_params:
        print("Running validation on out-of-sample data...")
        validation_results = run_backtest(
            ticker='SPY',
            start_date='2023-01-01',
            end_date='2025-02-15',  # Out-of-sample period
            macd_fast=best_params['macd_fast'],
            macd_slow=best_params['macd_slow'],
            macd_signal=best_params['macd_signal'],
            atr_multiplier=best_params['atr_multiplier'],
            initial_cash=10000.0,
            verbose=True,
            plot=True
        )
        
        # Report validation metrics
        print("\nVALIDATION RESULTS (Out-of-Sample Performance):")
        print(f"Sharpe Ratio: {validation_results['sharpe_ratio']:.3f}")
        print(f"Total Return: {validation_results['total_return']:.2f}%")
        print(f"Max Drawdown: {validation_results['max_drawdown']:.2f}%")
