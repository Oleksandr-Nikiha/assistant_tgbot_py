from dataclasses import dataclass
from google.api_core.datetime_helpers import DatetimeWithNanoseconds


@dataclass
class Accounting:
    value: float
    type: str
    created: DatetimeWithNanoseconds
    user: int
    annotation: str
