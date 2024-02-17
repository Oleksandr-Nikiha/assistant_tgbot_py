import logging
import requests

from app.config import PB_URL
from utils.memo import memorize_stamp
from models.currency import ListCurrency, Currency

from datetime import date


def fetch_currency_data():
    try:
        response = requests.get(PB_URL + date.today().strftime('%d.%m.%Y'))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching currency data: {e}")
        return None


@memorize_stamp
def get_currency_rate() -> ListCurrency | None:
    currency_net_data = fetch_currency_data()
    currency_data = currency_net_data.get('exchangeRate')

    if currency_data:
        list_of_currencies = [Currency(**currency_dict) for currency_dict in currency_data]
        list_currency_instance: ListCurrency = ListCurrency(currencies=list_of_currencies)
        return list_currency_instance

    return None


async def main():
    get_currency_rate()


if __name__ == '__main__':
    get_currency_rate()
