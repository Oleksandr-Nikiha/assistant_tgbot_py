import logging
import requests

from app.config import PB_URL
from utils.memo import memorize_stamp
from models.currency import ListCurrency, Currency

from datetime import date, timedelta


def fetch_currency_data() -> dict:
    today = date.today()
    yesterday = today - timedelta(days=1)

    try:
        today_request = requests.get(PB_URL + today.strftime('%d.%m.%Y'))
        today_request.raise_for_status()
        today_response = today_request.json()
        if today_response.get('exchangeRate'):
            return {'value': today_response.get('exchangeRate')}
        else:
            yesterday_request = requests.get(PB_URL + yesterday.strftime('%d.%m.%Y'))
            yesterday_request.raise_for_status()
            yesterday_response = yesterday_request.json()

            return {'date': yesterday, 'value': yesterday_response.get('exchangeRate')}

    except requests.RequestException as e:
        logging.error(f"Error fetching currency data: {e}")
        exit()


@memorize_stamp
def get_currency_rate() -> ListCurrency | None:
    currency_dict: dict = fetch_currency_data()
    currency_date: date = currency_dict.get('date')
    currency_data: list = currency_dict.get('value')

    if currency_data:
        list_of_currencies = [Currency(**currency_dict) for currency_dict in currency_data]
        list_currency_instance: ListCurrency = ListCurrency(currencies=list_of_currencies, by_date=currency_date)
        return list_currency_instance

    return None


async def main():
    get_currency_rate()


if __name__ == '__main__':
    get_currency_rate()
