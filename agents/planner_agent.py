import json
import os
import random
from datetime import datetime

class PlannerAgent:
    def __init__(self, event_bus=None):
        self.today_path = os.path.join("data", "today.json")
        self.history_path = os.path.join("data", "history", "activity_history.json")
        os.makedirs(os.path.join("data", "history"), exist_ok=True)

        self.weather_activity_map = {
            "Sunny": ["Go for a picnic", "Go for a walk", "Outdoor sports"],
            "Partly cloudy": ["Take a walk", "Visit a cafe"],
            "Cloudy": ["Visit a museum", "Read a book at home"],
            "Rain": ["Watch a movie", "Indoor games", "Read a book"],
            "Snow": ["Build a snowman", "Skiing", "Snowball fight"],
            "Thunderstorm": ["Stay indoors", "Watch movies", "Board games"]
        }

        self.event_bus = event_bus
        if self.event_bus:
            # Subscribe to weather updates
            self.event_bus.subscribe("weather_updated", self.on_weather_updated)

    def suggest_activity(self, weather_descriptions):
        normalized_map = {k.lower(): v for k, v in self.weather_activity_map.items()}
        possible_activities = []

        for desc in weather_descriptions:
            desc_lower = desc.lower()
            for key, activities in normalized_map.items():
                if key in desc_lower:
                    possible_activities.extend(activities)

        if possible_activities:
            return random.choice(possible_activities)

        return "Relax at home"

    def load_today_weather(self):
        if not os.path.exists(self.today_path):
            return None
        with open(self.today_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return None

    def append_history(self, activity_suggestion):
        """Append activity to history, merging by date and preventing duplicates."""
        history = {}
        if os.path.exists(self.history_path):
            with open(self.history_path, "r") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = {}

        # Extract date (YYYY-MM-DD) from timestamp
        date_key = activity_suggestion["timestamp"][:10]

        if date_key not in history:
            history[date_key] = {
                "date": date_key,
                "city": activity_suggestion.get("city", ""),
                "temperature": activity_suggestion.get("temperature"),
                "weather_descriptions": activity_suggestion.get("weather_descriptions", []),
                "activities": [activity_suggestion["suggested_activity"]]
            }
        else:
            if activity_suggestion["suggested_activity"] not in history[date_key]["activities"]:
                history[date_key]["activities"].append(activity_suggestion["suggested_activity"])

        with open(self.history_path, "w") as f:
            json.dump(history, f, indent=4)

    def process_weather(self, today_weather):
        activity = self.suggest_activity(today_weather.get("weather_descriptions", []))
        suggestion_record = {
            "timestamp": datetime.now().isoformat(),
            "weather_timestamp": today_weather.get("timestamp"),
            "city": today_weather.get("city", ""),
            "temperature": today_weather.get("temperature", None),
            "weather_descriptions": today_weather.get("weather_descriptions", []),
            "suggested_activity": activity
        }

        self.append_history(suggestion_record)

        # Publish event
        if self.event_bus:
            self.event_bus.publish("activity_suggested", suggestion_record)

        print(f"Planner Suggestion for {suggestion_record['city']}: {activity}")
        return suggestion_record

    # Callback for EventBus
    def on_weather_updated(self, today_weather):
        self.process_weather(today_weather)

    def run(self):
        # Optional manual run without EventBus
        today_weather = self.load_today_weather()
        if today_weather:
            self.process_weather(today_weather)
            return today_weather
        return None


if __name__ == "__main__":
    agent = PlannerAgent()
    agent.run()
