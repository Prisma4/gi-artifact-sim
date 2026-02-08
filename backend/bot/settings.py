from pydantic_settings import BaseSettings, SettingsConfigDict

from localization.localization_data import AvailableLocalizations


class BotSettings(BaseSettings):
    bot_token: str
    static_folder: str = "static"
    bot_language: str = AvailableLocalizations.EN.value
