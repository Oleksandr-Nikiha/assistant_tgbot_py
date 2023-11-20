import logging
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
    """
    This handler receives error events with "Invalid" message in them.
    """
    # Because we specified `ExceptionTypeFilter` with `InvalidAge` exception type earlier,
    # this handler will receive error events with any exception type except `InvalidAge` and
    # only if the exception message contains "Invalid" substring.
    logging.error("Error `Invalid` caught: %r while processing %r", event.exception, event.update)