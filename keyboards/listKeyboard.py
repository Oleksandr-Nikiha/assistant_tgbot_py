from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from constans import listComm

general_menu = ReplyKeyboardBuilder()
for button in listComm.DEFAULT_MENU:
    general_menu.button(text=button)
general_menu.adjust(2, 1)

currency_menu = InlineKeyboardBuilder()
for key, value in listComm.CURRENCY_MENU.items():
    currency_menu.button(text=key, callback_data=value)
currency_menu.button(text=listComm.INL_BACK_COMMAND, callback_data=listComm.INL_BACK_ACTION)
currency_menu.adjust(3, 3, 1)

weather_menu = InlineKeyboardBuilder()
for key, value in listComm.WEATHER_MENU.items():
    weather_menu.button(text=key, callback_data=value)
weather_menu.button(text=listComm.INL_BACK_COMMAND, callback_data=listComm.INL_BACK_ACTION)
weather_menu.adjust(3, 1, 1)

accounting_menu = InlineKeyboardBuilder()
for key, value in listComm.ACCOUNTING_MENU.items():
    accounting_menu.button(text=key, callback_data=value)
accounting_menu.button(text=listComm.INL_BACK_COMMAND, callback_data=listComm.INL_BACK_ACTION)
accounting_menu.adjust(2, 1, 1)

canceled_menu = ReplyKeyboardBuilder()
canceled_menu.button(text=listComm.CANCELED_COMMAND)
canceled_menu.adjust(1)

inl_canceled_menu = InlineKeyboardBuilder()
inl_canceled_menu.button(text=listComm.CANCELED_COMMAND, callback_data=listComm.CANCELED_ACTION)
inl_canceled_menu.adjust(1)

approved_menu = InlineKeyboardBuilder()
for key, value in listComm.APPROVED_MENU.items():
    approved_menu.button(text=key, callback_data=value)
approved_menu.adjust(1, 1)