from app import bot

from app import config

from models.database.userDB import UserMongoDB
from services import userServ

user_db = UserMongoDB(config.MONGO_USER, config.MONGO_PASSWORD, config.MONGO_URL)


async def send_startup_message():
    user_data = await user_db.admins_users()
    admin_list = await userServ.parse_users(user_data)

    for admin in admin_list:
        await bot.send_message(admin.user_id, "Я прокинувся")
