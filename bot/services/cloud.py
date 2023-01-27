from data.dotenv_reader import dotenv_config
from loguru import logger
from nextcloud import NextCloud


def upload_to_cloud(file_path):
    with NextCloud(
        endpoint=dotenv_config.nextcloud_url,
        user=dotenv_config.nextcloud_username,
        password=dotenv_config.nextcloud_password.get_secret_value(),
        session_kwargs={"verify": True},
    ) as nxc:
        nxc.upload_file(
            file_path, dotenv_config.nextcloud_folder + file_path.split("/")[-1]
        )
    logger.info(f"Nextcloud - Uploaded media from {file_path}")
