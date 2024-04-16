from aiogram.dispatcher.filters.state import StatesGroup, State


class Load_acc(StatesGroup):
    login = State()
    password = State()
    game = State()