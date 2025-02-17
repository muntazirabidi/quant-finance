
# analysis/regime.py

from enum import Enum
from typing import List, Tuple
import numpy as np
import pandas as pd
from scipy import stats

class VolatilityRegime(Enum):
    LOW = 'Low Volatility'
    NORMAL = 'Normal Volatility'
    HIGH = 'High Volatility'
    EXTREME = 'Extreme Volatility'

class RegimeDetector:
    def __init__(self, 
                 volatility: pd.Series,
                 lookback: int = 252,
                 smooth_window: int = 21):
        self.volatility = volatility
        self.lookback = lookback
        self.smooth_window = smooth_window
        
    def detect_regimes(self) -> Tuple[pd.Series, pd.DataFrame]:
        """Detect volatility regimes using statistical approach"""
        # Calculate smoothed volatility
        smooth_vol = self.volatility.rolling(window=self.smooth_window).mean()
        
        # Calculate rolling statistics
        roll_mean = smooth_vol.rolling(window=self.lookback).mean()
        roll_std = smooth_vol.rolling(window=self.lookback).std()
        
        # Calculate z-scores
        z_scores = (smooth_vol - roll_mean) / roll_std
        
        # Classify regimes
        regimes = pd.Series(index=z_scores.index)
        regimes[z_scores <= -1] = VolatilityRegime.LOW.value
        regimes[(z_scores > -1) & (z_scores <= 1)] = VolatilityRegime.NORMAL.value
        regimes[(z_scores > 1) & (z_scores <= 2)] = VolatilityRegime.HIGH.value
        regimes[z_scores > 2] = VolatilityRegime.EXTREME.value
        
        # Calculate regime statistics
        regime_stats = self.calculate_regime_statistics(regimes)
        
        return regimes, regime_stats
        
    def calculate_regime_statistics(self, regimes: pd.Series) -> pd.DataFrame:
        """Calculate statistics for each regime"""
        stats_list = []
        
        for regime in VolatilityRegime:
            mask = regimes == regime.value
            if not any(mask):
                continue
                
            regime_vol = self.volatility[mask]
            regime_stats = {
                'regime': regime.value,
                'count': len(regime_vol),
                'avg_volatility': regime_vol.mean(),
                'std_volatility': regime_vol.std(),
                'max_volatility': regime_vol.max(),
                'min_volatility': regime_vol.min(),
                'persistence': self.calculate_persistence(regimes, regime.value)
            }
            stats_list.append(regime_stats)
            
        return pd.DataFrame(stats_list)
        
    def calculate_persistence(self, regimes: pd.Series, regime_value: str) -> float:
        """Calculate persistence probability of a regime"""
        regime_changes = (regimes != regimes.shift(1)).astype(int)
        regime_durations = []
        current_duration = 0
        
        for i in range(len(regimes)):
            if regimes.iloc[i] == regime_value:
                current_duration += 1
            elif current_duration > 0:
                regime_durations.append(current_duration)
                current_duration = 0
                
        if current_duration > 0:
            regime_durations.append(current_duration)
            
        return np.mean(regime_durations) if regime_durations else 0