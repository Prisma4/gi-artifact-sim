import logging
from typing import Type

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.keyboards.kb import ReplyKeyboards
from bot.states import BotStates
from localization.localization_data import BaseLocalization
from localization.interface import Localization

localization: Type[BaseLocalization] = Localization.get_localization()

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.main_state)
    await message.answer(
        localization.Messages.START_MESSAGE.format(message.from_user.username),
        reply_markup=ReplyKeyboards.get_main_keyboard()
    )
