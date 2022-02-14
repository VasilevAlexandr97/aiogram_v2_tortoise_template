from aiogram import Bot, Dispatcher, executor

from bot.configs.config import config
from bot.handlers.generals import register_generals_handlers
from bot.middlewares.set_user import SetUserMiddleware
from bot.models import connect_db, disconnect_db


async def on_startup(dp: Dispatcher) -> None:
    """Выполняется при старте бота"""
    await connect_db()


async def on_shutdown(dp: Dispatcher) -> None:
    """Выполняется при выключении бота"""
    await disconnect_db()


def loader():
    bot = Bot(config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(bot)

    dp.setup_middleware(SetUserMiddleware())

    register_generals_handlers(dp)

    executor.start_polling(dp, skip_updates=False, on_startup=on_startup,
                           on_shutdown=on_shutdown)
