import io
import os
import requests
import pandas as pd
import logging
from app.config import ALPHA_VANTAGE_API_KEY

logger = logging.getLogger(__name__)

def fetch_alpha_vantage_data(symbol, start_date, end_date):
    try:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=full&datatype=csv"
        response = requests.get(url)
        response.raise_for_status()

        data = pd.read_csv(io.BytesIO(response.content), index_col="timestamp", parse_dates=True)
        # Convert `start_date` and `end_date` to datetime objects
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Create a DatetimeIndex that covers the desired date range
        date_range = pd.date_range(start=start_date, end=end_date, freq="D")

        # Use `reindex()` to select the rows from `data` that match the closest dates in the index
        data = data.reindex(date_range, method="nearest")

        # Select only the 'adjusted_close' column and rename it to the stock symbol
        adjusted_close_data = data["adjusted_close"].rename(symbol)

        return adjusted_close_data

    except Exception as e:
        logger.error(f"Error in fetch_alpha_vantage_data: {e}")
        raise e

# DXMJ7O7ITS7K3JFJ