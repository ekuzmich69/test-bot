import telebot
import parser

from telebot import types
bot = telebot.TeleBot('5685641148:AAFHK9pktmJ-WIu95uvm4LqXHEP9-qRkxBE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('/Расписание')
    button2 = types.KeyboardButton('/ДЗ')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Привет, это <b>демо-версия</b> бота', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['Расписание'])
def but1(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but11 = types.KeyboardButton('пн')
    but22 = types.KeyboardButton('вт')
    but3 = types.KeyboardButton('ср')
    but4 = types.KeyboardButton('чт')
    but5 = types.KeyboardButton('пт')
    but6 = types.KeyboardButton('сб')
    but7 = types.KeyboardButton('/back')
    markup1.add(but11, but22, but3, but4, but5, but6, but7)
    bot.send_message(message.chat.id, 'Расписанием на какой день интересуешься? (кнопка /back - на главный экран)',
                     reply_markup=markup1)


@bot.message_handler(commands=['ДЗ'])
def but2(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but11 = types.KeyboardButton('Теор. Вер.')
    but22 = types.KeyboardButton('Мат. Анализ')
    but3 = types.KeyboardButton('Дифф. Уравнения')
    but4 = types.KeyboardButton('Электричество')
    but5 = types.KeyboardButton('/back')
    markup1.add(but11, but22, but3, but4, but5)
    bot.send_message(message.chat.id, 'Какое д/з нужно? (кнопка /back - на главный экран)', reply_markup=markup1)


@bot.message_handler(commands=['back'])
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('/Расписание')
    button2 = types.KeyboardButton('/ДЗ')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, 'Добро пожаловать обратно на главный экран(:',
                     parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
