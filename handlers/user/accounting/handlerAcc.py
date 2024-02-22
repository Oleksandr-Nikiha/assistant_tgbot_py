from app import bot, config

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import replyComm, inlineComm
from keyboards import inlineKeyboard

from aiogram.fsm.context import FSMContext
from models.states import Accounting
from models.database import user_db

accounting_router = Router()


# Global handlers for accounting
@accounting_router.message(F.text == replyComm.ACCOUNTING_COMMAND)
async def accounting_init(message: Message, state: FSMContext):
    await user_db.exists_user(message.from_user, message.chat)

    await state.clear()
    await state.set_state(Accounting.action)

    await message.answer('Ви в розділі Фінансовий облік \U0001f4d2 \nОберіть бажаний пункт.',
                         reply_markup=inlineKeyboard.accounting_menu.as_markup())


@accounting_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Accounting.type)
@accounting_router.callback_query(F.data == inlineComm.BEHIND_ACTION, Accounting.period)
@accounting_router.callback_query(F.data == inlineComm.CANCELED_ACTION, Accounting.value)
@accounting_router.callback_query(F.data == inlineComm.CANCELED_ACTION, Accounting.annotation)
async def canceled_accounting(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(Accounting.action)

    await bot.edit_message_text('Ви в розділі Фінансовий облік \U0001f4d2 \nОберіть бажаний пункт.',
                                callback.message.chat.id, callback.message.message_id,
                                reply_markup=inlineKeyboard.accounting_menu.as_markup())
