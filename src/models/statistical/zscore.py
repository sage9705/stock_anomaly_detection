import pandas as pd
import numpy as np
from ..base import AnomalyDetector

class ZScoreDetector(AnomalyDetector):
    def __init__(self, threshold=3):
        self.threshold = threshold
        self.mean = None
        self.std = None

    def fit(self, data: pd.DataFrame):
        self.mean = data.mean()
        self.std = data.std()

    def detect(self, data: pd.DataFrame) -> pd.Series:
        if self.mean is None or self.std is None:
            raise ValueError("Model not fitted. Call fit() before detect().")
        z_scores = (data - self.mean) / self.std
        return (z_scores.abs() > self.threshold).any(axis=1)