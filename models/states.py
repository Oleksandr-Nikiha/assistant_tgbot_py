from aiogram.fsm.state import State, StatesGroup


class General(StatesGroup):
    menu = State()
    currency = State()
    weather = State()
    accounting = State()


class Accounting(StatesGroup):
    action = State()
    value = State()
    annotation = State()
    validate = State()
    statistics = State()
    period = State()
