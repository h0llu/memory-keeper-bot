import os
from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.types import Message
from data.config import TELETHON_SESSION_PATH, TG_API_HASH, TG_API_ID
from loguru import logger
from services.cloud import upload_to_cloud
from states.sync_states import Sync
from telethon import TelegramClient, functions

router = Router()
router.message.filter(
    Sync.synching,
    ~F.forward_from_chat,
)


@router.message(F.photo, F.photo[-1].file_size < 19000000)
async def download_small_photo(message: Message, bot: Bot):
    destination = (
        f"media/document_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')}.jpg"
    )
    await bot.download(
        message.photo[-1],
        destination=destination,
    )

    logger.info(f"Aiogram - Downloaded small photo to {destination}")

    upload_to_cloud(file_path=destination)

    os.remove(destination)
    logger.info(f"Aiogram - Small photo ({destination}) was removed")


@router.message(F.video, F.video.file_size < 19000000)
async def download_small_video(message: Message, bot: Bot):
    destination = (
        f"media/document_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')}.mp4"
    )
    await bot.download(
        message.video,
        destination=destination,
    )

    logger.info(f"Aiogram - Downloaded small video to {destination}")

    upload_to_cloud(file_path=destination)

    os.remove(destination)
    logger.info(f"Aiogram - Small video ({destination}) was removed")


@router.message(F.photo)
@router.message(F.video)
async def download_large_media(message: Message):
    media_path = None

    async with TelegramClient(
        TELETHON_SESSION_PATH,
        api_id=TG_API_ID,
        api_hash=TG_API_HASH,
    ) as app:
        result = await app(
            functions.messages.GetMessagesRequest(id=[message.message_id])
        )
        telethon_message = result.messages[0]
        media_path = await app.download_media(telethon_message, file="media/")

    if media_path is None:
        file_id = message.photo[-1].file_id if message.photo else message.video.file_id
        logger.error(f"Telethon - Large media (file_id={file_id}) was not downloaded")
        return

    logger.info(f"Telethon - Downloaded large media to {media_path}")

    upload_to_cloud(file_path=media_path)

    os.remove(media_path)
    logger.info(f"Telethon - Large media ({media_path}) was removed")
