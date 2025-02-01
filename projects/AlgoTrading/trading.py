import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('trading.log'), logging.StreamHandler()]
)

class TradingConfig:
    API_KEY = 'YOUR_API_KEY'
    API_SECRET = 'YOUR_API_SECRET'
    BASE_URL = 'https://paper-api.alpaca.markets'  # Paper trading URL
    SYMBOL = 'SPY'  # ETF for S&P 500
    SHORT_SMA = 20
    LONG_SMA = 50
    ORDER_SIZE = 10  # Number of shares per trade
    POLL_INTERVAL = 60  # Seconds between market data checks

class TradingStrategy:
    def __init__(self):
        self.short_sma = TradingConfig.SHORT_SMA
        self.long_sma = TradingConfig.LONG_SMA
        self.data = pd.DataFrame()
        
    def calculate_indicators(self, new_data):
        """Calculate technical indicators"""
        self.data = pd.concat([self.data, new_data])
        
        # Calculate SMAs
        self.data['short_sma'] = self.data['close'].rolling(self.short_sma).mean()
        self.data['long_sma'] = self.data['close'].rolling(self.long_sma).mean()
        
        # Keep only the most recent data
        self.data = self.data.tail(self.long_sma * 2)
        
    def generate_signal(self):
        """Generate trading signals"""
        if len(self.data) < self.long_sma:
            return None  # Not enough data
        
        last_close = self.data.iloc[-1]
        prev_close = self.data.iloc[-2]
        
        # Check for crossover
        if (prev_close['short_sma'] < prev_close['long_sma'] and
            last_close['short_sma'] > last_close['long_sma']):
            return 'BUY'
        elif (prev_close['short_sma'] > prev_close['long_sma'] and
              last_close['short_sma'] < last_close['long_sma']):
            return 'SELL'
        return None

class PaperTradingBot:
    def __init__(self):
        self.api = tradeapi.REST(
            TradingConfig.API_KEY,
            TradingConfig.API_SECRET,
            TradingConfig.BASE_URL,
            api_version='v2'
        )
        self.strategy = TradingStrategy()
        self.position = 0
        self.equity = []
        
    def get_historical_data(self):
        """Fetch initial historical data"""
        end_date = datetime.utcnow() - timedelta(seconds=1)
        start_date = end_date - timedelta(days=TradingConfig.LONG_SMA*2)
        
        bars = self.api.get_bars(
            TradingConfig.SYMBOL,
            '1Day',
            start=start_date.isoformat(),
            end=end_date.isoformat(),
            limit=TradingConfig.LONG_SMA*2
        ).df
        
        return bars
    
    def check_market_open(self):
        """Check if market is currently open"""
        clock = self.api.get_clock()
        return clock.is_open
    
    def execute_trade(self, signal):
        """Execute paper trade based on signal"""
        try:
            if signal == 'BUY' and self.position <= 0:
                order = self.api.submit_order(
                    symbol=TradingConfig.SYMBOL,
                    qty=TradingConfig.ORDER_SIZE,
                    side='buy',
                    type='market',
                    time_in_force='gtc'
                )
                self.position += TradingConfig.ORDER_SIZE
                logging.info(f"Executed BUY order: {order}")
                
            elif signal == 'SELL' and self.position >= 0:
                order = self.api.submit_order(
                    symbol=TradingConfig.SYMBOL,
                    qty=TradingConfig.ORDER_SIZE,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )
                self.position -= TradingConfig.ORDER_SIZE
                logging.info(f"Executed SELL order: {order}")
                
            self.track_performance()
            
        except Exception as e:
            logging.error(f"Error executing trade: {str(e)}")
    
    def track_performance(self):
        """Track portfolio performance"""
        account = self.api.get_account()
        self.equity.append({
            'timestamp': datetime.utcnow(),
            'equity': float(account.equity),
            'cash': float(account.cash)
        })
    
    def run(self):
        """Main trading loop"""
        logging.info("Initializing trading bot...")
        
        # Initialize with historical data
        self.strategy.data = self.get_historical_data()
        logging.info(f"Loaded {len(self.strategy.data)} historical bars")
        
        while True:
            try:
                if not self.check_market_open():
                    logging.info("Market closed. Sleeping...")
                    time.sleep(TradingConfig.POLL_INTERVAL)
                    continue
                
                # Get latest price data
                latest_bar = self.api.get_bars(
                    TradingConfig.SYMBOL,
                    '1Day',
                    limit=1
                ).df.iloc[-1:]
                
                # Update strategy with new data
                self.strategy.calculate_indicators(latest_bar)
                
                # Generate trading signal
                signal = self.strategy.generate_signal()
                
                if signal:
                    logging.info(f"Generated signal: {signal}")
                    self.execute_trade(signal)
                
                # Wait for next interval
                time.sleep(TradingConfig.POLL_INTERVAL)
                
            except Exception as e:
                logging.error(f"Error in main loop: {str(e)}")
                time.sleep(60)

if __name__ == "__main__":
    bot = PaperTradingBot()
    bot.run()