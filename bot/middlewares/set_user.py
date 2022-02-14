from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from models.user import User


class SetUserMiddleware(BaseMiddleware):
    async def get_or_create_user(self, message: types.Message) -> User:
        if message.chat.type == "private":
            user, created = await User.get_or_create(
                defaults={"telegram_id": message.chat.id},
                username=message.chat.username,
                first_name=message.chat.first_name,
                last_name=message.chat.last_name
            )
            return user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        data["user"] = await self.get_or_create_user(message)

    async def on_post_process_message(self, message: types.Message,
                                      results: list, data: dict):
        del data["user"]

    async def on_pre_process_callback_query(self, call: types.CallbackQuery,
                                            data: dict):
        data["user"] = await self.get_or_create_user(call.message)

    async def on_post_process_callback_query(self, call: types.CallbackQuery,
                                             results, data: dict):
        del data["user"]
