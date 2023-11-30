from .fireBase import FireDB

from aiogram.types import User, Chat

from datetime import datetime, timezone


class UserDB:
    def __init__(self, fireDB: FireDB):
        self.collection = 'users'
        self.tz = timezone.utc
        self.db: FireDB = fireDB

    async def exists_user(self, user: User, chat: Chat = None):
        user_in_db = await self.db.get_document(self.collection, str(user.id))
        if not user_in_db:
            await self.create_user(user, chat)
        else:
            await self.update_user(user)

    async def create_user(self, user: User, chat: Chat = None):
        create_data = {
            'chat_id': chat.id,
            'username': user.username,
            'first_name': user.first_name,
            'created': datetime.now(self.tz),
            'last_action': datetime.now(self.tz)
        }

        await self.db.add_document(self.collection, document=str(user.id), objects=create_data)

    async def update_user(self, user: User):
        update_data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_action': datetime.now(self.tz)
        }

        await self.db.update_document(self.collection, document=str(user.id), objects=update_data)

    async def delete_user(self, user: User):
        await self.db.delete_document(self.collection, document=str(user.id))
