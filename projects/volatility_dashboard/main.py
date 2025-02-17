# main.py

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List

from config.settings import Config
from config.symbols import STOCK_UNIVERSE
from data.data_loader import MarketDataLoader
from models.volatility import VolatilityAnalyzer
from models.risk_metrics import RiskAnalyzer
from models.garch import GarchModel
from portfolio.risk_manager import PortfolioRiskManager
from portfolio.optimization import PortfolioOptimizer
from visualization.dashboard import VolatilityDashboard
from analysis.clustering import VolatilityClustering
from analysis.regime import RegimeDetector
from visualization.plots import VolatilityPlots

def initialize_session_state():
    """Initialize session state variables"""
    if 'portfolio_value' not in st.session_state:
        st.session_state.portfolio_value = 1000000
    if 'selected_symbols' not in st.session_state:
        st.session_state.selected_symbols = []
    if 'timeframe' not in st.session_state:
        st.session_state.timeframe = '1y'
    if 'analysis_mode' not in st.session_state:
        st.session_state.analysis_mode = 'Basic'

def load_market_data(symbols: List[str], timeframe: str) -> Dict:
    """Load and process market data with error handling"""
    try:
        data_loader = MarketDataLoader(symbols)
        market_data = data_loader.fetch_data()
        
        if not market_data:
            st.error("Failed to fetch market data. Please check your internet connection.")
            return None
            
        return market_data
    except Exception as e:
        st.error(f"Error loading market data: {str(e)}")
        return None

def create_analyzers(market_data: Dict, symbols: List[str]) -> Dict:
    """Initialize analysis components"""
    analyzers = {}
    
    try:
        for symbol in symbols:
            returns = market_data[symbol]['Returns']
            
            # Initialize GARCH model
            garch_model = GarchModel(returns)
            garch_results = garch_model.fit()
            
            # Initialize volatility analyzer with GARCH results
            vol_analyzer = VolatilityAnalyzer(returns)
            vol_analyzer.volatility = garch_results.volatility
            
            # Initialize clustering analysis
            clustering = VolatilityClustering(returns, garch_results.volatility)
            clusters = clustering.identify_clusters()
            
            # Initialize regime detection
            regime_detector = RegimeDetector(garch_results.volatility)
            regimes, regime_stats = regime_detector.detect_regimes()
            
            # Initialize risk analyzer
            risk_analyzer = RiskAnalyzer(returns, garch_results.volatility)
            
            analyzers[symbol] = {
                'volatility': vol_analyzer,
                'risk': risk_analyzer,
                'garch': garch_model,
                'clustering': clustering,
                'regime': regime_detector,
                'results': {
                    'clusters': clusters,
                    'regimes': regimes,
                    'regime_stats': regime_stats
                }
            }
            
        return analyzers
    except Exception as e:
        st.error(f"Error initializing analyzers: {str(e)}")
        return None

def create_sidebar() -> Dict:
    """Create and handle sidebar inputs"""
    st.sidebar.title("Configuration")
    
    # Analysis mode selection
    analysis_mode = st.sidebar.selectbox(
        "Analysis Mode",
        ["Basic", "Advanced"],
        key="analysis_mode"
    )
    
    # Portfolio value input
    portfolio_value = st.sidebar.number_input(
        "Portfolio Value ($)",
        value=st.session_state.portfolio_value,
        min_value=10000
    )
    
    # Timeframe selection
    timeframe = st.sidebar.selectbox(
        "Timeframe",
        ["1m", "3m", "6m", "1y", "2y", "5y"],
        index=3
    )
    
    # Asset class and symbol selection
    asset_class = st.sidebar.selectbox(
        "Select Asset Class",
        list(STOCK_UNIVERSE.keys())
    )
    
    symbols = st.sidebar.multiselect(
        "Select Symbols",
        STOCK_UNIVERSE[asset_class],
        default=[STOCK_UNIVERSE[asset_class][0]]
    )
    
    # Advanced settings
    if analysis_mode == "Advanced":
        with st.sidebar.expander("Advanced Settings"):
            garch_p = st.number_input("GARCH p", value=1, min_value=1, max_value=5)
            garch_q = st.number_input("GARCH q", value=1, min_value=1, max_value=5)
            confidence_level = st.slider("Confidence Level", 0.9, 0.99, 0.95)
            
        advanced_settings = {
            'garch_p': garch_p,
            'garch_q': garch_q,
            'confidence_level': confidence_level
        }
    else:
        advanced_settings = None
    
    return {
        'mode': analysis_mode,
        'portfolio_value': portfolio_value,
        'timeframe': timeframe,
        'symbols': symbols,
        'advanced_settings': advanced_settings
    }

def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="Volatility Clustering Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Create sidebar and get configurations
    config = create_sidebar()
    
    # Load market data
    market_data = load_market_data(config['symbols'], config['timeframe'])
    if market_data is None:
        return
    
    # Initialize analyzers
    analyzers = create_analyzers(market_data, config['symbols'])
    if analyzers is None:
        return
    
    # Initialize portfolio manager and optimizer
    portfolio_manager = PortfolioRiskManager(config['portfolio_value'])
    portfolio_optimizer = PortfolioOptimizer(
        pd.DataFrame({symbol: market_data[symbol]['Returns'] for symbol in config['symbols']})
    )
    
    # Initialize plotting
    plotter = VolatilityPlots()
    
    # Create and display dashboard
    dashboard = VolatilityDashboard(
        market_data=market_data,
        analyzers=analyzers,
        portfolio_manager=portfolio_manager,
        portfolio_optimizer=portfolio_optimizer,
        plotter=plotter,
        mode=config['mode']
    )
    
    try:
        dashboard.create_dashboard()
    except Exception as e:
        st.error(f"Error creating dashboard: {str(e)}")
        st.error("Please try refreshing the page or selecting different symbols.")

if __name__ == "__main__":
    main()