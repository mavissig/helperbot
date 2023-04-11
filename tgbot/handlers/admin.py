from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def info_com(message: Message):
    await message.reply(f'{message.from_user}')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(info_com, commands=["info"], state="*", is_admin=True)
