import enum
from typing import Type

from localization.enums import BaseLocalization
from localization.interface import Localization

localization_enum: Type[BaseLocalization] = Localization.get_localization_enum()


class KeyboardEnums(enum.Enum):
    ARTIFACT_LEVEL_UP = "level up"
    REROLL = "reroll"


class ReplyKeyboardEnums(enum.StrEnum):
    ARTIFACTS = localization_enum.Keyboards.ROLL_ARTIFACTS.value
    CHANGE_SET = localization_enum.Keyboards.CHANGE_ARTIFACT_SET.value
    CHANGE_TYPE = localization_enum.Keyboards.CHANGE_ARTIFACT_TYPE.value

    FORCE_MAIN_STAT = localization_enum.Keyboards.SET_FORCED_MAINSTAT.value
    FORCE_SUB_STAT = localization_enum.Keyboards.SET_FORCED_SUBSTAT.value
    FORCE_SUB_STAT_LUCK = localization_enum.Keyboards.SET_FORCED_SUBSTAT_LUCK.value


class ColorsEnums(enum.Enum):
    ARTIFACT_LEVEL = (247, 255, 255)
    SUBSTAT_ACTIVE = (74, 84, 102)
    SUBSTAT_NOT_ACTIVE = (154, 156, 159)
    MAIN_STAT_NAME = (190, 174, 165)
    MAIN_STAT_VALUE = (255, 255, 255)
    ARTIFACT_NAME = (255, 255, 255)
    ARTIFACT_TYPE_NAME = (255, 255, 255)


class ArtifactLuck(enum.Enum):
    WORST_LUCK = localization_enum.Keyboards.WORST_LUCK.value
    AVERAGE_LUCK = localization_enum.Keyboards.AVERAGE_LUCK.value
    GOOD_LUCK = localization_enum.Keyboards.GOOD_LUCK.value
    BEST_LUCK = localization_enum.Keyboards.BEST_LUCK.value


class PaginatorEnums(enum.Enum):
    ARTIFACT_SET_PREV = "prev_artifact_sets_"
    ARTIFACT_SET_NEXT = "next_artifact_sets_"

