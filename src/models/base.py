from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class AnomalyDetector(ABC):
    @abstractmethod
    def fit(self, data: pd.DataFrame):
        """
        Fit the model to the data.
        """
        pass

    @abstractmethod
    def detect(self, data: pd.DataFrame) -> pd.Series:
        """
        Detect anomalies in the data.
        Returns a boolean series where True indicates an anomaly.
        """
        pass