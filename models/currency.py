from dataclasses import dataclass
from typing import Optional


@dataclass
class Currency:
    baseCurrency: str
    currency: str
    saleRateNB: float
    purchaseRateNB: float
    saleRate: Optional[float] = None
    purchaseRate: Optional[float] = None


@dataclass
class ListCurrency:
    currencies: list[Currency]

    def get_currency_by_code(self, currency_code: str) -> Currency:
        currency = next((c for c in self.currencies if c.currency == currency_code), None)
        return currency
