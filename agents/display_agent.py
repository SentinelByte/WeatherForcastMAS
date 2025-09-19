import os
import json
import streamlit as st

class DisplayAgent:
    def __init__(self, event_bus=None):
        self.today_path = os.path.join("data", "today.json")
        self.activity_history_path = os.path.join("data", "history", "activity_history.json")
        self.forecast_path = os.path.join("data", "forecast.json")
        self.event_bus = event_bus

        # Initialize dashboard placeholders
        self.today_placeholder = st.empty()
        self.activity_placeholder = st.empty()
        self.forecast_placeholder = st.empty()

        # Initialize stored data
        self.today_weather = {}
        self.forecast_data = {}
        self.latest_activity = None

        # Subscribe to events
        if self.event_bus:
            self.event_bus.subscribe("weather_updated", self.on_weather_updated)
            self.event_bus.subscribe("forecast_updated", self.on_forecast_updated)
            self.event_bus.subscribe("activity_suggested", self.on_activity_suggested)

    # Event callbacks
    def on_weather_updated(self, data):
        self.today_weather = data
        self.update_today_weather()

    def on_forecast_updated(self, data):
        self.forecast_data = data
        self.update_forecast()

    def on_activity_suggested(self, data):
        self.latest_activity = data
        self.update_activity()

    # Streamlit update functions
    def update_today_weather(self):
        self.today_placeholder.subheader(f"Today's Weather in {self.today_weather.get('city','')}")
        self.today_placeholder.write(self.today_weather)

    def update_forecast(self):
        self.forecast_placeholder.subheader("7-Day Forecast")
        self.forecast_placeholder.json(self.forecast_data)

    def update_activity(self):
        self.activity_placeholder.subheader("Suggested Activity")
        if self.latest_activity:
            self.activity_placeholder.write(self.latest_activity.get("suggested_activity", "N/A"))

    # Initial load from disk
    def load_initial_data(self):
        # Load today's weather
        if os.path.exists(self.today_path):
            with open(self.today_path, "r") as f:
                try:
                    self.today_weather = json.load(f)
                    self.update_today_weather()
                except json.JSONDecodeError:
                    pass

        # Load latest activity
        if os.path.exists(self.activity_history_path):
            with open(self.activity_history_path, "r") as f:
                try:
                    history = json.load(f)
                    if history:
                        self.latest_activity = history[-1]
                        self.update_activity()
                except json.JSONDecodeError:
                    pass

        # Load forecast
        if os.path.exists(self.forecast_path):
            with open(self.forecast_path, "r") as f:
                try:
                    self.forecast_data = json.load(f)
                    self.update_forecast()
                except json.JSONDecodeError:
                    pass

    # Run dashboard
    def run_dashboard(self):
        st.title("Weather MAS Dashboard")
        self.load_initial_data()
        st.info("Waiting for updates...")  # placeholder message
