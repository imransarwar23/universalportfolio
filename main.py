from ibkr_fetcher import fetch_ibkr_data
from webull_fetcher import fetch_webull_data
from normalizer import normalize_ibkr, normalize_webull
from price_fetcher import update_prices
import pandas as pd

# Fetch raw data
ibkr_raw = fetch_ibkr_data()
webull_raw = fetch_webull_data()

# Normalize
ibkr_normalized = normalize_ibkr(ibkr_raw)
webull_normalized = normalize_webull(webull_raw)

# Merge and update prices
combined = ibkr_normalized + webull_normalized
portfolio = update_prices(combined)

# Print summary
df = pd.DataFrame(portfolio)
print(df)
print("\nTotal Portfolio Value:", df['market_value'].sum())