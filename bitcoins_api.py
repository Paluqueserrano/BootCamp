print("Hello World")

import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def fetch_crypto_data(BTC, USD, api_key, days=180):
    """
    Fetches cryptocurrency data for the specified symbol and market from Alpha Vantage API
    and returns a DataFrame containing the data for the past specified number of days.

    Parameters:
    - symbol: str, the symbol of the cryptocurrency (e.g., 'BTC')
    - market: str, the market to compare against (e.g., 'USD')
    - api_key: str, the API key for Alpha Vantage
    - days: int, the number of past days to filter the data (default is 90)

    Returns:
    - DataFrame: Pandas DataFrame containing the filtered data
    """
    function = 'DIGITAL_CURRENCY_DAILY'  # For daily data

    # Construct the URL for the API request
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&market={market}&apikey={api_key}'

    # Make the API request and get the JSON response
    response = requests.get(url).json()

    # Check if the response contains the expected data
    if 'Time Series (Digital Currency Daily)' not in response:
        raise ValueError("Unexpected response format: 'Time Series (Digital Currency Daily)' key not found.")

    # Extract the 'Time Series (Daily)' data
    time_series_daily = response.get('Time Series (Digital Currency Daily)', {})

    # Convert the time series data to a DataFrame
    df = pd.DataFrame.from_dict(time_series_daily, orient='index')

    # Inspect the columns of the DataFrame to see what needs to be renamed
    df.columns = [
        'open (USD)', 'high (USD)', 'low (USD)', 'close (USD)', 
        'volume'
    ]

    # Convert the index to datetime
    df.index = pd.to_datetime(df.index)
  

    # Filter the data for the past specified number of days
    date_threshold = datetime.now() - timedelta(days=days)
    df = df[df.index >= date_threshold]

    return df

# Get the API key from environment variable
api_key = os.getenv('ALPHAVANTAGE_API_KEY')

# Use the function to fetch data
symbol = 'BTC'
market = 'USD'
days = 90
df = fetch_crypto_data(symbol, market, api_key, days)

# Save the DataFrame to a CSV file
csv_bitcoin = f'{symbol}_{market}_past_{days}_days.csv'
df.to_csv(csv_bitcoin)

print(f'Data for the past {days} days has been saved to {csv_bitcoin}')

