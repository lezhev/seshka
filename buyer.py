import telebot
from telebot import types
from config import TOKEN_BUYER
from seshka_backend.seshka_lib import Item, Seller, Buyer

bot = telebot.TeleBot(TOKEN_BUYER)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Лента', callback_data='surfing')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Мои магазины', callback_data='test')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Уведомления', callback_data='test')
    btn4 = types.InlineKeyboardButton('Избранное', callback_data='test')
    markup.row(btn3, btn4)

    bot.send_message(message.chat.id, 'Привет, что вы хотите сделать?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    Seller.print_database()

    if call.data == 'surfing':
        item_list, id_list = Buyer.get_all_items()
        for i in item_list:
            print(i)
            bot.send_message(call.message.chat.id, i.__str__(), parse_mode='Markdown')


bot.polling(none_stop=True)

