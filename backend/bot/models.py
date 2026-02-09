import enum
from typing import Type

from localization.localization_data import BaseLocalization
from localization.interface import Localization

localization: Type[BaseLocalization] = Localization.get_localization()


class KeyboardEnums(enum.Enum):
    ARTIFACT_LEVEL_UP = "level up"
    REROLL = "reroll"
    SHOW_PROC_HISTORY = "proc history"


class ReplyKeyboardEnums(enum.Enum):
    ARTIFACTS = localization.Keyboards.ROLL_ARTIFACTS
    CHANGE_SET = localization.Keyboards.CHANGE_ARTIFACT_SET
    CHANGE_TYPE = localization.Keyboards.CHANGE_ARTIFACT_TYPE

    FORCE_MAIN_STAT = localization.Keyboards.SET_FORCED_MAINSTAT
    FORCE_SUB_STAT = localization.Keyboards.SET_FORCED_SUBSTAT
    FORCE_SUB_STAT_LUCK = localization.Keyboards.SET_FORCED_SUBSTAT_LUCK


class ColorsEnums(enum.Enum):
    ARTIFACT_LEVEL = (247, 255, 255)
    SUBSTAT_ACTIVE = (74, 84, 102)
    SUBSTAT_NOT_ACTIVE = (154, 156, 159)
    MAIN_STAT_NAME = (190, 174, 165)
    MAIN_STAT_VALUE = (255, 255, 255)
    ARTIFACT_NAME = (255, 255, 255)
    ARTIFACT_TYPE_NAME = (255, 255, 255)


class ArtifactLuck(enum.Enum):
    WORST_LUCK = localization.Keyboards.WORST_LUCK
    AVERAGE_LUCK = localization.Keyboards.AVERAGE_LUCK
    GOOD_LUCK = localization.Keyboards.GOOD_LUCK
    BEST_LUCK = localization.Keyboards.BEST_LUCK


class PaginatorEnums(enum.Enum):
    ARTIFACT_SET = "set_artifact_set"
    ARTIFACT_MAIN_STAT = "set_main_stat"
    ARTIFACT_SUB_STAT = "set_sub_stat"

