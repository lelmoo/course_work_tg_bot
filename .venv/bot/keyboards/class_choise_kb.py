from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_classes_keyboard(buttons, callback_data):
    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(*[InlineKeyboardButton(
        text=button,
        callback_data=f'{callback_data}_{button}') for button in buttons],
        width=1
    )
    return kb_builder.as_markup()