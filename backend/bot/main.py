import logging
from aiogram import Bot, Dispatcher

from bot.settings import BotSettings
from localization.interface import Localization

settings = BotSettings()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bot_token)
dp = Dispatcher()

Localization.init_localization(language=settings.bot_language)
