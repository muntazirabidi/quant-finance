# utils/helpers.py (continued)
from typing import Union, List, Dict
import pandas as pd
import numpy as np

def calculate_rolling_metrics(returns: pd.Series, 
                            window: int = 252) -> pd.DataFrame:
    """Calculate rolling performance metrics"""
    rolling_metrics = pd.DataFrame(index=returns.index)
    
    # Rolling returns
    rolling_metrics['returns'] = returns.rolling(window=window).mean() * 252
    
    # Rolling volatility
    rolling_metrics['volatility'] = returns.rolling(window=window).std() * np.sqrt(252)
    
    # Rolling Sharpe Ratio
    rolling_metrics['sharpe'] = (rolling_metrics['returns'] / rolling_metrics['volatility'])
    
    # Rolling max drawdown
    rolling_metrics['max_drawdown'] = returns.rolling(window=window).apply(
        lambda x: calculate_drawdowns(x).min()
    )
    
    return rolling_metrics

def calculate_var_breaches(returns: pd.Series, 
                          var_percentile: float = 0.95,
                          window: int = 252) -> pd.DataFrame:
    """Calculate VaR breaches"""
    rolling_var = returns.rolling(window=window).quantile(1 - var_percentile)
    breaches = returns < rolling_var
    
    return pd.DataFrame({
        'VaR': rolling_var,
        'Breach': breaches,
        'Cumulative_Breaches': breaches.cumsum()
    })

def format_currency(value: float) -> str:
    """Format value as currency"""
    return f"${value:,.2f}"

def format_percentage(value: float) -> str:
    """Format value as percentage"""
    return f"{value:.2%}"
