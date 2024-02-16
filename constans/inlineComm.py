# Global command && action
INL_BACK_COMMAND: str = 'До головного меню \U0001f519'
INL_BACK_ACTION: str = 'back'

CANCELED_ACTION = 'Cancel'
BEHIND_ACTION = 'Behind'

CANCELED_MENU = {
    'Скасувати \u2B55': CANCELED_ACTION
}

BEHIND_MENU = {
    'Повернутися \u21A9\uFE0F': BEHIND_ACTION
}


#                  Currency menu buttons                 #
CURRENT_CURR = 'current_currency'
CURRENT_SWAP = 'current_swap'

CURRENCY_MENU = {
    'Поточний курс \u2139\uFE0F': CURRENT_CURR,
    'Обмін валюти \U0001f504': CURRENT_SWAP
}

BUY_ACTION = 'buy_curr'
SELL_ACTION = 'sell_curr'

SWAP_MENU = {
    "Купити Валюту \U0001f53c": BUY_ACTION,
    "Продати Валюту \U0001f53d": SELL_ACTION
}

USD_ACTION = 'USD'
EUR_ACTION = 'EUR'
PLN_ACTION = 'PLN'
GBP_ACTION = 'GBP'
CHF_ACTION = 'CHF'
JPY_ACTION = 'JPY'

CURRENCY_TYPE = {
    'USD \U0001f1fa\U0001f1f8': USD_ACTION,
    'EUR \U0001f1ea\U0001f1fa': EUR_ACTION,
    'PLN \U0001f1f5\U0001f1f1': PLN_ACTION,
    'GBP \U0001f1ec\U0001f1e7': GBP_ACTION,
    'CHF \U0001f1e8\U0001f1ed': CHF_ACTION,
    'JPY \U0001f1ef\U0001f1f5': JPY_ACTION
}


#                    Weather menu buttons             #
KYIV_ACTION = 'Kyiv'
VYSH_ACTION = 'Vyshhorod'
TETV_ACTION = 'Tetiyiv'
BT_ACTION = 'Bila%20Tserkva'

WEATHER_MENU = {
    "Київ": KYIV_ACTION,
    "Вишгород": VYSH_ACTION,
    "Тетіїв": TETV_ACTION,
    "Біла церква": BT_ACTION
}


#                       Accounting menu buttons                  #
INCOME_ACTION = 'Income'
COST_ACTION = 'Cost'
STATS_ACTION = 'Stats'
ALL_ACTION = 'All'
CONFIRM_ACTION = 'Confirm'
REJECT_ACTION = 'Reject'

DAY_ACTION = 'Day'
WEEK_ACTION = 'Week'
MONTH_ACTION = 'Month'
YEAR_ACTION = 'Year'

ACCOUNTING_MENU = {
    'Дохід \u2B06\uFE0F': INCOME_ACTION,
    'Витрата \u2B07\uFE0F': COST_ACTION,
    'Статистика \U0001f4ca': STATS_ACTION
}

APPROVED_MENU = {
    'Підтвердити \u2705': CONFIRM_ACTION,
    'Відхилити \u274E': REJECT_ACTION
}

STATISTICS_TYPE = {
    'Дохід \u2B06\uFE0F': INCOME_ACTION,
    'Витрата \u2B07\uFE0F': COST_ACTION,
    'Всі \u2195\uFE0F': ALL_ACTION
}

STATISTICS_PERIOD = {
    'Поточний день ': DAY_ACTION,
    'Поточний тиждень ': WEEK_ACTION,
    'Поточний місяць': MONTH_ACTION,
    'Поточний рік ': YEAR_ACTION,
}
