import logging
from typing import Type

from bot.settings import BotSettings
from localization.localization_data import AvailableLocalizations, RuLocalization, BaseLocalization, EnLocalization

logger = logging.getLogger(__name__)


settings = BotSettings()


class Localization:
    _available_localizations = {
        AvailableLocalizations.RU.value: RuLocalization,
        AvailableLocalizations.EN.value: EnLocalization,
    }
    _localization: Type[BaseLocalization] = None

    @classmethod
    def init_localization(cls, language: str) -> Type[BaseLocalization]:
        if language not in cls._available_localizations:
            cls._localization = EnLocalization

            logger.warning(
                f"Language '{language}' is not available. Available languages: {cls._available_localizations.keys()}."
                f" Default language '{cls._localization.__name__}' will be used."
            )
        else:
            cls._localization = cls._available_localizations[language]
        return cls._localization

    @classmethod
    def get_localization(cls, language: str = settings.bot_language) -> Type[BaseLocalization]:
        if cls._localization is None:
            cls.init_localization(language)
        return cls._localization
