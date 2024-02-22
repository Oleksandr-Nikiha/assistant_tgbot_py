from app import bot, config

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import replyComm, inlineComm
from keyboards import inlineKeyboard

from aiogram.fsm.context import FSMContext
from models.states import Currency
from models.database import user_db


currency_router = Router()


@currency_router.message(F.text == replyComm.CURRENCY_COMMAND)
async def currency_init(message: Message, state: FSMContext):
    await user_db.exists_user(message.from_user, message.chat)

    await state.clear()
    await state.set_state(Currency.menu)

    await message.answer("Ви в розділі Валют \U0001f4b1 \nОберіть бажаний пункт.",
                         reply_markup=inlineKeyboard.currency_menu.as_markup())


@currency_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Currency.curr_types)
@currency_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Currency.curr_result)
@currency_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Currency.swap_types)
async def canceled_accounting(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(Currency.menu)

    await bot.edit_message_text('Ви в розділі Валют \U0001f4b1 \nОберіть бажаний пункт.',
                                callback.message.chat.id, callback.message.message_id,
                                reply_markup=inlineKeyboard.currency_menu.as_markup())
