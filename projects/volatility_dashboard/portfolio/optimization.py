# portfolio/optimization.py
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional

class PortfolioOptimizer:
    def __init__(self, returns: pd.DataFrame, risk_free_rate: float = 0.02):
        self.returns = returns
        self.risk_free_rate = risk_free_rate
        
    def calculate_optimal_weights(self, 
                                target_volatility: float,
                                constraints: Optional[Dict] = None) -> np.array:
        """Calculate optimal portfolio weights using mean-variance optimization"""
        n_assets = len(self.returns.columns)
        
        # Calculate mean returns and covariance
        mean_returns = self.returns.mean() * 252  # Annualized
        cov_matrix = self.returns.cov() * 252
        
        def portfolio_volatility(weights):
            return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        def portfolio_return(weights):
            return np.sum(mean_returns * weights)
        
        # Optimization constraints
        constraints = []
        constraints.append({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights sum to 1
        
        if target_volatility:
            constraints.append({
                'type': 'eq',
                'fun': lambda x: portfolio_volatility(x) - target_volatility
            })
            
        # Bounds for weights (0 to 1)
        bounds = tuple((0, 1) for _ in range(n_assets))
        
        # Objective function (Sharpe Ratio)
        def objective(weights):
            ret = portfolio_return(weights)
            vol = portfolio_volatility(weights)
            return -(ret - self.risk_free_rate) / vol
            
        # Optimize
        result = minimize(
            objective,
            n_assets * [1./n_assets],
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result.x
        
    def calculate_efficient_frontier(self, 
                                   points: int = 50) -> pd.DataFrame:
        """Calculate efficient frontier points"""
        min_vol = self.calculate_minimum_volatility()
        max_ret = self.calculate_maximum_return()
        
        target_vols = np.linspace(min_vol, max_ret['volatility'], points)
        efficient_points = []
        
        for target_vol in target_vols:
            weights = self.calculate_optimal_weights(target_vol)
            ret = np.sum(self.returns.mean() * 252 * weights)
            efficient_points.append({
                'return': ret,
                'volatility': target_vol,
                'sharpe': (ret - self.risk_free_rate) / target_vol
            })
            
        return pd.DataFrame(efficient_points)