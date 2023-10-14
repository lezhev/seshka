import telebot
from telebot import types
from config import TOKEN_SELLER
from seshka_backend.seshka_lib import Item, Seller, Buyer

bot = telebot.TeleBot(TOKEN_SELLER)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Мои объявления', callback_data='test')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Создать объявление', callback_data='create')
    btn3 = types.InlineKeyboardButton('Удалить объявление', callback_data='remove')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('Уведомления', callback_data='test')
    btn5 = types.InlineKeyboardButton('Оплата', callback_data='test')
    markup.row(btn4, btn5)

    bot.send_message(message.chat.id, 'Привет, что вы хотите сделать?', reply_markup=markup)


item = Item(0, 0, 'qwer', 'tyui', 'asd', 0, {}, '123')
tag_dict = {'disco': 0, 'y2k': 0, 'boho': 0, 'vintage': 0, 't-shorts': 0, 'shoes': 0, 'jampers': 0, 'hoody': 0}
item_size = 0


@bot.callback_query_handler(func=lambda call: True)
def callback_create(call):
    if call.data == 'create':
        bot.send_message(call.message.chat.id, 'Укажите название вещи')
        bot.register_next_step_handler(call.message, set_title)
        bot.answer_callback_query(call.id)

    if call.data in ['xs', 's', 'm', 'l', 'xl']:
        item.size = call.data
        bot.answer_callback_query(call.id)

    if call.data == 'size_continue':

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('disco', callback_data='disco')
        btn2 = types.InlineKeyboardButton('boho', callback_data='boho')
        btn3 = types.InlineKeyboardButton('y2k', callback_data='y2k')
        btn4 = types.InlineKeyboardButton('vintage', callback_data='vintage')
        markup.row(btn1, btn2, btn3, btn4)
        btn5 = types.InlineKeyboardButton('styles_continue', callback_data='styles_continue')
        markup.row(btn5)
        bot.send_message(call.message.chat.id, 'Укажите теги по стилю', reply_markup=markup)

        bot.answer_callback_query(call.id)

    if call.data == 'styles_continue':

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('t-shorts', callback_data='t-shorts')
        btn2 = types.InlineKeyboardButton('shoes', callback_data='shoes')
        btn3 = types.InlineKeyboardButton('jampers', callback_data='jampers')
        btn4 = types.InlineKeyboardButton('hoody', callback_data='hoody')
        markup.row(btn1, btn2, btn3, btn4)
        btn5 = types.InlineKeyboardButton('type_continue', callback_data='type_continue')
        markup.row(btn5)
        bot.send_message(call.message.chat.id, 'Укажите теги по типу', reply_markup=markup)

        bot.answer_callback_query(call.id)

    if call.data == 'type_continue':

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Подтвердить', callback_data='test')
        btn2 = types.InlineKeyboardButton('Редактировать', callback_data='test')
        btn3 = types.InlineKeyboardButton('Отменить', callback_data='test')
        markup.row(btn1, btn2, btn3)

        bot.send_message(call.message.chat.id, 'отлично, вот ваше объявление')
        item.tags = tag_dict
        bot.send_message(call.message.chat.id, item.__str__(), reply_markup=markup, parse_mode='Markdown')

        bot.answer_callback_query(call.id)

    if call.data == 'remove':
        pass
        Seller.remove()

        #bot.answer_callback_query(call.id)

    if call.data in tag_dict:
        if tag_dict[call.data] == 0:
            tag_dict[call.data] = 1
        else:
            tag_dict[call.data] = 0
        print(tag_dict)
        bot.answer_callback_query(call.id)


@bot.message_handler(content_types=['text'])
def set_title(message):
    item.title = str(message.text)
    bot.send_message(message.chat.id, 'Теперь отправьте фото')
    bot.register_next_step_handler(message, set_photo)


@bot.message_handler(content_types=['photo'])
def set_photo(message):
    raw = str(message.photo[len(message.photo)-1].file_id)
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    item.photo = downloaded_file
    bot.send_message(message.chat.id, 'Укажите цену вещи')
    bot.register_next_step_handler(message, set_price)


@bot.message_handler(content_types=['text'])
def set_price(message):
    item.price = int(message.text)
    bot.send_message(message.chat.id, 'Опишите эту вещь')
    bot.register_next_step_handler(message, set_description)


@bot.message_handler(content_types=['text'])
def set_description(message):
    item.description = str(message.text)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('xs', callback_data='xs')
    btn2 = types.InlineKeyboardButton('s', callback_data='s')
    btn3 = types.InlineKeyboardButton('m', callback_data='m')
    btn4 = types.InlineKeyboardButton('l', callback_data='l')
    btn5 = types.InlineKeyboardButton('xl', callback_data='xl')
    btn6 = types.InlineKeyboardButton('size_continue', callback_data='size_continue')
    markup.row(btn1, btn2, btn3, btn4, btn5)
    markup.row(btn6)

    bot.send_message(message.chat.id, 'Укажите размер вещи', reply_markup=markup)


bot.polling(none_stop=True)

