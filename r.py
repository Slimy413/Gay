import telebot
from telebot import types

bot = telebot.TeleBot('6147823845:AAGDw9rj2fS-5p8WhRIAlNuLxanXT_dyKrc')

@bot.message_handler(content_types = ['start'])
def f1(message):
    bot.send_message(message.text, 'Привет я калькулятор назови первое число')
    k = 0
    first = message.text
    if first in '1234567890':
        k = int(f1)
        bot.register_next_step_handler(message, f3, k)

@bot.message_handler(content_types = ['f2'])
def f2(message):
    t = 0
    second = message.text
    if second in '1234567890':
        k = int(f2)
        bot.register_next_step_handler(message, f3, t)

@bot.message_handler(commands=['main'])
def com_main(message):
   markup = types.ReplyKeyboardMarkup(row_width=4)
   button1 = types.KeyboardButton('умножить')
   button2 = types.KeyboardButton('делить')
   button3 = types.KeyboardButton('сложить')
   button4 = types.KeyboardButton('вычесть')
   markup.add(button1, button2, button3, button4)
   bot.send_message(message.chat.id, text='Выберите действие', reply_markup=markup)

@bot.message_handler(func=lambda x: True)
def f3(message):

    if message.text == 'умножить':
        bot.send_message.text('k * t')
    elif message.text == 'делить':
        bot.send_message.text('k / t')
    elif message.text == 'сложить':
        bot.send_message.text('k + t')
    elif message.text == 'вычесть':
        bot.send_message.text('k - t')

bot.polling(none_stop=True)
