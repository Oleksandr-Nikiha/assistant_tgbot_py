from os import getenv

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN: str = getenv('BOT_TOKEN')
NBU_URL: str = getenv('NBU_URL')

WEATHER_URL: str = getenv('WEATHER_URL')
CONDITION_URL: str = getenv('CONDITION_URL')
WEATHER_TOKEN: str = getenv('WEATHER_TOKEN')