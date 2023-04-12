from aiogram import Dispatcher
from aiogram.types import Message

from ..keyboards.inline import main_menu


async def admin_start(message: Message):
    await message.answer("Hello, admin!", reply_markup=main_menu())


async def info_com(message: Message):
    await message.reply(f'{message.from_user}')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(info_com, commands=["info"], state="*", is_admin=True)
