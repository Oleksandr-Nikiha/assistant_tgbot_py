from typing import AsyncGenerator, AsyncIterator


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore_async
from google.cloud.firestore_v1 import DocumentSnapshot
from google.cloud.firestore_v1.base_query import FieldFilter


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

    async def get_document(self, collection: str, document: str = None) -> dict:
        doc_ref = self.db.collection(collection).document(document)

        doc = await doc_ref.get()
        if doc.exists:
            return doc.to_dict()

    async def get_documents(self, collection) -> AsyncIterator[DocumentSnapshot] | None:
        col_list = self.db.collection(collection)

        return col_list.stream()

    async def get_documents_by_filters(self, collection, filters: list[FieldFilter]) \
            -> AsyncIterator[DocumentSnapshot] | None:
        col_list = self.db.collection(collection)

        for filtering in filters:
            col_list.where(filter=filtering)

        return col_list.stream()

    async def get_latest_document_by_filter(self, collection: str, filters: FieldFilter, orderBy: str) \
            -> AsyncGenerator[DocumentSnapshot, None] | None:
        col_list = self.db.collection(collection)

        docs = (
            col_list.where(filter=filters)
            .order_by(orderBy)
            .limit(1)
        )

        return docs.stream()

    async def get_latest_document(self, collection: str, orderBy: str) -> AsyncGenerator[DocumentSnapshot, None] | None:
        col_list = self.db.collection(collection)

        docs = (
            col_list.order_by(orderBy)
            .limit(1)
        )

        return docs.stream()

    async def delete_document(self, collection: str, document: str):
        doc_ref = self.db.collection(collection).document(document)

        await doc_ref.delete()
