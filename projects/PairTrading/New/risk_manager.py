"""
Risk management module.
Handles position sizing, stop-losses, and portfolio-level risk management.
"""
import pandas as pd
import numpy as np
from typing import Dict, Tuple
from config import RiskConfig

class RiskManager:
    def __init__(self, config: RiskConfig):
        self.config = config
    
    def calculate_position_size(self, zscore: pd.Series, 
                              current_portfolio_value: float,
                              pair_correlation: float) -> pd.Series:
        """Calculate position size with multiple risk constraints."""
        # Base position size from z-score
        raw_position_size = np.minimum(
            np.abs(zscore) / self.config.max_position_size,
            1.0
        )
        
        # Adjust for correlation
        correlation_factor = 1 - (pair_correlation / self.config.max_correlation)
        position_size = raw_position_size * correlation_factor
        
        # Apply portfolio-level constraints
        max_position = (current_portfolio_value * 
                       self.config.position_limit_pct)
        
        return np.minimum(position_size, max_position)

    def apply_stop_loss(self, position: pd.Series, 
                       cumulative_returns: pd.Series) -> pd.Series:
        """Apply stop-loss and dynamic risk management."""
        drawdown = (cumulative_returns / 
                   cumulative_returns.expanding().max() - 1)
        
        return np.where(drawdown < -self.config.stop_loss, 0, position)