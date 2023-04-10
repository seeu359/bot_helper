from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)


def get_action() -> InlineKeyboardMarkup:
    add_button = InlineKeyboardButton(text='Add Task', callback_data='add')
    get_button = InlineKeyboardMarkup(text='Get tasks', callback_data='get')
    keyboard = InlineKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    keyboard.add(add_button).add(get_button)
    return keyboard


def get_month() -> ReplyKeyboardMarkup:
    january = KeyboardButton('January')
    february = KeyboardButton('February')
    march = KeyboardButton('March')
    april = KeyboardButton('April')
    may = KeyboardButton('May')
    june = KeyboardButton('June')
    july = KeyboardButton('July')
    august = KeyboardButton('August')
    september = KeyboardButton('September')
    october = KeyboardButton('October')
    november = KeyboardButton('November')
    december = KeyboardButton('December')
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    keyboard.add(january).add(february).add(march).add(
        april).add(may).add(june).add(july).add(august).add(
        september).add(october).add(november).add(december)
    return keyboard


def get_task_period() -> ReplyKeyboardMarkup:
    today = KeyboardButton('Today tasks')
    all = KeyboardButton('All tasks')
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    keyboard.add(today).add(all)
    return keyboard
