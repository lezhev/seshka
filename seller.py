import telebot
from telebot import types
from config import TOKEN_SELLER
from seshka_backend.seshka_lib import Item, Seller

bot = telebot.TeleBot(TOKEN_SELLER)


@bot.message_handler()
def strt(message):
    start(message)


@bot.message_handler(commands=['start'])
def start(message):

    if Seller.get_seller_name(message.chat.id) == '':
        markup = types.InlineKeyboardMarkup()
        markup.row(types.InlineKeyboardButton('Да', callback_data='Y'),
                   types.InlineKeyboardButton('Нет', callback_data='N'))
        bot.send_message(message.chat.id, 'Здравствуйте, вы хотите зарегистрировать ваш магазин?', reply_markup=markup)
    else:
        action(message)


@bot.message_handler(commands=['action'])
def action(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Мои объявления', callback_data='my_ad')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Создать объявление', callback_data='create')
    btn3 = types.InlineKeyboardButton('Удалить объявление', callback_data='remove')
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup)
    # bot.register_next_step_handler(message, action)


item = Item('name', 'photo', 0, 'description', 'size', {}, 0)
tag_dict = {'Диско': 0, 'Бохо': 0, 'Y2K': 0, 'Винтаж': 0, 'Футболки': 0, 'Куртки': 0, 'Платья': 0, 'Юбки': 0}


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'my_ad':
        item_list, id_list = Seller.get_seller_items(call.message.chat.id)
        count = 0
        for items in item_list:
            try:
                bot.send_photo(call.message.chat.id, items.photo, items.__str__() + '\n' + Seller.get_seller_link(call.message.chat.id), parse_mode='Markdown')
            except telebot.apihelper.ApiTelegramException:
                continue
            count += 1
        bot.edit_message_text('text', call.message.chat.id, call.message.message_id-count)
        action(call.message)

    if call.data == 'Y':
        bot.edit_message_text('Здравствуйте, вы хотите зарегистрировать ваш магазин?',
                              call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да', callback_data='Yes'))
        markup.add(types.InlineKeyboardButton('Нет', callback_data='No'))
        bot.send_message(call.message.chat.id,
                         'Хорошо, вот список наших условий\n ....\n Вы с ними согласны?',
                         reply_markup=markup)
        bot.answer_callback_query(call.id)

    if call.data == 'Yes':
        bot.edit_message_text('Хорошо, вот список наших условий\n ....\n Вы с ними согласны?',
                              call.message.chat.id, call.message.message_id)

        bot.send_message(call.message.chat.id, 'Как вы будете называться?')

        bot.register_next_step_handler(call.message, set_name_of_seller)

    if call.data == 'N':
        bot.send_message(call.message.chat.id, 'Очень жаль, но вы всегда можете вернуться, написав "/start"')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.answer_callback_query(call.id)

    if call.data == 'No':
        bot.send_message(call.message.chat.id, 'Очень жаль, но вы всегда можете вернуться, написав "/start"')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id-1)
        bot.answer_callback_query(call.id)

    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'Как вы будете называться?')
        bot.register_next_step_handler(call.message, set_name_of_seller)

    if call.data == 'no_link':
        bot.send_message(call.message.chat.id, 'Введите вашу ссылку')
        bot.register_next_step_handler(call.message, set_link_of_seller)

    if call.data == 'yes':

        bot.edit_message_text('Теперь это ваше название',
                              call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите *ссылку* на ваш магазин', parse_mode='Markdown')
        bot.register_next_step_handler(call.message, set_link_of_seller)

    if call.data == 'yes_link':

        bot.edit_message_text('Теперь это ваша ссылка',
                              call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Вы успешно зарегистрировались')
        action(call.message)

    if call.data == 'create':
        bot.edit_message_text('СОЗДАЁМ ОБЪЯВЛЕНИЕ',
                              call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Укажите название вещи')
        bot.register_next_step_handler(call.message, set_title)
        bot.answer_callback_query(call.id)

    if call.data in ['xs', 's', 'm', 'l', 'xl']:
        item.it_size = call.data
        bot.answer_callback_query(call.id)

    if call.data == 'size_continue':
        if item.it_size != 'size':
            bot.edit_message_text(f'Укажите размер вещи: {item.it_size.upper()}', call.message.chat.id, call.message.message_id)

            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Диско', callback_data='Диско')
            btn2 = types.InlineKeyboardButton('Бохо', callback_data='Бохо')
            btn3 = types.InlineKeyboardButton('Y2K', callback_data='Y2K')
            btn4 = types.InlineKeyboardButton('Винтаж', callback_data='Винтаж')
            markup.row(btn1, btn2, btn3, btn4)
            btn5 = types.InlineKeyboardButton('Продолжить', callback_data='styles_continue')
            markup.row(btn5)
            bot.send_message(call.message.chat.id, 'Укажите теги по стилю', reply_markup=markup)

            bot.answer_callback_query(call.id)

    if call.data == 'styles_continue':

        bot.edit_message_text(f'Укажите теги по стилю', call.message.chat.id, call.message.message_id)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Футболки', callback_data='Футболки')
        btn2 = types.InlineKeyboardButton('Куртки', callback_data='Куртки')
        btn3 = types.InlineKeyboardButton('Платья', callback_data='Платья')
        btn4 = types.InlineKeyboardButton('Юбки', callback_data='Юбки')
        markup.row(btn1, btn2, btn3, btn4)
        btn5 = types.InlineKeyboardButton('Продолжить', callback_data='type_continue')
        markup.row(btn5)
        bot.send_message(call.message.chat.id, 'Укажите теги по типу', reply_markup=markup)

        bot.answer_callback_query(call.id)

    if call.data == 'type_continue':

        bot.edit_message_text(f'Укажите теги по типу', call.message.chat.id, call.message.message_id)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Подтвердить', callback_data='accept')
        btn2 = types.InlineKeyboardButton('Отменить', callback_data='cancel')
        markup.row(btn1, btn2)

        bot.send_message(call.message.chat.id, 'отлично, вот ваше объявление')
        item.tags = tag_dict
        bot.send_photo(call.message.chat.id, item.photo, item.__str__(), reply_markup=markup, parse_mode='Markdown')

        bot.answer_callback_query(call.id)

    if call.data == 'accept':
        item.seller_id = call.message.chat.id
        Seller.set_item(call.message.chat.id, item)
        Seller.print_database()
        bot.send_message(call.message.chat.id, 'записано')
        action(call.message)

    if call.data == 'cancel':

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton('Нет, подтвердить сохранение', callback_data='accept'))
        markup.add(types.InlineKeyboardButton('Отменить', callback_data='delete'))

        bot.send_message(call.message.chat.id, 'Точно отменить?', reply_markup=markup)

    if call.data == 'delete':
        for i in range(8):
            bot.delete_message(call.message.chat.id, call.message.message_id-i)
        action(call.message)

    if call.data in tag_dict:
        if tag_dict[call.data] == 0:
            tag_dict[call.data] = 1
        else:
            tag_dict[call.data] = 0
        print(tag_dict)
        bot.answer_callback_query(call.id)

    if call.data == 'remove':
        item_list, id_list = Seller.get_seller_items(call.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Удалить', callback_data='del'))
        for items in item_list:

            bot.send_photo(call.message.chat.id, items.photo, items.__str__(), parse_mode='Markdown', reply_markup='markup')

    if call.data == 'del':
        item_list, id_list = Seller.get_seller_items(call.message.chat.id)

@bot.message_handler()
def set_link_of_seller(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes_link'),
               types.InlineKeyboardButton('Нет', callback_data='no_link'))
    Seller.set_seller_link(message.chat.id, str(message.text))
    bot.send_message(message.chat.id,
                     f'Это ваша ссылка?\n<b>{str(message.text)}</b>',
                     parse_mode='html',
                     reply_markup=markup)

@bot.message_handler()
def set_name_of_seller(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes'),
               types.InlineKeyboardButton('Нет', callback_data='no'))
    Seller.set_seller_name(message.chat.id, str(message.text), 'link')
    bot.send_message(message.chat.id,
                     f'Это ваше название?\n<b>{str(message.text)}</b>',
                     parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def set_title(message):
    item.title = str(message.text)
    bot.send_message(message.chat.id, 'Теперь отправьте фото')
    bot.register_next_step_handler(message, set_photo)


@bot.message_handler()
def set_photo(message):
    try:
        bot.get_file(message.photo[len(message.photo)-1].file_id)
    except TypeError:
        bot.send_message(message.chat.id, 'Неверный  формат, попробуйте снова')
        bot.register_next_step_handler(message, set_photo)
        return

    raw = str(message.photo[-1].file_id)
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    item.photo = downloaded_file
    bot.send_message(message.chat.id, 'Укажите цену вещи')
    bot.register_next_step_handler(message, set_price)


@bot.message_handler(content_types=['text'])
def set_price(message):
    try:
        float(message.text)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный  формат, попробуйте снова')
        bot.register_next_step_handler(message, set_price)
        return

    item.price = float(message.text)
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
    btn6 = types.InlineKeyboardButton('Продолжить', callback_data='size_continue')
    markup.row(btn1, btn2, btn3, btn4, btn5)
    markup.row(btn6)

    bot.send_message(message.chat.id, 'Укажите размер вещи', reply_markup=markup)


bot.polling(none_stop=True)

