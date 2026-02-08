import logging
from typing import Type

from bot.settings import BotSettings
from localization.enums import AvailableLocalizations, RuLocalization, BaseLocalization, EnLocalization

logger = logging.getLogger(__name__)


settings = BotSettings()


class Localization:
    _available_localizations = {
        AvailableLocalizations.RU.value: RuLocalization,
        AvailableLocalizations.EN.value: EnLocalization,
    }
    _localization_enum: Type[BaseLocalization] = None

    @classmethod
    def init_localization(cls, language: str) -> Type[BaseLocalization]:
        if language not in cls._available_localizations:
            cls._localization_enum = EnLocalization

            logger.warning(
                f"Language '{language}' is not available. Available languages: {cls._available_localizations.keys()}."
                f" Default language '{cls._localization_enum.__name__}' will be used."
            )
        else:
            cls._localization_enum = cls._available_localizations[language]
        return cls._localization_enum

    @classmethod
    def get_localization_enum(cls, language: str = settings.bot_language) -> Type[BaseLocalization]:
        if cls._localization_enum is None:
            cls.init_localization(language)
        return cls._localization_enum
