# WeatherForecastMAS 🌦️

WeatherForecastMAS is a **Multi-Agent System (MAS)** that fetches live weather data, plans daily activities, and maintains a 7-day forecast.  
It is designed for learning MAS concepts and for practical use as a personal weather + activity assistant.

---

`Owner: DanCohVax`

## 🚀 Features
- **Daily Weather Plan** → Fetches today’s conditions & suggests an activity.
- **Weekly Forecast** → Stores 7-day weather outlook.
- **Automatic Updates** → Refreshes forecast every 6 hours.
- **Dashboard** → View data in a Streamlit-powered local web app.
- **Lightweight & Free** → Uses OpenWeatherMap free API tier.

---

## 📂 Project Structure
```

weather\_mas/
│
├── agents/                          # all agents live here
│   ├── weather_agent.py              # fetch today’s weather, update history, publish event
│   ├── planner_agent.py              # suggest activities, update history, subscribe to weather events
│   ├── forecast_agent.py             # fetch 7-day forecast, update history
│   ├── update_agent.py               # refresh forecast & notify planner periodically
│   └── display_agent.py              # output via console or Streamlit dashboard
│
├── data/                             # storage for JSON / DB
│   ├── today.json                     # latest weather
│   ├── forecast.json                  # 7-day forecast
│   └── history/                       # historical records
│       ├── weather_history.json       # daily weather records with timestamps
│       └── activity_history.json      # daily activity suggestions with timestamps
│
├── dashboard/                        # Streamlit dashboard files
│   └── app.py
│
├── utils/                            # helpers (logging, API calls, config)
│   ├── api_client.py
│   ├── config.py                      # API keys, city, units
│   └── event_bus.py                   # simple Pub/Sub EventBus implementation
│
├── main.py                            # entry point → runs daily workflow using agents
├── main_event_mas.py                  # optional: MAS workflow with EventBus and dashboard
├── update.py                          # entry point → runs every 6h (Update Agent)
├── requirements.txt                   # dependencies: requests, streamlit, etc.
└── README.md

````

---

## ⚙️ Configuration
Create a `utils/config.py` file with your OpenWeatherMap API key:

```python
API_KEY = "your_openweathermap_api_key"
CITY = "Berlin"
UNITS = "metric"  # "imperial" for Fahrenheit
````

You can get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

> ⚠️ Do **not** commit `config.py` to GitHub. Keep it ignored in `.gitignore`. Use a `config.example.py` instead.

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

---

## 📜 License

MIT License – feel free to use and modify.

```

---

This README is **ready to drop** in your repo. It covers:  
- Project purpose  
- Features  
- Folder structure  
- Setup & usage instructions  
- Automation & roadmap  
