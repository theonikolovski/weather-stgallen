# ============================================
# Weather Scraper for St. Gallen
# Group project by Theo and Tobias
# ============================================
# What this program does:
# - Connects to wttr.in (a free weather website)
# - Gets the JSON weather data for St. Gallen
# - Shows a 3-day forecast in a clean table
# ============================================

import requests
import pandas as pd
from datetime import datetime, timedelta

def get_weather():
    # wttr.in has a handy JSON format we can use directly - no HTML parsing needed
    url = "https://wttr.in/St.Gallen?format=j1"

    # adding a browser header so the website accepts our request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print("Fetching weather data for St. Gallen...")

    # sending the request to download the weather data
    response = requests.get(url, headers=headers)

    # 200 means the request worked, anything else means something went wrong
    if response.status_code != 200:
        print("Error: Could not reach wttr.in. Check your internet connection.")
        return

    # reading the response as JSON (like a structured dictionary)
    data = response.json()

    # empty lists to collect all the weather info
    dates = []
    descriptions = []
    max_temps = []
    min_temps = []
    rain_chances = []

    # today's date so we can label each row properly
    today = datetime.now()

    # wttr.in gives us 3 days of forecast in data["weather"]
    for i, day in enumerate(data["weather"]):
        # calculating the date label for each day
        date_label = (today + timedelta(days=i)).strftime("%A %d %b")
        dates.append(date_label)

        # max and min temperature for the day in celsius
        max_temps.append(day["maxtempC"] + " °C")
        min_temps.append(day["mintempC"] + " °C")

        # chance of rain - we take the midday reading (index 4 = noon)
        rain_chances.append(day["hourly"][4]["chanceofrain"] + "%")

        # the weather description for the day
        descriptions.append(day["hourly"][4]["weatherDesc"][0]["value"])

    # building a nice table with all the info using pandas
    weather_table = pd.DataFrame({
        "Date": dates,
        "Description": descriptions,
        "Max Temp": max_temps,
        "Min Temp": min_temps,
        "Rain Chance": rain_chances
    })

    # printing the final result
    print("\n==============================================")
    print("  3-Day Weather Forecast - St. Gallen, CH")
    print("==============================================\n")
    print(weather_table.to_string(index=False))
    print("\nSource: wttr.in")
    print("Scraped on:", datetime.now().strftime("%Y-%m-%d at %H:%M"))

    # saving the results to a CSV file so the professor can open it in Excel
    # the filename includes today's date so each run creates a new file
    filename = "weather_stgallen_" + datetime.now().strftime("%Y-%m-%d") + ".csv"
    weather_table.to_csv(filename, index=False)
    print("Results saved to:", filename)

# this starts the program
get_weather()
