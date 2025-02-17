
# models/risk_metrics.py
import numpy as np
import pandas as pd
from arch import arch_model
from scipy.stats import norm
from typing import Dict, Tuple, Optional
from dataclasses import dataclass

class RiskAnalyzer:
    def __init__(self, returns: pd.Series, volatility: pd.Series):
        self.returns = returns
        self.volatility = volatility
        
    def calculate_var(self, confidence: float = 0.95) -> float:
        """Calculate Value at Risk"""
        return norm.ppf(1 - confidence) * self.volatility.iloc[-1]
        
    def calculate_expected_shortfall(self, confidence: float = 0.95) -> float:
        """Calculate Expected Shortfall"""
        var = self.calculate_var(confidence)
        return -self.returns[self.returns < -var].mean()
        
    def stress_test(self, scenarios: Dict[str, float]) -> pd.Series:
        """Perform stress testing under different scenarios"""
        results = {}
        for scenario, shock in scenarios.items():
            results[scenario] = self.returns.mean() + shock * self.volatility.iloc[-1]
        return pd.Series(results)