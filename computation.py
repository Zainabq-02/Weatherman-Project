# computation.py

def get_yearly_summary(readings, year):
    yearly = [r for r in readings if r.reading_date.year == year]

    # filter out missing values
    valid_max = [r for r in yearly if r.max_temp is not None]
    valid_min = [r for r in yearly if r.min_temp is not None]
    valid_hum = [r for r in yearly if r.humidity is not None]

    if not valid_max or not valid_min or not valid_hum:
        return None

    hottest = max(valid_max, key=lambda r: r.max_temp)
    coldest = min(valid_min, key=lambda r: r.min_temp)
    most_humid = max(valid_hum, key=lambda r: r.humidity)

    return hottest, coldest, most_humid


def get_monthly_averages(readings, year, month):
    monthly = [r for r in readings if r.reading_date.year == year and r.reading_date.month == month]

    max_temps = [r.max_temp for r in monthly if r.max_temp is not None]
    min_temps = [r.min_temp for r in monthly if r.min_temp is not None]
    humidities = [r.humidity for r in monthly if r.humidity is not None]

    if not max_temps or not min_temps or not humidities:
        return None

    avg_high = sum(max_temps) / len(max_temps)
    avg_low = sum(min_temps) / len(min_temps)
    avg_humidity = sum(humidities) / len(humidities)

    return avg_high, avg_low, avg_humidity


def get_daily_chart(readings, year, month):
    daily = [r for r in readings if r.reading_date.year == year and r.reading_date.month == month]
    chart = []

    for r in daily:
        if r.max_temp is not None and r.min_temp is not None:
            bar_high = "+" * r.max_temp
            bar_low = "+" * r.min_temp
            chart.append((r.reading_date.day, bar_high, bar_low))

    return chart



#  BONUS FEATURE: Combined daily bar chart
def get_combined_daily_chart(readings, year, month):
    daily = [r for r in readings if r.reading_date.year == year and r.reading_date.month == month]
    chart = []

    for r in daily:
        if r.max_temp is not None and r.min_temp is not None:
            min_bar = "-" * r.min_temp
            max_bar = "+" * (r.max_temp - r.min_temp)
            bar = min_bar + max_bar
            chart.append((r.reading_date.day, bar, r.min_temp, r.max_temp))

    return chart
