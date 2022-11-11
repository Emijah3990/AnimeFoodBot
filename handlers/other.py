from aiogram import types, Dispatcher

from create_bot import dp

import json
import string


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('forbidden_words/forbidden_words.json')))) != set():
        await message.reply('Swearing is forbidden')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
