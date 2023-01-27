from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from data.message_texts import HELP_MESSAGE
from loguru import logger
from states.sync_states import Sync

router = Router()


@router.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer(HELP_MESSAGE)


@router.message(Command(commands=["sync"]))
async def cmd_sync(message: Message, state: FSMContext):
    await state.set_state(Sync.synching)
    logger.info("Sync is on")
    await message.answer("Синхронизация включена!")


@router.message(Command(commands=["unsync"]))
async def cmd_stop_sync(message: Message, state: FSMContext):
    await state.set_state(Sync.not_synching)
    logger.info("Sync is off")
    await message.answer("Синхронизация выключена!")
