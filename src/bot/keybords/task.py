from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.callback_data import CallbackData


def get_action() -> InlineKeyboardMarkup:
    add_button = InlineKeyboardButton(text='Add Task', callback_data='add task')
    get_button = InlineKeyboardMarkup(text='Get tasks', callback_data='get tasks')
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


task_cb_data = CallbackData('tcd', 'task_id')
task_done_cb_data = CallbackData('dcb', 'task_id')


def get_inline_for_tasks(tasks) -> InlineKeyboardMarkup:
    buttons = list()
    for index, task in enumerate(tasks):
        text = f'{index + 1}) {task.start_date}, {task.title}'
        buttons.append(
            InlineKeyboardButton(
                text=text, callback_data=task_cb_data.new(task_id=task.id)
            )
        )
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for button in buttons:
        keyboard.add(button)
    return keyboard


def inline_done_for_task(task_id):
    done_button = InlineKeyboardButton(
        text='Press to done task', callback_data=task_done_cb_data.new(task_id=task_id)
    )
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(done_button)
    return keyboard
