from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import keyboards as kb


sched = AsyncIOScheduler()
bot = Bot(token='token')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg):
    await bot.send_message(msg.from_user.id, "Wow, you've just launched me!",
                           reply_markup=kb.inline_kb1_hi)

@dp.callback_query_handler(text='btn_hi')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Hi! I can help you to get the stock quotes. '
                                             'Just type /choose_stocks command in order to choose stocks you like.')


@dp.message_handler(commands=['choose_stocks'])
async def choose_stocks(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Now you can choose only between several stocks '
                                             'indexed on the Moscow Exchange',
                           reply_markup=kb.inline_kb_stocks)

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



