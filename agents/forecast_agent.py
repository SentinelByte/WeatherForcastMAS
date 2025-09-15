import requests
import json
import os
from utils.config import API_KEY, CITY, UNITS

class ForecastAgent:
    def __init__(self, event_bus=None):
        self.api_url = "http://api.weatherstack.com/forecast"
        self.forecast_path = os.path.join("data", "forecast.json")
        os.makedirs("data", exist_ok=True)
        self.event_bus = event_bus

    def fetch_forecast(self):
        params = {
            "access_key": API_KEY,
            "query": CITY,
            "forecast_days": 7,  # depends on API, might ignore if not supported
            "units": UNITS
        }
        response = requests.get(self.api_url, params=params)
        data = response.json()
        if "forecast" not in data and "daily" not in data:
            print("Error fetching forecast:", data)
            return None
        return data.get("forecast") or data.get("daily")  # adapt to API response

    def save_forecast(self, forecast_data):
        with open(self.forecast_path, "w") as f:
            json.dump(forecast_data, f, indent=4)

    def run(self):
        forecast_data = self.fetch_forecast()
        if forecast_data:
            self.save_forecast(forecast_data)
            print(f"7-day forecast saved for {CITY}")
            if self.event_bus:
                self.event_bus.publish("forecast_updated", forecast_data)
            return forecast_data
        return None

if __name__ == "__main__":
    agent = ForecastAgent()
    agent.run()
