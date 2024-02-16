import logging
import re

from app import bot

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import replyComm, inlineComm
from keyboards import inlineKeyboard

from services.currencyServ import get_currency_rate

from aiogram.fsm.context import FSMContext
from models.states import Currency

swapCurr_router = Router()


@swapCurr_router.callback_query(F.data == inlineComm.CURRENT_SWAP, Currency.menu)
@swapCurr_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Currency.swap_action)
@swapCurr_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Currency.swap_result)
async def swap_type(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Currency.swap_types)
    await bot.edit_message_text(text="Оберіть Валюту яка вас цікавить.",
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.currency_type.as_markup())


@swapCurr_router.callback_query(Currency.swap_types)
@swapCurr_router.callback_query(F.data == inlineComm.CANCELED_ACTION, Currency.swap_values)
async def swap_action(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Currency.swap_action)

    if callback.data != inlineComm.CANCELED_ACTION:
        curr_type = callback.data
        await state.update_data(types=callback.data)

        currency = get_currency_rate().get_currency_by_code(callback.data)
        await state.update_data(currency=currency.rate)
    else:
        data = await state.get_data()

        curr_type = data.get('types')
        currency = get_currency_rate().get_currency_by_code(data.get('types'))

    await bot.edit_message_text(text=f'На поточний день курс складає {round(currency.rate, 2)} UAH до 1 {curr_type}'
                                     f'\nЗгідно офіційним даним з відкритого ресурсу НБУ.'
                                     f'\nОберіть дію яка вас цікавить',
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.currency_action.as_markup())


@swapCurr_router.callback_query(Currency.swap_action)
@swapCurr_router.callback_query(Currency.swap_result)
async def swap_value(callback: CallbackQuery, state: FSMContext):
    await state.update_data(action=callback.data)
    await state.set_state(Currency.swap_values)

    data = await state.get_data()
    text = None

    if callback.data == inlineComm.BUY_ACTION:
        text = (f'Вкажіть суму {data.get('types')} яку ви хочете придбати'
                f'\nУ форматі 0.00 (напр. 123, 123.22, 123,32).'
                f'\nТа відправте її.')
    elif callback.data == inlineComm.SELL_ACTION:
        text = (f'Вкажіть суму {data.get('types')} яку ви хочете продати '
                f'\nУ форматі 0.00 (напр. 123, 123.22, 123,32).'
                f'\nТа відправте її.')

    await bot.edit_message_text(text=text,
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.inl_canceled_menu.as_markup())


@swapCurr_router.message(F.text.regexp(r'^\d+(?:[.,]\d{1,2})?$'), Currency.swap_values)
async def swap_result(message: Message, state: FSMContext):
    await state.set_state(Currency.swap_result)

    data = await state.get_data()
    value_list = re.findall(r"^\d+(?:[.,]\d{1,2})?$", message.text)
    result_value = float(value_list[0]) * float(data.get('currency'))
    text = None

    if data.get('action') == inlineComm.BUY_ACTION:
        text = f'Для купівлі {value_list[0]} {data.get('types')} вам знадобиться {round(result_value, 2)} UAH'
    if data.get('action') == inlineComm.SELL_ACTION:
        text = f'За продаж {value_list[0]} {data.get('types')} ви отримаєте {round(result_value, 2)} UAH'

    text += f'\nЯку наступну операцію бажаєте здійснити з {data.get('types')}?'
    await message.answer(text, reply_markup=inlineKeyboard.currency_action.as_markup())
