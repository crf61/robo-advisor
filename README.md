# robo-advisor
# Create a repository 
    Create your own repository by cloning or downloading this repository to your desktop.
    Open Terminal and navigate to your file 
    ~cd/Desktop/Robo_advisor

# Create a virtual environment
    Enter /conda create -n stocks-env python=3.7 in the command line
    Enter /Y
    And then activate and enter /conda activate stocks-env

# Install packages in terminal
    Enter /pip install -r requirements.txt in the command line
# RUN   
   Enter /python app/robo_advisor.py to run the code

# Where are we getting the code from?

    The code is taken from "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}" 
    
    In order to see the directory of items that comes from a certain link, we need to have a symbol and an API Key.
# Entering Dynamic Fields - Symbol

    Symbol is the same as a ticker. For example, entering TSLA in the NYSE will give us information for Tesla such as closing, open, high and low.

    The program will require that the user enters the ticker so they can see the information they want.

# DONE

    The program will spit out a recommendation for you to either buy or sell the stock

