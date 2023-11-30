from .fireBase import FireDB

from aiogram.types import User, Chat

from datetime import datetime, timezone

from typing import AsyncGenerator, AsyncIterator

from google.cloud.firestore_v1 import DocumentSnapshot
from google.cloud.firestore_v1.base_query import FieldFilter


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
            'value': float(value.replace(',', '.')),
            'annotation': annotation
        }

        await self.db.add_document(self.collection, objects=objects)

    async def get_accounting_by_user(self, user: User) -> AsyncIterator[DocumentSnapshot] | None:
        filters = [FieldFilter("user", "==", user.id)]

        docs = await self.db.get_documents_by_filters(self.collection, filters)
        return docs

    async def delete_accounting(self, user: User):
        document = None

        filters = FieldFilter("user", "=", user.id)
        docs = await self.db.get_latest_document_by_filter(self.collection, filters, 'created')

        async for doc in docs:
            document = doc

        await self.db.delete_document(self.collection, document.id)
