from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


def get_action() -> InlineKeyboardMarkup:
    add_button = InlineKeyboardButton(text='Add course', callback_data='add course')
    get_button = InlineKeyboardButton(text='Get course', callback_data='get course')
    get_statistics = InlineKeyboardButton(text='Get Statistics', callback_data='get statistics')

    keyboard = InlineKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    keyboard.add(add_button).add(get_button).add(get_statistics)
    return keyboard


python_course_cb_data = CallbackData('pccd', 'course')
python_premium_cb_data = CallbackData('ppcd', 'premium')


def get_course() -> InlineKeyboardMarkup:
    buttons = ['Python Start', 'Python Pro']
    keyboard = InlineKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    for button in [
        InlineKeyboardButton(text=button, callback_data=python_course_cb_data.new(course=button.lower()))
        for button in buttons
    ]:
        keyboard.add(button)
    return keyboard


def get_premium() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    true = InlineKeyboardButton(
        text='Yes', callback_data=python_premium_cb_data.new(premium=True)
    )
    false = InlineKeyboardButton(
        text='No', callback_data=python_premium_cb_data.new(premium=False)
    )
    keyboard.add(true).add(false)
    return keyboard
