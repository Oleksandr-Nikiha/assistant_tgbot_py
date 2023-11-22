from dataclasses import dataclass


@dataclass
class Currency:
    r030: int
    txt: str
    rate: float
    cc: str
    exchangedate: str


@dataclass
class ListCurrency:
    currencies: list[Currency]

    def get_currency_by_code(self, currency_code: str) -> Currency:
        currency = next((c for c in self.currencies if c.cc == currency_code), None)
        return currency
    