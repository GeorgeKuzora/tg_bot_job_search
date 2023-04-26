import asyncio 
from aiogram import Bot, Dispatcher
from src.config.config import Config, load_config
from src.handlers import user_handlers


async def main() -> None:
    config: Config = load_config(path=".env")
    bot_token: str = config.tg_bot.token
    bot: Bot = Bot(token=bot_token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
