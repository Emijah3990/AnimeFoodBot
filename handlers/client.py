from aiogram import types, Dispatcher

from create_bot import dp, bot


#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        # bot sends message to users personal chat
        await bot.send_message(message.from_user.id, 'Hello, enjoy your meal!')
        await message.delete()
    except:
        await message.reply('talking to bot through the personal chat, text to him:\nhttps://t.me/AnimeFoodBot')


#@dp.message_handler(commands=['Working_hours'])
async def caffee_open_time_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Everyday, 9:00 to 20:00')


#@dp.message_handler(commands=['Where?'])
async def caffee_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Backer street 221b')

def register_handlers_client(dp : Dispatcher):

    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(caffee_open_time_command, commands=['Working_hours'] )
    dp.register_message_handler(caffee_place_command, commands=['Where?'])