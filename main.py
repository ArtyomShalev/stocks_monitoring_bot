from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import TOKEN
from apscheduler.schedulers.asyncio import AsyncIOScheduler


sched = AsyncIOScheduler()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg):
    await bot.send_message(msg.from_user.id, 'Hi! I can help you to get the stock quotes you like. '
                                             'Just type /choose_stocks command in order to choose stocks you like.')


@dp.message_handler(commands=['reschedule'])
async def reschedule(msg):
    await bot.send_message(msg.from_user.id, 'Youre rescheduling now')
    await reshedule_mailing(msg.from_user.id)


def update_data():
    pass

async def reshedule_mailing(id):
    # 1 option
    # sched.pause(id)
    # sched.reschedule_job(id, trigger='cron', day='*', hour='*', minute='*', second='*/3')
    # 2 option
    sched.remove_job(str(id))
    update_data()
    # await run_mailing(id, 'New message')

async def run_mailing(user_id, msg):
    update_data() # from database

    @sched.scheduled_job(trigger='cron', day='*', hour='*', minute='*', second='*', id=str(user_id))
    async def timed_job():
        await bot.send_message(user_id, msg)

    sched.start()


if __name__ == '__main__':
    executor.start_polling(dp)



