import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from handlers import click, myid, rcpoll
from scheldule.scheldule import  send_schedule
from aiogram.methods.send_message import SendMessage
from aiogram.types import Message, ReplyKeyboardRemove, Poll, PollAnswer
from datetime import datetime
import aioschedule
from tzlocal import get_localzone
import sys
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# Включаем логирование
logging.basicConfig(level=logging.INFO, format='%(filename)s:%(lineno)d #%(levelname)-8s '
                    '[%(asctime)s] - %(name)s - %(message)s'
                    )


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    async def schedule_daily_broadcast(bot_instance):
        subscribers = [921953226, -1001965799227]
        for subscriber in subscribers:
            await bot_instance.send_message(subscriber, send_schedule())

    current_time = datetime.now(get_localzone())

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(schedule_daily_broadcast, trigger='cron', hour=12, minute=0, start_date=current_time, args=[bot])

    async def start_poll():
        markup = types.ReplyKeyboardRemove()
        poll_text = "Всем привет✌🏻, в эфире наша еженедельная программа по наработке социального капитала!🥳 Примешь участие в нашем празднике жизни? ☺️🎉"
        options = ["✅ Да", "❌ Нет, в другой раз"]
        await bot.send_poll(
            chat_id=921953226,
            question=poll_text,
            options=options,
            is_anonymous=False,  # Устанавливаем опрос как неанонимный
            reply_markup=markup
        )
    async def poll_answer_handler(poll_answer: PollAnswer):
    # Проверяем, что опрос соответствует вашему ожиданию
        if poll_answer.poll.question == "Всем привет✌🏻, в эфире наша еженедельная программа по наработке социального капитала!🥳 Примешь участие в нашем празднике жизни? ☺️🎉(Досрочно завершить голосование /pairs)":
            # Получаем список пользователей, проголосовавших в опросе
            user_ids = [user.user.id for user in poll_answer.user]
            # Выводим список user_id пользователей
            print("User IDs who voted in the poll:", user_ids)

    scheduler.add_job(start_poll, trigger='cron', hour=17, minute=27, start_date=current_time)
    scheduler.start()
    dp.include_routers(click.router, myid.myid_router, rcpoll.rf_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


