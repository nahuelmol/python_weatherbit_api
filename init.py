import requests
import os 
import json

from dotenv import load_dotenv
from pathlib import Path

load_dotenv(verbose=True)

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

key_weather_bit = "WEATHERBIT_KEY"

def req():
	lon = '38.123'
	lat = '78.543'
	API_KEY = os.getenv(key_weather_bit)
	time = 'minutely'
	x = requests.get("https://api.weatherbit.io/v2.0/current?lat="+lat+"&lon="+lon+"&key="+API_KEY+"&include="+time)
	data_schon = x.json()

	pressure = data_schon['data'][0]['pres']
	country = data_schon['data'][0]['country_code']
	state = data_schon['data'][0]['state_code']

	print('The pressure is: '+str(pressure))
	print('The country code is: '+country)
	print('The state code is: '+str(state))

if __name__ == "__main__":
	req()