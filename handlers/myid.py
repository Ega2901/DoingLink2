from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from scheldule.scheldule import  format_schedule_message

myid_router = Router()

@myid_router.message(Command("myid"))  # [2]
async def answer_id(message: Message):
    new_chat = message.chat.id
    await message.answer(str(new_chat))