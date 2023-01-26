# import os
# import sys

from data.dotenv_reader import dotenv_config
from loguru import logger
from nextcloud import NextCloud

# # УДАЛИТЬ НИЖЕ
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# # УДАЛИТЬ ВЫШЕ


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
    logger.success(f"Uploaded media from {file_path} to NextCloud")
