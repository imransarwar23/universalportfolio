def normalize_ibkr(data):
    return [
        {
            "platform": "IBKR",
            "ticker": item["symbol"],
            "quantity": item["quantity"],
            "avg_price": item["costBasis"],
            "market_value": item["value"]
        } for item in data
    ]

def normalize_webull(data):
    return [
        {
            "platform": "Webull",
            "ticker": item["ticker"],
            "quantity": item["position"],
            "avg_price": item["averagePrice"],
            "market_value": item["marketValue"]
        } for item in data
    ]