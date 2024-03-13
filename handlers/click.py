from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from scheldule.scheldule import  format_schedule_message

from keyboards.afterstart import get_after

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Привет, это DoingLink!🔥🔥🔥\n Я умею отправлять события из вашего Google Calendar 📅 создавать RandomCoffee ☕️ , а также поздравлять с днем рождения!🥳 Давайте познакомимся, введите свои Фамилию и Имя:",
        reply_markup=get_after()
    )

@router.message(F.text.lower() == "узнать расписание")
async def answer_yes(message: Message):
    await message.answer(
        format_schedule_message(),
        reply_markup=get_after()
    )
    
@router.message(F.text.lower() == "отметиться на паре")
async def answer_yes(message: Message):
    await message.answer(
        "Привет это ChemBot, здесь вы можете купить необходимый набор реактивов для ЕГЭ",
        reply_markup=get_after()
    )
    
