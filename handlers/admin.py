from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# beginning of chat for uploading food
@dp.message_handler(commands='Upload', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Uplaod photo')


# getting first answer and writing it in dict.
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Type a name plesae: ')
