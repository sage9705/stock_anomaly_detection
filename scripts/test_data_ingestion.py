import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import Config
from src.data.ingestion import DataIngestion

def main():
    config = Config()
    data_ingestion = DataIngestion(config)

    # Test getting and preprocessing data for a single symbol
    symbol = "AAPL"
    try:
        aapl_data = data_ingestion.get_symbol_data(symbol)
        print(f"\n{symbol} Preprocessed Data:")
        print(aapl_data.head())
        print(f"\nColumns: {aapl_data.columns.tolist()}")
    except Exception as e:
        print(f"\nError processing {symbol} data: {str(e)}")

    # Test getting and preprocessing data for all symbols
    try:
        all_data = data_ingestion.fetch_and_preprocess_data()
        print(f"\nProcessed data for {len(all_data)} symbols")
        for symbol, data in list(all_data.items())[:3]:  # Print details for first 3 symbols
            print(f"\n{symbol} shape: {data.shape}")
            print(f"{symbol} columns: {data.columns.tolist()}")
    except Exception as e:
        print(f"\nError processing all data: {str(e)}")

if __name__ == "__main__":
    main()