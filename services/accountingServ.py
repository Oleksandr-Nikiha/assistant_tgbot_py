from constans import parseDict
from datetime import datetime, timedelta
from models.accounting import Accounting


async def parse_statistics(data, time_delta: str):
    list_of_accounting = [Accounting(**accounting_dict) for accounting_dict in data]

    setup = False
    message = ''
    cost_val = 0
    income_val = 0

    match time_delta:
        case 'Day':
            message += 'Статистика за день:\n'
            date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        case 'Week':
            message += 'Статистика за тиждень:\n'
            date = (datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
                    - timedelta(days=datetime.today().weekday() % 7))

        case 'Month':
            message += 'Статистика за місяць:\n'
            date = datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        case _:
            message += 'Статистика за рік:\n'
            date = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    for account in list_of_accounting:
        acc_created = datetime.fromtimestamp(account.created.timestamp())
        if acc_created >= date:
            setup = True
            message += (f'{acc_created.strftime("%d.%m.%Y %H:%M")} - {parseDict.ACCOUNT_TYPE.get(account.type)} '
                        f'на суму {account.value} грн.\n')

            cost_val += account.value if account.type == 'Cost' else 0
            income_val += account.value if account.type == 'Income' else 0

    if cost_val != 0 or income_val != 0:
        message += f"\nЗагальна сума надходжень: {income_val} грн.\nЗагальна сума витрат: {cost_val} грн."

    if not setup:
        message += 'Відсутня'

    return message
