import argparse
from parser import load_all_files
from calculations import get_highest_temperature, get_lowest_temperature, get_average_humidity
from reports import (
    print_summary,
    print_yearly_summary,
    print_monthly_averages,
    print_daily_chart,
    print_combined_daily_chart,
)
from computation import (
    get_yearly_summary,
    get_monthly_averages,
    get_daily_chart,
    get_combined_daily_chart,
)


def main():
    parser = argparse.ArgumentParser(description="Weather Report Generator CLI")
    parser.add_argument("folder", help="Path to folder containing weather data files")
    parser.add_argument("-e", "--yearly", type=int, help="Yearly summary report for given year")
    parser.add_argument("-a", "--monthly", help="Monthly averages report in YEAR/MONTH format, e.g., 2005/6")
    parser.add_argument("-c", "--chart", help="Daily temperature chart in YEAR/MONTH format, e.g., 2011/03")

    # Bonus combined daily chart
    parser.add_argument("-b", "--bonus", help="Combined daily bar chart in YEAR/MONTH format, e.g., 2011/03")

    args = parser.parse_args()

    # ---- Load all readings ----
    readings = load_all_files(args.folder)
    print(f"Loaded {len(readings)} rows from all files")

    # ---- Overall stats ----
    hottest = get_highest_temperature(readings)
    coldest = get_lowest_temperature(readings)
    avg_humidity = get_average_humidity(readings)
    print_summary(hottest, coldest, avg_humidity)

    printed_yearly = False

    # ---- Yearly summary (if requested) ----
    if args.yearly:
        summary = get_yearly_summary(readings, args.yearly)
        if summary:
            hottest_y, coldest_y, most_humid_y = summary
            print_yearly_summary(hottest_y, coldest_y, most_humid_y)
            printed_yearly = True

    # ---- Monthly averages ----
    monthly_year = None
    if args.monthly:
        try:
            year, month = map(int, args.monthly.split("/"))
            monthly_year = year
        except Exception:
            year = None
            month = None
        if year and month:
            averages = get_monthly_averages(readings, year, month)
            if averages:
                print_monthly_averages(averages, year, month)

    # ---- Daily chart ----
    if args.chart:
        year_c, month_c = map(int, args.chart.split("/"))
        chart = get_daily_chart(readings, year_c, month_c)
        if chart:
            print_daily_chart(chart, year_c, month_c)

    # ---- Bonus combined daily chart ----
    if args.bonus:
        year_b, month_b = map(int, args.bonus.split("/"))
        combined_chart = get_combined_daily_chart(readings, year_b, month_b)
        if combined_chart:
            print_combined_daily_chart(combined_chart, year_b, month_b)

    # ---- Print yearly summary at the bottom if user asked monthly but didn't ask yearly ----
    if not printed_yearly and monthly_year is not None:
        summary = get_yearly_summary(readings, monthly_year)
        if summary:
            print("\nYearly Summary for {}:".format(monthly_year))
            print_yearly_summary(*summary)


if __name__ == "__main__":
    main()
