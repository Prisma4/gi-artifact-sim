from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from artifacts.constants import ArtifactType
from bot.handlers.handlers import localization_enum, logger
from bot.keyboards.kb import InlineKeyboards
from bot.models import ReplyKeyboardEnums


router = Router()


@router.message(F.text == ReplyKeyboardEnums.CHANGE_TYPE.value)
async def change_artifact_type(message: types.Message):
    try:
        await message.answer(text=localization_enum.Messages.ARTIFACT_CHOOSE_TYPE,
                             reply_markup=InlineKeyboards.get_artifact_type_keyboard())
    except Exception as e:
        logger.error(e)


@router.callback_query(F.data.in_([e.value for e in ArtifactType]))
async def set_artifact_type(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(artifact_type=ArtifactType(call.data))
        await call.answer(
            localization_enum.Messages.ARTIFACT_CHOOSE_TYPE_SUCCESS.format(call.data),
        )
    except Exception as e:
        logger.error(e)
        await call.answer(
            localization_enum.Messages.SOMETHING_WENT_WRONG,
        )
