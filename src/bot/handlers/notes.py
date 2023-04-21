from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.bot.keybords.notes import get_action
from src.bot.events import task as task_events
from src.bot import bot
from src.service import formatters
from src.domain import bussines_rules, models
from src.service import uow as _uow


async def notes(message: types.Message):
    await message.answer('Choose your action:', reply_markup=get_action())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(notes, commands='notes')
