import requests
import pandas as pd
from typing import Dict, List
from .base import DataSource
from ...utils.config import Config

class AlphaVantageSource(DataSource):
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, config: Config):
        self.api_key = config.get_setting('alpha_vantage_api_key')
        self.symbols = config.get_tickers()

    def _make_request(self, params: Dict[str, str]) -> Dict:
        params['apikey'] = self.api_key
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_daily_data(self, symbol: str) -> pd.DataFrame:
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "outputsize": "full"
        }
        data = self._make_request(params)
        time_series = data['Time Series (Daily)']
        
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        df.columns = ['open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
        return df.sort_index()

    def get_intraday_data(self, symbol: str, interval: str = '5min') -> pd.DataFrame:
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "outputsize": "full"
        }
        data = self._make_request(params)
        time_series = data[f'Time Series ({interval})']
        
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        return df.sort_index()

    def get_symbols(self) -> List[str]:
        return self.symbols

    def get_all_daily_data(self) -> Dict[str, pd.DataFrame]:
        return {symbol: self.get_daily_data(symbol) for symbol in self.symbols}

    def get_all_intraday_data(self, interval: str = '5min') -> Dict[str, pd.DataFrame]:
        return {symbol: self.get_intraday_data(symbol, interval) for symbol in self.symbols}