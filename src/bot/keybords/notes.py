from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_action() -> InlineKeyboardMarkup:
    add_button = InlineKeyboardButton(text='Add note', callback_data='add note')
    get_button = InlineKeyboardMarkup(text='Get notes', callback_data='get notes')
    add_category = InlineKeyboardMarkup(text='Add category', callback_data='add category')
    keyboard = InlineKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    )
    keyboard.add(add_button).add(get_button).add(add_category)
    return keyboard


def select_category(categories, _filter) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(
            text=category.name, callback_data=_filter.new(category_id=category.id)
        )
        for category in categories
    ]
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for button in buttons:
        keyboard.add(button)
    return keyboard


def notes_list(notes, _filter) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(
            text=note.title, callback_data=_filter.new(note_id=note.id)
        )
        for note in notes
    ]
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for button in buttons:
        keyboard.add(button)
    return keyboard
