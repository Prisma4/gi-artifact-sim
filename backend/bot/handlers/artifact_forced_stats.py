from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from artifacts.constants import Stat, PercentStat
from bot.models import ArtifactLuck, PaginatorEnums
from bot.handlers.handlers import localization_enum, logger, BotStates
from bot.keyboards.kb import InlineKeyboards
from bot.models import ReplyKeyboardEnums

router = Router()


# FORCE MAIN STAT


@router.message(F.text == ReplyKeyboardEnums.FORCE_MAIN_STAT.value)
async def force_main_stat(message: types.Message, state: FSMContext):
    try:
        await message.answer(text=localization_enum.Messages.CHOOSE_FORCED_MAINSTAT,
                             reply_markup=InlineKeyboards.get_paginated_keyboard(
                                 objects=list(Stat) + list(PercentStat),
                                 callback_data=PaginatorEnums.ARTIFACT_MAIN_STAT.value,
                             ))
        await state.set_state(BotStates.waiting_for_forced_main_stat)
    except Exception as e:
        logger.error(e)
        await message.edit_text(
            text=localization_enum.Messages.SOMETHING_WENT_WRONG
        )


@router.callback_query(BotStates.waiting_for_forced_main_stat,
                       F.data.in_([e.value for e in Stat] + [e.value for e in PercentStat]))
async def set_artifact_main_stat(call: types.CallbackQuery, state: FSMContext):
    try:
        if call.data in [e.value for e in Stat]:
            forced_stat = Stat(call.data)
        elif call.data in [e.value for e in PercentStat]:
            forced_stat = PercentStat(call.data)
        else:
            raise ValueError("Unexpected value: {}".format(call.data))

        await state.update_data(forced_main_stat=forced_stat)
        await call.message.edit_text(
            text=localization_enum.Messages.CHOOSE_FORCED_MAINSTAT_SUCCESS.format(forced_stat.value)
        )
        await state.set_state(BotStates.main_state)
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG,
        )


@router.callback_query(F.data.startswith(PaginatorEnums.ARTIFACT_MAIN_STAT.value))
async def show_artifact_main_stats_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[-1])
    keyboard = InlineKeyboards.get_paginated_keyboard(
        objects=list(Stat) + list(PercentStat),
        callback_data=PaginatorEnums.ARTIFACT_MAIN_STAT.value,
        page=page
    )
    await call.message.edit_text(
        localization_enum.Messages.CHOOSE_FORCED_MAINSTAT,
        reply_markup=keyboard
    )


# FORCE SUBSTAT


@router.message(F.text == ReplyKeyboardEnums.FORCE_SUB_STAT.value)
async def force_sub_stat(message: types.Message, state: FSMContext):
    try:
        await message.answer(text=localization_enum.Messages.CHOOSE_FORCED_SUBSTAT,
                             reply_markup=InlineKeyboards.get_paginated_keyboard(
                                 objects=list(Stat) + list(PercentStat),
                                 callback_data=PaginatorEnums.ARTIFACT_SUB_STAT.value,
                             ))
        await state.set_state(BotStates.waiting_for_forced_sub_stat)
    except Exception as e:
        logger.error(e)
        await message.edit_text(
            text=localization_enum.Messages.SOMETHING_WENT_WRONG
        )


@router.callback_query(BotStates.waiting_for_forced_sub_stat,
                       F.data.in_([e.value for e in Stat] + [e.value for e in PercentStat]))
async def set_artifact_sub_stat(call: types.CallbackQuery, state: FSMContext):
    try:
        if call.data in [e.value for e in Stat]:
            forced_stat = Stat(call.data)
        elif call.data in [e.value for e in PercentStat]:
            forced_stat = PercentStat(call.data)
        else:
            raise ValueError("Unexpected value: {}".format(call.data))

        await state.update_data(forced_sub_stat=forced_stat)
        await call.message.edit_text(
            text=localization_enum.Messages.CHOOSE_FORCED_SUBSTAT_SUCCESS.format(forced_stat.value)
        )
        await state.set_state(BotStates.main_state)
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG,
        )


@router.callback_query(F.data.startswith(PaginatorEnums.ARTIFACT_SUB_STAT.value))
async def show_artifact_sub_stats_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[-1])
    keyboard = InlineKeyboards.get_paginated_keyboard(
        objects=list(Stat) + list(PercentStat),
        callback_data=PaginatorEnums.ARTIFACT_SUB_STAT.value,
        page=page
    )
    await call.message.edit_text(
        localization_enum.Messages.CHOOSE_FORCED_SUBSTAT,
        reply_markup=keyboard
    )


# FORCE SUBSTAT LUCK


@router.message(F.text == ReplyKeyboardEnums.FORCE_SUB_STAT_LUCK.value)
async def change_sub_stat_luck(message: types.Message, state: FSMContext):
    try:
        await message.answer(text=localization_enum.Messages.CHOOSE_FORCED_SUBSTAT_LUCK,
                             reply_markup=InlineKeyboards.get_sub_stat_luck_keyboard())
    except Exception as e:
        logger.error(e)
        await message.answer(
            text=localization_enum.Messages.SOMETHING_WENT_WRONG,
        )


artifact_luck_mapping = {
    ArtifactLuck.WORST_LUCK.value: 0,
    ArtifactLuck.AVERAGE_LUCK.value: 1,
    ArtifactLuck.GOOD_LUCK.value: 2,
    ArtifactLuck.BEST_LUCK.value: 3
}


@router.callback_query(F.data.in_([e.value for e in ArtifactLuck]))
async def set_sub_stat_luck(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(forced_sub_stat_luck=artifact_luck_mapping.get(call.data))
        await call.answer(
            localization_enum.Messages.CHOOSE_FORCED_SUBSTAT_LUCK_SUCCESS.format(call.data)
        )
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG,
        )
