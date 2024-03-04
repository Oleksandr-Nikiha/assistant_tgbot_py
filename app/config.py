"""This config module where get and set configuration for bot use"""
import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN: str = os.getenv('BOT_TOKEN')
WEATHER_TOKEN: str = os.getenv('WEATHER_TOKEN')

PB_URL: str = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
WEATHER_URL: str = 'https://api.weatherapi.com/v1/current.json?q='
CONDITION_URL: str = 'https://www.weatherapi.com/docs/conditions.json'

MONGO_USER: str = os.getenv('MONGO_USER')
MONGO_PASSWORD: str = os.getenv('MONGO_PASSWORD')
MONGO_URL: str = os.getenv('MONGO_URL')
