"""
data_fetcher.py
------------------------------------
Handles all crypto data fetching:
- Historical price data
- Live current price
- Error handling
- Rate limit handling
- Data cleaning
------------------------------------
"""

import requests
import pandas as pd
import time
from datetime import datetime


# ============================================
# CONFIGURATION
# ============================================

BASE_URL = "https://api.coingecko.com/api/v3"
REQUEST_TIMEOUT = 10


# ============================================
# HELPER FUNCTION: Safe API Request
# ============================================

def safe_request(url, params=None, retries=3):
    """
    Makes a safe API request with retry logic.
    Handles:
    - Connection errors
    - Rate limits
    - Temporary failures
    """

    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                params=params,
                timeout=REQUEST_TIMEOUT,
                headers={
                    "Accept": "application/json",
                    "User-Agent": "crypto-prediction-mvp"
                }
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 429:
                print("⚠ Rate limit hit. Waiting 5 seconds...")
                time.sleep(5)
            elif response.status_code == 401:
                raise Exception("Unauthorized request. Check API access.")
            else:
                raise http_err

        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
            time.sleep(2)

    raise Exception("Failed after multiple retries.")


# ============================================
# FETCH HISTORICAL DATA
# ============================================

def fetch_historical_data(crypto_id: str, days: int = 60) -> pd.DataFrame:
    """
    Fetch historical price data from CoinGecko.

    Parameters:
    ----------
    crypto_id : str
        e.g. 'bitcoin', 'ethereum'
    days : int
        Number of days of data

    Returns:
    -------
    pd.DataFrame with:
        - date
        - price
    """

    url = f"{BASE_URL}/coins/{crypto_id}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }

    data = safe_request(url, params)

    if "prices" not in data:
        raise Exception("Invalid response structure from API.")

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])

    # Convert timestamp to datetime
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    # Sort by date
    df = df.sort_values("date")

    # Reset index
    df = df.reset_index(drop=True)

    # Keep only necessary columns
    df = df[["date", "price"]]

    return df


# ============================================
# FETCH LIVE CURRENT PRICE
# ============================================

def fetch_current_price(crypto_id: str) -> float:
    """
    Fetch live current price of a cryptocurrency.

    Returns:
        float (USD price)
    """

    url = f"{BASE_URL}/simple/price"

    params = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }

    data = safe_request(url, params)

    if crypto_id not in data:
        raise Exception("Crypto ID not found in API response.")

    return float(data[crypto_id]["usd"])


# ============================================
# FETCH FULL MARKET DATA (Optional Advanced)
# ============================================

def fetch_market_data(crypto_id: str, days: int = 60) -> pd.DataFrame:
    """
    Fetch extended market data including:
    - price
    - volume
    - market cap

    Useful for improving model accuracy.
    """

    url = f"{BASE_URL}/coins/{crypto_id}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }

    data = safe_request(url, params)

    prices = data.get("prices", [])
    volumes = data.get("total_volumes", [])
    market_caps = data.get("market_caps", [])

    df_prices = pd.DataFrame(prices, columns=["timestamp", "price"])
    df_volumes = pd.DataFrame(volumes, columns=["timestamp", "volume"])
    df_caps = pd.DataFrame(market_caps, columns=["timestamp", "market_cap"])

    df = df_prices.merge(df_volumes, on="timestamp")
    df = df.merge(df_caps, on="timestamp")

    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    df = df.sort_values("date").reset_index(drop=True)

    return df[["date", "price", "volume", "market_cap"]]


# ============================================
# AVAILABLE CRYPTO LIST (Optional Utility)
# ============================================

def get_available_cryptos():
    """
    Fetch list of supported cryptos from CoinGecko.
    """

    url = f"{BASE_URL}/coins/list"

    data = safe_request(url)

    return [coin["id"] for coin in data]