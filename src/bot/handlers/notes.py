from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData
from loguru import logger


from src.bot.keybords import notes as notes_kb
from src.bot.events import notes as notes_events
from src.bot import bot
from src.service import formatters
from src.domain import models
from src.service import uow as _uow


select_cat_data_add = CallbackData('scdadd', 'category_id')
select_cat_data_get = CallbackData('scdget', 'category_id')
note_data = CallbackData('nd', 'note_id')


async def notes(message: types.Message):
    await message.answer('Choose your action:', reply_markup=notes_kb.get_action())


async def enter_category_name(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Enter category name')
    await notes_events.AddCategory.name.set()


async def add_category(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    data['user_id'] = message.from_user.id
    uow = _uow.DatabaseService()
    with uow:
        note_category = models.NoteCategory(**data)
        uow.item.add(note_category)
        uow.commit()
    await state.finish()
    await message.answer('Category was successfully added')


async def select_category_for_add(callback_query: types.CallbackQuery):
    uow = _uow.DatabaseService()
    with uow:
        categories = uow.item.get_list(models.NoteCategory, callback_query.from_user.id)
    await callback_query.message.answer(
        'Select category for note:',  reply_markup=notes_kb.select_category(categories, _filter=select_cat_data_add)
    )
    await notes_events.AddNote.category.set()


async def get_title(callback_query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    category_id = callback_data.get('category_id')
    await state.update_data(category_id=category_id)
    await callback_query.message.answer('Enter note title:')
    await notes_events.AddNote.next()


async def get_description(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer('Enter note description')
    await notes_events.AddNote.next()


async def add_note(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    data['user_id'] = message.from_user.id
    uow = _uow.DatabaseService()
    with uow:
        note = models.Note(**data)
        uow.item.add(note)
        uow.commit()
    await state.finish()
    await message.answer('Note has successfully added')


async def select_category_for_get(callback_query: types.CallbackQuery):
    uow = _uow.DatabaseService()
    with uow:
        categories = uow.item.get_list(models.NoteCategory, callback_query.from_user.id)
    await callback_query.message.answer(
        'Select category', reply_markup=notes_kb.select_category(categories, _filter=select_cat_data_get)
    )
    await notes_events.GetNotes.category.set()


async def get_notes(callback_query: types.CallbackQuery, state: FSMContext, callback_data: dict):

    category_id = callback_data.get('category_id')
    user_id = callback_query.from_user.id
    uow = _uow.DatabaseService()
    with uow:
        logger.info(f'Notes from category {category_id}, user id {user_id}')
        notes = uow.item.get_notes(user_id, category_id)
        logger.info(f'Notes: {notes}')
    await callback_query.message.answer(
        'Your notes:', reply_markup=notes_kb.notes_list(notes, _filter=note_data)
    )
    await notes_events.GetNotes.next()


async def get_note_info(callback_query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    note_id = callback_data.get('note_id')
    uow = _uow.DatabaseService()
    with uow:
        note = uow.item.get(models.Note, note_id)
    formatter = formatters.NoteFormatter()
    await callback_query.message.answer(formatter.format(note))
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(notes, commands='notes')

    dp.register_callback_query_handler(
        enter_category_name, lambda call: call.data == 'add category'
    )
    dp.register_message_handler(add_category, state=notes_events.AddCategory.name)

    dp.register_callback_query_handler(
        select_category_for_add, lambda call: call.data == 'add note',
    )
    dp.register_callback_query_handler(
        get_title, select_cat_data_add.filter(), state=notes_events.AddNote.category
    )
    dp.register_message_handler(get_description, state=notes_events.AddNote.title)
    dp.register_message_handler(add_note, state=notes_events.AddNote.description)

    dp.register_callback_query_handler(
        select_category_for_get, lambda call: call.data == 'get notes',
    )
    dp.register_callback_query_handler(
        get_notes, select_cat_data_get.filter(), state=notes_events.GetNotes.category
    )
    dp.register_callback_query_handler(
        get_note_info, note_data.filter(), state=notes_events.GetNotes.task_info
    )
