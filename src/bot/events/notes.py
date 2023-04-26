from aiogram.dispatcher.filters.state import StatesGroup, State


class AddCategory(StatesGroup):
    name = State()


class AddNote(StatesGroup):
    category = State()
    title = State()
    description = State()


class GetNotes(StatesGroup):
    category = State()
    task_info = State()
