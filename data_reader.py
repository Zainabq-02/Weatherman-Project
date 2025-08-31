# data_reader.py
import os
from datetime import datetime
from models import WeatherReading


def read_data(folder_path, year=None):
    """
    Reads all .txt weather files from the given folder.
    Returns a list of WeatherReading objects.

    Args:
        folder_path (str): path to folder containing .txt weather files
        year (int, optional): filter readings for a specific year
    """
    readings = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r") as f:
                lines = f.readlines()[1:]  # skip header row

                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) < 5:
                        continue  # skip bad rows

                    try:
                        station = filename.replace(".txt", "")
                        reading_date = datetime.strptime(parts[0], "%Y-%m-%d").date()
                        max_temp = int(parts[1]) if parts[1] else None
                        min_temp = int(parts[2]) if parts[2] else None
                        mean_temp = int(parts[3]) if parts[3] else None
                        humidity = int(parts[4]) if parts[4] else None

                        if year is None or reading_date.year == year:
                            readings.append(
                                WeatherReading(
                                    station=station,
                                    reading_date=reading_date,
                                    max_temp=max_temp,
                                    min_temp=min_temp,
                                    mean_temp=mean_temp,
                                    humidity=humidity
                                )
                            )
                    except Exception:
                        continue  # skip malformed rows

    return readings
