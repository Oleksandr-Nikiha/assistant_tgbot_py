from app import bot, db

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards import listKeyboard
from constans import listComm

commands_router = Router()


@commands_router.message(Command('start'))
async def start_command(message: Message) -> None:
    await db.exists_user(message.from_user, message.chat)
    await message.answer(f"Вітаю, <b>{message.from_user.full_name}</b>!"
                         f"\nРадий познайомитися, я бот \"Домашній помічник\"."
                         f"\nБуду радий допомогти.",
                         reply_markup=listKeyboard.general_menu.as_markup(
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ))


@commands_router.message(Command('menu'))
async def menu_command(message: Message) -> None:
    await db.exists_user(message.from_user, message.chat)
    await message.answer(f"Ви в головному меню.",
                         reply_markup=listKeyboard.general_menu.as_markup(
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ))


@commands_router.callback_query(F.data == listComm.INL_BACK_ACTION)
async def back_menu(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await bot.send_message(callback.message.chat.id,
                           f"Ви в головному меню.",
                           reply_markup=listKeyboard.general_menu.as_markup(
                               resize_keyboard=True,
                               one_time_keyboard=True
                           ))
