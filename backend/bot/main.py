import logging
from aiogram import Bot, Dispatcher

from bot.settings import BotSettings

settings = BotSettings()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bot_token)
dp = Dispatcher()
