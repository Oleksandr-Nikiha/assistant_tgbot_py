from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from constans import listComm

general_menu = ReplyKeyboardBuilder()
for button in listComm.DEFAULT_MENU:
    general_menu.button(text=button)
general_menu.adjust(2, 1)

currency_menu = InlineKeyboardBuilder()
for key, value in listComm.CURRENCY_DATA.items():
    currency_menu.button(text=key, callback_data=value)
currency_menu.button(text=listComm.INL_BACK_COMMAND, callback_data=listComm.INL_BACK_ACTION)
currency_menu.adjust(3, 3, 1)

weather_menu = InlineKeyboardBuilder()
for key, value in listComm.WEATHER_CITY.items():
    weather_menu.button(text=key, callback_data=value)
weather_menu.button(text=listComm.INL_BACK_COMMAND, callback_data=listComm.INL_BACK_ACTION)
weather_menu.adjust(3, 1, 1)

other_menu = InlineKeyboardBuilder()
for key, value in listComm.OTHER_MENU.items():
    other_menu.button(text=key, callback_data=value)
other_menu.button(text=listComm.INL_BACK_COMMAND, callback_data=listComm.INL_BACK_ACTION)
other_menu.adjust(1, 1)
