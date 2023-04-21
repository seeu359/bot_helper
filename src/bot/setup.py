from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from src.bot import bot
from src.bot.handlers import info, task, notes

load_dotenv()

HANDLERS_REG = [
    info.register_handlers,
    task.register_handlers,
    notes.register_handlers,
]


def initial_bot() -> Dispatcher:
    storage = MemoryStorage()
    dispatcher = Dispatcher(bot, storage=storage)
    for reg_func in HANDLERS_REG:
        reg_func(dispatcher)
    return dispatcher
