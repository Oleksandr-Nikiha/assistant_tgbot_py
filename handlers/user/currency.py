from app import bot

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import replyComm
from keyboards import inlineKeyboard

from services.currencyServ import get_currency_rate

from aiogram.fsm.context import FSMContext
from models.states import General

currency_router = Router()


@currency_router.message(F.text == replyComm.CURRENCY_COMMAND)
async def currency_init(message: Message, state: FSMContext):
    await state.set_state(General.currency)
    await message.answer("Ви в розділі курсу валют \U0001f4b1 \nОберіть валюту яка вас цікавить.",
                         reply_markup=inlineKeyboard.currency_menu.as_markup())


@currency_router.callback_query(General.currency)
async def selected_currency(callback: CallbackQuery):
    currency = get_currency_rate().get_currency_by_code(callback.data)
    await bot.edit_message_text(text=f'На поточний день курс складає {round(currency.rate, 2)} UAH до 1 {callback.data} '
                                     f'\nЗгідно офіційним даним з відкритого ресурсу НБУ.',
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.currency_menu.as_markup())
