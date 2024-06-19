from notifypy import Notify
import time
import requests

# FINNHUB IS THE API USED FOR THE SCRIPT

def fetch_stock_price(symbol):
    api_key = "INSERT_API_KEY" # PUT YOUR API KEY HERE
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['c']
    else:
        print(f"Failed to fetch data for {symbol}")
        return None
    
stocks = ['xxx'] # INSERT STOCKS HERE
threshold_high = 125.5 # PUT ANY POSITIVE NUMBER HERE
threshold_low = 115.5 # PUT ANY POSITIVE NUMBER HERE

while True:
    for stock in stocks:
        price = fetch_stock_price(stock)
        if price is not None and price > threshold_high or price < threshold_low:
            notification = Notify()
            notification.title = f"{stock} Price Alert"
            notification.message = f"Current Price: {price}"
            notification.icon = ""
            notification.send()
    time.sleep(15) # PUT ANY AMOUNT OF SECONDS HERE

