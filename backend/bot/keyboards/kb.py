import enum
from typing import Type, List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from artifacts.constants import ArtifactType
from bot.models import KeyboardEnums, ReplyKeyboardEnums, ArtifactLuck
from localization.localization_data import BaseLocalization
from localization.interface import Localization

localization: Type[BaseLocalization] = Localization.get_localization()


class ReplyKeyboards:
    @staticmethod
    def get_main_keyboard():
        keyboard = [
            [KeyboardButton(text=ReplyKeyboardEnums.ARTIFACTS.value)],
            [
                KeyboardButton(text=ReplyKeyboardEnums.CHANGE_SET.value),
                KeyboardButton(text=ReplyKeyboardEnums.CHANGE_TYPE.value),
            ],
            [KeyboardButton(text=ReplyKeyboardEnums.FORCE_MAIN_STAT.value)],
            [
                KeyboardButton(text=ReplyKeyboardEnums.FORCE_SUB_STAT.value),
                KeyboardButton(text=ReplyKeyboardEnums.FORCE_SUB_STAT_LUCK.value),
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
    def get_paginated_keyboard(
            objects: List[enum.Enum],
            callback_data: str,
            page: int = 1,
            per_page: int = 5,
            pagination_button_previous_text: str = localization.Keyboards.PAGINATION_PREVIOUS,
            pagination_button_next_text: str = localization.Keyboards.PAGINATION_NEXT,
    ) -> InlineKeyboardMarkup:
        total_objects = len(objects)
        start_idx = (page - 1) * per_page
        end_idx = min(start_idx + per_page, total_objects)
        keyboard = [
            [InlineKeyboardButton(
                text=obj.value,
                callback_data=obj.value
            )] for obj in objects[start_idx:end_idx]
        ]
        navigation_buttons = []
        if page > 1:
            navigation_buttons.append(
                InlineKeyboardButton(text=pagination_button_previous_text,
                                     callback_data=f"{callback_data}_{page - 1}")
            )
        if end_idx < total_objects:
            navigation_buttons.append(
                InlineKeyboardButton(text=pagination_button_next_text,
                                     callback_data=f"{callback_data}_{page + 1}")
            )
        if navigation_buttons:
            keyboard.append(navigation_buttons)
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    @staticmethod
    def get_sub_stat_luck_keyboard():
        keyboard = [
            [InlineKeyboardButton(text=localization.Keyboards.WORST_LUCK,
                                  callback_data=ArtifactLuck.WORST_LUCK.value),
             InlineKeyboardButton(text=localization.Keyboards.AVERAGE_LUCK,
                                  callback_data=ArtifactLuck.AVERAGE_LUCK.value)],
            [InlineKeyboardButton(text=localization.Keyboards.GOOD_LUCK,
                                  callback_data=ArtifactLuck.GOOD_LUCK.value),
             InlineKeyboardButton(text=localization.Keyboards.BEST_LUCK,
                                  callback_data=ArtifactLuck.BEST_LUCK.value)],
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    @staticmethod
    def get_artifact_keyboard(is_max_level: bool = False):
        base_keyboard = [InlineKeyboardButton(text=localization.Keyboards.NEW_ARTIFACT,
                                              callback_data=KeyboardEnums.REROLL.value)]

        if not is_max_level:
            keyboard = [
                [InlineKeyboardButton(text=localization.Keyboards.LEVEL_UP_ARTIFACT,
                                      callback_data=KeyboardEnums.ARTIFACT_LEVEL_UP.value)],
                base_keyboard,
            ]
        else:
            keyboard = [base_keyboard]

        return InlineKeyboardMarkup(inline_keyboard=keyboard)
