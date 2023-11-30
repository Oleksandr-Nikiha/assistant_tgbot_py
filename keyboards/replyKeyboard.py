from aiogram.utils.keyboard import ReplyKeyboardBuilder

from constans import replyComm

# Reply Keyboard (Standard)
general_menu = ReplyKeyboardBuilder()
for button in replyComm.DEFAULT_MENU:
    general_menu.button(text=button)
general_menu.adjust(2, 1)
