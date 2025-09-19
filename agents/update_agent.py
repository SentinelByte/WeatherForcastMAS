import time
from agents.weather_agent import WeatherAgent
from agents.forecast_agent import ForecastAgent

class UpdateAgent:
    def __init__(self, event_bus=None, interval_hours=6):
        self.interval = interval_hours * 3600  # convert hours to seconds
        self.event_bus = event_bus
        self.weather_agent = WeatherAgent(event_bus=event_bus)
        self.forecast_agent = ForecastAgent(event_bus=event_bus)

    def run(self):
        print(f"UpdateAgent started: refreshing every {self.interval/3600}h")
        while True:
            print("\n=== Updating Weather ===")
            self.weather_agent.run()
            print("\n=== Updating Forecast ===")
            self.forecast_agent.run()
            time.sleep(self.interval)  # wait before next update

if __name__ == "__main__":
    agent = UpdateAgent()
    agent.run()
