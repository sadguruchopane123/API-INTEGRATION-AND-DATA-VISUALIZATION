"""
TASK-1: API Integration and Data Visualization
Internship: CODTECH

Description:
This script fetches real-time weather forecast data from the
OpenWeatherMap API and creates a visualization dashboard
using Matplotlib. It displays temperature and humidity trends.
"""

import requests
import matplotlib.pyplot as plt

# ==============================
# 🔑 ENTER YOUR API KEY HERE
# ==============================
API_KEY = "YOUR_API_KEY_HERE"

# ==============================
# 🌍 ENTER CITY NAME
# ==============================
CITY = "Pune"

# ==============================
# 🌐 API URL
# ==============================
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ==============================
# 📡 FETCH DATA FROM API
# ==============================
def fetch_data():
    print("Fetching data from API...")
    response = requests.get(URL)

    if response.status_code == 200:
        print("✅ Data fetched successfully")
        return response.json()
    else:
        print("❌ Failed to fetch data")
        return None

# ==============================
# 📊 PROCESS DATA
# ==============================
def process_data(data):
    dates = []
    temperatures = []
    humidity = []

    for item in data['list'][:12]:  # take 12 records (~36 hrs)
        dates.append(item['dt_txt'])
        temperatures.append(item['main']['temp'])
        humidity.append(item['main']['humidity'])

    return dates, temperatures, humidity

# ==============================
# 📈 CREATE DASHBOARD
# ==============================
def create_dashboard(dates, temps, hum):
    print("Creating visualization dashboard...")

    plt.figure(figsize=(12, 6))

    # Temperature Graph
    plt.subplot(2, 1, 1)
    plt.plot(dates, temps, marker='o')
    plt.title(f"Temperature Forecast - {CITY}")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    # Humidity Graph
    plt.subplot(2, 1, 2)
    plt.plot(dates, hum, marker='o')
    plt.title(f"Humidity Forecast - {CITY}")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)

    plt.tight_layout()

    # Save dashboard as image (important for submission)
    plt.savefig("weather_dashboard.png")

    plt.show()

    print("✅ Dashboard saved as 'weather_dashboard.png'")

# ==============================
# 🚀 MAIN FUNCTION
# ==============================
def main():
    data = fetch_data()

    if data:
        dates, temps, hum = process_data(data)
        create_dashboard(dates, temps, hum)
        print("🎉 Task-1 Completed Successfully!")

# ==============================
# ▶️ RUN
# ==============================
if __name__ == "__main__":
    main()
