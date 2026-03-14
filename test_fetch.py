# test_fetch.py

from utils.data_fetcher import fetch_historical_data

df = fetch_historical_data("bitcoin", days=7, interval="daily")
print(df.head())
print(df.tail())
