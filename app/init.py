import asyncio
import logging
import sys

from app import dp, bot

from handlers.service.commands import commands_router
from handlers.user.currency import currency_router
from handlers.user.weather import weather_router
from handlers.error.catcher import error_router


async def main() -> None:
    dp.include_routers(
        commands_router,
        currency_router,
        weather_router,
        error_router
    )

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
