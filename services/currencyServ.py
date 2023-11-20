import requests
from datetime import datetime, timedelta

from models.currency import ListCurrency, Currency
from app.config import NBU_URL


def memorize(func):
    cache = {}
    stamp = {}

    def wrapper(*args):
        if args in cache:
            if datetime.now() - stamp[args] > timedelta(hours=1):
                result = func(*args)
                cache[args] = result
                stamp[args] = datetime.now()
                return result
            else:
                return cache[args]
        else:
            stamp[args] = datetime.now()
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


def fetch_currency_data():
    try:
        response = requests.get(NBU_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching currency data: {e}")
        return None


@memorize
def get_currency_rate():
    currency_data = fetch_currency_data()

    if currency_data:
        list_of_currencies = [Currency(**currency_dict) for currency_dict in currency_data]
        list_currency_instance: ListCurrency[Currency] = ListCurrency(currencies=list_of_currencies)
        return list_currency_instance

    return None


if __name__ == '__main__':
    get_currency_rate()
