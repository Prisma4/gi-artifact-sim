import logging
from typing import Type

from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.keyboards.kb import ReplyKeyboards
from localization.enums import BaseLocalization
from localization.interface import Localization

localization_enum: Type[BaseLocalization] = Localization.get_localization_enum()


class BotStates(StatesGroup):
    main_state = State()
    waiting_for_forced_main_stat = State()
    waiting_for_forced_sub_stat = State()


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.main_state)
    await message.answer(
        localization_enum.Messages.START_MESSAGE.format(message.from_user.username),
        reply_markup=ReplyKeyboards.get_main_keyboard()
    )
