from .mongoDB import MongoDB

from aiogram.types import User, Chat

from datetime import datetime


class UserMongoDB(MongoDB):
    def __init__(self, username: str, password: str, url: str):
        super().__init__(username, password, url)
        self.collection = self.db.users

    async def exists_user(self, user: User, chat: Chat = None):
        search = {
            "user_id": user.id
        }

        user_in_db = await self.get_document(self.collection, search)

        if not user_in_db:
            await self.create_user(user, chat)
        else:
            await self.update_user(user)

    async def admins_users(self):
        search = {
            "admin": True
        }

        users_in_db = await self.find_document(self.collection, search)
        return await users_in_db.to_list(length=100)

    async def create_user(self, user: User, chat: Chat = None):
        create_data = {
            'chat_id': chat.id,
            'username': user.username,
            'first_name': user.first_name,
            'created': datetime.now(),
            'last_action': datetime.now(),
            'admin': False
        }

        await self.insert_document(self.collection, create_data)

    async def update_user(self, user: User):
        search = {
            "user_id": user.id
        }

        update_data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_action': datetime.now()
        }

        await self.update_document(self.collection, search, update_data)

    async def delete_user(self, user: User):
        search = {
            "user_id": user.id
        }

        await self.delete_document(self.collection, search)
