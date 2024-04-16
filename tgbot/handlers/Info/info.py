from aiogram import Dispatcher
from aiogram.types import Message

from loader import db


async def info(message: Message):
    acc_count = db.get_count_acc()
    hell_count = db.get_count_hell()
    busy_hell_count = db.get_count_busy_hell()
    await message.answer(f"📊 <b>Информация о таблице</b>\n"
                         f"---------------------------\n"
                         f"👨‍💼 <b>Всего аккаунтов:</b> {acc_count}\n"
                         f"❗️ <b>Детали:</b>\n"
                         f"    😈 Helldivers 2: {hell_count} | 🔴 Занято: {busy_hell_count}")


def register_info(dp: Dispatcher):
    dp.register_message_handler(info, text="📋 Получить информацию по Таблице")
