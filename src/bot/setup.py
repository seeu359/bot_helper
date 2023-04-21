from aiogram import Dispatcher
from dotenv import load_dotenv

from src.bot import dispatcher
from src.bot.handlers import task, notes

load_dotenv()

HANDLERS_REG = [
    task.register_handlers,
    notes.register_handlers,
]


def initial_bot(dp=dispatcher) -> Dispatcher:
    for reg_func in HANDLERS_REG:
        reg_func(dp)
    return dispatcher
