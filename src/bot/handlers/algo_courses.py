from aiogram import Dispatcher, types

from src.bot.keybords.algo_courses import get_action


async def algo_courses(message: types.Message):
    await message.answer('Choose your action:', reply_markup=get_action())


async def select_course(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Select course:')


async def select_data(callback_query: types.CallbackQuery, callback_data: dict):
    await callback_query.message.answer(str(callback_data))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(algo_courses, commands='courses')
    dp.register_callback_query_handler(select_course, lambda call: call.data == 'add course')
    dp.register_callback_query_handler(
        select_data,
        lambda call: call.data == 'python start' or call.data == 'python pro'
    )
