"""
Configuration settings for the pairs trading strategy.
This module centralizes all configurable parameters and constants.
"""
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TradingConfig:
    window: int = 30
    z_threshold: float = 1.5
    stop_loss: float = 0.05
    transaction_cost: float = 0.001  # 10 bps per trade
    initial_capital: float = 100000
    trading_days_per_year: int = 252
    winsorize_limits: tuple = (0.05, 0.05)

@dataclass
class DataConfig:
    price_column: str = 'Close'
    min_data_points: int = 100
    min_liquidity_threshold: float = 1000000  # Minimum daily volume in USD

@dataclass
class RiskConfig:
    max_position_size: float = 1.0
    max_correlation: float = 0.95
    max_portfolio_var: float = 0.15
    position_limit_pct: float = 0.1  # Maximum position size as % of portfolio