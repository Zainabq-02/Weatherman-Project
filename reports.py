from models import WeatherReading


def print_summary(highest: WeatherReading, lowest: WeatherReading, avg_humidity: float):
    print(f"Hottest Day: {highest.reading_date} in {highest.station} with {highest.max_temp}°C")
    print(f"Coldest Day: {lowest.reading_date} in {lowest.station} with {lowest.min_temp}°C")
    print(f"Average Humidity: {avg_humidity:.2f}%")


def print_yearly_summary(highest: WeatherReading, lowest: WeatherReading, most_humid: WeatherReading):
    print(f"Highest: {highest.max_temp}°C on {highest.reading_date} in {highest.station}")
    print(f"Lowest: {lowest.min_temp}°C on {lowest.reading_date} in {lowest.station}")
    print(f"Humidity: {most_humid.humidity}% on {most_humid.reading_date} in {most_humid.station}")


def print_monthly_averages(result, year, month):
    """
    result is (avg_high, avg_low, avg_humidity)
    Print in the format the assignment example uses:
      Highest Average: 39C
      Lowest Average: 18C
      Average Mean Humidity: 71%
    """
    avg_high, avg_low, avg_humidity = result
    print(f"\nMonthly Averages for {year}-{month:02d}:")
    # round to nearest integer to match sample formatting
    print(f"Highest Average: {round(avg_high)}C")
    print(f"Lowest Average: {round(avg_low)}C")
    print(f"Average Mean Humidity: {round(avg_humidity)}%")  # percent, rounded


def print_daily_chart(result, year, month):
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"

    print(f"\nDaily Temperature Chart for {year}-{month:02d}:")
    for day, bar_high, bar_low in result:
        print(f"{day:02d} {RED}{bar_high}{RESET}")
        print(f"{day:02d} {BLUE}{bar_low}{RESET}")



# BONUS FEATURE: Combined daily bar chart
def print_combined_daily_chart(result, year, month):
    """
    result is list of tuples: (day, bar, min_temp, max_temp)
      '-' characters = min temp portion, '+' characters = additional up to max temp
    Example printed line:
      01: ---+++++ (3°C - 8°C)
    """
    print(f"\nCombined Daily Temperature Chart for {year}-{month:02d}:")
    for day, bar, min_temp, max_temp in result:
        print(f"{day:02d}: {bar} ({min_temp}°C - {max_temp}°C)")
