import os
from pathlib import Path

from .dotenv_reader import dotenv_config

LOGS_BASE_PATH = str(Path(__file__).parent.parent.parent / "logs")
BOT_TOKEN = dotenv_config.bot_token.get_secret_value()

# BOT_TOKEN = os.getenv("BOT_TOKEN")
# redis = {
#     "host": "localhost",
#     "password": "",
# }
