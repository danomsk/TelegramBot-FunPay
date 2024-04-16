from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="📥 Загрузить Аккаунты")
    ],
    [
        KeyboardButton(text="📋 Получить информацию по Таблице")
    ]
], resize_keyboard=True)
