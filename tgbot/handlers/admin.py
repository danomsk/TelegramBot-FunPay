import os.path

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.menu_keyboard import menu

async def admin_start(message: Message):
    await message.answer("Привет, Админ\n"
                         "Выберите действие" ,reply_markup=menu)

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
