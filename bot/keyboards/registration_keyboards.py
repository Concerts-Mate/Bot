from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from .callback_data import KeyboardCallbackData
from .utils import create_resizable_reply_keyboard, create_resizable_inline_keyboard


def get_location_keyboard_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(
        text='Отправить геолокацию',
        request_location=True
    ))
    return create_resizable_reply_keyboard(builder)


skip_add_cities_texts = 'Прекратить ввод городов'

skip_add_links_texts = 'Прекратить ввод ссылок'


def get_skip_add_cities_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(
        text=skip_add_cities_texts,
    ))
    return create_resizable_reply_keyboard(builder)


def get_skip_add_links_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(
        text=skip_add_links_texts,
    ))
    return create_resizable_reply_keyboard(builder)


def get_fuzz_variants_markup() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text='Принять', callback_data=KeyboardCallbackData.APPLY
        ),
        types.InlineKeyboardButton(
            text='Отказаться', callback_data=KeyboardCallbackData.DENY
        )
    )
    return create_resizable_inline_keyboard(builder)
