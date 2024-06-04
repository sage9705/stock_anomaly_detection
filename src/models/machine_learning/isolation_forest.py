import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from ..base import AnomalyDetector

class IsolationForestDetector(AnomalyDetector):
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination, random_state=42)

    def fit(self, data: pd.DataFrame):
        self.model.fit(data)

    def detect(self, data: pd.DataFrame) -> pd.Series:
        predictions = self.model.predict(data)
        return pd.Series(predictions == -1, index=data.index)