from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from data.message_texts import HELP_MESSAGE

router = Router()


@router.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer(HELP_MESSAGE)
