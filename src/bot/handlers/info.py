from aiogram import types

from src.bot import dispatcher as dp


@dp.message_handlers(commands='info')
async def get_info(message: types.Message):
    await message.reply('Info message handler')

