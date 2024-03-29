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
    currency_data = get_currency_rate()
    currency = currency_data.get_currency_by_code(callback.data)
    by_date = currency_data.by_date

    days_text = 'поточний день' if not by_date else by_date.strftime('%d.%m.%Y')

    text = (f'На {days_text} вартість 1 {currency.currency} складає'
            f'\n{round(currency.saleRateNB, 2)} UAH - за курсом НБУ'
            f'\n{round(currency.saleRate, 2)} UAH - курс купівлі.'
            f'\n{round(currency.purchaseRate, 2)} UAH - курс продажу'
            f'\nЗгідно офіційним даним з відкритого ресурсу PrivatBank.')

    await bot.edit_message_text(text=text,
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.currency_type.as_markup())
