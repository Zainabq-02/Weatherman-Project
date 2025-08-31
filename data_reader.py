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

                    station = filename.replace(".txt", "")
                    reading_date = datetime.strptime(parts[0], "%Y-%m-%d").date()

                    # Only convert if value exists
                    max_temp = int(parts[1]) if part_
