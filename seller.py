import telebot
from telebot import types

bot = telebot.TeleBot('6506191359:AAE-NC1rl4CwZMGQ3TaZasB73PU5uS53_Vc')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Мои объявления', callback_data='test')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Создать объявление', callback_data='create')
    btn3 = types.InlineKeyboardButton('Удалить объявление', callback_data='test')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('Уведомления', callback_data='test')
    btn5 = types.InlineKeyboardButton('Оплата', callback_data='test')
    markup.row(btn4, btn5)

    bot.send_message(message.chat.id, 'Привет, что вы хотите сделать?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_create(call):
    if call.data == 'create':
        bot.send_message(call.message.chat.id, 'Укажите название вещи')
        bot.register_next_step_handler(call.chat.message, set_name)


@bot.message_handler(content_types=['text'])
def set_name(message):
    # нужна функция set_name
    bot.send_message(message.chat.id, 'Теперь отправьте фото')
    bot.register_next_step_handler(message, set_photo)


@bot.message_handler(content_types=['photo'])
def set_photo(message):
    photo = message.photo[len(message.photo)-1]
    # нужна функция set_photo
    bot.send_message(message.chat.id, 'Укажите цену вещи')
    bot.register_next_step_handler(message, set_price)


@bot.message_handler(content_types=['text'])
def set_price(message):
    # нужна функция set_price
    bot.send_message(message.chat.id, 'Опишите эту вещь')
    bot.register_next_step_handler(message, set_description)


@bot.message_handler(content_types=['text'])
def set_description(message):
    # нужна функция set_description
    bot.send_message(message.chat.id, 'Укажите размер вещи')
    bot.register_next_step_handler(message, set_size)


@bot.message_handler(content_types=['text'])
def set_size(message):
    bot.send_message(message.chat.id, 'Укажите теги по типу')
    bot.register_next_step_handler(message, set_type_tags)


@bot.message_handler(content_types=['text'])
def set_type_tags(message):
    bot.send_message(message.chat.id, 'Укажите теги по стилю')
    bot.register_next_step_handler(message, set_style_tags)


@bot.message_handler(content_types=['text'])
def set_style_tags(message):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Подтвердить', callback_data='test')
    btn2 = types.InlineKeyboardButton('Редактировать', callback_data='test')
    btn3 = types.InlineKeyboardButton('Отменить', callback_data='test')
    markup.row(btn1, btn2, btn3)

    bot.send_message(message.chat.id, 'отлично, вот ваше объявление', reply_markup=markup)
    # нужна функция get_item


bot.polling(none_stop=True)

