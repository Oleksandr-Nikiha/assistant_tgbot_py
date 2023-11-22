from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from . import config

dp = Dispatcher(BaseStorage=MemoryStorage)
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
