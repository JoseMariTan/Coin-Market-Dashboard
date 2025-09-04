import pandas as pd 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import ast
import re

# CoinMarketCap API endpoint for latest cryptocurrency listings
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start': '1', # starting rank (1 means top coin)
  'limit': '5000', # number of coins to fetch (up to 5000)
  'convert': 'USD' # currency for values (USD in this case)
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',   # Insert your API key here
}

session = Session()
session.headers.update(headers)

try:
    # Send GET request to CoinMarketCap
    response = session.get(url, params=parameters)

    # Parse response JSON into a Python dict
    data = json.loads(response.text)
    print(data)  # (Optional) Preview the raw data
except (ConnectionError, Timeout, TooManyRedirects) as e:
    # Print any connection-related errors
    print(e)

# Normalize nested JSON and create initial DataFrame
df = pd.DataFrame(data['data'])

# Convert the 'quote' column (stored as string) back into a dictionary
df["quote"] = df["quote"].apply(lambda x: ast.literal_eval(x))

# Extract all fields inside 'quote.USD' and create separate columns
for key in df["quote"].iloc[0]["USD"].keys():
    df[f"usd_{key}"] = df["quote"].apply(lambda q: q["USD"][key])

# Drop the original 'quote' column (no longer needed)
df = df.drop('quote', axis='columns')

# Remove any columns that contain null values
df = df.dropna(axis='columns', how='any')

# Save the cleaned dataset to CSV
df.to_csv("CoinMarket.csv", index=False)
