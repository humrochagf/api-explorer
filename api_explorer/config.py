from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: HttpUrl = HttpUrl("https://api.thecatapi.com/v1")
    auth_token: str = ""

    model_config = SettingsConfigDict(
        env_prefix="api_explorer_", env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()
