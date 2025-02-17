# analysis/clustering.py

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from typing import Dict, Tuple

class VolatilityClustering:
    def __init__(self, returns: pd.Series, volatility: pd.Series):
        self.returns = returns
        self.volatility = volatility
        self.clusters = None
        
    def identify_clusters(self, n_clusters: int = 3) -> Dict[str, pd.Series]:
        """Identify volatility clusters using K-means"""
        # Prepare features
        features = pd.DataFrame({
            'volatility': self.volatility,
            'abs_returns': np.abs(self.returns)
        })
        
        # Normalize features
        normalized_features = (features - features.mean()) / features.std()
        
        # Fit K-means
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.clusters = kmeans.fit_predict(normalized_features)
        
        # Create masks for each cluster
        cluster_masks = {}
        for i in range(n_clusters):
            cluster_masks[f'cluster_{i}'] = pd.Series(
                self.clusters == i,
                index=self.volatility.index
            )
            
        return cluster_masks
        
    def analyze_cluster_characteristics(self) -> pd.DataFrame:
        """Analyze characteristics of each cluster"""
        if self.clusters is None:
            self.identify_clusters()
            
        characteristics = []
        
        for i in np.unique(self.clusters):
            mask = self.clusters == i
            cluster_data = {
                'cluster': i,
                'size': np.sum(mask),
                'avg_volatility': self.volatility[mask].mean(),
                'max_volatility': self.volatility[mask].max(),
                'avg_abs_return': np.abs(self.returns[mask]).mean(),
                'max_abs_return': np.abs(self.returns[mask]).max()
            }
            characteristics.append(cluster_data)
            
        return pd.DataFrame(characteristics)
