import asyncio
import logging
import sys

from app import dp, bot

from handlers.service.commands import commands_router
from handlers.user.currency import currency_router
from handlers.user.weather import weather_router
from handlers.error.catcher import error_router

from services import currencyServ, weatherServ

from utils import addMessage


async def main() -> None:
    dp.include_routers(
        commands_router,
        currency_router,
        weather_router,
        error_router
    )

    await weatherServ.main()
    await currencyServ.main()

    # Startup message for admins
    await addMessage.send_startup_message()

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
