import asyncio

from bot.handlers import base, artifact, artifact_set, artifact_type, artifact_forced_stats
from bot.main import dp, bot

dp.include_routers(base.router)
dp.include_routers(artifact.router)
dp.include_routers(artifact_set.router)
dp.include_routers(artifact_type.router)
dp.include_routers(artifact_forced_stats.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
