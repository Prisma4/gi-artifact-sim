import logging
from typing import Type

from localization.enums import AvailableLocalizations, RuLocalization, BaseLocalization, EnLocalization

logger = logging.getLogger(__name__)


class Localization:
    _available_localizations = {
        AvailableLocalizations.RU.value: RuLocalization,
        AvailableLocalizations.EN.value: EnLocalization,
    }
    _localization_enum: Type[BaseLocalization] = BaseLocalization

    @classmethod
    def init_localization(cls, language: str) -> Type[BaseLocalization]:
        if language not in cls._available_localizations:
            localization_enum = EnLocalization

            logger.warning(
                f"Language '{language}' is not available. Available languages: {cls._available_localizations.keys()}."
                f" Default language '{localization_enum.__name__}' will be used."
            )
        else:
            localization_enum = cls._available_localizations[language]
        return localization_enum

    @classmethod
    def get_localization_enum(cls, language: str = None) -> Type[BaseLocalization]:
        if cls._localization_enum is None or language:
            cls._localization_enum = cls.init_localization(language)
        return cls._localization_enum
