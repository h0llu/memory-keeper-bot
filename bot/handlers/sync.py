from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.types import Message
from data.dotenv_reader import dotenv_config
from loguru import logger
from services.cloud import upload_to_cloud
from telethon import TelegramClient, functions

router = Router()
router.message.filter(~F.forward_from_chat)


@router.message(F.photo, F.photo[-1].file_size < 19000000)
async def download_small_photo(message: Message, bot: Bot):
    destination = (
        f"media/document_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')}.jpg"
    )
    await bot.download(
        message.photo[-1],
        destination=destination,
    )

    logger.success(f"Downloaded small photo to {destination} with aiogram")

    upload_to_cloud(file_path=destination)


@router.message(F.video, F.video.file_size < 19000000)
async def download_small_video(message: Message, bot: Bot):
    destination = (
        f"media/document_{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')}.mp4"
    )
    await bot.download(
        message.video,
        destination=destination,
    )

    logger.success(f"Downloaded small photo to {destination} with aiogram")

    upload_to_cloud(file_path=destination)


@router.message(F.photo)
@router.message(F.video)
async def download_large_media(message: Message):
    async with TelegramClient(
        "telethon-session/bot",
        api_id=dotenv_config.api_id,
        api_hash=dotenv_config.api_hash.get_secret_value(),
    ) as app:
        result = await app(
            functions.messages.GetMessagesRequest(id=[message.message_id])
        )
        telethon_message = result.messages[0]
        media_path = await app.download_media(telethon_message, file="media/")

        logger.success(f"Downloaded large media to {media_path} with telethon")

        upload_to_cloud(file_path=media_path)
