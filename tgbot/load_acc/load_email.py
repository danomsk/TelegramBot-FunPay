from aiogram.dispatcher.filters.state import StatesGroup, State


class Load_email(StatesGroup):
    login_email = State()
    password_email = State()