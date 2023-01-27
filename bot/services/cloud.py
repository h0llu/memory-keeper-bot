from data.config import (
    NEXTCLOUD_FOLDER,
    NEXTCLOUD_PASSWORD,
    NEXTCLOUD_URL,
    NEXTCLOUD_USERNAME,
)
from loguru import logger
from nextcloud import NextCloud


def upload_to_cloud(file_path):
    with NextCloud(
        endpoint=NEXTCLOUD_URL,
        user=NEXTCLOUD_USERNAME,
        password=NEXTCLOUD_PASSWORD,
        session_kwargs={"verify": True},
    ) as nxc:
        nxc.upload_file(file_path, NEXTCLOUD_FOLDER + file_path.split("/")[-1])
    logger.info(f"Nextcloud - Uploaded media from {file_path}")
