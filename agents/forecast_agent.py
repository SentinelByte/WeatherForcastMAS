import os
import json
from datetime import datetime
from utils.config import API_KEY, CITY, UNITS
from utils.api_client import fetch_json

class ForecastAgent:
    def __init__(self, event_bus=None):
        self.api_url = "http://api.weatherstack.com/forecast"
        self.forecast_path = os.path.join("data", "forecast.json")
        self.history_path = os.path.join("data", "history", "forecast_history.json")
        os.makedirs(os.path.join("data", "history"), exist_ok=True)
        self.event_bus = event_bus

    def fetch_forecast(self):
        params = {
            "access_key": API_KEY,
            "query": CITY,
            "units": UNITS,
            "forecast_days": 7
        }
        data = fetch_json(self.api_url, params=params)
        if not data or "forecast" not in data:
            print("Error fetching forecast:", data)
            return None

        return {
            "timestamp": datetime.now().isoformat(),
            "city": CITY,
            "forecast": data["forecast"]
        }

    def save_forecast(self, forecast_data):
        with open(self.forecast_path, "w") as f:
            json.dump(forecast_data, f, indent=4)

    def append_history(self, forecast_data):
        history = []
        if os.path.exists(self.history_path):
            with open(self.history_path, "r") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []

        # Avoid duplication for same timestamp
        timestamps = [h.get("timestamp") for h in history]
        if forecast_data["timestamp"] not in timestamps:
            history.append(forecast_data)
            with open(self.history_path, "w") as f:
                json.dump(history, f, indent=4)

    def run(self):
        forecast_data = self.fetch_forecast()
        if forecast_data:
            self.save_forecast(forecast_data)
            self.append_history(forecast_data)

            if self.event_bus:
                self.event_bus.publish("forecast_updated", forecast_data)

            print(f"7-day forecast for {CITY} fetched successfully.")
            return forecast_data
        return None

if __name__ == "__main__":
    agent = ForecastAgent()
    agent.run()
