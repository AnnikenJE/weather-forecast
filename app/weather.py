import requests

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Heavy freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

def weather(city):
    try:

        # Get the latitude and longitude of the city
        city_response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
        city_data = city_response.json()

        # Get the current weather for the city
        weather_response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={city_data['results'][0]['latitude']}&longitude={city_data['results'][0]['longitude']}&current_weather=true")
        weather_data = weather_response.json()

        print(city_data)
        print("\nWEATHER DATA:\n",weather_data, "\n")

        weather_right_now = WEATHER_CODES.get(weather_data["current_weather"]["weathercode"], "Unknown weather code")

        return weather_data, weather_right_now
    
    except Exception as e:
        print("Error:", e)
        return None, "Unknown weather code"


def weather_outfit():
    return "This will show something.. Soon :)"