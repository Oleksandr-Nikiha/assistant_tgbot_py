from typing import AsyncGenerator

from aiogram.types import User, Chat

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore_async
from google.cloud.firestore_v1 import DocumentSnapshot
from google.cloud.firestore_v1.base_query import FieldFilter

from datetime import datetime, timezone


class FireDB:
    def __init__(self, path_to_cert: str):
        self.cred = credentials.Certificate(path_to_cert)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore_async.client()

    async def add_document(self, collection: str, objects: dict, document: str = None, ):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.set(objects)

    async def update_document(self, collection: str, objects: dict, document: str = None):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.update(objects)

    async def read_document(self, collection: str, document: str = None) -> dict:
        doc_ref = self.db.collection(collection).document(document)

        doc = await doc_ref.get()
        if doc.exists:
            return doc.to_dict()

    async def latest_document(self, collection: str, filters: FieldFilter, orderBy: str) \
            -> AsyncGenerator[DocumentSnapshot, None]:
        col_list = self.db.collection(collection)

        docs = (
            col_list.where(filter=filters)
            .order_by(orderBy)
            .limit(1)
        )

        return docs.stream()

    async def del_document(self, collection: str, document: str):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.delete()


class UserDB:
    def __init__(self, fireDB: FireDB):
        self.collection = 'users'
        self.tz = timezone.utc
        self.db: FireDB = fireDB

    async def exists_user(self, user: User, chat: Chat = None):
        user_in_db = await self.db.read_document(self.collection, str(user.id))
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
        await self.db.del_document(self.collection, document=str(user.id))


class AccountingDB:
    def __init__(self, fireDB: FireDB):
        self.collection = 'accounting'
        self.tz = timezone.utc
        self.db = fireDB

    async def create_accounting(self, value: str, types: str, user: User, annotation: str):
        objects = {
            'created': datetime.now(self.tz),
            'type': types,
            'user': user.id,
            'value': float(value),
            'annotation': annotation
        }

        await self.db.add_document(self.collection, objects=objects)

    async def delete_accounting(self, user: User):
        document = None

        filters = FieldFilter("user", "=", user.id)
        docs = await self.db.latest_document(self.collection, filters, 'created')

        async for doc in docs:
            document = doc

        await self.db.del_document(self.collection, document.id)
