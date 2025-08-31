from typing import List, Optional
from models import WeatherReading

def get_highest_temperature(readings: List[WeatherReading]) -> Optional[WeatherReading]:
    return max((r for r in readings if r.max_temp is not None), key=lambda r: r.max_temp, default=None)

def get_lowest_temperature(readings: List[WeatherReading]) -> Optional[WeatherReading]:
    return min((r for r in readings if r.min_temp is not None), key=lambda r: r.min_temp, default=None)

def get_average_humidity(readings: List[WeatherReading]) -> float:
    humidities = [r.humidity for r in readings if r.humidity is not None]
    return sum(humidities) / len(humidities) if humidities else 0
