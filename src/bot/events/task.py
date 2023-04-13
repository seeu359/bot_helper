from aiogram.dispatcher.filters.state import StatesGroup, State


class AddTask(StatesGroup):
    title = State()
    description = State()
    month_day = State()
    month = State()


class GetTasks(StatesGroup):
    period = State()
    get_task = State()
