import requests
from datetime import datetime

#get the city and url
city = input("Enter your city: ")
api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c5b75ec2e9f579331669cc59ff1bd7b6".format(city)
res = requests.get(api_url)

#get the data
data = res.json()
temp = data['main']['temp']
longitude = data['coord']['lon']
latitude = data['coord']['lat']
humidity = data['main']['humidity']
description = data['weather'][0]['description']
windspeed = data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#print the data
print("Date and Time: ",date_time)
print("Location: {}".format(city))
print("Longitude: {}".format(longitude))
print("Latitude: {}".format(latitude))
print("Temperature: {} degree celcius".format(temp))
print("Humidity: {}".format(humidity))
print("Wind Speed: {} m/s".format(windspeed))
print("Description: {}".format(description))