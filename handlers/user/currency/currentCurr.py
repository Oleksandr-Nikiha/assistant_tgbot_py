from app import bot

from aiogram import F, Router
from aiogram.types import CallbackQuery

from constans import inlineComm
from keyboards import inlineKeyboard

from services.currencyServ import get_currency_rate

from aiogram.fsm.context import FSMContext
from models.states import Currency

currentCurr_router = Router()


@currentCurr_router.callback_query(F.data == inlineComm.CURRENT_CURR, Currency.menu)
async def currency_type(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Currency.curr_types)
    await bot.edit_message_text(text="Оберіть валюту яка вас цікавить.",
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.currency_type.as_markup())


@currentCurr_router.callback_query(Currency.curr_types)
@currentCurr_router.callback_query(Currency.curr_result)
async def current_currency(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Currency.curr_result)

    currency = get_currency_rate().get_currency_by_code(callback.data)
    await bot.edit_message_text(text=f'На поточний день курс складає {round(currency.rate, 2)} UAH до 1 {callback.data} '
                                     f'\nЗгідно офіційним даним з відкритого ресурсу НБУ.',
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.currency_type.as_markup())
