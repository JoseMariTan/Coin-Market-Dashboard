📊 Coin Market Dashboard

📌 Overview
This project fetches real-time cryptocurrency data from the CoinMarketCap API, processes and cleans it using Python (Pandas), and visualizes the results in an interactive Power BI dashboard. The workflow demonstrates end-to-end data handling — from API integration to cleaning and transformation, and finally to dashboard creation for actionable insights.

🚀 Features
- Extracts up-to-date cryptocurrency data (price, market cap, volume, supply, percent changes).

- Cleans and structures raw API responses into a usable dataset.

- Removes incomplete and unnecessary fields for accuracy.

- Power BI dashboard for interactive exploration, including:
    Market cap, volume, and supply metrics
    Price changes over 24h, 7d, and 30d
    Coin ranking and filtering

🛠️ Tech Stack
- Python 3.11
- pandas
- requests
- json / ast
- Power BI for dashboard visualization

Install dependencies:

pip install pandas requests

Add your CoinMarketCap API key in crypto_script.py:

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR_API_KEY_HERE',
}

📸 Dashboard Preview
<img width="1311" height="735" alt="image" src="https://github.com/user-attachments/assets/576c0677-30c1-4f42-962b-c010cab4b4c1" />

📈 Example Use Cases
- Tracking and comparing cryptocurrency performance
- Analyzing price volatility and market trends
- Building insights for trading strategies or research
