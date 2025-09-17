import os
import json
from datetime import datetime
from utils.config import API_KEY, CITY, UNITS
from utils.api_client import fetch_json

class WeatherAgent:
    def __init__(self, event_bus=None):
        self.api_url = "http://api.weatherstack.com/current"
        self.today_path = os.path.join("data", "today.json")
        self.history_path = os.path.join("data", "history", "weather_history.json")
        os.makedirs(os.path.join("data", "history"), exist_ok=True)
        self.event_bus = event_bus

    def fetch_weather(self):
        params = {
            "access_key": API_KEY,
            "query": CITY,
            "units": UNITS
        }
        data = fetch_json(self.api_url, params=params)
        if not data or "current" not in data:
            print("Error fetching weather:", data)
            return None

        return {
            "timestamp": datetime.now().isoformat(),
            "city": CITY,
            "temperature": data["current"]["temperature"],
            "weather_descriptions": data["current"]["weather_descriptions"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_speed"]
        }

    def save_today(self, today_weather):
        with open(self.today_path, "w") as f:
            json.dump(today_weather, f, indent=4)

    def append_history(self, today_weather):
        history = []
        if os.path.exists(self.history_path):
            with open(self.history_path, "r") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []

        # Avoid duplication for same timestamp
        timestamps = [h.get("timestamp") for h in history]
        if today_weather["timestamp"] not in timestamps:
            history.append(today_weather)
            with open(self.history_path, "w") as f:
                json.dump(history, f, indent=4)

    def run(self):
        today_weather = self.fetch_weather()
        if today_weather:
            self.save_today(today_weather)
            self.append_history(today_weather)

            print(f"Today's weather in {CITY}:")
            print(today_weather)

            if self.event_bus:
                self.event_bus.publish("weather_updated", today_weather)

            return today_weather
        return None

if __name__ == "__main__":
    agent = WeatherAgent()
    agent.run()
