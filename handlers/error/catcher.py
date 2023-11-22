import logging

from app import bot

from aiogram import Router
from aiogram.types import Message, InlineQuery, ErrorEvent

error_router = Router()


@error_router.message()
async def echo_message(message: Message):
    print(message)


@error_router.callback_query()
async def echo_inline(inline_query: InlineQuery):
    print(inline_query)


@error_router.errors()
async def handle_invalid_exceptions(event: ErrorEvent) -> None:
    if 'message is not modified' in str(event.exception):
        logging.error("Error `Invalid` caught: %r while processing %r", event.exception, event.update)
        await bot.answer_callback_query(event.update.callback_query.id,
                                        "Перепрошую, але я не розумію що вам треба."
                                        "\nЯкщо ця помилка виникла в неочікуваному місці, повідомте розробника."
                                        "\nРозробник @LuckerDie",
                                        True)
    else:
        logging.error("Error `Invalid` caught: %r while processing %r", event.exception, event.update)
