from dataclasses import dataclass
from datetime import date

@dataclass
class WeatherReading:
    station: str
    reading_date: date
    max_temp: int
    min_temp: int
    mean_temp: int
    humidity: int
