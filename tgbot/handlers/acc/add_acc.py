from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import db
from tgbot.load_acc import Load_acc, Load_email


async def load_account(message: Message):
    await message.answer("👤 Введи Логин от Steam")
    await Load_acc.login.set()

async def load_login(message: Message, state: FSMContext):
    login = message.text
    await state.update_data(answerLog=login)
    await message.answer("🔐 Введи Пароль от Steam")
    await Load_acc.password.set()

async def load_password(message: Message, state: FSMContext):
    password = message.text
    await state.update_data(answerPass=password)
    await message.answer("👥 Введи Логин от Почты")
    await Load_email.login_email.set()

async def load_email_login(message: Message, state: FSMContext):
    email_login = message.text
    await state.update_data(answerLogEmail=email_login)
    await message.answer("🔒 Введи Пароль от Почты")
    await Load_email.password_email.set()

async def load_email_password(message: Message, state: FSMContext):
    email_password = message.text
    data = await state.get_data()
    login_email = data.get("answerLogEmail")
    db.get_email(login_email, email_password)
    await message.answer(f"✉️ В таблицу было добавлено:\n"
                         f" Логин: {login_email}\n"
                         f"Пароль: {email_password}")
    email_id = db.email_id()
    await state.update_data(email_id=email_id)
    await message.answer("🎮 Введи Игру\n"
                         "1. Helldivers")
    await Load_acc.game.set()

async def load_game(message: Message, state: FSMContext):
    game = message.text
    data = await state.get_data()
    login = data.get("answerLog")
    password = data.get("answerPass")
    email_id = data.get("email_id")
    db.get_acc(login, password, game, email_id, False)
    await message.answer(f"💌 Ты прислал\n"
                          f"Логин: {login}\n"
                          f"Пароль: {password}\n"
                         f"😎 Email и Account заполнены!")

    await state.finish()

def register_added_account(dp: Dispatcher):
    dp.register_message_handler(load_account, text="📥 Загрузить Аккаунты")
    dp.register_message_handler(load_login, state=Load_acc.login)
    dp.register_message_handler(load_password, state=Load_acc.password)
    dp.register_message_handler(load_email_login, state=Load_email.login_email)
    dp.register_message_handler(load_email_password, state=Load_email.password_email)
    dp.register_message_handler(load_game, state=Load_acc.game)


