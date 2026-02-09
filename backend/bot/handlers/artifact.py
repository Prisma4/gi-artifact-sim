from typing import Optional, Literal

from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto, BufferedInputFile

from artifacts.constants import ArtifactType, ArtifactSet, Stat, PercentStat
from artifacts.interface import ArtifactInterface
from artifacts.models import Artifact
from bot.defs.artifact import ArtifactImageGenerator
from bot.handlers.base import logger, localization
from bot.keyboards.kb import InlineKeyboards
from bot.models import ReplyKeyboardEnums, KeyboardEnums

router = Router()


async def generate_artifact_image_from_state(state: FSMContext):
    state_data = await state.get_data()

    artifact_type: ArtifactType = state_data.get("artifact_type", ArtifactType.FLOWER_OF_LIFE)
    artifact_set: ArtifactSet = state_data.get("artifact_set", ArtifactSet.GLADIATORS_FINALE)

    forced_main_stat: Optional[Stat | PercentStat] = state_data.get("forced_main_stat", None)
    forced_sub_stat: Optional[Stat | PercentStat] = state_data.get("forced_sub_stat", None)
    forced_sub_stat_luck: Optional[Stat | PercentStat] = state_data.get("forced_sub_stat_luck", None)

    artifact_obj: Artifact = ArtifactInterface.generate_artifact_obj(
        artifact_type=artifact_type,
        artifact_set=artifact_set,
        forced_main_stat=forced_main_stat,
        forced_sub_stat=forced_sub_stat,
        forced_sub_stat_luck=forced_sub_stat_luck,
    )
    await state.update_data(artifact_obj=artifact_obj)

    return await ArtifactImageGenerator.generate_artifact_image(artifact_obj)


def generate_proc_history(
        artifact: Artifact
) -> str:
    title = ""
    if isinstance(artifact.logs, list):
        for i, proc_log in enumerate(artifact.logs):
            title += f"{i+1} - " + str(proc_log.substat.stat.value) + ": " + str(proc_log.increased_by) + "\n"
    return title


@router.message(F.text == ReplyKeyboardEnums.ARTIFACTS.value)
async def handle_new_artifact(message: types.Message, state: FSMContext):
    try:
        artifact_image = await generate_artifact_image_from_state(state)

        await message.answer_photo(
            reply_markup=InlineKeyboards.get_artifact_keyboard(),
            photo=BufferedInputFile(artifact_image, filename="artifact.png"),
        )
    except Exception as e:
        logger.exception(e)
        await message.answer(
            text=localization.Messages.SOMETHING_WENT_WRONG,
        )


@router.callback_query(F.data.in_([KeyboardEnums.REROLL.value, ]))
async def handle_reroll(call: types.CallbackQuery, state: FSMContext):
    try:
        artifact_image = await generate_artifact_image_from_state(state)

        await call.message.edit_media(
            reply_markup=InlineKeyboards.get_artifact_keyboard(),
            media=InputMediaPhoto(media=BufferedInputFile(artifact_image, filename="artifact.png"))
        )

        await call.answer()
    except Exception as e:
        logger.exception(e)
        await call.answer(
            text=localization.Messages.SOMETHING_WENT_WRONG,
        )


@router.callback_query(F.data.in_([KeyboardEnums.ARTIFACT_LEVEL_UP.value, ]))
async def handle_artifact_level_up(call: types.CallbackQuery, state: FSMContext):
    try:
        state_data = await state.get_data()
        artifact_obj: Artifact = state_data.get('artifact_obj')

        if artifact_obj is None:
            raise ValueError("Artifact object was not found in the state")

        is_max_level: bool = True if artifact_obj.level >= 20 else False

        if is_max_level:
            raise ValueError("Artifact level is already max")

        forced_sub_stat: Optional[Stat | PercentStat] = state_data.get('forced_sub_stat', None)
        forced_sub_stat_luck: Optional[Literal[0, 1, 2, 3]] = state_data.get('forced_sub_stat_luck', None)

        for i in range(4):
            substat, value_increase = ArtifactInterface.raise_artifact_level(
                artifact=artifact_obj,
                forced_substat=forced_sub_stat,
                forced_substat_luck=forced_sub_stat_luck,
            )
            if substat:
                await call.answer(
                    localization.Messages.ARTIFACT_SUBSTAT_WAS_INCREASED.format(substat.stat.value, value_increase)
                )
        await state.update_data(artifact_obj=artifact_obj)

        artifact_image = await ArtifactImageGenerator.generate_artifact_image(artifact_obj)

        is_max_level: bool = True if artifact_obj.level >= 20 else False

        await call.message.edit_media(
            reply_markup=InlineKeyboards.get_artifact_keyboard(is_max_level=is_max_level),
            media=InputMediaPhoto(media=BufferedInputFile(artifact_image, filename="artifact.png"))
        )
    except Exception as e:
        logger.exception(e)
        await call.answer(
            text=localization.Messages.SOMETHING_WENT_WRONG,
        )


@router.callback_query(F.data == KeyboardEnums.SHOW_PROC_HISTORY.value)
async def show_proc_history(call: types.CallbackQuery, state: FSMContext):
    try:
        state_data = await state.get_data()
        artifact_obj: Artifact = state_data.get('artifact_obj')

        if artifact_obj is None:
            raise ValueError("Artifact object was not found in the state")

        is_max_level: bool = True if artifact_obj.level >= 20 else False

        if not is_max_level:
            raise ValueError("Artifact level is not max")

        await call.answer(
            text=generate_proc_history(artifact=artifact_obj)[:200],
            show_alert=True,
        )
    except Exception as e:
        logger.exception(e)
        await call.answer(
            text=localization.Messages.SOMETHING_WENT_WRONG,
        )
