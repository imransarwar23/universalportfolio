import yfinance as yf

def update_prices(portfolio):
    for item in portfolio:
        try:
            ticker = yf.Ticker(item["ticker"])
            price = ticker.info.get("regularMarketPrice", item["avg_price"])
            item["current_price"] = price
            item["gain_loss"] = (price - item["avg_price"]) * item["quantity"]
        except Exception as e:
            item["current_price"] = None
            item["gain_loss"] = None
    return portfolio