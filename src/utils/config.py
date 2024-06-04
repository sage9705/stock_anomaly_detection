import yaml
import json
import os
from typing import Dict, Any

class Config:
    def __init__(self, config_dir: str = 'config'):
        self.config_dir = config_dir
        self.settings = self._load_yaml('settings.yaml')
        self.tickers = self._load_tickers()

    def _load_yaml(self, filename: str) -> Dict[str, Any]:
        with open(os.path.join(self.config_dir, filename), 'r') as file:
            return yaml.safe_load(file)

    def _load_tickers(self) -> Dict[str, list]:
        tickers = {}
        ticker_files = ['nasdaq.json', 'nyse.json', 'custom.json']
        for file in ticker_files:
            with open(os.path.join(self.config_dir, 'tickers', file), 'r') as f:
                tickers[file.split('.')[0]] = json.load(f)['tickers']
        return tickers

    def get_setting(self, key: str) -> Any:
        return self.settings.get(key)

    def get_tickers(self, exchange: str = None) -> list:
        if exchange:
            return self.tickers.get(exchange, [])
        return [ticker for tickers in self.tickers.values() for ticker in tickers]