from aiogram.dispatcher.filters.state import StatesGroup, State


class AddTask(StatesGroup):
    course = State()
    date = State()
    time = State()
    premium = State()
