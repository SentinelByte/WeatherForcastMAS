# utils/event_bus.py
from collections import defaultdict

class EventBus:
    def __init__(self):
        # event_name → list of callback functions
        self.listeners = defaultdict(list)

    def subscribe(self, event_name, callback):
        """Subscribe a callback to an event"""
        self.listeners[event_name].append(callback)

    def publish(self, event_name, data=None):
        """Publish an event and call all subscribed callbacks"""
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(data)
