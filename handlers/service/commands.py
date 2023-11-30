from app import bot, db

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards import replyKeyboard
from constans import inlineComm

from aiogram.fsm.context import FSMContext
from models.states import General

from models.database.userDB import UserDB

commands_router = Router()
user_db = UserDB(db)


@commands_router.message(Command('start'))
async def start_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(General.menu)
    await user_db.exists_user(message.from_user, message.chat)
    await message.answer(f"Вітаю, <b>{message.from_user.full_name}</b>!"
                         f"\nРадий познайомитися, я бот \"Домашній помічник\"."
                         f"\nБуду радий допомогти.",
                         reply_markup=replyKeyboard.general_menu.as_markup(
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ))


@commands_router.message(Command('menu'))
async def menu_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(General.menu)
    await user_db.exists_user(message.from_user, message.chat)
    await message.answer(f"Ви в головному меню.",
                         reply_markup=replyKeyboard.general_menu.as_markup(
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ))


@commands_router.callback_query(F.data == inlineComm.INL_BACK_ACTION)
async def back_menu(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(General.menu)
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await bot.send_message(callback.message.chat.id,
                           f"Ви в головному меню.",
                           reply_markup=replyKeyboard.general_menu.as_markup(
                               resize_keyboard=True,
                               one_time_keyboard=True
                           ))

