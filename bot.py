from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5324055764:AAEGTIrZUQJ-J3KBDtyoHk9_BQ1JUN2lLHg'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# getting message that bot is online
async def on_startup(_):
    print('Bot is online')


'''*************************************CLIENT PART*************************'''


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        # bot sends message to users personal chat
        await bot.send_message(message.from_user.id, 'Hello, enjoy your meal!')
        await message.delete()
    except:
        await message.reply('talking to bot through the personal chat, text to him:\nhttps://t.me/AnimeFoodBot')


@dp.message_handler(commands=['Working_hours'])
async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Everyday, 9:00 to 20:00')


@dp.message_handler(commands=['Where?'])
async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Backer street 221b')


'''*************************************ADMIN PART*************************************'''
'''*************************************PART***********************************'''


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Hello':
        await message.answer('Hello to you too!')
    else:
        await message.answer(message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
