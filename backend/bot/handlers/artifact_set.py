from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from artifacts.constants import ArtifactSet
from bot.handlers.handlers import router, localization_enum, logger
from bot.keyboards.kb import InlineKeyboards
from bot.models import ReplyKeyboardEnums, PaginatorEnums


@router.message(F.text == ReplyKeyboardEnums.CHANGE_SET.value)
async def change_artifact_set(message: types.Message):
    try:
        await message.answer(text=localization_enum.Messages.ARTIFACT_CHOOSE_SET.value, reply_markup=InlineKeyboards.get_artifact_set_keyboard())
    except Exception as e:
        logger.error(e)


@router.callback_query(F.data.in_([e.value for e in ArtifactSet]))
async def set_artifact_set(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(artifact_set=ArtifactSet(call.data))
        await call.answer(
            localization_enum.Messages.ARTIFACT_CHOOSE_SET_SUCCESS.value.format(call.data)
        )
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG.value,
        )


@router.callback_query(F.data.startswith(PaginatorEnums.ARTIFACT_SET_PREV.value))
async def prev_artifact_sets_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[-1])
    keyboard = InlineKeyboards.get_artifact_set_keyboard(artifact_sets=ArtifactSet, page=page)
    await call.message.edit_text(
        localization_enum.Messages.ARTIFACT_CHOOSE_SET.value,
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith(PaginatorEnums.ARTIFACT_SET_NEXT.value))
async def next_artifacts_sets_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[-1])
    keyboard = InlineKeyboards.get_artifact_set_keyboard(artifact_sets=ArtifactSet, page=page)
    await call.message.edit_text(
        localization_enum.Messages.ARTIFACT_CHOOSE_SET.value,
        reply_markup=keyboard
    )
