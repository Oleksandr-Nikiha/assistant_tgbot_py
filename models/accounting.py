from bson import ObjectId
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Accounting:
    _id: ObjectId
    value: float
    type: str
    created: datetime
    user: int
    annotation: str
