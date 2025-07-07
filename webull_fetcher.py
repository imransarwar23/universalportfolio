from webull import webull
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="confidential.env")

def fetch_webull_data():
    wb = webull()
    email = os.getenv("WEBULL_EMAIL")
    password = os.getenv("WEBULL_PASSWORD")

    # Login
    wb.get_mfa(email) #mobile number should be okay as well.
    wb.get_security(email) #get your security question.
    wb.login(email, password)
    login_success = wb.login(email, password)
    print("LOGIN SUCCESS:", login_success)

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