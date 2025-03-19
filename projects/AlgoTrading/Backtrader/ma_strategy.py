import backtrader as bt
import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Set matplotlib to use Agg backend to avoid display issues
import matplotlib
matplotlib.use('Agg')


class ImprovedSMAStrategy(bt.Strategy):
    """
    Enhanced SMA Crossover Strategy with:
    - Trend filter using longer-term moving average
    - RSI confirmation
    - Proper position sizing
    - Stop-loss and trailing stops
    """
    params = (
        ('fast_ma', 10),        # Fast SMA period
        ('slow_ma', 30),        # Slow SMA period
        ('trend_ma', 100),      # Trend filter MA period
        ('rsi_period', 14),     # RSI period
        ('rsi_overbought', 70), # RSI overbought level
        ('rsi_oversold', 30),   # RSI oversold level
        ('position_size', 0.95),# % of capital to use per trade
        ('stop_loss', 0.05),    # Stop loss percentage
        ('trail_percent', 0.15),# Trailing stop percentage
        ('verbose', False),     # Logging flag
    )

    def log(self, txt, dt=None):
        """Logging function"""
        if self.params.verbose:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
        
    def __init__(self):
        # Data
        self.data_close = self.datas[0].close
        
        # Indicators
        # Moving Averages
        self.fast_ma = bt.indicators.SMA(self.data_close, period=self.params.fast_ma)
        self.slow_ma = bt.indicators.SMA(self.data_close, period=self.params.slow_ma)
        self.trend_ma = bt.indicators.SMA(self.data_close, period=self.params.trend_ma)
        
        # Crossover signal
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)
        
        # RSI for confirmation
        self.rsi = bt.indicators.RSI(self.data_close, period=self.params.rsi_period)
        
        # Order and trade tracking
        self.order = None
        self.trade_count = 0
        self.profitable_trades = 0
        self.buy_price = None

    def notify_order(self, order):
        """Called when order status changes"""
        if order.status in [order.Submitted, order.Accepted]:
            return  # Nothing to do
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.buy_price = order.executed.price
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            else:
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                if self.buy_price:
                    profit_pct = (order.executed.price / self.buy_price - 1) * 100
                    self.log(f'Trade Profit: {profit_pct:.2f}%')
        
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Canceled/Margin/Rejected: {order.status}')

        self.order = None

    def notify_trade(self, trade):
        """Called when a trade is closed"""
        if not trade.isclosed:
            return
            
        self.trade_count += 1
        if trade.pnl > 0:
            self.profitable_trades += 1
            
        self.log(f'TRADE COMPLETED, PROFIT: {trade.pnl:.2f}, NET: {trade.pnlcomm:.2f}')

    def next(self):
        """Called for each market bar"""
        # Skip if an order is pending
        if self.order:
            return
            
        # Trading logic
        if not self.position:
            # --- BUY LOGIC ---
            # 1. Only buy in uptrends (price > trend_ma)
            uptrend = self.data_close[0] > self.trend_ma[0]
            
            # 2. SMA crossover signal
            buy_signal = self.crossover > 0
            
            # 3. RSI confirmation - not overbought
            rsi_ok = self.rsi[0] < self.params.rsi_overbought
            
            if uptrend and buy_signal and rsi_ok:
                # Calculate position size
                cash = self.broker.getcash()
                price = self.data_close[0]
                size = int((cash * self.params.position_size) / price)
                
                if size > 0:
                    self.log(f'BUY CREATE, {self.data_close[0]:.2f}, Size: {size}')
                    self.order = self.buy(size=size)
                    
                    # Set stop loss order
                    stop_price = price * (1.0 - self.params.stop_loss)
                    self.sell(exectype=bt.Order.Stop, price=stop_price, size=size)
                    self.log(f'STOP LOSS SET AT {stop_price:.2f}')
        
        else:
            # --- SELL LOGIC ---
            # 1. SMA crossover signal
            sell_signal = self.crossover < 0
            
            # 2. RSI confirmation - overbought
            rsi_sell = self.rsi[0] > self.params.rsi_overbought
            
            # 3. Downtrend confirmation
            downtrend = self.data_close[0] < self.trend_ma[0]
            
            # Sell if any sell signal is triggered
            if sell_signal or rsi_sell or downtrend:
                self.log(f'SELL CREATE, {self.data_close[0]:.2f}')
                self.order = self.sell()
            
            # Update trailing stop if appropriate
            elif self.buy_price:
                current_profit_pct = (self.data_close[0] / self.buy_price - 1) * 100
                if current_profit_pct > self.params.trail_percent:
                    # New stop is a percentage below current price
                    trail_price = self.data_close[0] * (1.0 - (self.params.stop_loss / 2))
                    
                    # Only update stop if it's higher than previous stop
                    if not hasattr(self, 'trailing_stop') or trail_price > self.trailing_stop:
                        self.trailing_stop = trail_price
                        self.sell(exectype=bt.Order.Stop, price=trail_price, size=self.position.size)
                        self.log(f'TRAILING STOP UPDATED TO {trail_price:.2f}')
    
    def stop(self):
        """Called at the end of the backtest"""
        win_rate = self.profitable_trades / self.trade_count * 100 if self.trade_count > 0 else 0
        print('-' * 50)
        print('STRATEGY PERFORMANCE SUMMARY:')
        print(f'Win rate: {win_rate:.2f}%')
        print(f'Profitable trades: {self.profitable_trades}/{self.trade_count}')
        print('-' * 50)


def run_backtest(ticker='AAPL', start_date='2018-01-01', end_date='2020-12-31', 
                 fast_ma=10, slow_ma=30, trend_ma=100, rsi_period=14, 
                 position_size=0.95, stop_loss=0.05, initial_cash=10000.0, 
                 commission=0.001, verbose=False, plot=True):
    """
    Run a backtest with the improved strategy
    """
    # Create Cerebro engine
    cerebro = bt.Cerebro()
    
    # Add strategy
    cerebro.addstrategy(ImprovedSMAStrategy, 
                         fast_ma=fast_ma, 
                         slow_ma=slow_ma,
                         trend_ma=trend_ma,
                         rsi_period=rsi_period,
                         position_size=position_size,
                         stop_loss=stop_loss,
                         verbose=verbose)
    
    # Download data - use longer timeframe for proper indicator calculation
    extended_start = pd.to_datetime(start_date) - pd.Timedelta(days=trend_ma*2)
    extended_start_str = extended_start.strftime('%Y-%m-%d')
    
    print(f"Downloading data for {ticker} from {extended_start_str} to {end_date}...")
    data_df = yf.download(ticker, start=extended_start_str, end=end_date)
    
    # Display data info
    print(f"Downloaded {len(data_df)} bars of data")
    print(f"Data columns: {data_df.columns}")
    
    # Handle multi-level columns that might come from yfinance
    if isinstance(data_df.columns[0], tuple):
        # If we have multi-level columns, take the first level
        data_df.columns = [col[0].lower() for col in data_df.columns]
    else:
        # Otherwise, just lowercase the column names
        data_df.columns = [col.lower() for col in data_df.columns]
    
    # Convert to Backtrader data feed
    data = bt.feeds.PandasData(dataname=data_df)
    cerebro.adddata(data)
    
    # Set broker parameters
    cerebro.broker.setcash(initial_cash)
    cerebro.broker.setcommission(commission=commission)
    
    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    
    # Print starting portfolio value
    print(f'Starting Portfolio Value: ${initial_cash:.2f}')
    
    # Run backtest
    results = cerebro.run()
    strat = results[0]
    
    # Get trade analyzer results
    trade_analysis = strat.analyzers.trades.get_analysis()
    
    # Calculate final portfolio value
    final_value = cerebro.broker.getvalue()
    
    # Get performance metrics
    sharpe_ratio = strat.analyzers.sharpe.get_analysis().get('sharperatio', 0)
    max_drawdown = strat.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0)
    annual_return = strat.analyzers.returns.get_analysis().get('rnorm100', 0)
    
    # Print performance summary
    print('-' * 50)
    print('BACKTEST RESULTS:')
    print(f'Final Portfolio Value: ${final_value:.2f}')
    print(f'Total Return: {(final_value/initial_cash - 1) * 100:.2f}%')
    print(f'Sharpe Ratio: {sharpe_ratio:.3f}')
    print(f'Max Drawdown: {max_drawdown:.2f}%')
    print(f'Annual Return: {annual_return:.2f}%')
    
    # Trade statistics if there were any trades
    if trade_analysis.get('total', {}).get('total', 0) > 0:
        print('\nTRADE STATISTICS:')
        print(f'Total Trades: {trade_analysis["total"]["total"]}')
        print(f'Winning Trades: {trade_analysis.get("won", {}).get("total", 0)}')
        print(f'Losing Trades: {trade_analysis.get("lost", {}).get("total", 0)}')
        
        if trade_analysis.get("won", {}).get("total", 0) > 0:
            print(f'Average Profit: ${trade_analysis["won"]["pnl"]["average"]:.2f}')
            print(f'Max Profit: ${trade_analysis["won"]["pnl"]["max"]:.2f}')
        
        if trade_analysis.get("lost", {}).get("total", 0) > 0:
            print(f'Average Loss: ${trade_analysis["lost"]["pnl"]["average"]:.2f}')
            print(f'Max Loss: ${trade_analysis["lost"]["pnl"]["max"]:.2f}')
    
    print('-' * 50)
    
    # Plot results
    if plot:
        plt.rcParams['figure.figsize'] = [15, 10]
        figs = cerebro.plot(style='candlestick', barup='green', bardown='red', 
                           plotdist=0.5, volume=True)
        
        # Save plot as file
        plot_filename = f"{ticker}_strategy_{start_date}_{end_date}.png"
        for fig in figs[0]:
            fig.savefig(plot_filename)
            print(f"Plot saved as {plot_filename}")
    
    # Return results as a dictionary
    return {
        'final_value': final_value,
        'total_return': (final_value/initial_cash - 1) * 100,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': max_drawdown,
        'annual_return': annual_return,
        'trade_analysis': trade_analysis
    }


def optimize_strategy(ticker='AAPL', start_date='2018-01-01', end_date='2020-12-31',
                     fast_ma_range=(5, 25), slow_ma_range=(20, 100), trend_ma_range=(50, 200),
                     initial_cash=10000.0):
    """
    Optimize strategy parameters using a grid search
    """
    best_return = -999
    best_params = {}
    
    print(f"Optimizing strategy for {ticker} from {start_date} to {end_date}...")
    
    # Grid search through parameter combinations
    for fast_ma in range(fast_ma_range[0], fast_ma_range[1] + 1, 5):
        for slow_ma in range(slow_ma_range[0], slow_ma_range[1] + 1, 10):
            # Skip invalid combinations
            if fast_ma >= slow_ma:
                continue
                
            for trend_ma in range(trend_ma_range[0], trend_ma_range[1] + 1, 50):
                # Skip invalid combinations
                if slow_ma >= trend_ma:
                    continue
                    
                print(f"Testing: Fast MA={fast_ma}, Slow MA={slow_ma}, Trend MA={trend_ma}")
                
                # Run backtest with current parameters
                results = run_backtest(
                    ticker=ticker,
                    start_date=start_date,
                    end_date=end_date,
                    fast_ma=fast_ma,
                    slow_ma=slow_ma,
                    trend_ma=trend_ma,
                    initial_cash=initial_cash,
                    verbose=False,
                    plot=False
                )
                
                # Update best parameters if current run is better
                if results['annual_return'] > best_return:
                    best_return = results['annual_return']
                    best_params = {
                        'fast_ma': fast_ma,
                        'slow_ma': slow_ma,
                        'trend_ma': trend_ma,
                        'annual_return': best_return,
                        'sharpe_ratio': results['sharpe_ratio'],
                        'max_drawdown': results['max_drawdown']
                    }
                    
                    print(f"New best parameters found! Annual Return: {best_return:.2f}%")
    
    print("\nOPTIMIZATION RESULTS:")
    print(f"Best Parameters: Fast MA={best_params['fast_ma']}, Slow MA={best_params['slow_ma']}, Trend MA={best_params['trend_ma']}")
    print(f"Annual Return: {best_params['annual_return']:.2f}%")
    print(f"Sharpe Ratio: {best_params['sharpe_ratio']:.3f}")
    print(f"Max Drawdown: {best_params['max_drawdown']:.2f}%")
    
    return best_params


if __name__ == "__main__":
    # Test the improved strategy
    results = run_backtest(
        ticker='AAPL',
        start_date='2019-01-01',
        end_date='2020-12-31',
        fast_ma=10,
        slow_ma=30,
        trend_ma=100,
        rsi_period=14,
        position_size=0.95,
        stop_loss=0.05,
        initial_cash=10000.0,
        verbose=True,
        plot=True
    )
    
    # Uncomment to run optimization (warning: can be time-consuming)
    best_params = optimize_strategy(
         ticker='AAPL',
         start_date='2019-01-01',
         end_date='2020-12-31'
     )