from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5324055764:AAEGTIrZUQJ-J3KBDtyoHk9_BQ1JUN2lLHg'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

'''*************************************CLIENT PART*************************'''
'''*************************************ADMIN PART*************************************'''
'''*************************************PART***********************************'''





@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Hello':
        await message.answer('Hello to you too!')
    else:
        await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)