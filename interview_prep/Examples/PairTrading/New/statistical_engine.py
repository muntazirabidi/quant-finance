"""
Statistical analysis module.
Handles all statistical calculations and signal generation.
"""
from statsmodels.tsa.stattools import coint
from scipy import stats
import numpy as np
import pandas as pd
from typing import Tuple, Dict
from config import TradingConfig

class StatisticalEngine:
    def __init__(self, config: TradingConfig):
        self.config = config
    
    def calculate_spread(self, price_A: pd.Series, price_B: pd.Series) -> Tuple[pd.Series, pd.Series]:
        """Calculate spread and z-score with enhanced statistical methods."""
        # Perform cointegration test
        coint_stat, p_value, critical_values = coint(price_A, price_B)
        
        # Calculate dynamic hedge ratio using Kalman filter
        hedge_ratio = self._calculate_dynamic_hedge_ratio(price_A, price_B)
        
        # Calculate spread
        spread = price_A - hedge_ratio * price_B
        
        # Calculate robust z-score
        zscore = self._calculate_robust_zscore(spread)
        
        return spread, zscore
    
    def _calculate_dynamic_hedge_ratio(self, price_A: pd.Series, 
                                     price_B: pd.Series) -> pd.Series:
        """Calculate hedge ratio using advanced statistical methods."""
        # Implement Kalman filter here
        # For now, using simplified rolling calculation
        return (price_A.rolling(window=self.config.window)
                .cov(price_B) / price_B.rolling(window=self.config.window).var())

    def _calculate_robust_zscore(self, spread: pd.Series) -> pd.Series:
        """Calculate robust z-score with outlier resistance."""
        rolling_mean = spread.rolling(window=self.config.window, 
                                    min_periods=self.config.window).mean()
        rolling_std = spread.rolling(window=self.config.window, 
                                   min_periods=self.config.window).std()
        
        raw_zscore = (spread - rolling_mean) / rolling_std
        return pd.Series(
            stats.mstats.winsorize(raw_zscore, 
                                 limits=self.config.winsorize_limits),
            index=spread.index
        )