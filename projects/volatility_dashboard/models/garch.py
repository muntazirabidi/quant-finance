# models/garch.py

import numpy as np
import pandas as pd
from arch import arch_model
from scipy.stats import norm
from typing import Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class GarchResults:
    volatility: pd.Series
    residuals: pd.Series
    params: Dict
    model_fit: any
    forecasts: Optional[pd.DataFrame] = None

class GarchModel:
    def __init__(self, 
                 returns: pd.Series,
                 p: int = 1,
                 q: int = 1,
                 dist: str = 'normal',
                 vol: str = 'Garch'):
        """
        Initialize GARCH model
        
        Parameters:
        -----------
        returns : pd.Series
            Asset returns
        p : int
            GARCH lag order
        q : int
            ARCH lag order
        dist : str
            Error distribution ('normal', 'studentst', 'skewt')
        vol : str
            Volatility model type ('Garch', 'EGARCH', 'GJR-GARCH')
        """
        self.returns = returns
        self.p = p
        self.q = q
        self.dist = dist
        self.vol = vol
        self.model = None
        self.results = None
        
    def fit(self, update_freq: Optional[int] = None) -> GarchResults:
        """
        Fit GARCH model to returns data
        
        Parameters:
        -----------
        update_freq : int, optional
            Frequency to update the model (e.g., every 5 days)
        
        Returns:
        --------
        GarchResults
            Fitted model results
        """
        # Scale returns for numerical stability
        scaled_returns = self.returns * 100
        
        # Initialize model
        self.model = arch_model(
            scaled_returns,
            p=self.p,
            q=self.q,
            dist=self.dist,
            vol=self.vol,
            rescale=True
        )
        
        # Fit model
        self.results = self.model.fit(
            disp='off',
            update_freq=update_freq,
            show_warning=False
        )
        
        # Scale volatility back to original scale
        volatility = pd.Series(
            self.results.conditional_volatility / 100,
            index=self.returns.index
        )
        
        # Extract residuals
        residuals = pd.Series(
            self.results.resid / self.results.conditional_volatility,
            index=self.returns.index
        )
        
        # Extract parameters
        params = self.results.params.to_dict()
        
        return GarchResults(
            volatility=volatility,
            residuals=residuals,
            params=params,
            model_fit=self.results
        )
    
    def forecast(self, 
                horizon: int = 5, 
                reindex: bool = True) -> pd.DataFrame:
        """
        Generate volatility forecasts
        
        Parameters:
        -----------
        horizon : int
            Forecast horizon
        reindex : bool
            Whether to reindex forecasts to match return dates
            
        Returns:
        --------
        pd.DataFrame
            Volatility forecasts with confidence intervals
        """
        if self.results is None:
            raise ValueError("Model must be fit before forecasting")
            
        # Generate forecasts
        forecasts = self.results.forecast(
            horizon=horizon,
            reindex=reindex
        )
        
        # Extract forecast components
        mean = forecasts.mean.iloc[-1] / 100  # Scale back
        variance = forecasts.variance.iloc[-1] / 10000
        residual_var = self.results.resid.var()
        
        # Calculate confidence intervals
        alpha = 0.05  # 95% confidence level
        z_score = norm.ppf(1 - alpha/2)
        
        std_dev = np.sqrt(variance)
        lower = mean - z_score * std_dev
        upper = mean + z_score * std_dev
        
        # Create forecast DataFrame
        forecast_df = pd.DataFrame({
            'mean': mean,
            'lower': lower,
            'upper': upper,
            'variance': variance
        })
        
        return forecast_df
    
    def simulate_paths(self, 
                      horizon: int = 21, 
                      num_paths: int = 1000) -> np.ndarray:
        """
        Simulate future return paths using fitted GARCH model
        
        Parameters:
        -----------
        horizon : int
            Number of days to simulate
        num_paths : int
            Number of simulation paths
            
        Returns:
        --------
        np.ndarray
            Simulated return paths
        """
        if self.results is None:
            raise ValueError("Model must be fit before simulation")
            
        # Get last volatility estimate
        last_vol = self.results.conditional_volatility[-1]
        
        # Get GARCH parameters
        omega = self.results.params['omega']
        alpha = self.results.params[f'alpha[1]']
        beta = self.results.params[f'beta[1]']
        
        # Initialize arrays
        returns = np.zeros((horizon, num_paths))
        volatility = np.zeros((horizon, num_paths))
        volatility[0] = last_vol
        
        # Simulate paths
        for t in range(1, horizon):
            # Generate random shocks
            epsilon = np.random.standard_normal(num_paths)
            
            # Update volatility
            volatility[t] = np.sqrt(omega + 
                                  alpha * returns[t-1]**2 + 
                                  beta * volatility[t-1]**2)
            
            # Generate returns
            returns[t] = epsilon * volatility[t]
        
        return returns, volatility

    def diagnostic_tests(self) -> Dict:
        """
        Perform diagnostic tests on fitted model
        
        Returns:
        --------
        Dict
            Dictionary of test results
        """
        if self.results is None:
            raise ValueError("Model must be fit before testing")
            
        # Standardized residuals
        std_resid = self.results.resid / self.results.conditional_volatility
        
        # Ljung-Box test for autocorrelation
        from statsmodels.stats.diagnostic import acorr_ljungbox
        lb_test = acorr_ljungbox(std_resid, lags=[10], return_df=True)
        
        # Engle's test for ARCH effects
        from statsmodels.stats.diagnostic import het_arch
        arch_test = het_arch(std_resid)
        
        # Jarque-Bera test for normality
        from scipy.stats import jarque_bera
        jb_test = jarque_bera(std_resid)
        
        return {
            'ljung_box': lb_test,
            'arch_test': arch_test,
            'jarque_bera': jb_test,
            'aic': self.results.aic,
            'bic': self.results.bic
        }