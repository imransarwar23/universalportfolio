from webull import webull

def fetch_webull_data():
    wb = webull()

    # Login
    wb.login('your_email@example.com', 'your_password')  # Add MFA if needed

    # Get open positions
    positions = wb.get_positions()
    
    parsed = []
    for p in positions:
        if p['position']:
            parsed.append({
                "ticker": p["ticker"]["symbol"],
                "position": float(p["position"]["position"]),
                "averagePrice": float(p["position"]["costPrice"]),
                "marketValue": float(p["position"]["marketValue"])
            })
    
    return parsed

if __name__ == "__main__":
    portfolio = fetch_webull_data()
    for stock in portfolio:
        print(stock)