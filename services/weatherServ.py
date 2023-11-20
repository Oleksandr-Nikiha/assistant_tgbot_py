import json

import requests
import logging
from datetime import datetime, timedelta

from models.weather import Weather, ListWeather
from models.forecast import Forecast, Language, ListForecast
# from app.config import WEATHER_URL, CONDITION_URL, WEATHER_TOKEN
from constans import listComm

WEATHER_URL="https://api.weatherapi.com/v1/current.json?q="
WEATHER_TOKEN="2883999254fe47928d861353232909"
CONDITION_URL="https://www.weatherapi.com/docs/conditions.json"


def memorize(func):
    cache = {}
    stamp = {}

    def wrapper(*args):
        if args in cache:
            if datetime.now() - stamp[args] > timedelta(hours=1):
                result = func(*args)
                cache[args] = result
                stamp[args] = datetime.now()
                return result
            else:
                return cache[args]
        else:
            stamp[args] = datetime.now()
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


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
def parsing_forecast_data():
    forecast_data = fetch_weather_condition()

    if forecast_data:
        list_of_forecasting = [Forecast(**forecast_dict) for forecast_dict in forecast_data]
        list_forecast_instance: ListForecast[Forecast] = ListForecast(forecasting=list_of_forecasting)
        return list_forecast_instance

    return None


def fetch_weather_data():
    data = []
    forecast_data: ListForecast[Forecast] = parsing_forecast_data()
    try:
        for city in listComm.WEATHER_CITY.values():
            objects = {}

            response = requests.get(WEATHER_URL + city + "&key=" + WEATHER_TOKEN)
            response.raise_for_status()

            r = response.json()
            is_day = r.get('current').get('is_day')
            weather_type = r.get('current').get('condition').get('code')
            forecast_info = forecast_data.get_forecast_by_code(weather_type).get_text_by_lang_code('uk', is_day)

            objects.update({
                'city_data_name': r.get('location').get('name'),
                'city_mapped_name': city,
                'weather_type': forecast_info,
                'last_update_date': r.get('current').get('last_updated'),
                'temperature': r.get('current').get('temp_c'),
                'relativeHumidity': r.get('current').get('humidity'),
                'pressure': r.get('current').get('pressure_mb'),
                'windSpeed': r.get('current').get('wind_kph'),
            })

            print(objects)

            data.append(objects)
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching currency data: {e}")
        return None


@memorize
def parsing_weather():
    weather_data = fetch_weather_data()

    if weather_data:
        list_of_weathering = [Weather(**weather_dict) for weather_dict in weather_data]
        list_weather_instance: ListWeather[Weather] = ListWeather(weathering=list_of_weathering)
        return list_weather_instance

    return None


if __name__ == '__main__':
    parsing_forecast_data()
    parsing_weather()
