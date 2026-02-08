from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from bot.models import ReplyKeyboardEnums, ArtifactLuck
from bot.handlers.handlers import router, localization_enum, logger
from bot.keyboards.kb import InlineKeyboards
from bot.models import ReplyKeyboardEnums, PaginatorEnums


@router.message(F.text == ReplyKeyboardEnums.FORCE_MAIN_STAT.value)
async def force_main_stat(message: types.Message, state: FSMContext):
    try:
        pass
    except Exception as e:
        logger.error(e)
        await message.answer(
            text=localization_enum.Messages.SOMETHING_WENT_WRONG.value,
        )


@router.message(F.text == ReplyKeyboardEnums.FORCE_SUB_STAT.value)
async def force_sub_stat(message: types.Message, state: FSMContext):
    try:
        pass
    except Exception as e:
        logger.error(e)
        await message.answer(
            text=localization_enum.Messages.SOMETHING_WENT_WRONG.value,
        )


@router.message(F.text == ReplyKeyboardEnums.FORCE_SUB_STAT_LUCK.value)
async def force_sub_stat_luck(message: types.Message, state: FSMContext):
    try:
        await message.answer(text=localization_enum.Messages.CHOOSE_FORCED_SUBSTAT_LUCK,
                             reply_markup=InlineKeyboards.get_sub_stat_luck_keyboard())
    except Exception as e:
        logger.error(e)
        await message.answer(
            text=localization_enum.Messages.SOMETHING_WENT_WRONG.value,
        )


@router.callback_query(F.data.in_([e.value for e in ArtifactLuck]))
async def set_artifact_set(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(artifact_set=ArtifactLuck(call.data))
        await call.answer(
            localization_enum.Messages.ARTIFACT_CHOOSE_SET_SUCCESS.value.format(call.data)
        )
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG.value,
        )
