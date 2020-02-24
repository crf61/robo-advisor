# app/robo_advisor.py

import requests
import json
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


import datetime
x = datetime.datetime.now ()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", x)
print("-------------------------")
print(f"LATEST DAY: {lastest_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(lastest_close))}")
print("RECENT HIGH: $101,000.00") 
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")