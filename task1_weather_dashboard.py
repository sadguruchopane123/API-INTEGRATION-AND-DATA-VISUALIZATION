"""
TASK-1: API Integration and Data Visualization
Internship: CODTECH

Description:
This script fetches weather data from OpenWeatherMap API
and creates a visualization dashboard using Matplotlib.
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

def fetch_weather_data():
    """Fetch weather data from API"""
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API")
        return None

def process_data(data):
    """Extract temperature, humidity, and dates"""
    dates = []
    temperatures = []
    humidity = []

    for item in data['list'][:10]:  # First 10 entries
        dates.append(item['dt_txt'])
        temperatures.append(item['main']['temp'])
        humidity.append(item['main']['humidity'])

    return dates, temperatures, humidity

def create_dashboard(dates, temperatures, humidity):
    """Create visualization dashboard"""
    plt.figure(figsize=(12, 6))

    # Temperature Graph
    plt.subplot(2, 1, 1)
    plt.plot(dates, temperatures, marker='o')
    plt.title("Temperature Forecast")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    # Humidity Graph
    plt.subplot(2, 1, 2)
    plt.plot(dates, humidity, marker='o')
    plt.title("Humidity Forecast")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

def main():
    print("Fetching weather data...")

    data = fetch_weather_data()
    if data:
        dates, temps, hum = process_data(data)
        create_dashboard(dates, temps, hum)
        print("✅ Weather Data Visualization Completed Successfully")

if __name__ == "__main__":
    main()
