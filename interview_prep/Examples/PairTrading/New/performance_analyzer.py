"""
Performance analysis module.
Calculates and reports strategy performance metrics.
"""
import pandas as pd
import numpy as np
from typing import Dict, Any
from config import TradingConfig

class PerformanceAnalyzer:
    def __init__(self, config: TradingConfig):
        self.config = config
    
    def calculate_metrics(self, returns: pd.Series, 
                         portfolio_value: pd.Series) -> Dict[str, Any]:
        """Calculate comprehensive performance metrics."""
        # Basic return metrics
        total_return = (portfolio_value.iloc[-1] / 
                       portfolio_value.iloc[0]) - 1
        
        # Risk-adjusted metrics
        sharpe = self._calculate_sharpe_ratio(returns)
        sortino = self._calculate_sortino_ratio(returns)
        
        # Risk metrics
        max_drawdown = self._calculate_max_drawdown(portfolio_value)
        
        # Trading metrics
        win_rate = (returns > 0).mean()
        
        return {
            'total_return': total_return,
            'sharpe_ratio': sharpe,
            'sortino_ratio': sortino,
            'max_drawdown': max_drawdown,
            'win_rate': win_rate
        }