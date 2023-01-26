from aiogram import Dispatcher

from . import commands, sync


def setup(dp: Dispatcher):
    dp.include_router(commands.router)
    dp.include_router(sync.router)
