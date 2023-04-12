from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def pattern():
    buttons = [
        [
            InlineKeyboardButton(
                text=f'pattern',
                callback_data=f"pattern_menu:pattern_func")
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard


def main_menu():
    buttons = [
        [
            InlineKeyboardButton(
                text=f'User info',
                callback_data=f"user_info:user_info_menu")
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard


def user_info():
    buttons = [
        [
            InlineKeyboardButton(
                text=f'User Id',
                callback_data=f"user_info:get_id"),

            InlineKeyboardButton(
                text=f'Username',
                callback_data=f"user_info:get_username")
        ],
        [
            InlineKeyboardButton(
                text=f'В главное меню',
                callback_data=f"back:main_menu")
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard
