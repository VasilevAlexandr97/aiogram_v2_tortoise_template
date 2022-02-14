from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart


async def start_handler(message: types.Message):
    print("hello")


def register_generals_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start_handler, )
