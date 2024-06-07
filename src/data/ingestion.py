from typing import Dict
import pandas as pd
from .sources.alpha_vantage import AlphaVantageSource
from .preprocessing import DataPreprocessor
from ..utils.config import Config

class DataIngestion:
    def __init__(self, config: Config):
        self.data_source = AlphaVantageSource(config)
        self.preprocessor = DataPreprocessor()

    def fetch_and_preprocess_data(self) -> Dict[str, pd.DataFrame]:
        """
        Fetch data for all symbols and preprocess it.
        """
        raw_data = self.data_source.get_all_daily_data()
        preprocessed_data = self.preprocessor.preprocess(raw_data)
        return preprocessed_data

    def get_symbol_data(self, symbol: str) -> pd.DataFrame:
        """
        Fetch and preprocess data for a single symbol.
        """
        raw_data = self.data_source.get_daily_data(symbol)
        preprocessed_data = self.preprocessor._preprocess_symbol(raw_data)
        return preprocessed_data