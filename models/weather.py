from dataclasses import dataclass


@dataclass
class Weather:
    city_data_name: str
    city_mapped_name: str
    weather_type: int
    last_update_date:  str
    temperature: float
    relative_humidity: int
    pressure: int
    wind_speed: float


@dataclass
class ListWeather:
    weathering: list[Weather]

    def get_weather_by_name(self, city_mapped: str) -> Weather:
        weather = next((w for w in self.weathering if w.city_mapped_name == city_mapped), None)
        return weather
