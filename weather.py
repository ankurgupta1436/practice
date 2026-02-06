import requests
import sys

API_KEY = "YOUR_API_KEY"  # put this in env later
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()

def display_weather(data):
    print(f"\n🌍 Weather in {data['name']}")
    print(f"🌡 Temperature: {data['main']['temp']}°C")
    print(f"💧 Humidity: {data['main']['humidity']}%")
    print(f"☁ Condition: {data['weather'][0]['description']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather_app.py <city>")
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    try:
        data = get_weather(city)
        display_weather(data)
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch weather data")
        print(e)

if __name__ == "__main__":
    main()
