from abc import ABC, abstractmethod
import pandas as pd
from typing import List, Dict

class DataSource(ABC):
    @abstractmethod
    def get_daily_data(self, symbol: str) -> pd.DataFrame:
        """Fetch daily data for a given symbol."""
        pass

    @abstractmethod
    def get_intraday_data(self, symbol: str, interval: str) -> pd.DataFrame:
        """Fetch intraday data for a given symbol and interval."""
        pass

    @abstractmethod
    def get_symbols(self) -> List[str]:
        """Get list of symbols available from this data source."""
        pass

    @abstractmethod
    def get_all_daily_data(self) -> Dict[str, pd.DataFrame]:
        """Fetch daily data for all available symbols."""
        pass

    @abstractmethod
    def get_all_intraday_data(self, interval: str) -> Dict[str, pd.DataFrame]:
        """Fetch intraday data for all available symbols."""
        pass