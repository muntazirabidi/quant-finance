
# data/market_data.py
import pandas as pd
import numpy as np
from typing import Dict

class MarketData:
    def __init__(self, data: Dict[str, pd.DataFrame]):
        self.data = data
        
    def calculate_correlation_matrix(self) -> pd.DataFrame:
        """Calculate correlation matrix of returns"""
        returns = pd.DataFrame({
            symbol: data['Returns'] for symbol, data in self.data.items()
        })
        return returns.corr()
    
    def calculate_volatility(self, window: int = 30) -> Dict[str, pd.Series]:
        """Calculate rolling volatility for all symbols"""
        volatilities = {}
        for symbol, data in self.data.items():
            volatilities[symbol] = data['Returns'].rolling(window=window).std() * np.sqrt(252)
        return volatilities
    
    def get_latest_prices(self) -> pd.Series:
        """Get latest prices for all symbols"""
        return pd.Series({
            symbol: data['Close'].iloc[-1] for symbol, data in self.data.items()
        })