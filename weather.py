# ============================================
# Weather Scraper for St. Gallen
# Group project by Theo Nikolovski and Tobias Nordström
# ============================================
# What this program does:
# - Connects to wttr.in (a free weather website)
# - Gets the JSON weather data for St. Gallen
# - Shows a 3-day forecast in a clean table
# - Answers research questions about the forecast
# - Shows detailed pandas statistics
# - Saves results to a CSV file
# - Creates a matplotlib bar chart
# - Creates a seaborn chart for a nicer visualization
# ============================================

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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

    # we also need plain numbers for analysis and the charts
    max_temps_num = []
    min_temps_num = []
    rain_chances_num = []

    # today's date so we can label each row properly
    today = datetime.now()

    # wttr.in gives us 3 days of forecast in data["weather"]
    for i, day in enumerate(data["weather"]):
        # calculating the date label for each day
        date_label = (today + timedelta(days=i)).strftime("%A %d %b")
        dates.append(date_label)

        # max and min temperature for the day in celsius
        max_temp = int(day["maxtempC"])
        min_temp = int(day["mintempC"])
        max_temps_num.append(max_temp)
        min_temps_num.append(min_temp)
        max_temps.append(str(max_temp) + " C")
        min_temps.append(str(min_temp) + " C")

        # chance of rain - we take the midday reading (index 4 = noon)
        rain = int(day["hourly"][4]["chanceofrain"])
        rain_chances_num.append(rain)
        rain_chances.append(str(rain) + "%")

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

    # printing the forecast table
    print("\n==============================================")
    print("  3-Day Weather Forecast - St. Gallen, CH")
    print("==============================================\n")
    print(weather_table.to_string(index=False))
    print("\nSource: wttr.in")
    print("Scraped on:", datetime.now().strftime("%Y-%m-%d at %H:%M"))

    # saving the results to a CSV file so it can be opened in Excel
    # the filename includes today's date so each run creates a new file
    filename = "weather_stgallen_" + datetime.now().strftime("%Y-%m-%d") + ".csv"
    weather_table.to_csv(filename, index=False)
    print("Results saved to:", filename)

    # ============================================
    # Pandas Statistics
    # ============================================
    # using pandas and numpy to get proper stats on the temperature data
    # this is the kind of analysis we learned during the course

    # building a numeric dataframe so pandas can run stats on it
    stats_df = pd.DataFrame({
        "Max Temp (C)": max_temps_num,
        "Min Temp (C)": min_temps_num,
        "Rain Chance (%)": rain_chances_num
    })

    print("\n==============================================")
    print("  Temperature Statistics (pandas)")
    print("==============================================\n")
    print(stats_df.describe())

    # using numpy to calculate the temperature range for each day
    temp_ranges = np.array(max_temps_num) - np.array(min_temps_num)
    print("\nTemperature range per day (Max - Min):")
    for i in range(len(dates)):
        print("    " + dates[i] + ": " + str(temp_ranges[i]) + " C")

    # ============================================
    # Research Questions
    # ============================================
    # we wanted to do more than just collect the data
    # so we added some simple analysis to answer useful questions

    print("\n==============================================")
    print("  Research Questions")
    print("==============================================\n")

    # question 1 - what is the warmest day this week?
    warmest_index = max_temps_num.index(max(max_temps_num))
    print("Q1: What is the warmest day this week?")
    print("    " + dates[warmest_index] + " with a max of " + str(max_temps_num[warmest_index]) + " C\n")

    # question 2 - what is the coldest day this week?
    coldest_index = min_temps_num.index(min(min_temps_num))
    print("Q2: What is the coldest day this week?")
    print("    " + dates[coldest_index] + " with a min of " + str(min_temps_num[coldest_index]) + " C\n")

    # question 3 - which day has the highest chance of rain?
    rainiest_index = rain_chances_num.index(max(rain_chances_num))
    print("Q3: Which day has the highest chance of rain?")
    print("    " + dates[rainiest_index] + " with " + str(rain_chances_num[rainiest_index]) + "% chance of rain\n")

    # question 4 - what is the average max temperature over the 3 days?
    avg_max = sum(max_temps_num) / len(max_temps_num)
    print("Q4: What is the average maximum temperature over the 3 days?")
    print("    " + str(round(avg_max, 1)) + " C\n")

    # ============================================
    # Chart 1 - Matplotlib Bar Chart
    # ============================================
    # classic bar chart showing max and min temps side by side

    short_dates = [(today + timedelta(days=i)).strftime("%a %d %b") for i in range(len(dates))]

    x = range(len(short_dates))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))

    # drawing the bars for max and min temperatures
    bars_max = ax.bar([i - width/2 for i in x], max_temps_num, width, label="Max Temp", color="#e07b54")
    bars_min = ax.bar([i + width/2 for i in x], min_temps_num, width, label="Min Temp", color="#5b9bd5")

    # adding the temperature numbers on top of each bar
    for bar in bars_max:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                str(int(bar.get_height())) + "C", ha="center", va="bottom", fontsize=10)
    for bar in bars_min:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                str(int(bar.get_height())) + "C", ha="center", va="bottom", fontsize=10)

    # labelling the chart
    ax.set_title("3-Day Temperature Forecast - St. Gallen, Switzerland", fontsize=13, pad=15)
    ax.set_ylabel("Temperature (C)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(short_dates)
    ax.legend()
    ax.set_ylim(0, max(max_temps_num) + 8)

    plt.tight_layout()

    # saving the matplotlib chart
    chart_filename = "weather_chart_" + datetime.now().strftime("%Y-%m-%d") + ".png"
    plt.savefig(chart_filename)
    print("Temperature chart saved to:", chart_filename)

    # ============================================
    # Chart 2 - Seaborn Chart
    # ============================================
    # seaborn gives us a nicer looking visualization
    # we learned seaborn during the course and wanted to use it here too

    # building a long format dataframe so seaborn can plot both max and min
    seaborn_data = pd.DataFrame({
        "Date": short_dates * 2,
        "Temperature (C)": max_temps_num + min_temps_num,
        "Type": ["Max Temp"] * len(short_dates) + ["Min Temp"] * len(short_dates)
    })

    plt.figure(figsize=(9, 5))
    sns.barplot(data=seaborn_data, x="Date", y="Temperature (C)", hue="Type",
                palette=["#e07b54", "#5b9bd5"])
    plt.title("3-Day Temperature Forecast - St. Gallen (Seaborn)", fontsize=13)
    plt.tight_layout()

    # saving the seaborn chart
    seaborn_filename = "weather_chart_seaborn_" + datetime.now().strftime("%Y-%m-%d") + ".png"
    plt.savefig(seaborn_filename)
    print("Seaborn chart saved to:", seaborn_filename)

# this starts the program
get_weather()
