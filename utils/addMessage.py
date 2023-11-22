from app import bot

from app import config


async def send_startup_message():
    for admin_id in config.ADMINS:
        await bot.send_message(admin_id, "Я прокинувся")
