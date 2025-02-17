# models/volatility.py

import numpy as np
import pandas as pd
from arch import arch_model
from typing import Tuple, Dict, Optional
from dataclasses import dataclass
from scipy import stats

@dataclass
class VolatilityRegime:
    current_volatility: float
    historical_volatility: float
    regime: str
    risk_factor: float

class VolatilityAnalyzer:
    def __init__(self, returns: pd.Series, lookback: int = 252):
        # Data cleaning and validation
        self.returns = self._clean_returns(returns)
        self.lookback = lookback
        self.model = None
        self.result = None
        self.volatility = None
        
        # Initial volatility calculation (simple)
        self._calculate_simple_volatility()
        
    def _clean_returns(self, returns: pd.Series) -> pd.Series:
        """Clean returns data thoroughly"""
        if returns is None or returns.empty:
            raise ValueError("Returns series is empty or None")
            
        # Remove any non-numeric values
        clean_returns = pd.to_numeric(returns, errors='coerce')
        
        # Remove inf, -inf
        clean_returns = clean_returns.replace([np.inf, -np.inf], np.nan)
        
        # Remove NaN values
        clean_returns = clean_returns.dropna()
        
        # Remove extreme outliers (> 5 standard deviations)
        mean = clean_returns.mean()
        std = clean_returns.std()
        clean_returns = clean_returns[
            (clean_returns > mean - 5 * std) & 
            (clean_returns < mean + 5 * std)
        ]
        
        if clean_returns.empty:
            raise ValueError("No valid returns data after cleaning")
            
        return clean_returns
        
    def _calculate_simple_volatility(self, window: int = 21):
        """Calculate simple rolling volatility as backup"""
        try:
            self.volatility = self.returns.rolling(
                window=window,
                min_periods=1
            ).std() * np.sqrt(252)
        except Exception as e:
            raise ValueError(f"Error calculating simple volatility: {str(e)}")
    
    def fit_garch(self) -> None:
        """Fit GARCH(1,1) model to returns with robust error handling"""
        try:
            # Scale returns for numerical stability
            scaled_returns = self.returns * 100
            
            # Additional validation
            if scaled_returns.isnull().any():
                raise ValueError("NaN values found in scaled returns")
            
            if scaled_returns.empty:
                raise ValueError("No data available for GARCH fitting")
            
            # Initialize and fit GARCH model
            self.model = arch_model(
                scaled_returns,
                vol='Garch',
                p=1,
                q=1,
                rescale=True
            )
            
            self.result = self.model.fit(
                disp='off',
                show_warning=False,
                update_freq=0
            )
            
            # Scale volatility back to original scale
            self.volatility = pd.Series(
                self.result.conditional_volatility / 100,
                index=self.returns.index
            )
            
            # Validate output
            if self.volatility.isnull().any():
                print("Warning: NaN values in GARCH volatility, using simple volatility")
                self._calculate_simple_volatility()
                
        except Exception as e:
            print(f"GARCH fitting failed: {str(e)}, using simple volatility")
            self._calculate_simple_volatility()
    
    def detect_regime(self) -> VolatilityRegime:
        """Detect current volatility regime"""
        if self.volatility is None:
            self._calculate_simple_volatility()
            
        try:
            current_vol = self.volatility.iloc[-1]
            hist_vol = self.volatility.mean()
            
            # Ensure values are finite
            if not (np.isfinite(current_vol) and np.isfinite(hist_vol)):
                raise ValueError("Non-finite values in volatility")
            
            vol_ratio = current_vol / hist_vol if hist_vol != 0 else 1.0
            
            if vol_ratio > 1.5:
                regime = 'High Volatility'
                risk_factor = 0.5
            elif vol_ratio < 0.7:
                regime = 'Low Volatility'
                risk_factor = 1.2
            else:
                regime = 'Normal Volatility'
                risk_factor = 1.0
                
            return VolatilityRegime(
                current_volatility=float(current_vol),
                historical_volatility=float(hist_vol),
                regime=regime,
                risk_factor=risk_factor
            )
        except Exception as e:
            # Return default regime if calculation fails
            return VolatilityRegime(
                current_volatility=0.0,
                historical_volatility=0.0,
                regime='Error',
                risk_factor=1.0
            )
    
    def calculate_clusters(self) -> Dict[str, pd.Series]:
        """Identify volatility clusters"""
        if self.volatility is None:
            self._calculate_simple_volatility()
            
        try:
            # Calculate thresholds using mean and standard deviation
            vol_mean = self.volatility.mean()
            vol_std = self.volatility.std()
            
            # Create masks for different volatility regimes
            high_vol = self.volatility > (vol_mean + vol_std)
            low_vol = self.volatility < (vol_mean - vol_std)
            normal_vol = ~(high_vol | low_vol)
            
            # Calculate cluster persistence
            high_vol_persistence = self._calculate_cluster_persistence(high_vol)
            low_vol_persistence = self._calculate_cluster_persistence(low_vol)
            
            # Only include clusters that persist for at least 5 days
            high_vol = high_vol & (high_vol_persistence >= 5)
            low_vol = low_vol & (low_vol_persistence >= 5)
            normal_vol = ~(high_vol | low_vol)
            
            return {
                'high_volatility': high_vol,
                'low_volatility': low_vol,
                'normal_volatility': normal_vol
            }
        except Exception as e:
            print(f"Error calculating clusters: {str(e)}")
            # Return empty clusters if calculation fails
            empty_series = pd.Series(False, index=self.volatility.index)
            return {
                'high_volatility': empty_series,
                'low_volatility': empty_series,
                'normal_volatility': empty_series
            }
    
    def _calculate_cluster_persistence(self, mask: pd.Series) -> pd.Series:
        """Calculate how long each regime persists"""
        persistence = pd.Series(0, index=mask.index)
        current_count = 0
        
        for i, value in enumerate(mask):
            if value:
                current_count += 1
            else:
                current_count = 0
            persistence.iloc[i] = current_count
            
        return persistence

    def forecast_volatility(self, horizon: int = 5) -> pd.Series:
        """Forecast volatility for next n days"""
        if self.model is None:
            self.fit_garch()
            
        try:
            forecasts = self.result.forecast(horizon=horizon)
            return np.sqrt(forecasts.variance.iloc[-1])
        except Exception as e:
            print(f"Error forecasting volatility: {str(e)}")
            # Return current volatility as forecast if forecasting fails
            return pd.Series([self.volatility.iloc[-1]] * horizon)

    def analyze_volatility_jumps(self) -> Dict[str, pd.Series]:
        """Analyze significant volatility jumps"""
        if self.volatility is None:
            self._calculate_simple_volatility()
            
        try:
            # Calculate daily changes in volatility
            vol_changes = self.volatility.pct_change()
            
            # Define significant jumps (>2 standard deviations)
            std_changes = vol_changes.std()
            significant_up = vol_changes > (2 * std_changes)
            significant_down = vol_changes < (-2 * std_changes)
            
            return {
                'up_jumps': significant_up,
                'down_jumps': significant_down,
                'jump_sizes': vol_changes[significant_up | significant_down]
            }
        except Exception as e:
            print(f"Error analyzing volatility jumps: {str(e)}")
            return {}
            
    def get_summary_statistics(self) -> Dict[str, float]:
        """Calculate summary statistics for volatility"""
        try:
            stats = {
                'mean_volatility': self.volatility.mean(),
                'median_volatility': self.volatility.median(),
                'std_volatility': self.volatility.std(),
                'skew': stats.skew(self.volatility),
                'kurtosis': stats.kurtosis(self.volatility),
                'min_volatility': self.volatility.min(),
                'max_volatility': self.volatility.max(),
                'current_volatility': self.volatility.iloc[-1],
                'volatility_of_volatility': self.volatility.std() / self.volatility.mean()
            }
            return stats
        except Exception as e:
            print(f"Error calculating summary statistics: {str(e)}")
            return {}