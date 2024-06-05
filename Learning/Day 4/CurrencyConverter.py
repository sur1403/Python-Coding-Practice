import requests

API_KEY = "fca_live_CZJB9QpspL7JMYKVCJFhG3Zi7RW31CHGzX3cCxSg"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e: 
        print(e)
        return None
while True:
 base = input("Enter base currency (q for quit):").upper()

 if base in CURRENCIES:
    data = convert_currency("CAD")
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
 else: 
    print("Enter only USD, CAD, EUR, AUD, CNY")