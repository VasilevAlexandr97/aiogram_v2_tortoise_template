from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from aiogram import types
from bot.configs.config import config


@dataclass
class InlineButton:
    title: str
    callback_data: Optional[str] = None
    url: Optional[str] = None


INLINE_BUTTONS = {
    "add_bot_in_chat": InlineButton(
        "Добавить бота в чат",
        url=f"https://t.me/{config.tg_bot.bot_username}?startgroup=add_chat"
    ),
    "user_chats": InlineButton(
        "Мои чаты",
        callback_data="user_chats"
    )
}

INLINE_KEYBOARDS = {
    "user_start": (
        (INLINE_BUTTONS["add_bot_in_chat"],),
        (INLINE_BUTTONS["user_chats"],)
    )
}


class InlineKeyboard:
    def __init__(self, keyboards_dict: Dict[str, Tuple[Tuple[InlineButton]]]
                 ) -> None:
        self.keyboards_dict = keyboards_dict

    async def generate_json(self, keyboard_title: str) -> str:
        keyboard = types.InlineKeyboardMarkup()

        for row in self.keyboards_dict[keyboard_title]:
            row_buttons: List[InlineButton] = []
            for button in row:
                row_buttons.append(types.InlineKeyboardButton(
                    text=button.title,
                    url=button.url,
                    callback_data=button.callback_data
                ))
            keyboard.row(*row_buttons)

        return keyboard.as_json()


inline_kb = InlineKeyboard(INLINE_KEYBOARDS)