from app import bot

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from keyboards import listKeyboard
from constans import listComm

from services.currencyServ import get_currency_rate

currency_router = Router()


@currency_router.message(F.text == listComm.CURRENCY_COMMAND)
async def currency_init(message: Message):
    await message.answer("Ви в розділі курсу валют \U0001f4b1 \nОберіть валюту яка вас цікавить.",
                         reply_markup=listKeyboard.currency_menu.as_markup())


@currency_router.callback_query(F.data.in_(listComm.CURRENCY_DATA.values()))
async def selected_currency(callback: CallbackQuery):
    rate = float(get_currency_rate().get_rate_by_currency_code(callback.data))
    rate = round(rate, 2)
    await bot.edit_message_text(text=f'На поточний день курс складає {rate} UAH до 1 {callback.data} '
                                     f'\nЗгідно офіційним даним з відкритого ресурсу НБУ.',
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=listKeyboard.currency_menu.as_markup())
