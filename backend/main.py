import asyncio

from bot.handlers import handlers
from bot.main import dp, bot

dp.include_routers(arts.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
