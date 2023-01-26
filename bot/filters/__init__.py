from aiogram import Dispatcher

from .chat_type import ChatTypeFilter


def setup(dp: Dispatcher):
    dp.message.filter(ChatTypeFilter(is_group=True))
