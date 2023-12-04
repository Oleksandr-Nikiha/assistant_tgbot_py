from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCursor
from pymongo.server_api import ServerApi


class MongoDB:
    def __init__(self, username: str, password: str, url: str):
        self.uri = f'mongodb+srv://{username}:{password}@{url}/?retryWrites=true&w=majority'
        self.client = AsyncIOMotorClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client.telegram

    @staticmethod
    async def insert_document(collection, objects: dict):
        await collection.insert_one(objects)

    @staticmethod
    async def update_document(collection,  search: dict, objects: dict):
        await collection.update_one(search, {"$set": objects})

    @staticmethod
    async def get_document(collection, search: dict):
        document = await collection.find_one(search)
        return document

    @staticmethod
    async def find_document(collection, search: dict, sort: str = None) -> AsyncIOMotorCursor:
        if sort:
            documents = collection.find(search).sort(sort)
        else:
            documents = collection.find(search)

        return documents

    @staticmethod
    async def delete_document(collection, search: dict):
        await collection.delete_one(search)
