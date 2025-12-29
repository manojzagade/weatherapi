import requests

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather (city:str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units":"metric"
    }
    response = requests.get(BASE_URL,params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print ("API Error",response.status_code,response.text)
        return None

def main():
    for _ in range(3):
        city = input("\nEnter your city :\t ")
        data = get_weather(city)

        if not data:
            continue

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        country = data["sys"]["country"]

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
        print(f"Windspeed:{wind_speed}kmph")
        print(f"Humidity:{humidity}units")

        if temp> 30 :
            print("It's hot,🥵,stay hydrated.")

        elif temp<20:
            print("It's Cold 🥶,wear something warm.")
        
        else:
            print("Weather is pleasant🍃.")



if __name__=="__main__":
    main()
