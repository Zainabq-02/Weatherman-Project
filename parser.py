import os
import datetime
from typing import List, Optional
from models import WeatherReading


def _parse_int(value: str) -> Optional[int]:
    value = value.strip()
    return int(value) if value != "" else None


def _parse_date(date_str: str) -> Optional[datetime.date]:
    # try multiple formats
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"):
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


def load_file(file_path: str) -> List[WeatherReading]:
    readings: List[WeatherReading] = []

    filename = os.path.basename(file_path)
    station = filename.split("_weather_")[0] if "_weather_" in filename else filename.split("_")[0]

    with open(file_path, "r", encoding="utf-8") as f:
        f.readline()  # skip header

        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = [p.strip() for p in line.split(",")]
            if not parts or not parts[0]:
                continue

            reading_date = _parse_date(parts[0])
            if reading_date is None:
                continue

            max_temp = _parse_int(parts[1]) if len(parts) > 1 else None
            mean_temp = _parse_int(parts[2]) if len(parts) > 2 else None
            min_temp = _parse_int(parts[3]) if len(parts) > 3 else None
            mean_humidity = _parse_int(parts[8]) if len(parts) > 8 else None

            readings.append(
                WeatherReading(
                    station=station,
                    reading_date=reading_date,
                    max_temp=max_temp,
                    min_temp=min_temp,
                    mean_temp=mean_temp,
                    humidity=mean_humidity
                )
            )

    return readings


def load_all_files(folder_path: str) -> List[WeatherReading]:
    all_readings: List[WeatherReading] = []
    for name in os.listdir(folder_path):
        if not name.lower().endswith(".txt"):
            continue
        path = os.path.join(folder_path, name)
        all_readings.extend(load_file(path))
    return all_readings
