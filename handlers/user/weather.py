from app import bot

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import replyComm
from keyboards import inlineKeyboard

from services.weatherServ import parsing_weather

from aiogram.fsm.context import FSMContext
from models.states import General

weather_router = Router()


@weather_router.message(F.text == replyComm.WEATHER_COMMAND)
async def weather_init(message: Message, state: FSMContext):
    await state.set_state(General.weather)
    await message.answer("Ви в розділі Погоди \U0001f30d \nОберіть місто яке вас цікавить.",
                         reply_markup=inlineKeyboard.weather_menu.as_markup())


@weather_router.callback_query(General.weather)
async def answer_weather(callback: CallbackQuery):
    weather = parsing_weather().get_weather_by_name(callback.data)
    await bot.edit_message_text(text=f"\U0001f307 В місті {weather.city_data_name} - {weather.weather_type} \U0001f307"
                                     f"\n\U0001f321\uFE0F Температура: {weather.temperature}C°"
                                     f"\n\U0001f4a7 Вологість: {weather.relative_humidity}%%"
                                     f"\n\U0001fa90 Атмосферний тиск: \n{weather.pressure} мм рт. ст."
                                     f"\n\U0001f4a8 Швидкість вітру: \n{weather.wind_speed} км/г"
                                     f"\n\U0001f4c5 Останнє оновлення: \n{weather.last_update_date}",
                                message_id=callback.message.message_id,
                                chat_id=callback.message.chat.id,
                                reply_markup=inlineKeyboard.weather_menu.as_markup())
