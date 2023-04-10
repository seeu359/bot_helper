from aiogram import Dispatcher, types


async def get_info(message: types.Message):
    await message.answer('HIIII')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_info, commands='info', state=None)
