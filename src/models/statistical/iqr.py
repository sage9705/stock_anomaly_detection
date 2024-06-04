import pandas as pd
import numpy as np
from ..base import AnomalyDetector

class IQRDetector(AnomalyDetector):
    def __init__(self, factor=1.5):
        self.factor = factor
        self.Q1 = None
        self.Q3 = None

    def fit(self, data: pd.DataFrame):
        self.Q1 = data.quantile(0.25)
        self.Q3 = data.quantile(0.75)

    def detect(self, data: pd.DataFrame) -> pd.Series:
        if self.Q1 is None or self.Q3 is None:
            raise ValueError("Model not fitted. Call fit() before detect().")
        IQR = self.Q3 - self.Q1
        lower_bound = self.Q1 - (self.factor * IQR)
        upper_bound = self.Q3 + (self.factor * IQR)
        return ((data < lower_bound) | (data > upper_bound)).any(axis=1)