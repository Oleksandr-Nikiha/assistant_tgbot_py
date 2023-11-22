from aiogram.types import User, Chat

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore_async

from datetime import datetime, timezone


class FireDB:
    def __init__(self, path_to_cert: str):
        self.cred = credentials.Certificate(path_to_cert)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore_async.client()
        self.tz = timezone.utc

    async def __add_document(self, collection: str, objects: dict, document: str = None, ):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.set(objects)

    async def __update_document(self, collection: str, objects: dict, document: str = None):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.update(objects)

    async def __read_document(self, collection: str, document: str = None) -> dict:
        doc_ref = self.db.collection(collection).document(document)

        doc = await doc_ref.get()
        if doc.exists:
            return doc.to_dict()

    async def __del_document(self, collection: str, document: str):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.delete()

    async def exists_user(self, user: User, chat: Chat = None):
        user_in_db = await self.__read_document('users', str(user.id))
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

        await self.__add_document('users', document=str(user.id), objects=create_data)

    async def update_user(self, user: User):
        update_data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_action': datetime.now(self.tz)
        }

        await self.__update_document('users', document=str(user.id), objects=update_data)

    async def delete_user(self, user: User):
        await self.__del_document('users', document=str(user.id))