from aiogram import executor
from loguru import logger

from src.bot import setup
from src.database.orm import start_mapping

"""Entry point"""


def main():
    dispatcher = setup.initial_bot()
    start_mapping()
    logger.info('Bot started!')
    executor.start_polling(dispatcher, skip_updates=True)


if __name__ == '__main__':
    main()
