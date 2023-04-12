from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from ..keyboards.inline import main_menu
from ..keyboards.inline import user_info


async def user_start(message: Message):
    await message.answer("Hello, user!", reply_markup=main_menu())


async def get_user_info(callback: CallbackQuery):
    current_func = callback.data.split(':')[1]
    if current_func == 'user_info_menu':
        await callback.message.edit_text("Здесь можно получить информацию о своём профиле", reply_markup=user_info())
    if current_func == 'get_id':
        await callback.message.edit_text(f"Твой id: <code>{callback.from_user.id}</code>",
                                         parse_mode="html",
                                         reply_markup=user_info())
    if current_func == 'get_username':
        await callback.message.edit_text(f"Твой id: <code>@{callback.from_user.username}</code>",
                                         parse_mode="html",
                                         reply_markup=user_info())


async def get_back(callback: CallbackQuery):
    current_func = callback.data.split(':')[1]
    if current_func == 'main_menu':
        await callback.message.edit_text("Ты вернулся в главное меню", reply_markup=main_menu())


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(get_user_info, Text(startswith='user_info:'))
    dp.register_callback_query_handler(get_back, Text(startswith='back:'))
