# config/settings.py

class Config:
    # Data parameters
    DEFAULT_TIMEFRAME = '1d'
    LOOKBACK_PERIOD = 252  # One trading year
    
    # Model parameters
    GARCH_P = 1
    GARCH_Q = 1
    CONFIDENCE_LEVEL = 0.95
    
    # Portfolio parameters
    MAX_POSITION_SIZE = 0.2  # 20% of portfolio
    BASE_STOP_LOSS = 0.02   # 2% initial stop
    
    # Visualization parameters
    UPDATE_INTERVAL = 60    # Update every 60 seconds
    PLOT_HEIGHT = 600
    PLOT_WIDTH = 1000
    
    # Risk management
    MAX_DRAWDOWN = 0.25     # 25% maximum drawdown
    RISK_FREE_RATE = 0.03   # 3% risk-free rate
    
    # Regime detection
    REGIME_THRESHOLD = 1.5   # Volatility multiplier for regime change
    MIN_REGIME_DAYS = 5     # Minimum days for regime confirmation

