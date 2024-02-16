from aiogram.fsm.state import State, StatesGroup


class General(StatesGroup):
    menu = State()
    currency = State()
    weather = State()
    accounting = State()


class Currency(StatesGroup):
    menu = State()

    curr_types = State()
    curr_result = State()

    swap_types = State()
    swap_action = State()
    swap_values = State()
    swap_result = State()


class Accounting(StatesGroup):
    action = State()
    value = State()
    annotation = State()
    validate = State()
    statistics = State()
    type = State()
    period = State()
