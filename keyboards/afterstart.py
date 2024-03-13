from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_after() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Узнать расписание")
    kb.button(text="Задать вопрос")
    kb.button(text="Отметиться на паре", request_location=True)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)