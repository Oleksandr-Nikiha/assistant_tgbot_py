from bson import ObjectId

from .mongoDB import MongoDB

from aiogram.types import User

from datetime import datetime


class AccountingDB(MongoDB):
    def __init__(self, username: str, password: str, url: str):
        super().__init__(username, password, url)
        self.collection = self.db.account

    async def create_accounting(self, value: str, types: str, user: User, annotation: str):
        objects = {
            'created': datetime.now(),
            'type': types,
            'user': user.id,
            'value': float(value.replace(',', '.')),
            'annotation': annotation
        }

        await self.insert_document(self.collection, objects)

    async def get_accounting_by_user(self, user: User):
        search = {
            "user": user.id
        }

        documents = await self.find_document(self.collection, search, "created")
        return await documents.to_list(length=100)

    async def delete_accounting_by_id(self, ids: str):
        search = {
            "_id": ObjectId(ids)
        }

        await self.delete_document(self.collection, search)