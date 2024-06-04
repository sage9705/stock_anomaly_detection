import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import Config
from src.data.sources.alpha_vantage import AlphaVantageSource

def main():
    config = Config()
    av_source = AlphaVantageSource(config)

    # Test getting symbols
    print("Available symbols:", av_source.get_symbols())

    # Test getting daily data for a single symbol
    aapl_daily = av_source.get_daily_data("AAPL")
    print("\nAAPL Daily Data:")
    print(aapl_daily.head())

    # Test getting intraday data for a single symbol
    msft_intraday = av_source.get_intraday_data("MSFT", interval="15min")
    print("\nMSFT Intraday Data (15min):")
    print(msft_intraday.head())

if __name__ == "__main__":
    main()