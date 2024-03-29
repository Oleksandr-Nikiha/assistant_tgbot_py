from app import bot

from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from constans import inlineComm
from services import accountingServ
from keyboards import inlineKeyboard
from models.states import Accounting
from models.database import acc_db


statisticsAcc_router = Router()


# Statistics accounting handlers
@statisticsAcc_router.callback_query(F.data.in_(inlineComm.STATS_ACTION), Accounting.action)
async def set_type(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Accounting.period)

    await bot.edit_message_text('Оберіть період за який ви хочете отримати інформацію.',
                                callback.message.chat.id, callback.message.message_id,
                                reply_markup=inlineKeyboard.statistics_period.as_markup())


@statisticsAcc_router.callback_query(F.data.in_(inlineComm.STATISTICS_PERIOD.values()), Accounting.period)
async def get_statistics(callback: CallbackQuery):
    acc_data = await acc_db.get_accounting_by_user(callback.from_user)
    message = await accountingServ.parse_statistics(acc_data, callback.data)

    await bot.edit_message_text(message, callback.message.chat.id, callback.message.message_id,
                                reply_markup=inlineKeyboard.statistics_period.as_markup())
