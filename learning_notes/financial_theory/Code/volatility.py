import numpy as np
import pandas as pd
from arch import arch_model
from scipy.stats import norm

class VolatilityManager:
    def __init__(self, lookback=30):
        self.lookback = lookback
        
    def calculate_dynamic_volatility(self, returns):
        """Calculate conditional volatility using GARCH(1,1)"""
        # Scale returns as recommended in the warning
        scaled_returns = returns * 100
        model = arch_model(scaled_returns, vol='Garch', p=1, q=1)
        results = model.fit(disp='off')
        # Scale volatility back to original scale
        return results.conditional_volatility / 100
        
    def calculate_position_size(self, current_volatility, base_position, max_risk=0.02):
        """Adjust position size based on current volatility regime"""
        # Use scalar volatility value instead of series
        vol_ratio = float(current_volatility / np.mean(current_volatility))
        adjusted_position = base_position / vol_ratio
        
        # Cap maximum position size
        return min(adjusted_position, base_position * 2)
        
    def calculate_dynamic_stops(self, price, current_volatility, base_stops=0.02):
        """Calculate dynamic stop losses based on volatility"""
        # Use scalar volatility value
        vol_ratio = float(current_volatility)
        dynamic_stops = base_stops * vol_ratio
        return {
            'stop_loss': price * (1 - dynamic_stops),
            'stop_distance': dynamic_stops
        }
        
    def risk_metrics(self, returns, current_volatility, confidence=0.95):
        """Calculate risk metrics accounting for volatility clustering"""
        # Use scalar volatility value
        vol = float(current_volatility)
        
        # Calculate VaR assuming normal distribution but with dynamic volatility
        var = norm.ppf(1 - confidence) * vol
        
        # Calculate expected shortfall
        es = vol * norm.pdf(norm.ppf(1 - confidence)) / (1 - confidence)
        
        return {
            'VaR': var,
            'ES': es,
            'current_vol': vol
        }

def main():
    # Generate sample data
    np.random.seed(42)  # for reproducibility
    returns = pd.Series(np.random.normal(0, 0.01, 1000))
    
    # Initialize manager
    vm = VolatilityManager()
    
    # Calculate dynamic volatility
    volatility = vm.calculate_dynamic_volatility(returns)
    current_vol = volatility.iloc[-1]  # Properly access last element
    
    # Calculate position sizes
    base_position = 100000  # $100k base position
    dynamic_position = vm.calculate_position_size(current_vol, base_position)
    
    # Calculate stops
    current_price = 100
    stops = vm.calculate_dynamic_stops(current_price, current_vol)
    
    # Calculate risk metrics
    risk = vm.risk_metrics(returns, current_vol)
    
    # Print results
    print("\nVolatility Management Analysis:")
    print("-" * 30)
    print(f"Current Volatility: {current_vol:.2%}")
    print(f"Base Position: ${base_position:,.0f}")
    print(f"Adjusted Position: ${dynamic_position:,.0f}")
    print(f"Stop Loss Level: ${stops['stop_loss']:.2f}")
    print(f"Stop Distance: {stops['stop_distance']:.2%}")
    print(f"Daily VaR (95%): {risk['VaR']:.2%}")
    print(f"Expected Shortfall: {risk['ES']:.2%}")

if __name__ == "__main__":
    main()