from aiogram import Dispatcher, types

from src.bot.keybords.algo_courses import get_action, get_course, python_course_cb_data


async def algo_courses(message: types.Message):
    await message.answer('Choose your action:', reply_markup=get_action())


async def select_course(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Select course:', reply_markup=get_course())


async def select_data(callback_query: types.CallbackQuery, callback_data: dict):
    data = callback_data.get('course')
    await callback_query.message.answer(data)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(algo_courses, commands='courses')
    dp.register_callback_query_handler(select_course, lambda call: call.data == 'add course')
    dp.register_callback_query_handler(select_data, python_course_cb_data.filter())
