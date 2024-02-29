import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN: str = os.getenv('BOT_TOKEN')
NBU_URL: str = os.getenv('NBU_URL')
PB_URL: str = os.getenv('PB_CURRENCY')

WEATHER_URL: str = os.getenv('WEATHER_URL')
CONDITION_URL: str = os.getenv('CONDITION_URL')
WEATHER_TOKEN: str = os.getenv('WEATHER_TOKEN')
KEY_PATH: str = os.getenv('KEY_PATH')
MONGO_USER: str = os.getenv('MONGO_USER')
MONGO_PASSWORD: str = os.getenv('MONGO_PASSWORD')
MONGO_URL: str = os.getenv('MONGO_URL')