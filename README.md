# WeatherForecastMAS 🌦️

WeatherForecastMAS is a **Multi-Agent System (MAS)** that fetches live weather data, plans daily activities, and maintains a 7-day forecast.  
It is designed for learning MAS concepts and for practical use as a personal weather + activity assistant.

---

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
├── agents/                # Agent implementations
│   ├── weather\_agent.py
│   ├── planner\_agent.py
│   ├── forecast\_agent.py
│   ├── update\_agent.py
│   └── display\_agent.py
│
├── data/                  # Stores JSON files
│   ├── today.json
│   └── forecast.json
│
├── dashboard/             # Visualization (Streamlit app)
│   └── app.py
│
├── utils/                 # Config & helpers
│   ├── api\_client.py
│   └── config.py
│
├── main.py                # Daily workflow entry point
├── update.py              # Forecast updater entry point
├── requirements.txt       # Dependencies
└── README.md              # Documentation

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
