"""
Main strategy execution module for the pairs trading system.
This module orchestrates the overall strategy execution by coordinating
between different components like data handling, statistical analysis,
risk management, and performance analysis.
"""
from typing import List, Tuple, Dict, Any
import pandas as pd
import logging
from datetime import datetime

# Import our custom modules
from config import TradingConfig, DataConfig, RiskConfig
from data_handler import DataHandler
from statistical_engine import StatisticalEngine
from risk_manager import RiskManager
from performance_analyzer import PerformanceAnalyzer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PairsTrading:
    """
    Main class that orchestrates the pairs trading strategy execution.
    This class coordinates between different components and maintains
    the overall strategy flow.
    """
    def __init__(self, 
                 trading_config: TradingConfig,
                 data_config: DataConfig,
                 risk_config: RiskConfig):
        """
        Initialize the pairs trading strategy with configuration objects.
        
        Args:
            trading_config: Configuration for trading parameters
            data_config: Configuration for data handling
            risk_config: Configuration for risk management
        """
        self.trading_config = trading_config
        self.data_config = data_config
        self.risk_config = risk_config
        
        # Initialize component classes
        self.data_handler = DataHandler(data_config)
        self.statistical_engine = StatisticalEngine(trading_config)
        self.risk_manager = RiskManager(risk_config)
        self.performance_analyzer = PerformanceAnalyzer(trading_config)
        
        # Initialize strategy state
        self.current_portfolio_value = trading_config.initial_capital
        self.active_positions = {}

    def _trade_pair(self, 
                    symbol_A: str, 
                    symbol_B: str,
                    start_date: str,
                    end_date: str) -> Dict[str, Any]:
        """
        Execute trading strategy for a single pair of securities.
        
        Args:
            symbol_A: First security symbol
            symbol_B: Second security symbol
            start_date: Start date for analysis
            end_date: End date for analysis
            
        Returns:
            Dictionary containing trading results and performance metrics
        """
        logger.info(f"Starting analysis for pair: {symbol_A}-{symbol_B}")
        
        # Fetch and validate data
        try:
            data = self.data_handler.fetch_pair_data(
                symbol_A, symbol_B, start_date, end_date
            )
        except Exception as e:
            logger.error(f"Data fetching failed for {symbol_A}-{symbol_B}: {str(e)}")
            raise
        
        # Calculate spread and statistical indicators
        try:
            price_A = data[f'{symbol_A}_price']
            price_B = data[f'{symbol_B}_price']
            spread, zscore = self.statistical_engine.calculate_spread(price_A, price_B)
            
            # Calculate correlation for position sizing
            pair_correlation = price_A.corr(price_B)
            
        except Exception as e:
            logger.error(f"Statistical analysis failed: {str(e)}")
            raise

        # Generate trading signals and manage risk
        try:
            # Calculate position sizes with risk constraints
            position_sizes = self.risk_manager.calculate_position_size(
                zscore=zscore,
                current_portfolio_value=self.current_portfolio_value,
                pair_correlation=pair_correlation
            )
            
            # Calculate returns for the pair
            returns = self._calculate_pair_returns(
                price_A, price_B, position_sizes, self.trading_config.transaction_cost
            )
            
            # Update portfolio value
            portfolio_values = self.current_portfolio_value * (1 + returns).cumprod()
            
            # Apply stop-loss and risk management
            position_sizes = self.risk_manager.apply_stop_loss(
                position_sizes, portfolio_values
            )
            
        except Exception as e:
            logger.error(f"Position management failed: {str(e)}")
            raise

        # Calculate performance metrics
        try:
            metrics = self.performance_analyzer.calculate_metrics(
                returns, portfolio_values
            )
            
            # Update current portfolio value
            self.current_portfolio_value = portfolio_values.iloc[-1]
            
        except Exception as e:
            logger.error(f"Performance analysis failed: {str(e)}")
            raise

        # Compile results
        return {
            'pair': f'{symbol_A}-{symbol_B}',
            'returns': returns,
            'portfolio_values': portfolio_values,
            'metrics': metrics,
            'positions': position_sizes,
            'correlation': pair_correlation
        }

    def _calculate_pair_returns(self, 
                              price_A: pd.Series,
                              price_B: pd.Series,
                              positions: pd.Series,
                              transaction_cost: float) -> pd.Series:
        """
        Calculate returns for a pair trade considering transaction costs.
        
        Args:
            price_A: Price series for first security
            price_B: Price series for second security
            positions: Series of position sizes
            transaction_cost: Transaction cost per trade
            
        Returns:
            Series of strategy returns
        """
        # Calculate individual returns
        returns_A = price_A.pct_change()
        returns_B = price_B.pct_change()
        
        # Calculate strategy returns with position sizes
        strategy_returns = positions.shift(1) * (returns_A - returns_B)
        
        # Calculate transaction costs
        position_changes = positions.diff().fillna(0)
        costs = abs(position_changes) * transaction_cost
        
        # Apply transaction costs to returns
        return strategy_returns - costs

    def _aggregate_results(self, results: List[Dict]) -> Dict[str, Any]:
        """
        Aggregate results across all pairs and calculate portfolio metrics.
        
        Args:
            results: List of individual pair results
            
        Returns:
            Dictionary containing aggregated results and portfolio metrics
        """
        if not results:
            logger.warning("No results to aggregate")
            return {}

        # Combine returns from all pairs
        all_returns = pd.DataFrame({
            result['pair']: result['returns'] for result in results
        })
        
        # Calculate portfolio-level metrics
        portfolio_returns = all_returns.mean(axis=1)
        portfolio_values = self.trading_config.initial_capital * (
            1 + portfolio_returns
        ).cumprod()
        
        # Calculate aggregate metrics
        portfolio_metrics = self.performance_analyzer.calculate_metrics(
            portfolio_returns, portfolio_values
        )
        
        # Calculate correlation matrix
        correlation_matrix = all_returns.corr()
        
        return {
            'portfolio_metrics': portfolio_metrics,
            'individual_results': results,
            'correlation_matrix': correlation_matrix,
            'portfolio_returns': portfolio_returns,
            'portfolio_values': portfolio_values
        }

    def run_strategy(self, 
                    pairs: List[Tuple[str, str]],
                    start_date: str,
                    end_date: str) -> Dict[str, Any]:
        """
        Execute the pairs trading strategy across all pairs.
        
        Args:
            pairs: List of security pairs to trade
            start_date: Start date for analysis
            end_date: End date for analysis
            
        Returns:
            Dictionary containing complete strategy results
        """
        logger.info(f"Starting strategy execution with {len(pairs)} pairs")
        results = []
        
        for symbol_A, symbol_B in pairs:
            try:
                pair_result = self._trade_pair(symbol_A, symbol_B, 
                                             start_date, end_date)
                results.append(pair_result)
                logger.info(f"Successfully processed pair: {symbol_A}-{symbol_B}")
                
            except Exception as e:
                logger.error(f"Error trading {symbol_A}-{symbol_B}: {str(e)}")
                continue
        
        # Aggregate and return results
        aggregated_results = self._aggregate_results(results)
        
        logger.info("Strategy execution completed")
        return aggregated_results

if __name__ == "__main__":
    # Initialize configurations
    trading_config = TradingConfig()
    data_config = DataConfig()
    risk_config = RiskConfig()
    
    # Create strategy instance
    strategy = PairsTrading(trading_config, data_config, risk_config)
    
    # Define pairs with fundamental relationships
    pairs = [
        ('XLE', 'USO'),    # Energy sector ETF vs Oil ETF
        ('GDX', 'GLD'),    # Gold miners vs Gold
        ('QQQ', 'SPY'),    # Tech-heavy vs Broad market
        ('KO', 'PEP'),     # Beverage industry leaders
        ('INTC', 'AMD'),   # Semiconductor competitors
    ]
    
    # Run strategy
    results = strategy.run_strategy(
        pairs=pairs,
        start_date='2020-01-01',
        end_date='2023-12-31'
    )
    
    # Print summary results
    print("\nStrategy Performance Summary:")
    print("=" * 50)
    metrics = results['portfolio_metrics']
    print(f"Total Return: {metrics['total_return']:.2%}")
    print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
    print(f"Maximum Drawdown: {metrics['max_drawdown']:.2%}")
    print(f"Win Rate: {metrics['win_rate']:.2%}")