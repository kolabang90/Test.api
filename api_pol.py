import requests

symbol = "BTC_USDT"
limit = 10  # Optional
url = f"https://api.poloniex.com/markets/{symbol}/orderBook?limit={limit}"
response = requests.get(url)

if response.status_code == 200:
    order_book = response.json()
    print(order_book)
else:
    print(f"Error: {response.status_code}")
