INL_BACK_COMMAND: str = 'Назад \U0001f519'
INL_BACK_ACTION: str = 'back'

# General Menu
WEATHER_COMMAND: str = 'Погода \U0001f30d'
CURRENCY_COMMAND: str = 'Курс валют \U0001f4b1'
ACCOUNTING_COMMAND: str = 'Фінансовий облік \U0001f4d2'
DEFAULT_MENU: list[str] = [CURRENCY_COMMAND, WEATHER_COMMAND, ACCOUNTING_COMMAND]

# Currency menu buttons
CURRENCY_MENU = {
    'USD \U0001f1fa\U0001f1f8': 'USD',
    'EUR \U0001f1ea\U0001f1fa': 'EUR',
    'PLN \U0001f1f5\U0001f1f1': 'PLN',
    'GBP \U0001f1ec\U0001f1e7': 'GBP',
    'CHF \U0001f1e8\U0001f1ed': 'CHF',
    'JPY \U0001f1ef\U0001f1f5': 'JPY'
}

# Weather menu buttons
WEATHER_MENU = {
    "Київ": "Kyiv",
    "Вишгород": "Vyshhorod",
    "Тетіїв": "Tetiyiv",
    "Біла церква": "Bila%20Tserkva"
}

# Accounting menu buttons
INCOME_ACTION = 'Income'
COST_ACTION = 'Cost'
STATS_ACTION = 'Stats'

ACCOUNTING_MENU = {
    'Дохід \u2B06\uFE0F': INCOME_ACTION,
    'Витрата \u2B07\uFE0F': COST_ACTION,
    'Статистика \U0001f4ca': STATS_ACTION
}

CANCELED_COMMAND = 'Скасувати \u2B55'
CANCELED_ACTION = 'Cancel'

CONFIRM_ACTION = 'Confirm'
REJECT_ACTION = 'Reject'

APPROVED_MENU = {
    'Підтвердити \u2705': CONFIRM_ACTION,
    'Відхилити \u274E': REJECT_ACTION
}
