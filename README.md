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

    The code is taken from "https://www.alphavantage.co/documentation" 

    In order to see the directory of items that comes from a certain link, enter the code below

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