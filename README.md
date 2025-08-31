Weather Report Generator (Weatherman Project)

A Python CLI application to process weather data files and generate yearly summaries, monthly averages, and daily temperature charts.

Features:
Load multiple weather data files from a folder.
Generate yearly summary: hottest day, coldest day, highest humidity.
Generate monthly averages: average high, low, and humidity.
Generate daily charts: visualize high and low temperatures (highs in red, lows in blue).
Supports multiple reports at once.
Bonus: combined daily bar chart showing both highs and lows.

Usage: 
# Yearly summary
python weatherman.py data/weather_files -e 2005

# Monthly averages
python weatherman.py data/weather_files -a 2006/08

# Daily temperature chart
python weatherman.py data/weather_files -c 2011/03

# Multiple reports at once
python weatherman.py data/weather_files -e 2010 -a 2010/06 -c 2010/06


How it works
Reads all .txt weather files.
Parses daily readings (temperature & humidity).
Computes summaries and charts.
Prints results to CLI.