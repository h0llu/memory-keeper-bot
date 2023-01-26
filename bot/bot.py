import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.strategy import FSMStrategy
from aiogram.types import Message
from data import config
from loguru import logger


def init():
    from utils.misc import logging

    logging.setup()


def dispatcher_setup(dp: Dispatcher):
    import filters
    import handlers
    import middlewares

    middlewares.setup(dp)
    filters.setup(dp)
    handlers.setup(dp)
    logger.success("Successfully set up dispatcher")


async def main():
    bot = Bot(config.BOT_TOKEN, parse_mode="HTML")
    # storage = RedisStorage(**config.redis)
    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.CHAT)

    init()
    dispatcher_setup(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
