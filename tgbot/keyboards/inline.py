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
        [
            InlineKeyboardButton(
                text=f'Команда',
                callback_data=f"team:team_menu")
        ],
        [
            InlineKeyboardButton(
                text=f'Задачи',
                callback_data=f"task_manager:task_manager_menu")
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


def task_manager_menu():
    buttons = [
        [
            InlineKeyboardButton(
                text=f'ВСЕ',
                callback_data=f"task_manager:all_task"),

            InlineKeyboardButton(
                text=f'ПРИНЯТЫЕ',
                callback_data=f"task_manager:current_task"),
        ],
        [
            InlineKeyboardButton(
                text=f'СОЗДАТЬ ЗАДАЧУ',
                callback_data=f"task_manager:add_task")
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


def team_menu():
    buttons = [
        [
            InlineKeyboardButton(
                text=f'Моя команда',
                callback_data=f"user_info:get_id"),

            InlineKeyboardButton(
                text=f'Добавить участника',
                callback_data=f"user_info:get_username")
        ],
        [
            InlineKeyboardButton(
                text=f'Ливнуть',
                callback_data=f"back:main_menu")
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard
