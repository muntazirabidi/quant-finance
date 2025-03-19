import backtrader as bt
import datetime
import pandas as pd
import yfinance as yf
from IPython.display import Image

class SimpleStrategy(bt.Strategy):
    params = (('sma_period', 50),)
    
    def __init__(self):
        self.sma = bt.indicators.SMA(self.data.close, period=self.params.sma_period)
        self.order = None
    
    def next(self):
        if self.order:
            return
            
        if not self.position:
            if self.data.close[0] > self.sma[0]:
                # Buy with fixed position size
                size = int(self.broker.getcash() * 0.95 / self.data.close[0])
                self.order = self.buy(size=size)
        else:
            if self.data.close[0] < self.sma[0]:
                self.order = self.sell()

# Main backtest function
def run_simple_backtest(ticker='SPY', start_date='2023-01-01', end_date='2025-03-15'):
    cerebro = bt.Cerebro(stdstats=True)
    cerebro.broker.set_cash(10000.0)
    cerebro.broker.setcommission(commission=0.001)
    
    # Disable margin trading
    cerebro.broker.set_checksubmit(False)
    
    # Download data
    data_df = yf.download(ticker, start=start_date, end=end_date)
    data_df.columns = [col[0].lower() for col in data_df.columns]
    data = bt.feeds.PandasData(dataname=data_df)
    cerebro.adddata(data)
    
    cerebro.addstrategy(SimpleStrategy)
    
    print(f'Starting Portfolio Value: ${cerebro.broker.getvalue():.2f}')
    cerebro.run()
    print(f'Final Portfolio Value: ${cerebro.broker.getvalue():.2f}')
    
    return cerebro

# Test simple strategy
if __name__ == "__main__":
    cerebro = run_simple_backtest(ticker='SPY')
    cerebro.plot(style='candlestick')
