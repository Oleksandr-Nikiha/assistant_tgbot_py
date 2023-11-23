from app import bot, db

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import listComm
from keyboards import listKeyboard

from utils.fireBase import AccountingDB

from aiogram.fsm.context import FSMContext
from models.states import Accounting

accounting_router = Router()

acc_db = AccountingDB(db)


@accounting_router.message(F.text == listComm.ACCOUNTING_COMMAND)
async def accounting_init(message: Message, state: FSMContext):
    await state.set_state(Accounting.action)
    await message.answer('Ви в розділі Фінансовий облік \U0001f4d2 \nОберіть бажаний пункт.',
                         reply_markup=listKeyboard.accounting_menu.as_markup())


@accounting_router.message(F.text == listComm.CANCELED_COMMAND)
async def canceled_accounting(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Accounting.action)

    await message.answer('Ви в розділі Фінансовий облік \U0001f4d2 \nОберіть бажаний пункт.',
                         reply_markup=listKeyboard.accounting_menu.as_markup())


@accounting_router.callback_query(F.data == listComm.CANCELED_ACTION)
async def canceled_accounting(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(Accounting.action)

    await bot.edit_message_text('Ви в розділі Фінансовий облік \U0001f4d2 \nОберіть бажаний пункт.',
                                callback.message.chat.id, callback.message.message_id,
                                reply_markup=listKeyboard.accounting_menu.as_markup())


@accounting_router.callback_query(Accounting.action, F.data.in_([listComm.INCOME_ACTION, listComm.COST_ACTION]))
async def set_action(callback: CallbackQuery, state: FSMContext):
    await state.update_data(action=callback.data)
    await state.set_state(Accounting.value)

    text = None

    if callback.data == 'Income':
        text = 'Для фіксації доходу, вкажіть суму у форматі 0.00 (напр. 12590.00).\nТа відправте її.'
        await state.update_data(action_uah='Дохід')
    elif callback.data == 'Cost':
        text = 'Для фіксації витрати, вкажіть суму у форматі 0.00 (напр. 12590.00).\nТа відправте її.'
        await state.update_data(action_uah='Витрата')

    await bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id,
                                reply_markup=listKeyboard.inl_canceled_menu.as_markup())


@accounting_router.message(Accounting.value)
async def set_value(message: Message, state: FSMContext):
    await state.update_data(value=message.text)
    await state.set_state(Accounting.annotation)

    await message.answer(f'Сума {message.text} - зафіксована.\nДодайте опис напр. "Купив хліб" або '
                         f'"Знайшов по дорозі"',
                         reply_markup=listKeyboard.canceled_menu.as_markup(
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ))


@accounting_router.message(Accounting.annotation)
async def set_annotation(message: Message, state: FSMContext):
    await state.update_data(annotation=message.text)
    await state.set_state(Accounting.validate)
    data = await state.get_data()

    await message.answer(f'Наданий коментар був зафіксований.\nПеревірте коректність введених даних:\n'
                         f'Тип: {data.get("action_uah")}\n'
                         f'Сума: {data.get("value")}\n'
                         f'Нотаток: {data.get("annotation")}',
                         reply_markup=listKeyboard.approved_menu.as_markup())


@accounting_router.callback_query(Accounting.validate)
async def finalize_accounting(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await state.set_state(Accounting.action)

    if callback.data == listComm.CONFIRM_ACTION:
        await acc_db.create_accounting(data.get('value'), data.get('action'),
                                       callback.from_user, data.get('annotation'))
        text = 'Я зафіксував операцію та повернув вас до початкового етапу.'
    else:
        text = 'Я очистив вказані дані та повернув вас до початкового етапу.'

    await bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id,
                                reply_markup=listKeyboard.accounting_menu.as_markup())


