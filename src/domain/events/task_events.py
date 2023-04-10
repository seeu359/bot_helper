from aiogram.dispatcher.filters.state import State, StatesGroup


class AddTask(StatesGroup):
    title = State()
    description = State()
    month_day = State()
    month = State()


class GetTasks(StatesGroup):
    period = State()
