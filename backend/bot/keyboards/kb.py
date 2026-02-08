from typing import Type

import aiogram
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from artifacts.constants import ArtifactSet, ArtifactType
from bot.models import KeyboardEnums, ReplyKeyboardEnums, PaginatorEnums, ArtifactLuck
from localization.enums import BaseLocalization
from localization.interface import Localization

localization_enum: Type[BaseLocalization] = Localization.get_localization_enum()


class ReplyKeyboards:
    @staticmethod
    def get_main_keyboard():
        keyboard = [
            [KeyboardButton(text=ReplyKeyboardEnums.ARTIFACTS.value)],
            [
                [KeyboardButton(text=ReplyKeyboardEnums.CHANGE_SET.value)],
                [KeyboardButton(text=ReplyKeyboardEnums.CHANGE_TYPE.value)],
            ],
            [KeyboardButton(text=ReplyKeyboardEnums.FORCE_MAIN_STAT.value)],
            [
                [KeyboardButton(text=ReplyKeyboardEnums.FORCE_SUB_STAT.value)],
                [KeyboardButton(text=ReplyKeyboardEnums.FORCE_SUB_STAT_LUCK.value)],
            ]
        ]
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


class InlineKeyboards:
    @staticmethod
    def get_artifact_type_keyboard(artifact_types: Type[ArtifactType] = ArtifactType):
        keyboard = []

        for artifact_type in artifact_types:
            keyboard.append([
                InlineKeyboardButton(
                    text=artifact_type.value,
                    callback_data=artifact_type.value
                )
            ])

        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    @staticmethod
    def get_artifact_set_keyboard(artifact_sets: Type[ArtifactSet] = ArtifactSet, page: int = 1,
                                  sets_per_page: int = 10):
        artifact_sets_list = list(artifact_sets)
        total_sets = len(artifact_sets_list)
        start_idx = (page - 1) * sets_per_page
        end_idx = min(start_idx + sets_per_page, total_sets)
        current_sets = artifact_sets_list[start_idx:end_idx]
        keyboard = [
            [InlineKeyboardButton(
                text=artifact_set.value,
                callback_data=artifact_set.value
            )] for artifact_set in current_sets
        ]
        navigation_buttons = []
        if page > 1:
            navigation_buttons.append(
                InlineKeyboardButton(text=localization_enum.Keyboards.PAGINATION_PREVIOUS.value,
                                     callback_data=f"{PaginatorEnums.ARTIFACT_SET_PREV.value}{page - 1}")
            )
        if end_idx < total_sets:
            navigation_buttons.append(
                InlineKeyboardButton(text=localization_enum.Keyboards.PAGINATION_NEXT.value,
                                     callback_data=f"{PaginatorEnums.ARTIFACT_SET_NEXT.value}{page + 1}")
            )
        if navigation_buttons:
            keyboard.append(navigation_buttons)
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    @staticmethod
    def get_main_stats_keyboard():
        pass

    @staticmethod
    def get_sub_stats_keyboard():
        pass

    @staticmethod
    def get_sub_stat_luck_keyboard():
        keyboard = [
            InlineKeyboardButton(text=localization_enum.Keyboards.WORST_LUCK.value,
                                 callback_data=ArtifactLuck.WORST_LUCK.value),
            InlineKeyboardButton(text=localization_enum.Keyboards.AVERAGE_LUCK.value,
                                 callback_data=ArtifactLuck.AVERAGE_LUCK.value),
            InlineKeyboardButton(text=localization_enum.Keyboards.GOOD_LUCK.value,
                                 callback_data=ArtifactLuck.GOOD_LUCK.value),
            InlineKeyboardButton(text=localization_enum.Keyboards.BEST_LUCK.value,
                                 callback_data=ArtifactLuck.BEST_LUCK.value),
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    @staticmethod
    def get_artifact_keyboard(is_max_level: bool = False):
        base_keyboard = [InlineKeyboardButton(text=localization_enum.Keyboards.NEW_ARTIFACT.value,
                                              callback_data=KeyboardEnums.REROLL.value)]

        if not is_max_level:
            keyboard = [
                [InlineKeyboardButton(text=localization_enum.Keyboards.LEVEL_UP_ARTIFACT.value,
                                      callback_data=KeyboardEnums.ARTIFACT_LEVEL_UP.value)],
                base_keyboard,
            ]
        else:
            keyboard = [base_keyboard]

        return InlineKeyboardMarkup(inline_keyboard=keyboard)
