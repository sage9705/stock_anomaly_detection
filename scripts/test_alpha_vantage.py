import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import Config
from src.data.sources.alpha_vantage import AlphaVantageSource

def main():
    config = Config()
    av_source = AlphaVantageSource(config)

    # Test getting symbols
    symbols = av_source.get_symbols()
    print(f"Available symbols: {len(symbols)}")
    print(f"First 10 symbols: {symbols[:10]}")

    # Test getting daily data for a single symbol
    try:
        aapl_daily = av_source.get_daily_data("AAPL")
        if not aapl_daily.empty:
            print("\nAAPL Daily Data:")
            print(aapl_daily.head())
        else:
            print("\nFailed to retrieve AAPL daily data")
    except Exception as e:
        print(f"\nError retrieving AAPL daily data: {str(e)}")

    # Test getting intraday data for a single symbol
    try:
        msft_intraday = av_source.get_intraday_data("MSFT", interval="15min")
        if not msft_intraday.empty:
            print("\nMSFT Intraday Data (15min):")
            print(msft_intraday.head())
        else:
            print("\nFailed to retrieve MSFT intraday data")
    except Exception as e:
        print(f"\nError retrieving MSFT intraday data: {str(e)}")

if __name__ == "__main__":
    main()