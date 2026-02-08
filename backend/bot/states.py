from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    main_state = State()
    waiting_for_forced_main_stat = State()
    waiting_for_forced_sub_stat = State()
