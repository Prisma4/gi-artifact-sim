from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from artifacts.constants import ArtifactSet
from bot.handlers.handlers import localization_enum, logger
from bot.keyboards.kb import InlineKeyboards
from bot.models import ReplyKeyboardEnums, PaginatorEnums


router = Router()


@router.message(F.text == ReplyKeyboardEnums.CHANGE_SET.value)
async def change_artifact_set(message: types.Message):
    try:
        await message.answer(text=localization_enum.Messages.ARTIFACT_CHOOSE_SET,
                             reply_markup=InlineKeyboards.get_paginated_keyboard(
                                 objects=list(ArtifactSet),
                                 callback_data=PaginatorEnums.ARTIFACT_SET.value,
                             ))
    except Exception as e:
        logger.error(e)


@router.callback_query(F.data.in_([e.value for e in ArtifactSet]))
async def set_artifact_set(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(artifact_set=ArtifactSet(call.data))
        await call.answer(
            localization_enum.Messages.ARTIFACT_CHOOSE_SET_SUCCESS.format(call.data)
        )
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG,
        )


@router.callback_query(F.data.startswith(PaginatorEnums.ARTIFACT_SET.value))
async def show_artifact_sets_page(call: types.CallbackQuery, state: FSMContext):
    page = int(call.data.split("_")[-1])
    keyboard = InlineKeyboards.get_paginated_keyboard(
        objects=list(ArtifactSet),
        callback_data=PaginatorEnums.ARTIFACT_SET.value,
        page=page
    )
    await call.message.edit_text(
        localization_enum.Messages.ARTIFACT_CHOOSE_SET,
        reply_markup=keyboard
    )
