print("Hello World")

import requests
import datetime as dt
import pandas as pd


base_url= "https://api.openweathermap.org/data/2.5/weather?"

api_key="b1c1193a8c87f36a0f2208ff0baf7755"
city="Paris"

url= base_url+'appid='+api_key+'&q='+city

response=requests.get(url).json()

print(response)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)

feels_kelvin = response['main']['feels_like']
feels_celsius = kelvin_to_celsius(feels_kelvin)

humi = response['main']['humidity']
wind = response['wind']['speed']
desc = response['weather'][0]['description']

sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f'Temperature in {city}: {temp_celsius:.2f} C')
print(f'Temperature feels like in {city}: {feels_celsius:.2f} C')
print(f'Humidity in {city}: {humi}%')
print(f'Wind Speed in {city}: {wind} KM/h')
print(f'Description in {city}: {desc}')
print(f'Sun rises in {city}: {sunrise} local time')
print(f'Sun sets in {city}: {sunset} local time')


