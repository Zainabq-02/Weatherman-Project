# parser.py
import os
import datetime
from typing import List, Optional
from models import WeatherReading


def _parse_int(value: str) -> Optional[int]:
    """Return int(value) or None for empty strings."""
    value = value.strip()
    return int(value) if value != "" else None


def load_file(file_path: str) -> List[WeatherReading]:
    """
    Parse a single weather file and return a list of WeatherReading objects.

    Assumes files like: Murree_weather_2004_Aug.txt
    Column layout (based on samples):
      0 = date (YYYY-M-D)
      1 = Max TemperatureC
      2 = Mean TemperatureC
      3 = Min TemperatureC
      ...
      7 = Max Humidity
      8 = Mean Humidity
      9 = Min Humidity
    """
    readings: List[WeatherReading] = []

    # extract station from filename (e.g. "Murree_weather_2004_Aug.txt" -> "Murree")
    filename = os.path.basename(file_path)
    if "_weather_" in filename:
        station = filename.split("_weather_")[0]
    else:
        station = filename.split("_")[0]

    with open(file_path, "r", encoding="utf-8") as f:
        # skip header line
        header = f.readline()

        for line in f:
            line = line.strip()
            if not line:
                # skip blank lines
                continue

            parts = [p.strip() for p in line.split(",")]

            # date must exist
            if not parts or not parts[0]:
                continue

            try:
                # Flexible date parsing
                date_str = parts[0]
                reading_date = None
                for fmt in ("%Y-%m-%d", "%Y-%m-%d", "%Y-%m-%d"):  # you can add more formats if needed
                    try:
                        reading_date = datetime.datetime.strptime(date_str, fmt).date()
                        break
                    except ValueError:
                        continue
                if reading_date is None:
                    raise ValueError(f"Unrecognized date format: {date_str}")

                # correct column mapping:
                max_temp = _parse_int(parts[1]) if len(parts) > 1 else None
                mean_temp = _parse_int(parts[2]) if len(parts) > 2 else None
                min_temp = _parse_int(parts[3]) if len(parts) > 3 else None

                # humidity: choose the column you want to store in WeatherReading.humidity
                # currently we store the "Max Humidity" (index 7) because sample outputs used it.
                max_humidity = _parse_int(parts[7]) if len(parts) > 7 else None
                mean_humidity = _parse_int(parts[8]) if len(parts) > 8 else None

                readings.append(
                    WeatherReading(
                        station=station,
                        reading_date=reading_date,
                        max_temp=max_temp,
                        min_temp=min_temp,
                        mean_temp=mean_temp,
                        humidity=mean_humidity

                        # ... then append ...

                    )
                )
            except Exception as e:
                # keep the message short and helpful during parsing
                print(f"Skipping line: {line}\n  because: {e}")

    return readings


def load_all_files(folder_path: str) -> List[WeatherReading]:
    """Load every .txt file inside folder_path and return combined readings."""
    all_readings: List[WeatherReading] = []
    for name in os.listdir(folder_path):
        if not name.lower().endswith(".txt"):
            continue
        path = os.path.join(folder_path, name)
        all_readings.extend(load_file(path))
    return all_readings
