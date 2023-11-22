INL_BACK_COMMAND: str = 'Назад \U0001f519'
INL_BACK_ACTION: str = 'back'

WEATHER_COMMAND: str = 'Погода \U0001f30d'
CURRENCY_COMMAND: str = 'Курс валют \U0001f4b1'
OTHER_MENU_COMMAND: str = 'Інше \U0001f5ff'
# FINANCIAL_COMMAND: str = 'Фінансовий облік \u270D\uFE0F'
DEFAULT_MENU: list[str] = [CURRENCY_COMMAND, WEATHER_COMMAND, OTHER_MENU_COMMAND]

CURRENCY_DATA = {
    'USD \U0001f1fa\U0001f1f8': 'USD',
    'EUR \U0001f1ea\U0001f1fa': 'EUR',
    'PLN \U0001f1f5\U0001f1f1': 'PLN',
    'GBP \U0001f1ec\U0001f1e7': 'GBP',
    'CHF \U0001f1e8\U0001f1ed': 'CHF',
    'JPY \U0001f1ef\U0001f1f5': 'JPY'
}

WEATHER_CITY = {
    "Київ": "Kyiv",
    "Вишгород": "Vyshhorod",
    "Тетіїв": "Tetiyiv",
    "Біла церква": "Bila%20Tserkva"
}

TIP_COMMAND = 'random_tip'

OTHER_MENU = {
    'Випадкова порада \U0001f596': TIP_COMMAND
}
