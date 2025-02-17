# portfolio/risk_manager.py

import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class PositionInfo:
    symbol: str
    size: float
    stop_loss: float
    take_profit: Optional[float]
    risk_amount: float
    position_volatility: float

class PortfolioRiskManager:
    def __init__(self, 
                 portfolio_value: float,
                 max_position_risk: float = 0.02,
                 max_portfolio_risk: float = 0.05):
        self.portfolio_value = portfolio_value
        self.max_position_risk = max_position_risk
        self.max_portfolio_risk = max_portfolio_risk
        self.positions: Dict[str, PositionInfo] = {}
        
    def calculate_position_size(self, 
                              symbol: str,
                              current_price: float,
                              volatility: float,
                              stop_distance_atr: float = 2.0) -> PositionInfo:
        """Calculate optimal position size based on volatility and risk parameters"""
        # Calculate stop loss distance based on volatility
        stop_distance = volatility * stop_distance_atr
        stop_loss = current_price * (1 - stop_distance)
        
        # Calculate risk amount
        risk_amount = self.portfolio_value * self.max_position_risk
        
        # Calculate position size
        price_risk = current_price - stop_loss
        position_size = risk_amount / price_risk
        
        # Adjust for volatility regime
        if volatility > 0.4:  # High volatility regime
            position_size *= 0.5
        elif volatility < 0.15:  # Low volatility regime
            position_size *= 1.2
            
        return PositionInfo(
            symbol=symbol,
            size=position_size,
            stop_loss=stop_loss,
            take_profit=current_price * (1 + stop_distance * 2),  # 2:1 reward-risk
            risk_amount=risk_amount,
            position_volatility=volatility
        )
    
    def update_position(self, symbol: str, position_info: PositionInfo):
        """Update or add new position"""
        self.positions[symbol] = position_info
        
    def calculate_portfolio_risk(self) -> float:
        """Calculate total portfolio risk"""
        total_risk = sum(pos.risk_amount for pos in self.positions.values())
        return total_risk / self.portfolio_value
    
    def get_portfolio_metrics(self) -> Dict:
        """Get current portfolio metrics"""
        return {
            'total_positions': len(self.positions),
            'portfolio_risk': self.calculate_portfolio_risk(),
            'highest_vol_position': max(
                self.positions.items(),
                key=lambda x: x[1].position_volatility,
                default=(None, None)
            )[0],
            'total_risk_amount': sum(pos.risk_amount for pos in self.positions.values())
        }

