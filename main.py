from sys import excepthook

import pyttsx3
import json
import requests
city = input("Enter City: ")
engine = pyttsx3.init()

url = f"http://api.weatherapi.com/v1/current.json?key=8df92fec2f19458e9e9172733251303&q= {city}"
r = requests.get(url)
weather_data = r.json()
try:
    data = json.loads(r.text)
    w = data["current"]["temp_c"]
    print(f"say 'the current temperature in {city} is {w}'")
    engine.say(f"the current temperature in {city} is {w}")
    engine.runAndWait()
except KeyError:
    print("could not retrive data.please check the city name")
    engine.say("could not retrive data.please check the city name")
    engine.runAndWait()