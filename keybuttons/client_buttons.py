from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Working_hours')
b2 = KeyboardButton('/Where?')
b3 = KeyboardButton('/Menu')

#replacing usual keyboard on the one were making
b_client = ReplyKeyboardMarkup(resize_keyboard=True)

b_client.add(b3).add(b2).insert(b1)

#b_cliend.row(b2, b3, b1)