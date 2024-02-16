from bson import ObjectId
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    _id: ObjectId
    chat_id: int
    created: datetime
    last_action: datetime
    user_id: int
    first_name: str
    admin: bool
    username: str
