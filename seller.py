import telebot
from telebot import types

bot = telebot.TeleBot('6506191359:AAE-NC1rl4CwZMGQ3TaZasB73PU5uS53_Vc')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Мои объявления', callback_data='dkjf')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Создать объявление', callback_data='dkjf')
    btn3 = types.InlineKeyboardButton('Удалить объявление', callback_data='dkjf')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('Уведомления', callback_data='dkjf')
    btn5 = types.InlineKeyboardButton('Оплата', callback_data='dkjf')
    markup.row(btn4, btn5)

    bot.send_message(message.chat.id, 'Привет, что вы хотите сделать?', reply_markup=markup)


bot.polling(none_stop=True)

