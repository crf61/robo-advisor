# robo-advisor
# Create a repository 
    Create your own repository by cloning or downloading this repository to your desktop.
    Open Terminal and navigate to your file 
    ~cd/Desktop/Robo_advisor

# Create a virtual environment
    Enter #conda create -n stocks-env python=3.7 in the command line
    Enter Y
    And then activate conda activate stocks-env

# Install packages in terminal
    Enter "pip install -r requirements.txt" in the command line
# RUN   
   Enter "python app/robo_advisor.py" to run the code

# Creating syntax for code

    Copy and paste; The link was taken from "https://www.alphavantage.co/documentation/" 

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
    print(type(response))
    #print(dir(response))

    print(response.status_code)
    print(response.text)
    print(type(response.text))

    parsed_response = json.loads(response.text)
    print(type(parsed_response))
    #print(parsed_response["name"])

    for d in parsed_response:
    print(d["id"],d["name"])

    first_prod = parsed_response[0]
    print(first_prod["name"])