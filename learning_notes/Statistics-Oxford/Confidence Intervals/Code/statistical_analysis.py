import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from typing import Tuple, Union, List

class StatisticalAnalysis:
    """A class containing statistical analysis methods commonly used in inference."""
    
    @staticmethod
    def mle_exponential(data: np.ndarray) -> float:
        """
        Calculate MLE for exponential distribution parameter λ.
        
        Args:
            data: Array of observations
        Returns:
            MLE estimate of λ
        """
        return 1 / np.mean(data)
    
    @staticmethod
    def fisher_information_exponential(n: int, lambda_val: float) -> float:
        """
        Calculate Fisher Information for exponential distribution.
        
        Args:
            n: Sample size
            lambda_val: Parameter λ
        Returns:
            Fisher Information value
        """
        return n / (lambda_val ** 2)
    
    @staticmethod
    def confidence_interval_exponential(
        data: np.ndarray,
        alpha: float = 0.05,
        method: str = 'exact'
    ) -> Tuple[float, float]:
        """
        Calculate confidence interval for exponential parameter λ.
        
        Args:
            data: Array of observations
            alpha: Significance level (default 0.05 for 95% CI)
            method: 'exact', 'fisher', or 'alternative'
        Returns:
            Tuple of (lower_bound, upper_bound)
        """
        n = len(data)
        lambda_hat = 1 / np.mean(data)
        
        if method == 'exact':
            # Using gamma distribution relationship
            sum_x = np.sum(data)
            lower = stats.gamma.ppf(alpha/2, n) / sum_x
            upper = stats.gamma.ppf(1-alpha/2, n) / sum_x
            
        elif method == 'fisher':
            # Using Fisher Information
            z = stats.norm.ppf(1-alpha/2)
            se = lambda_hat / np.sqrt(n)
            lower = lambda_hat - z * se
            upper = lambda_hat + z * se
            
        elif method == 'alternative':
            # Alternative approximation
            z = stats.norm.ppf(1-alpha/2)
            lower = lambda_hat / (1 + z/np.sqrt(n))
            upper = lambda_hat / (1 - z/np.sqrt(n))
            
        else:
            raise ValueError("Method must be 'exact', 'fisher', or 'alternative'")
            
        return lower, upper
    
    @staticmethod
    def pooled_variance(sample1: np.ndarray, sample2: np.ndarray) -> float:
        """
        Calculate pooled variance for two samples.
        
        Args:
            sample1: First sample array
            sample2: Second sample array
        Returns:
            Pooled variance estimate
        """
        n1, n2 = len(sample1), len(sample2)
        var1 = np.var(sample1, ddof=1)
        var2 = np.var(sample2, ddof=1)
        
        pooled = ((n1-1)*var1 + (n2-1)*var2) / (n1 + n2 - 2)
        return pooled
    
    @staticmethod
    def two_sample_t_interval(
        sample1: np.ndarray,
        sample2: np.ndarray,
        alpha: float = 0.05
    ) -> Tuple[float, float]:
        """
        Calculate confidence interval for difference in means.
        
        Args:
            sample1: First sample array
            sample2: Second sample array
            alpha: Significance level
        Returns:
            Tuple of (lower_bound, upper_bound)
        """
        n1, n2 = len(sample1), len(sample2)
        mean_diff = np.mean(sample1) - np.mean(sample2)
        pooled_var = StatisticalAnalysis.pooled_variance(sample1, sample2)
        
        se = np.sqrt(pooled_var * (1/n1 + 1/n2))
        df = n1 + n2 - 2
        t_val = stats.t.ppf(1-alpha/2, df)
        
        lower = mean_diff - t_val * se
        upper = mean_diff + t_val * se
        
        return lower, upper
    
    @staticmethod
    def qq_plot_exponential(data: np.ndarray) -> Tuple[plt.Figure, float]:
        """
        Create Q-Q plot for exponential distribution and calculate R².
        
        Args:
            data: Array of observations
        Returns:
            Tuple of (figure, R_squared)
        """
        n = len(data)
        sorted_data = np.sort(data)
        
        # Theoretical quantiles
        p = np.arange(1, n+1) / (n+1)
        theoretical_quantiles = -np.log(1 - p) / StatisticalAnalysis.mle_exponential(data)
        
        # Calculate R²
        correlation_matrix = np.corrcoef(sorted_data, theoretical_quantiles)
        r_squared = correlation_matrix[0,1]**2
        
        # Create plot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(theoretical_quantiles, sorted_data, alpha=0.6)
        
        # Add diagonal line
        max_val = max(np.max(theoretical_quantiles), np.max(sorted_data))
        ax.plot([0, max_val], [0, max_val], 'r--', alpha=0.8)
        
        ax.set_xlabel('Theoretical Quantiles')
        ax.set_ylabel('Sample Quantiles')
        ax.set_title('Q-Q Plot for Exponential Distribution')
        
        return fig, r_squared

# Example usage:
def example_analysis():
    # Generate sample data
    np.random.seed(42)
    exponential_data = np.random.exponential(scale=2, size=100)
    
    # Create analyzer
    analyzer = StatisticalAnalysis()
    
    # Calculate MLE
    lambda_hat = analyzer.mle_exponential(exponential_data)
    print(f"MLE estimate of λ: {lambda_hat:.4f}")
    
    # Calculate confidence intervals using different methods
    ci_exact = analyzer.confidence_interval_exponential(exponential_data, method='exact')
    ci_fisher = analyzer.confidence_interval_exponential(exponential_data, method='fisher')
    
    print(f"Exact CI: ({ci_exact[0]:.4f}, {ci_exact[1]:.4f})")
    print(f"Fisher CI: ({ci_fisher[0]:.4f}, {ci_fisher[1]:.4f})")
    
    # Create Q-Q plot
    fig, r_squared = analyzer.qq_plot_exponential(exponential_data)
    print(f"R-squared value: {r_squared:.4f}")
    plt.show()

if __name__ == "__main__":
    example_analysis()