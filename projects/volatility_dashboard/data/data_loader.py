# data/data_loader.py

import yfinance as yf
import pandas as pd
import numpy as np
from typing import List, Dict, Union
from datetime import datetime, timedelta
import streamlit as st

class MarketDataLoader:
    def __init__(self, symbols: List[str], start_date: str = None, end_date: str = None):
        self.symbols = symbols
        self.start_date = start_date or (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        self.end_date = end_date or datetime.now().strftime('%Y-%m-%d')
        
    def fetch_data(self) -> Dict[str, pd.DataFrame]:
        """Fetch market data for given symbols"""
        data = {}
        
        if not self.symbols:
            st.warning("No symbols selected. Please select at least one symbol.")
            return {}
            
        st.info(f"Fetching data for {len(self.symbols)} symbols...")
        
        for symbol in self.symbols:
            try:
                # Show progress
                st.write(f"Loading data for {symbol}...")
                
                # Create ticker object
                ticker = yf.Ticker(symbol)
                
                # Fetch history with progress indicator
                df = ticker.history(
                    start=self.start_date,
                    end=self.end_date,
                    interval='1d'
                )
                
                # Check if we got any data
                if df.empty:
                    st.warning(f"No data received for {symbol}")
                    continue
                    
                # Calculate returns
                df['Returns'] = df['Close'].pct_change()
                df['Log_Returns'] = np.log(df['Close']/df['Close'].shift(1))
                
                # Store data
                data[symbol] = df
                
                # Show success
                st.success(f"Successfully loaded data for {symbol}")
                
            except Exception as e:
                st.error(f"Error fetching data for {symbol}: {str(e)}")
                continue
        
        if not data:
            st.error("Failed to fetch data for any symbols. Please check symbol names and try again.")
            return {}
            
        return data
    
    def get_returns(self, symbol: str) -> pd.Series:
        """Get returns series for a specific symbol"""
        data = self.fetch_data()
        if symbol in data:
            return data[symbol]['Returns'].dropna()
        return None

    def validate_symbol(self, symbol: str) -> bool:
        """Validate if a symbol exists and has data available"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return True if info else False
        except:
            return False
            
    def get_available_timeframes(self) -> Dict[str, timedelta]:
        """Get available timeframe options"""
        return {
            '1d': timedelta(days=1),
            '5d': timedelta(days=5),
            '1mo': timedelta(days=30),
            '3mo': timedelta(days=90),
            '6mo': timedelta(days=180),
            '1y': timedelta(days=365),
            '2y': timedelta(days=365*2),
            '5y': timedelta(days=365*5)
        }