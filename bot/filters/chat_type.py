from aiogram.filters import Filter
from aiogram.types import Message


class ChatTypeFilter(Filter):
    def __init__(self, is_group: bool) -> None:
        self.is_group = is_group

    async def __call__(self, message: Message) -> bool:
        if self.is_group:
            return message.chat.type in ["group", "supergroup"]
        return message.chat.type == "private"
