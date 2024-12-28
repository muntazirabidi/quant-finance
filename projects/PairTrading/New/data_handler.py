"""
Data management and preprocessing module.
Handles all data-related operations including fetching, cleaning, and validation.
This module emphasizes robust error handling and detailed data quality checks.
"""
import pandas as pd
import numpy as np
import yfinance as yf
from typing import Tuple, Optional, Dict
from datetime import datetime
import logging
from config import DataConfig

# Configure logging for data operations
logger = logging.getLogger(__name__)

class DataHandler:
    def __init__(self, config: DataConfig):
        """
        Initialize the data handler with configuration settings.
        
        Args:
            config: Configuration object containing data-related parameters
        """
        self.config = config
        
    def fetch_pair_data(self, symbol_A: str, symbol_B: str,
                       start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch and validate data for a pair of securities.
        
        Args:
            symbol_A: First security symbol
            symbol_B: Second security symbol
            start_date: Start date for analysis
            end_date: End date for analysis
            
        Returns:
            DataFrame containing aligned and validated price/volume data
        """
        try:
            logger.info(f"\nFetching data for {symbol_A} and {symbol_B}...")
            
            # Download data with proper error catching
            stock_A = yf.download(symbol_A, start=start_date, end=end_date)
            stock_B = yf.download(symbol_B, start=start_date, end=end_date)
            
            # Validate individual securities
            self._validate_data(stock_A, symbol_A)
            self._validate_data(stock_B, symbol_B)
            
            # Create combined DataFrame with careful index handling
            data = pd.DataFrame(index=stock_A.index)
            
            # Add price and volume data
            for symbol, stock_data in [(symbol_A, stock_A), (symbol_B, stock_B)]:
                data[f'{symbol}_price'] = stock_data[self.config.price_column]
                data[f'{symbol}_volume'] = stock_data['Volume']
                
                # Add additional metrics that might be useful
                data[f'{symbol}_dollar_volume'] = (
                    stock_data[self.config.price_column] * stock_data['Volume']
                )
            
            # Print diagnostic information
            self._print_data_summary(data, symbol_A, symbol_B)
            
            # Clean and validate the paired data
            return self._clean_and_validate_pair_data(data, symbol_A, symbol_B)
            
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            raise RuntimeError(f"Error fetching data: {str(e)}")

    def _validate_data(self, data: pd.DataFrame, symbol: str) -> None:
        """
        Validate individual security data with comprehensive checks.
        
        Args:
            data: DataFrame containing security data
            symbol: Security symbol for logging
        """
        if data.empty:
            raise ValueError(f"No data received for {symbol}")
            
        # Check for required columns
        required_columns = [self.config.price_column, 'Volume']
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns for {symbol}: {missing_columns}")
            
        # Check data quality
        if data[self.config.price_column].isnull().any():
            logger.warning(f"Found missing price data for {symbol}")
            
        # Check liquidity
        avg_daily_volume = (data['Volume'] * data[self.config.price_column]).mean()
        if avg_daily_volume < self.config.min_liquidity_threshold:
            raise ValueError(
                f"Insufficient liquidity for {symbol}. "
                f"Average daily volume: ${avg_daily_volume:,.2f}"
            )

    def _clean_and_validate_pair_data(self, data: pd.DataFrame,
                                    symbol_A: str, symbol_B: str) -> pd.DataFrame:
        """
        Clean and validate paired data with thorough quality checks.
        
        Args:
            data: DataFrame containing paired data
            symbol_A: First security symbol
            symbol_B: Second security symbol
            
        Returns:
            Cleaned and validated DataFrame
        """
        # Handle missing values
        missing_count = data.isnull().sum()
        if missing_count.any():
            logger.warning(f"\nFound missing values:\n{missing_count}")
            data = data.dropna()
            logger.info(f"Removed {len(missing_count)} rows with missing values")
        
        # Validate data sufficiency
        if len(data) < self.config.min_data_points:
            raise ValueError(
                f"Insufficient data points ({len(data)}) "
                f"after cleaning. Minimum required: {self.config.min_data_points}"
            )
        
        # Calculate and log correlation
        correlation = data[f'{symbol_A}_price'].corr(data[f'{symbol_B}_price'])
        logger.info(f"Price correlation between {symbol_A} and {symbol_B}: {correlation:.4f}")
        
        return data
        
    def _print_data_summary(self, data: pd.DataFrame, 
                           symbol_A: str, symbol_B: str) -> None:
        """
        Print comprehensive summary statistics for the data.
        
        Args:
            data: DataFrame containing paired data
            symbol_A: First security symbol
            symbol_B: Second security symbol
        """
        logger.info("\nData Summary:")
        logger.info(f"Start Date: {data.index[0]}")
        logger.info(f"End Date: {data.index[-1]}")
        logger.info(f"Trading Days: {len(data)}")
        
        # Print price statistics
        logger.info("\nPrice Statistics:")
        price_stats = data[[f'{symbol_A}_price', f'{symbol_B}_price']].describe()
        logger.info("\n" + str(price_stats))