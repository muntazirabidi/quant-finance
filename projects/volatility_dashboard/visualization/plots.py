# visualization/plots.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
import seaborn as sns
import matplotlib.pyplot as plt

class VolatilityPlots:
    def __init__(self, 
                 height: int = 600, 
                 width: int = 1000,
                 template: str = 'plotly_white'):
        self.height = height
        self.width = width
        self.template = template
        
    def plot_volatility_series(self,
                             volatility: pd.Series,
                             regimes: Optional[pd.Series] = None,
                             title: str = "Volatility Time Series") -> go.Figure:
        """Plot volatility time series with optional regime highlighting"""
        fig = go.Figure()
        
        # Add volatility line
        fig.add_trace(
            go.Scatter(
                x=volatility.index,
                y=volatility,
                name='Volatility',
                line=dict(color='blue')
            )
        )
        
        # Add regime backgrounds if provided
        if regimes is not None:
            regime_colors = {
                'Low Volatility': 'rgba(0, 255, 0, 0.1)',
                'Normal Volatility': 'rgba(255, 255, 0, 0.1)',
                'High Volatility': 'rgba(255, 0, 0, 0.1)',
                'Extreme Volatility': 'rgba(128, 0, 0, 0.1)'
            }
            
            for regime in regime_colors:
                mask = regimes == regime
                if mask.any():
                    fig.add_trace(
                        go.Scatter(
                            x=volatility.index[mask],
                            y=volatility[mask],
                            fill='tozeroy',
                            fillcolor=regime_colors[regime],
                            name=regime,
                            showlegend=True
                        )
                    )
        
        fig.update_layout(
            title=title,
            height=self.height,
            width=self.width,
            template=self.template,
            xaxis_title="Date",
            yaxis_title="Volatility",
            showlegend=True
        )
        
        return fig
    
    def plot_returns_volatility(self,
                              returns: pd.Series,
                              volatility: pd.Series,
                              clusters: Optional[pd.Series] = None) -> go.Figure:
        """Plot returns and volatility with optional cluster highlighting"""
        fig = make_subplots(
            rows=2, 
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=('Returns', 'Volatility')
        )
        
        # Plot returns
        fig.add_trace(
            go.Scatter(
                x=returns.index,
                y=returns,
                name='Returns',
                line=dict(color='blue')
            ),
            row=1, col=1
        )
        
        # Plot volatility
        fig.add_trace(
            go.Scatter(
                x=volatility.index,
                y=volatility,
                name='Volatility',
                line=dict(color='red')
            ),
            row=2, col=1
        )
        
        # Add cluster highlighting if provided
        if clusters is not None:
            cluster_colors = ['rgba(255,0,0,0.1)', 'rgba(0,255,0,0.1)', 'rgba(0,0,255,0.1)']
            for i in range(len(np.unique(clusters))):
                mask = clusters == i
                fig.add_trace(
                    go.Scatter(
                        x=returns.index[mask],
                        y=returns[mask],
                        fill='tozeroy',
                        fillcolor=cluster_colors[i],
                        name=f'Cluster {i}',
                        showlegend=True
                    ),
                    row=1, col=1
                )
        
        fig.update_layout(
            height=self.height,
            width=self.width,
            template=self.template,
            showlegend=True
        )
        
        return fig
    
    def plot_garch_forecast(self,
                          volatility: pd.Series,
                          forecast: pd.DataFrame,
                          confidence_level: float = 0.95) -> go.Figure:
        """Plot GARCH volatility forecast with confidence intervals"""
        fig = go.Figure()
        
        # Historical volatility
        fig.add_trace(
            go.Scatter(
                x=volatility.index,
                y=volatility,
                name='Historical Volatility',
                line=dict(color='blue')
            )
        )
        
        # Forecast mean
        fig.add_trace(
            go.Scatter(
                x=forecast.index,
                y=forecast['mean'],
                name='Forecast',
                line=dict(color='red', dash='dash')
            )
        )
        
        # Confidence intervals
        fig.add_trace(
            go.Scatter(
                x=forecast.index,
                y=forecast['upper'],
                fill=None,
                mode='lines',
                line=dict(color='red', width=0),
                showlegend=False
            )
        )
        
        fig.add_trace(
            go.Scatter(
                x=forecast.index,
                y=forecast['lower'],
                fill='tonexty',
                mode='lines',
                line=dict(color='red', width=0),
                name=f'{confidence_level*100}% Confidence Interval'
            )
        )
        
        fig.update_layout(
            title='Volatility Forecast',
            height=self.height,
            width=self.width,
            template=self.template,
            xaxis_title="Date",
            yaxis_title="Volatility",
            showlegend=True
        )
        
        return fig
    
    def plot_simulation_paths(self,
                            returns: np.ndarray,
                            volatility: np.ndarray,
                            num_paths: int = 100) -> go.Figure:
        """Plot simulated return and volatility paths"""
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=('Simulated Returns', 'Simulated Volatility')
        )
        
        # Plot return paths
        for i in range(min(num_paths, returns.shape[1])):
            fig.add_trace(
                go.Scatter(
                    y=returns[:, i],
                    mode='lines',
                    line=dict(width=1, color='blue'),
                    opacity=0.1,
                    showlegend=False
                ),
                row=1, col=1
            )
            
        # Plot volatility paths
        for i in range(min(num_paths, volatility.shape[1])):
            fig.add_trace(
                go.Scatter(
                    y=volatility[:, i],
                    mode='lines',
                    line=dict(width=1, color='red'),
                    opacity=0.1,
                    showlegend=False
                ),
                row=2, col=1
            )
            
        # Add mean paths
        fig.add_trace(
            go.Scatter(
                y=returns.mean(axis=1),
                mode='lines',
                line=dict(width=2, color='black'),
                name='Mean Return Path'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(
                y=volatility.mean(axis=1),
                mode='lines',
                line=dict(width=2, color='black'),
                name='Mean Volatility Path'
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=self.height,
            width=self.width,
            template=self.template,
            showlegend=True
        )
        
        return fig

    def plot_rolling_metrics(self,
                           metrics: pd.DataFrame,
                           title: str = "Rolling Performance Metrics") -> go.Figure:
        """Plot rolling performance metrics"""
        fig = make_subplots(
            rows=len(metrics.columns),
            cols=1,
            subplot_titles=metrics.columns,
            vertical_spacing=0.05
        )
        
        for i, col in enumerate(metrics.columns, 1):
            fig.add_trace(
                go.Scatter(
                    x=metrics.index,
                    y=metrics[col],
                    name=col,
                    line=dict(width=1)
                ),
                row=i, col=1
            )
            
        fig.update_layout(
            height=self.height,
            width=self.width,
            title=title,
            template=self.template,
            showlegend=True
        )
        
        return fig

    def plot_regime_heatmap(self,
                           correlation_matrix: pd.DataFrame,
                           regime: str,
                           title: str = None) -> go.Figure:
        """Plot correlation heatmap for different regimes"""
        fig = go.Figure(data=go.Heatmap(
            z=correlation_matrix.values,
            x=correlation_matrix.columns,
            y=correlation_matrix.index,
            colorscale='RdBu',
            zmin=-1,
            zmax=1
        ))
        
        fig.update_layout(
            title=title or f'Correlation Matrix - {regime} Regime',
            height=self.height,
            width=self.width,
            template=self.template
        )
        
        return fig

    def plot_volatility_surface(self,
                              dates: pd.DatetimeIndex,
                              horizons: List[int],
                              volatility_surface: np.ndarray) -> go.Figure:
        """Plot volatility term structure surface"""
        fig = go.Figure(data=[
            go.Surface(
                x=np.arange(len(dates)),
                y=horizons,
                z=volatility_surface,
                colorscale='Viridis'
            )
        ])
        
        fig.update_layout(
            title='Volatility Term Structure Surface',
            scene=dict(
                xaxis_title='Time',
                yaxis_title='Horizon',
                zaxis_title='Volatility'
            ),
            height=self.height,
            width=self.width,
            template=self.template
        )
        
        # Update x-axis labels with dates
        fig.update_layout(
            scene=dict(
                xaxis=dict(
                    ticktext=dates.strftime('%Y-%m-%d'),
                    tickvals=list(range(len(dates)))
                )
            )
        )
        
        return fig

    def plot_risk_metrics(self,
                         var_data: pd.DataFrame,
                         returns: pd.Series) -> go.Figure:
        """Plot VaR and return breaches"""
        fig = go.Figure()
        
        # Plot returns
        fig.add_trace(
            go.Scatter(
                x=returns.index,
                y=returns,
                name='Returns',
                line=dict(color='blue')
            )
        )
        
        # Plot VaR
        fig.add_trace(
            go.Scatter(
                x=var_data.index,
                y=-var_data['VaR'],
                name='VaR',
                line=dict(color='red')
            )
        )
        
        # Highlight breaches
        breach_dates = var_data.index[var_data['Breach']]
        breach_values = returns[breach_dates]
        
        fig.add_trace(
            go.Scatter(
                x=breach_dates,
                y=breach_values,
                mode='markers',
                name='VaR Breaches',
                marker=dict(color='red', size=10)
            )
        )
        
        fig.update_layout(
            title='Value at Risk and Breaches',
            height=self.height,
            width=self.width,
            template=self.template,
            xaxis_title="Date",
            yaxis_title="Returns",
            showlegend=True
        )
        
        return fig

    def plot_efficient_frontier(self,
                              efficient_points: pd.DataFrame,
                              current_portfolio: Optional[Tuple[float, float]] = None) -> go.Figure:
        """Plot efficient frontier with optional current portfolio position"""
        fig = go.Figure()
        
        # Plot efficient frontier
        fig.add_trace(
            go.Scatter(
                x=efficient_points['volatility'],
                y=efficient_points['return'],
                mode='lines',
                name='Efficient Frontier',
                line=dict(color='blue')
            )
        )
        
        # Add current portfolio if provided
        if current_portfolio is not None:
            fig.add_trace(
                go.Scatter(
                    x=[current_portfolio[1]],
                    y=[current_portfolio[0]],
                    mode='markers',
                    name='Current Portfolio',
                    marker=dict(color='red', size=10)
                )
            )
        
        fig.update_layout(
            title='Efficient Frontier',
            height=self.height,
            width=self.width,
            template=self.template,
            xaxis_title="Volatility",
            yaxis_title="Expected Return",
            showlegend=True
        )
        
        return fig

    def plot_regime_transitions(self,
                              regime_changes: pd.Series,
                              returns: pd.Series) -> go.Figure:
        """Plot regime transitions with returns"""
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=('Returns', 'Regime')
        )
        
        # Plot returns
        fig.add_trace(
            go.Scatter(
                x=returns.index,
                y=returns,
                name='Returns',
                line=dict(color='blue')
            ),
            row=1, col=1
        )
        
        # Plot regime changes
        fig.add_trace(
            go.Scatter(
                x=regime_changes.index,
                y=regime_changes,
                name='Regime',
                line=dict(color='red')
            ),
            row=2, col=1
        )
        
        fig.update_layout(
            height=self.height,
            width=self.width,
            template=self.template,
            showlegend=True,
            title='Regime Transitions'
        )
        
        return fig