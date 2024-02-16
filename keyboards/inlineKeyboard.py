from aiogram.utils.keyboard import InlineKeyboardBuilder

from constans import inlineComm

# Inline Keyboard
currency_menu = InlineKeyboardBuilder()
for key, value in inlineComm.CURRENCY_MENU.items():
    currency_menu.button(text=key, callback_data=value)
currency_menu.button(text=inlineComm.INL_BACK_COMMAND, callback_data=inlineComm.INL_BACK_ACTION)
currency_menu.adjust(1, 1, 1)

currency_type = InlineKeyboardBuilder()
for key, value in inlineComm.CURRENCY_TYPE.items():
    currency_type.button(text=key, callback_data=value)
for key, value in inlineComm.BEHIND_MENU.items():
    currency_type.button(text=key, callback_data=value)
currency_type.adjust(3, 3, 1)

currency_action = InlineKeyboardBuilder()
for key, value in inlineComm.SWAP_MENU.items():
    currency_action.button(text=key, callback_data=value)
for key, value in inlineComm.BEHIND_MENU.items():
    currency_action.button(text=key, callback_data=value)
currency_action.adjust(1, 1, 1)

weather_menu = InlineKeyboardBuilder()
for key, value in inlineComm.WEATHER_MENU.items():
    weather_menu.button(text=key, callback_data=value)
weather_menu.button(text=inlineComm.INL_BACK_COMMAND, callback_data=inlineComm.INL_BACK_ACTION)
weather_menu.adjust(3, 1, 1)

accounting_menu = InlineKeyboardBuilder()
for key, value in inlineComm.ACCOUNTING_MENU.items():
    accounting_menu.button(text=key, callback_data=value)
accounting_menu.button(text=inlineComm.INL_BACK_COMMAND, callback_data=inlineComm.INL_BACK_ACTION)
accounting_menu.adjust(2, 1, 1)

inl_canceled_menu = InlineKeyboardBuilder()
for key, value in inlineComm.CANCELED_MENU.items():
    inl_canceled_menu.button(text=key, callback_data=value)
inl_canceled_menu.adjust(1)

approved_menu = InlineKeyboardBuilder()
for key, value in inlineComm.APPROVED_MENU.items():
    approved_menu.button(text=key, callback_data=value)
approved_menu.adjust(1, 1)

statistics_type = InlineKeyboardBuilder()
for key, value in inlineComm.STATISTICS_TYPE.items():
    statistics_type.button(text=key, callback_data=value)
for key, value in inlineComm.BEHIND_MENU.items():
    statistics_type.button(text=key, callback_data=value)
statistics_type.adjust(3, 1)

statistics_period = InlineKeyboardBuilder()
for key, value in inlineComm.STATISTICS_PERIOD.items():
    statistics_period.button(text=key, callback_data=value)
for key, value in inlineComm.BEHIND_MENU.items():
    statistics_period.button(text=key, callback_data=value)
statistics_period.adjust(1, 1, 1, 1, 1)