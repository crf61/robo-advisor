# app/robo_advisor.py

import csv
import json

import requests
import os
from dotenv import load_dotenv


print("REQUESTING SOME DATA FROM THE INTERNET...")

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="oops") # "20YMD7USKUACWDVE"
symbol = "TSLA"

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
print ("URL:", request_url)


response = requests.get(request_url)
#print(type(response))
#print(dir(response))

#print(response.status_code)
#print(response.text)
#print(type(response.text))

parsed_response = json.loads(response.text)
#print(type(parsed_response))
#print(parsed_response["name"])

#for d in parsed_response:
#print(d["id"],d["name"])
 
#first_prod = parsed_response[0]
#print(first_prod["name"])

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
lastest_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
lastest_day = dates[0]
lastest_close = tsd[lastest_day]["4. close"]
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
recent_high = max(high_prices)

for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))
recent_low = min(low_prices)

import datetime
x = datetime.datetime.now ()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#taken from module folder

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above


    writer.writerow({
        "timestamp": "TODO", 
        "open": "TODO", 
        "high": "TODO", 
        "low": "TODO", 
        "close": "TODO", 
        "volume": "TODO"
    })

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT:", x)
print("-------------------------")
print(f"LATEST DAY: {lastest_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(lastest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

