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

    def get_rate_by_currency_code(self, currency_code: str) -> float:
        currency = next((c for c in self.currencies if c.cc == currency_code), None)
        return currency.rate if currency else None
