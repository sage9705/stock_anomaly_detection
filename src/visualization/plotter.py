import matplotlib.pyplot as plt
import pandas as pd

def plot_anomalies(data: pd.DataFrame, anomalies: pd.DataFrame, symbol: str):
    plt.figure(figsize=(15, 10))
    plt.plot(data.index, data['close'], label='Close Price')
    anomaly_points = data[anomalies['is_anomaly']]['close']
    plt.scatter(anomaly_points.index, anomaly_points.values, color='red', label='Anomaly')
    plt.title(f'Anomalies in {symbol} stock price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'anomalies_{symbol}.png')
    plt.close()