import pandas as pd
from typing import Dict, List
from ..models.base import AnomalyDetector
from ..models.statistical.zscore import ZScoreDetector
from ..models.statistical.iqr import IQRDetector
from ..models.machine_learning.isolation_forest import IsolationForestDetector

class AnomalyDetectionPipeline:
    def __init__(self, models: List[AnomalyDetector] = None):
        if models is None:
            self.models = [ZScoreDetector(), IQRDetector(), IsolationForestDetector()]
        else:
            self.models = models

    def detect_anomalies(self, data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
        results = {}
        for symbol, df in data.items():
            symbol_results = pd.DataFrame(index=df.index)
            for model in self.models:
                model.fit(df)
                symbol_results[model.__class__.__name__] = model.detect(df)
            symbol_results['is_anomaly'] = symbol_results.any(axis=1)
            results[symbol] = symbol_results
        return results