import aiogram
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

ARTIFACTS = "артефакты"

TYPE = "тип"

ARTIFACT_LEVEL_UP = "уровень"
REROLL = "reroll"
BACK = "назад"

FLOWER = 'flower'
FEATHER = 'feather'
CLOCK = 'clock'
GOBLET = 'goblet'
CROWN = 'crown'


async def main_keyboard():
    a = InlineKeyboardButton(text = "Артефакты", callback_data=ARTIFACTS)
    z = InlineKeyboardMarkup(inline_keyboard=[[a]])
    return z
async def type_keyboard():
    a = InlineKeyboardButton(text="Цветок", callback_data=FLOWER)
    b = InlineKeyboardButton(text="Перо", callback_data=FEATHER)
    c = InlineKeyboardButton(text="Часы", callback_data=CLOCK)
    d = InlineKeyboardButton(text="Кубок", callback_data=GOBLET)
    e = InlineKeyboardButton(text="Корона", callback_data=CROWN)
    z = InlineKeyboardMarkup(inline_keyboard=[[a, b],[c, d],[e]])
    return z
async def artifact_level_up_keyboard(artefact_level):
    if artefact_level < 20:
        a = InlineKeyboardButton(text="Новый артефакт", callback_data=REROLL)
        b = InlineKeyboardButton(text="Повысить уровень", callback_data=ARTIFACT_LEVEL_UP)
        c = InlineKeyboardButton(text="Назад", callback_data=BACK)
        z = InlineKeyboardMarkup(inline_keyboard=[[b],[a,c]])
    elif artefact_level == 20:
        a = InlineKeyboardButton(text="Новый артефакт", callback_data=REROLL)
        c = InlineKeyboardButton(text="Назад", callback_data=BACK)
        z = InlineKeyboardMarkup(inline_keyboard=[[a,c]])
    return z