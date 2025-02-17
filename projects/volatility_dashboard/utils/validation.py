
# utils/validation.py

from typing import Union, List, Dict
import pandas as pd
import numpy as np

class DataValidator:
    @staticmethod
    def validate_returns(returns: pd.Series) -> bool:
        """Validate returns series"""
        if not isinstance(returns, pd.Series):
            raise ValueError("Returns must be a pandas Series")
            
        if returns.isnull().any():
            raise ValueError("Returns series contains null values")
            
        if len(returns) < 252:  # At least one year of data
            raise ValueError("Insufficient data points")
            
        return True
        
    @staticmethod
    def validate_prices(prices: pd.Series) -> bool:
        """Validate price series"""
        if not isinstance(prices, pd.Series):
            raise ValueError("Prices must be a pandas Series")
            
        if prices.isnull().any():
            raise ValueError("Price series contains null values")
            
        if (prices <= 0).any():
            raise ValueError("Prices must be positive")
            
        return True
        
    @staticmethod
    def validate_portfolio_weights(weights: np.array, tolerance: float = 1e-5) -> bool:
        """Validate portfolio weights"""
        if not isinstance(weights, np.ndarray):
            raise ValueError("Weights must be a numpy array")
            
        if not np.isclose(np.sum(weights), 1.0, rtol=tolerance):
            raise ValueError("Weights must sum to 1")
            
        if (weights < 0).any():
            raise ValueError("Negative weights are not allowed")
            
        return True