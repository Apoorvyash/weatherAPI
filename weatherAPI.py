'''get current weather data from openweathermap.org''' 
import requests, json, pprint, datetime, time, sys, os 
#! python3
if(len(sys.argv) < 2):
    print("Usage: weatherAPI.py location")
    sys.exit()  

location = ' '.join(sys.argv[1:])

url="http://api.openweathermap.org/data/2.5/weather?q=%s&appid=0c14d536497f439a39cf86011099d24d" % location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
data = weatherData['weather']
print('Current weather in %s:' % (location))
print(data[0]['main'], '-', data[0]['description'])

temp=weatherData['main']
print("Current temperature: ",  temp['temp']-273.15, "Celsius")
print()