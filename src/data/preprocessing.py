import pandas as pd
import numpy as np
from typing import List, Dict
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

class DataPreprocessor:
    def __init__(self):
        self.imputer = SimpleImputer(strategy='mean')
        self.scaler = MinMaxScaler()

    def preprocess(self, data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
        """
        Preprocess the data for all symbols.
        """
        return {symbol: self._preprocess_symbol(df) for symbol, df in data.items()}

    def _preprocess_symbol(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess data for a single symbol.
        """
        df = self._handle_missing_values(df)
        df = self._remove_outliers(df)
        df = self._engineer_features(df)
        df = self._normalize(df)
        return df

    def _handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Handle missing values in the dataframe.
        """
        return pd.DataFrame(self.imputer.fit_transform(df), columns=df.columns, index=df.index)

    def _remove_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove outliers using the Interquartile Range (IQR) method.
        """
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

    def _engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Engineer new features from the existing data.
        """
        # Calculate daily returns
        df['daily_return'] = df['close'].pct_change()

        # Calculate 5-day and 20-day moving averages
        df['ma5'] = df['close'].rolling(window=5).mean()
        df['ma20'] = df['close'].rolling(window=20).mean()

        # Calculate relative strength index (RSI)
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))

        return df

    def _normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize the data using Min-Max scaling.
        """
        return pd.DataFrame(self.scaler.fit_transform(df), columns=df.columns, index=df.index)