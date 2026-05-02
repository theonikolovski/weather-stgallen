# Weather Scraper - St. Gallen

Group project for XCamp Coding@HSG
Authors: Theo Nikolovski and Tobias Nordström
Language: Python

---

## What does this program do?

This program automatically fetches the 3-day weather forecast for St. Gallen, Switzerland from the internet and displays the results in a clean table directly in the terminal.

It uses a technique called web scraping. Web scraping means the program connects to a website, downloads its data, and extracts only the information we need. In this case, we connect to wttr.in, a free and public weather service, and we extract the date, weather description, maximum temperature, minimum temperature, and chance of rain for each of the next 3 days.

Once the data is collected the program does several things with it. First it displays the forecast in a clean table in the terminal. Second it runs a full statistical analysis using pandas and numpy, showing mean, min, max and the temperature range for each day. Third it answers 4 research questions about the data, such as which day is the warmest and which day has the highest chance of rain. Finally it creates two charts and saves them as PNG image files, one using matplotlib and one using seaborn for a nicer visualization.

The program also saves all the results to a CSV file on your computer. A CSV file is a simple spreadsheet format that can be opened directly in Microsoft Excel or Google Sheets. This is useful because it means the weather data is not just printed once and lost. It gets saved with today's date in the filename, so you can collect multiple days of data over time and analyze it later. This is exactly how data analysts work in real life: they automate the collection of data and store it so they can study trends, compare days, or create charts.

Example of what the terminal output looks like:

```
==============================================
  3-Day Weather Forecast - St. Gallen, CH
==============================================

           Date Description Max Temp Min Temp Rain Chance
Thursday 30 Apr       Sunny    17 C     3 C          0%
  Friday 01 May       Sunny    17 C     2 C          0%
Saturday 02 May       Sunny    20 C     7 C          0%

Source: wttr.in
Scraped on: 2026-04-30 at 17:06
Results saved to: weather_stgallen_2026-04-30.csv

==============================================
  Temperature Statistics (pandas)
==============================================

       Max Temp (C)  Min Temp (C)  Rain Chance (%)
count      3.000000      3.000000         3.000000
mean      18.000000      4.000000         0.000000
std        1.732051      2.645751         0.000000
min       17.000000      2.000000         0.000000
25%       17.000000      2.500000         0.000000
50%       17.000000      3.000000         0.000000
75%       18.500000      5.000000         0.000000
max       20.000000      7.000000         0.000000

Temperature range per day (Max - Min):
    Thursday 30 Apr: 14 C
    Friday 01 May: 15 C
    Saturday 02 May: 13 C

==============================================
  Research Questions
==============================================

Q1: What is the warmest day this week?
    Saturday 02 May with a max of 20 C

Q2: What is the coldest day this week?
    Thursday 30 Apr with a min of 3 C

Q3: Which day has the highest chance of rain?
    Thursday 30 Apr with 0% chance of rain

Q4: What is the average maximum temperature over the 3 days?
    18.0 C

Temperature chart saved to: weather_chart_2026-04-30.png
Seaborn chart saved to: weather_chart_seaborn_2026-04-30.png
```

---

## How the program works (step by step)

1. The program sends a request to wttr.in, a free weather website, asking for the weather data for St. Gallen in JSON format. JSON is a structured data format that is easy for Python to read.

2. It checks that the request was successful. If the website could not be reached, it prints an error message and stops.

3. It loops through the 3 days of forecast data and collects the date, description, max temperature, min temperature, and rain chance for each day.

4. It puts all the collected data into a table using the pandas library, which is a popular Python tool for working with structured data.

5. It prints the table in the terminal in a clean and readable format.

6. It runs a full statistical analysis using pandas .describe() and numpy to calculate mean, min, max, standard deviation and the daily temperature range.

7. It answers 4 research questions about the forecast data, for example which day is the warmest, which day has the highest chance of rain, and what the average maximum temperature is over the 3 days.

8. It creates a bar chart using matplotlib and saves it as a PNG image file.

9. It creates a second nicer looking chart using seaborn and saves it as a separate PNG image file.

10. It saves the full table as a CSV file with today's date in the filename, for example: weather_stgallen_2026-04-30.csv. This file can be opened in Excel.

---

## What Theo and Tobias did

Theo was responsible for setting up the project, writing the data extraction logic (connecting to the website and reading the JSON response), building the output table using pandas, adding the research questions and analysis, and creating the temperature bar chart using matplotlib.

Tobias was responsible for testing the program, checking that the output matched the real weather, writing the documentation, and helping debug issues during development. Tobias also added the CSV export feature so the data gets saved automatically each time the program runs.

Both students followed the DataQuest web scraping tutorial together and adapted the approach to work with a real Swiss weather source instead of the US National Weather Service used in the tutorial.

---

## How to download and run the program

Follow these steps exactly and the program will work.

### Step 1 - Check that Python is installed

You need Python 3 on your computer. To check, open a terminal and type:

```
python --version
```

If you see something like Python 3.x.x you are ready. If not, download Python from https://www.python.org/downloads/ and install it.

On Mac, open Terminal by pressing Command + Space and typing Terminal.
On Windows, search for "cmd" or "PowerShell" in the Start menu.

### Step 2 - Download the project

Go to the GitHub page for this project. Click the green "Code" button at the top right, then click "Download ZIP". Save the ZIP file and unzip it somewhere easy to find, for example your Desktop.

When you unzip the file, GitHub will create a folder called weather-stgallen-main. That is normal, the name always includes -main at the end when downloaded from GitHub.

### Step 3 - Install the required libraries

The program uses five Python libraries that need to be installed before running. Open your terminal and navigate to the project folder. If you unzipped it on the Desktop, type:

On Mac:
```
cd ~/Desktop/weather-stgallen-main
```

On Windows:
```
cd C:\Users\YourName\Desktop\weather-stgallen-main
```

Then run this command to install the libraries:

```
pip install requests pandas numpy matplotlib seaborn
```

You only need to do this once.

### Step 4 - Run the program

While still in the project folder in your terminal, type:

```
python weather.py
```

The program will connect to the internet, fetch the weather for St. Gallen, print the forecast table, and save a CSV file in the same folder.

The CSV file will be named something like weather_stgallen_2026-04-30.csv and can be opened directly in Excel.

---

## Requirements

- Python 3 or newer
- An internet connection
- The following Python libraries: requests, pandas, numpy, matplotlib, seaborn (installed in Step 3)

---

## Data source

This project scrapes weather data from wttr.in, a free and publicly available weather service that does not require an account or API key.

The URL we use is: https://wttr.in/St.Gallen?format=j1

We considered using AccuWeather, which was suggested in the project brief, but it turned out not to be possible for two reasons. First, AccuWeather loads its data dynamically using JavaScript, which means when Python requests the page it only receives an empty HTML shell with no weather data in it. BeautifulSoup cannot run JavaScript so it would see nothing useful. Second, AccuWeather actively blocks automated requests and their terms of service forbid scraping since they sell their data commercially.

wttr.in is a better fit for this project because it is specifically designed to be used the way we use it, it is completely free and open, and it provides the data in clean JSON format which Python can read directly. The weather data it provides comes from the same reliable underlying sources used by large weather platforms.

---

## What we learned during the course and used in this project

During the XCamp Coding@HSG course we worked through a series of individual Python tasks covering all the core programming skills. This group project was a chance to bring everything together in one real program. Here is a breakdown of what we learned and where it shows up in the code.

**Variables and data types** were the first thing we learned. In this project we use variables constantly, for example to store the website URL, the response from the server, and all the weather values like temperatures and descriptions.

**Input and output** was one of the first tasks we did, starting with simple print statements. In this project the print function is used to display the forecast table and status messages to the user in the terminal.

**Conditionals** came shortly after. We use an if statement to check whether the request to the website was successful. If the status code is not 200, the program prints an error message and stops instead of crashing.

**Loops** were a big part of the course. We use a for loop to go through each of the 3 days returned by the weather API and collect the data for each one. Without loops we would have had to write the same code 3 times manually.

**Lists** were used throughout the course in many tasks. In this project we create lists to collect all the dates, descriptions, temperatures and rain chances before putting them into a table.

**String manipulation** was something we practiced a lot, including replacing characters, counting letters, and formatting text. In this project we use string formatting to build the CSV filename with today's date included, for example weather_stgallen_2026-04-30.csv.

**Functions** were introduced later in the course. The entire program is wrapped inside a function called get_weather(). This keeps the code organized and makes it easy to run or reuse.

**File handling** was one of the last skills we learned in the individual tasks, where we practiced writing to and reading from files. In this project we use it to save the weather results to a CSV file on the computer so the data is stored and can be opened later in Excel.

**numpy** was something we learned and used in the data science tasks. In this project we use numpy to calculate the temperature range for each day by subtracting the min temperature array from the max temperature array. numpy makes working with numbers and arrays much faster and cleaner than doing it manually.

**seaborn** was a library we learned during the data visualization tasks in the course. We used it to create a second chart that looks cleaner and more professional than the standard matplotlib chart. Seaborn is built on top of matplotlib and makes it much easier to create good looking visualizations with less code.

**pandas data analysis** went beyond just displaying data. We used the pandas .describe() method to generate a full statistical summary of the temperature data including mean, standard deviation, min, max and percentiles. This is exactly how data analysts explore datasets in real life.

**Debugging** was also part of the course. During development we ran into issues with the website not returning data as expected and had to read error messages carefully and fix the code step by step.

Overall this project required us to combine almost every skill from the course into one working program, which is exactly what made it a good challenge to finish with.

---

## Project files

| File | What it does |
|---|---|
| weather.py | The main Python program that scrapes and saves the weather data |
| README.md | This documentation file explaining the project and how to run it |
| weather_stgallen_YYYY-MM-DD.csv | The CSV file generated when you run the program (opens in Excel) |
| weather_chart_YYYY-MM-DD.png | The matplotlib temperature bar chart generated when you run the program |
| weather_chart_seaborn_YYYY-MM-DD.png | The seaborn temperature chart generated when you run the program |
