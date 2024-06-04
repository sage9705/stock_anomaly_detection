import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import Config
from src.data.ingestion import DataIngestion
from src.anomaly_detection.detector import AnomalyDetectionPipeline

def main():
    config = Config()
    data_ingestion = DataIngestion(config)
    anomaly_detector = AnomalyDetectionPipeline()

    # Fetch and preprocess data
    print("Fetching and preprocessing data...")
    data = data_ingestion.fetch_and_preprocess_data()

    # Detect anomalies
    print("Detecting anomalies...")
    anomalies = anomaly_detector.detect_anomalies(data)

    # Print results
    for symbol, df in anomalies.items():
        anomaly_count = df['is_anomaly'].sum()
        print(f"{symbol}: {anomaly_count} anomalies detected")
        if anomaly_count > 0:
            print(df[df['is_anomaly']].head())
        print()

if __name__ == "__main__":
    main()