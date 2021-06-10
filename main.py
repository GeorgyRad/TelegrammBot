import telebot
from aiogram.types import chat
from aiogram.utils import callback_data
from telebot import types
from aiogram import types

token = ('1717036359:AAEvhTrIn_eDtciqDk7_wPn3KcphrYmp9W0')
bot = telebot.TeleBot(token)

async def cmd_start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["С пюрешкой", "Без пюрешки"]
        keyboard.add(*buttons)
        await message.answer("Как подавать котлеты?", reply_markup=keyboard)

def zhabka():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, '+message.from_user.first_name)

@bot.message_handler(func=lambda call: True)
def cont(message):
        if callback_data == 'Свя':
            bot.send_message(message.chat.id, 'лебедь норм чел', reply_markup=zhabka())
        elif message.text == 'Ближайшее мероприятие':
            bot.send_message(message.chat.id, 'чел ты...', reply_markup=zhabka())
        else:
            bot.send_message(message.chat.id, 'пошел нахуй валенок', reply_markup=cmd_start())

bot.polling()

if __name__ == '__main__':
    bot.polling(none_stop=True)