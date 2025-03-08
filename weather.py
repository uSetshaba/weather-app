import requests
import json

#ask for user input using input()

city = input("Enter the name of your city: ")

api_key = "1aa9db816e047786c5e95bfa04c4acfa" #API Key
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url) #sending requests to the API

if response.status_code == 200:
    #parse the response JSON
    data = response.json()

    #extracting useful weather data 
    
    city_name = data ['name'] #extracts the city
    temparature = data['main']['temp'] #extracts temparature
    description = data['weather'][0]['description'] 
    humidity = data ['main']['humidity']
    wind_speed = data ['wind']['speed']

    # Print the results in a readable format
    print(f"\nWeather in {city_name}:")
    print(f"Temparature: {temparature}°C")
    print(f"Condition: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Error: {response.status_code}")