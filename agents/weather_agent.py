import requests
import json
import os
from utils.config import API_KEY, CITY, UNITS

class WeatherAgent:
    def __init__(self):
        self.api_url = "http://api.weatherstack.com/current"
        self.data_path = os.path.join("data", "today.json")

    def run(self):
        params = {
            "access_key": API_KEY,
            "query": CITY,
            "units": UNITS
        }
        response = requests.get(self.api_url, params=params)
        data = response.json()

        if "current" in data:
            today_weather = {
                "city": CITY,
                "temperature": data["current"]["temperature"],
                "weather_descriptions": data["current"]["weather_descriptions"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_speed"]
            }

            # Save to JSON
            os.makedirs("data", exist_ok=True)
            with open(self.data_path, "w") as f:
                json.dump(today_weather, f, indent=4)

            print(f"Today's weather in {CITY}:")
            print(today_weather)
            return today_weather
        else:
            print("Error fetching weather:", data)
            return None

# Run standalone
if __name__ == "__main__":
    agent = WeatherAgent()
    agent.run()
