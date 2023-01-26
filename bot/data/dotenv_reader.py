from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    nextcloud_url: str
    nextcloud_username: str
    nextcloud_password: SecretStr
    nextcloud_folder: str
    api_id: int
    api_hash: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


dotenv_config = Settings()
