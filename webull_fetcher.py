from webull import webull
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="confidential.env")

def fetch_webull_data():
    
    phone = os.getenv("WEBULL_PHONE")
    password = os.getenv("WEBULL_PASSWORD")

    # Login
    wb = webull()
    wb.login(phone, password)
    resp = wb.login(phone, password)
    print("Login response:", resp)

    if resp.get("success") is False:
        print("❌ Login failed:", resp.get("msg", "Unknown error"))
        exit(1)
    else:
        print("✅ Login succeeded")


    # Get open positions
    # positions = wb.get_positions()
    
    # parsed = []
    # for p in positions:
    #     if p['position']:
    #         parsed.append({
    #             "ticker": p["ticker"]["symbol"],
    #             "position": float(p["position"]["position"]),
    #             "averagePrice": float(p["position"]["costPrice"]),
    #             "marketValue": float(p["position"]["marketValue"])
    #         })
    
    # return parsed

if __name__ == "__main__":
    portfolio = fetch_webull_data()
    for stock in portfolio:
        print(stock)