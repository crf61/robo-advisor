# app/robo_advisor.py

import csv
import json

import requests
import os
from dotenv import load_dotenv


print("REQUESTING SOME DATA FROM THE INTERNET...")

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="oops") # "1N162NXV71A8C5LM"
symbol = input("PLEASE ENTER A SYMBOL OR TICKER ")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
print ("URL:", request_url)

if (symbol.isalpha) == False:
    print("ERROR. THE SYMBOL IS INVALID.")
    exit()

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
latest_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]
latest_open = tsd[latest_day]["1. open"]
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
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
        "timestamp": date, 
        "open": daily_prices["1. open"], 
        "high": daily_prices["2. high"], 
        "low": daily_prices["3. low"], 
        "close": daily_prices["4. close"], 
        "volume": daily_prices["5. volume"],
    })

x = float(latest_close)
y = float(latest_open)
if x >= y:
    recommendation = "BUY"
    recommendation_reason = "The price of the stock increased. Things look good."
else:
    recommendation = "I RECOMMEND YOU PASS ON THIS INVESTMENT."
    recommendation_reason = "LATEST OPEN IS LOWER THAN YESTERDAY. THE STOCK MAY NOT BE DOING WELL RIGHT NOW."

print("-------------------------")
print("SELECTED SYMBOL:", symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT:", x)
print("-------------------------")
print(f"LATEST DAY: {latest_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION:" + recommendation)
print("RECOMMENDATION REASON:" + recommendation_reason)
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

