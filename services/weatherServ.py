import json
import logging
import requests

from constans import inlineComm, parseDict
from utils.memo import memorize, memorize_stamp
from models.weather import Weather, ListWeather
from models.forecast import Forecast, Language, ListForecast
from app.config import WEATHER_URL, CONDITION_URL, WEATHER_TOKEN


def fetch_weather_condition():
    try:
        response = requests.get(CONDITION_URL)
        response.raise_for_status()

        result = json.loads(response.content)
        return result
    except requests.RequestException as e:
        logging.error(f"Error fetching currency data: {e}")
        return None


@memorize
def parsing_forecast_data() -> ListForecast | None:
    forecast_data = fetch_weather_condition()

    if forecast_data:
        list_of_forecasting = [Forecast(**{
            'code': d['code'],
            'day': d['day'],
            'night': d['night'],
            'icon': d['icon'],
            'languages': [
                Language(**lang) for lang in d['languages']
            ]
        }) for d in forecast_data]
        list_forecast_instance = ListForecast(forecasting=list_of_forecasting)
        return list_forecast_instance

    return None


def fetch_weather_data() -> list[dict] | None:
    data = []
    forecast_data = parsing_forecast_data()
    try:
        for city in inlineComm.WEATHER_MENU.values():
            objects = {}

            response = requests.get(WEATHER_URL + city + "&key=" + WEATHER_TOKEN)
            response.raise_for_status()

            r = response.json()

            is_day = r.get('current').get('is_day')
            weather_type = r.get('current').get('condition').get('code')
            forecast_info = forecast_data.get_forecast_by_code(weather_type).get_text_by_lang_code('uk', is_day)
            city_data_name = parseDict.WEATHER_DICT.get(city)

            objects.update({
                'city_data_name': city_data_name,
                'city_mapped_name': city,
                'weather_type': forecast_info,
                'last_update_date': r.get('current').get('last_updated'),
                'temperature': r.get('current').get('temp_c'),
                'relative_humidity': r.get('current').get('humidity'),
                'pressure': r.get('current').get('pressure_mb'),
                'wind_speed': r.get('current').get('wind_kph'),
            })

            data.append(objects)
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching currency data: {e}")
        return None


@memorize_stamp
def parsing_weather() -> ListWeather | None:
    weather_data = fetch_weather_data()

    if weather_data:
        list_of_weathering = [Weather(**weather_dict) for weather_dict in weather_data]
        list_weather_instance = ListWeather(weathering=list_of_weathering)
        return list_weather_instance

    return None


async def main():
    parsing_weather()


if __name__ == "__main__":
    parsing_weather()
