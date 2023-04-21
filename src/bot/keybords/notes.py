from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_action() -> InlineKeyboardMarkup:
    add_button = InlineKeyboardButton(text='Add note', callback_data='add note')
    get_button = InlineKeyboardMarkup(text='Get notes', callback_data='get notes')
    keyboard = InlineKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    keyboard.add(add_button).add(get_button)
    return keyboard
