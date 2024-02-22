import re

from app import bot, config

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from constans import inlineComm
from keyboards import inlineKeyboard
from models.states import Accounting
from models.database import acc_db

writeAcc_router = Router()


# Set accounting handlers
@writeAcc_router.callback_query(F.data.in_([inlineComm.INCOME_ACTION, inlineComm.COST_ACTION]), Accounting.action)
async def set_action(callback: CallbackQuery, state: FSMContext):
    await state.update_data(action=callback.data)
    await state.set_state(Accounting.value)

    text = None

    if callback.data == 'Income':
        text = 'Для фіксації доходу, вкажіть суму у форматі 0.00 (напр. 123, 123.22, 123,32).\nТа відправте її.'
        await state.update_data(action_uah='Дохід')
    elif callback.data == 'Cost':
        text = 'Для фіксації витрати, вкажіть суму у форматі 0.00 (напр. 123, 123.22, 123,32).\nТа відправте її.'
        await state.update_data(action_uah='Витрата')

    await bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id,
                                reply_markup=inlineKeyboard.inl_canceled_menu.as_markup())


@writeAcc_router.message(F.text.regexp(r'^\d+(?:[.,]\d{1,2})?$'), Accounting.value)
async def set_value(message: Message, state: FSMContext):
    await state.update_data(value=message.text)
    await state.set_state(Accounting.annotation)

    value_list = re.findall(r"^\d+(?:[.,]\d{1,2})?$", message.text)

    await message.answer(f'Сума {value_list[0]} - зафіксована.\nДодайте опис напр. "Купив хліб" '
                         'або "Знайшов по дорозі"', reply_markup=inlineKeyboard.inl_canceled_menu.as_markup())


@writeAcc_router.message(~F.text.regexp(r'^\d+(?:[.,]\d{1,2})?$'), Accounting.value)
async def set_value(message: Message):

    await message.answer(f'Вибачте, але ви вказали не коректну суму. Спробуйте ще раз. Нагадаю формат який '
                         f'підходить: 123\n, 123.22\n, 123,32',
                         reply_markup=inlineKeyboard.inl_canceled_menu.as_markup())


@writeAcc_router.message(Accounting.annotation)
async def set_annotation(message: Message, state: FSMContext):
    await state.update_data(annotation=message.text)
    await state.set_state(Accounting.validate)
    data = await state.get_data()

    await message.answer(f'Наданий коментар був зафіксований.\nПеревірте коректність введених даних:\n'
                         f'Тип: {data.get("action_uah")}\n'
                         f'Сума: {data.get("value")}\n'
                         f'Нотаток: {data.get("annotation")}',
                         reply_markup=inlineKeyboard.approved_menu.as_markup())


@writeAcc_router.callback_query(F.data.in_(inlineComm.APPROVED_MENU.values()), Accounting.validate)
async def finalize_accounting(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await state.set_state(Accounting.action)

    if callback.data == inlineComm.CONFIRM_ACTION:
        await acc_db.create_accounting(data.get('value'), data.get('action'),
                                       callback.from_user, data.get('annotation'))
        text = 'Я зафіксував операцію.'
    else:
        text = 'Я очистив вказані дані.'

    await bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id,
                                reply_markup=inlineKeyboard.accounting_menu.as_markup())
