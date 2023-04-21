from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src import config


bot = Bot(token=config.TG_TOKEN)

storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
