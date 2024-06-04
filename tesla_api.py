print('Hello World')#bot.py

import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
base_url="https://cloud.iexapis.com/stable"
api_token="pk_56ee13d1359e4c2d8ce2898fc7f5beda"
symbol="TSLA"

url= {{base_url}}?function=OVERVIEW&symbol=TSLA&apikey={{api_token}}
response=requests.get(url).json()

print(response)
