import telebot
from telebot import types
from config import TOKEN_BUYER

bot = telebot.TeleBot(TOKEN_BUYER)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Мои магазины', callback_data='test')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Новые объявления', callback_data='test')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Уведомления', callback_data='test')
    btn4 = types.InlineKeyboardButton('Избранное', callback_data='test')
    markup.row(btn3, btn4)

    bot.send_message(message.chat.id, 'Привет, что вы хотите сделать?', reply_markup=markup)


bot.polling(none_stop=True)

