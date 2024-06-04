import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.config import Config
from src.data.ingestion import DataIngestion
from src.anomaly_detection.detector import AnomalyDetectionPipeline
from src.visualization.plotter import plot_anomalies
from src.alerts.email_alert import EmailAlerter

def main():
    config = Config()
    data_ingestion = DataIngestion(config)
    anomaly_detector = AnomalyDetectionPipeline()

    # Email alerter setup
    email_settings = config.get_setting('email_settings')
    alerter = EmailAlerter(
        email_settings['smtp_server'],
        email_settings['port'],
        email_settings['sender_email'],
        email_settings['password']
    )

    # Fetch and preprocess data
    print("Fetching and preprocessing data...")
    data = data_ingestion.fetch_and_preprocess_data()

    # Detect anomalies
    print("Detecting anomalies...")
    anomalies = anomaly_detector.detect_anomalies(data)

    # Process results and send alerts
    for symbol, df in anomalies.items():
        anomaly_count = df['is_anomaly'].sum()
        print(f"{symbol}: {anomaly_count} anomalies detected")
        
        if anomaly_count > 0:
            print(df[df['is_anomaly']].head())
            
            # Plot anomalies
            plot_anomalies(data[symbol], df, symbol)
            
            # Send email alert
            subject = f"Anomaly Alert: {symbol}"
            body = f"{anomaly_count} anomalies detected in {symbol} stock.\n\nPlease check the attached image for details."
            alerter.send_alert(
                email_settings['recipient_email'],
                subject,
                body,
                f'anomalies_{symbol}.png'
            )
        
        print()

if __name__ == "__main__":
    main()