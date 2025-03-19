import backtrader as bt
import yfinance as yf

class SimpleMACDStrategy(bt.Strategy):
    params = (('macd_fast', 12), ('macd_slow', 26), ('macd_signal', 9))
    
    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1=self.params.macd_fast,
            period_me2=self.params.macd_slow,
            period_signal=self.params.macd_signal
        )
        self.crossover = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
        self.order = None
    
    def next(self):
        if self.order:
            return
            
        if not self.position:
            if self.crossover > 0:  # MACD crosses above signal
                size = int(self.broker.getcash() * 0.9 / self.data.close[0])
                self.order = self.buy(size=size)
        else:
            if self.crossover < 0:  # MACD crosses below signal
                self.order = self.sell()
    
    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                print(f'BUY EXECUTED: {order.executed.price:.2f}')
            else:
                print(f'SELL EXECUTED: {order.executed.price:.2f}')
        self.order = None 