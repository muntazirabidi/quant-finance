# visualization/dashboard.py

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict

class VolatilityDashboard:
    def __init__(self, market_data, analyzers, portfolio_manager):
        self.market_data = market_data
        self.analyzers = analyzers
        self.portfolio_manager = portfolio_manager

    def create_dashboard(self):
        st.title('Volatility Clustering Analysis Dashboard')
        
        # Get selected symbol from sidebar if not already selected
        if 'selected_symbol' not in st.session_state:
            st.session_state.selected_symbol = list(self.market_data.keys())[0]
            
        selected_symbol = st.selectbox(
            'Select Symbol for Detailed Analysis',
            list(self.market_data.keys()),
            key='selected_symbol'
        )
        
        # Create tabs for different analyses
        tabs = st.tabs(['Price & Returns', 'Volatility Analysis', 'Risk Metrics'])
        
        with tabs[0]:
            self.plot_price_and_returns(selected_symbol)
            
        with tabs[1]:
            self.plot_volatility_analysis(selected_symbol)
            
        with tabs[2]:
            self.plot_risk_metrics(selected_symbol)

    def plot_price_and_returns(self, symbol: str):
        """Plot price and returns charts"""
        data = self.market_data[symbol]
        
        # Create figure with secondary y-axis
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
        
        # Add candlestick
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name='Price'
            ),
            row=1, col=1
        )
        
        # Add returns
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data['Returns'],
                name='Returns',
                line=dict(color='blue')
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=800,
            title=f'{symbol} Price and Returns',
            xaxis_title='Date',
            yaxis_title='Price',
            yaxis2_title='Returns'
        )
        
        st.plotly_chart(fig, use_container_width=True)

    def plot_volatility_analysis(self, symbol: str):
        """Plot volatility analysis charts"""
        analyzer = self.analyzers[symbol]['volatility']
        
        # Create volatility plot
        fig = go.Figure()
        
        # Add volatility line
        fig.add_trace(
            go.Scatter(
                x=analyzer.volatility.index,
                y=analyzer.volatility,
                name='Rolling Volatility',
                line=dict(color='red')
            )
        )
        
        # Add moving average
        ma_vol = analyzer.volatility.rolling(window=21).mean()
        fig.add_trace(
            go.Scatter(
                x=ma_vol.index,
                y=ma_vol,
                name='21-day MA',
                line=dict(color='blue', dash='dash')
            )
        )
        
        fig.update_layout(
            height=500,
            title=f'{symbol} Volatility Analysis',
            xaxis_title='Date',
            yaxis_title='Volatility'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Add volatility distribution
        fig_dist = go.Figure()
        fig_dist.add_trace(
            go.Histogram(
                x=analyzer.volatility.dropna(),
                nbinsx=50,
                name='Volatility Distribution'
            )
        )
        
        fig_dist.update_layout(
            height=400,
            title=f'{symbol} Volatility Distribution',
            xaxis_title='Volatility',
            yaxis_title='Frequency'
        )
        
        st.plotly_chart(fig_dist, use_container_width=True)

    def plot_risk_metrics(self, symbol: str):
        """Plot risk metrics"""
        analyzer = self.analyzers[symbol]['risk']
        data = self.market_data[symbol]
        
        # Calculate rolling risk metrics
        window = 252  # One year
        rolling_data = pd.DataFrame({
            'Returns': data['Returns'],
            'Volatility': data['Returns'].rolling(window=window).std() * np.sqrt(252),
            'Sharpe': (data['Returns'].rolling(window=window).mean() * 252) / 
                     (data['Returns'].rolling(window=window).std() * np.sqrt(252))
        })
        
        # Create metrics plot
        fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
        
        # Add returns
        fig.add_trace(
            go.Scatter(
                x=rolling_data.index,
                y=rolling_data['Returns'],
                name='Returns'
            ),
            row=1, col=1
        )
        
        # Add volatility
        fig.add_trace(
            go.Scatter(
                x=rolling_data.index,
                y=rolling_data['Volatility'],
                name='Volatility'
            ),
            row=2, col=1
        )
        
        # Add Sharpe ratio
        fig.add_trace(
            go.Scatter(
                x=rolling_data.index,
                y=rolling_data['Sharpe'],
                name='Sharpe Ratio'
            ),
            row=3, col=1
        )
        
        fig.update_layout(
            height=900,
            title=f'{symbol} Risk Metrics',
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Display summary statistics
        st.subheader('Summary Statistics')
        stats = pd.DataFrame({
            'Metric': ['Annual Return', 'Annual Volatility', 'Sharpe Ratio'],
            'Value': [
                f"{(rolling_data['Returns'].mean() * 252 * 100):.2f}%",
                f"{(rolling_data['Volatility'].mean() * 100):.2f}%",
                f"{rolling_data['Sharpe'].mean():.2f}"
            ]
        })
        
        st.table(stats)