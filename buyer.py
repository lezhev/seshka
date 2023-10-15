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
    btn2 = types.InlineKeyboardButton('Мои магазины', callback_data='my_markets')
    btn3 = types.InlineKeyboardButton('Мои подписки', callback_data='my_subs')
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, 'Привет, что вы хотите сделать?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    Seller.print_database()

    if call.data == 'surfing':
        item_list, id_list = Buyer.get_all_items()
        for items in item_list:
            print(items)
            bot.send_photo(call.message.chat.id, items.photo, items.__str__(), parse_mode='Markdown')
        for i in item_list:
            print(i)

            seller_id = Seller.get_seller_name(item.seller_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в магазин', callback_data='go_to'))
            bot.send_message(call.message.chat.id, i.__str__(), parse_mode='Markdown', reply_markup=markup)

    if call.data == 'go_to':
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton('Подписаться', callback_data='sub'),
                   types.InlineKeyboardButton('Посмотреть все вещи', callback_data='check'))

        bot.send_message(call.message.chat.id,
                         f'Название магазина: {Seller.get_seller_name(item.seller_id)}\nКонтакты:',
                         reply_markup=markup)

    if call.data == 'my_subs':
        for i in Buyer.get_subs(call.message.chat.id):
            Seller.get_seller_name(i)


bot.polling(none_stop=True)

