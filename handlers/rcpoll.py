from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, Poll, PollAnswer
from scheldule.scheldule import  format_schedule_message
from keyboards.afterstart import get_after
import sys
import json

rf_router = Router() 
yes_users = {}
@rf_router.poll_answer()
async def poll_answer(poll_answer: PollAnswer):
    await poll_answer.answer(
        print(str(PollAnswer))
    )
