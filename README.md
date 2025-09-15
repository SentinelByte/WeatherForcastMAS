# WeatherForecastMAS 🌦️

WeatherForecastMAS is a **Multi-Agent System (MAS)** that fetches live weather data, plans daily activities, and maintains a 7-day forecast.  
It is designed for learning MAS concepts and for practical use as a personal weather + activity assistant.

---

`Owner: DanCohVax`

## 🚀 Features
- **Daily Weather Plan** → Fetches today’s conditions & suggests a randomized activity.
- **Weekly Forecast** → Stores 7-day weather outlook.
- **Automatic Updates** → Refreshes forecast every 6 hours via UpdateAgent.
- **Dashboard** → View data in a Streamlit-powered local web app.
- **Event-Driven MAS** → Agents communicate via a simple Pub/Sub EventBus.
- **History Tracking** → Maintains daily weather and activity history with timestamps.
- **Lightweight & Free** → Uses free-tier weather APIs.

---

## 📂 Project Structure
```

weather\_mas/
│
├── agents/                          # all agents live here
│   ├── weather\_agent.py              # fetch today’s weather, update history, publish event
│   ├── planner\_agent.py              # suggest activities, update history, subscribe to weather events
│   ├── forecast\_agent.py             # fetch 7-day forecast, update history
│   ├── update\_agent.py               # refresh forecast & notify planner periodically
│   └── display\_agent.py              # output via console or Streamlit dashboard
│
├── data/                             # storage for JSON / DB
│   ├── today.json                     # latest weather
│   ├── forecast.json                  # 7-day forecast
│   └── history/                       # historical records
│       ├── weather\_history.json       # daily weather records with timestamps
│       └── activity\_history.json      # daily activity suggestions with timestamps
│
├── dashboard/                        # Streamlit dashboard files
│   └── app.py
│
├── utils/                            # helpers (logging, API calls, config)
│   ├── api\_client.py
│   ├── config.py                      # API keys, city, units
│   └── event\_bus.py                   # simple Pub/Sub EventBus implementation
│
├── main.py                            # entry point → runs daily workflow using agents
├── main\_event\_mas.py                  # optional: MAS workflow with EventBus and dashboard
├── update.py                          # entry point → runs every 6h (Update Agent)
├── requirements.txt                   # dependencies: requests, streamlit, etc.
└── README.md

````

---

## ⚙️ Configuration
Create a `utils/config.py` file with your weather API key:

```python
API_KEY = "your_weather_api_key"
CITY = "Berlin"
UNITS = "metric"  # "imperial" for Fahrenheit
````

You can use [WeatherStack](https://weatherstack.com/) or another free API.

> ⚠️ Do **not** commit `config.py` to GitHub. Use `config.example.py` instead.

---

## 🛠️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/SentinelByte/WeatherForcastMAS.git
   cd WeatherForecastMAS
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Run Daily Workflow (fetch today’s weather + weekly forecast)

```bash
python main.py
```

### Run EventBus MAS (optional, with dashboard & inter-agent events)

```bash
python main_event_mas.py
```

### Run Forecast Updater (every 6h, via cron/Task Scheduler)

```bash
python update.py
```

### Run Dashboard (local visualization)

```bash
streamlit run dashboard/app.py
```

---

## 📅 Automation

Use cron (Linux/macOS) or Task Scheduler (Windows) to automate:

```bash
# Run daily plan at 7 AM
0 7 * * * /usr/bin/python3 /path/to/weather_mas/main.py

# Run forecast updater every 6 hours
0 */6 * * * /usr/bin/python3 /path/to/weather_mas/update.py
```

---

## 📌 Roadmap

* [ ] Add support for multiple cities
* [ ] Store historical weather in SQLite
* [ ] Email/Telegram notifications
* [ ] Grafana/Streamlit advanced dashboard
* [ ] Add AI-powered activity recommendations

---

## 📜 License

MIT License – feel free to use and modify.
