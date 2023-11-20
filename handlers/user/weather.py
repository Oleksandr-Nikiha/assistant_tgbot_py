from app import bot

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from constans import listComm
from keyboards import listKeyboard

from services.weatherServ import parsing_weather

weather_router = Router()


@weather_router.message(F.text == listComm.WEATHER_COMMAND)
async def weather_init(message: Message):
    await message.answer("Ви в розділі Погоди \U0001f30d \nОберіть місто яке вас цікавить.",
                         reply_markup=listKeyboard.weather_menu.as_markup())


@weather_router.callback_query(F.data.in_(listComm.WEATHER_CITY.values()))
async def answer_weather(callback: CallbackQuery):
    wether = parsing_weather().get_weather_by_name(callback.data)
    await bot.edit_message_text(text=f"\uD83C\uDF07 В місті {wether.getCityMappedName()} - %s \uD83C\uDF07\n"
                                     f"\uD83C\uDF21\uFE0F Температура: %sC°\n" +
            "\uD83D\uDCA7 Вологість: %s%%\n" +
            "\uD83E\uDE90 Атмосферний тиск: \n%s мм рт. ст.\n" +
            "\uD83D\uDCA8 Швидкість вітру: \n%s км/г\n" +
            "\uD83D\uDCC5 Останнє оновлення: \n%s")