# Gay
import telebot
from telebot import types

bot = telebot.TeleBot('6147823845:AAGDw9rj2fS-5p8WhRIAlNuLxanXT_dyKrc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'program starting')


name = 'Капибара'
energy = 100
happiness = 100

# кормление питомца
def feed():
    global energy
    energy += 5

# игры с питомцем
def play():
    global energy, happiness
    energy -= 10
    happiness += 10

def sleep():
    global energy
    energy += 50

def Show():
    global energy, happiness


# def nothing():
#     global happiness
#     happiness -= 10

@bot.message_handler(commands=['main'])
def com_main(message):
   markup = types.ReplyKeyboardMarkup(row_width=3)
   button1 = types.KeyboardButton('Покормить')
   button2 = types.KeyboardButton('Поиграть')
   button3 = types.KeyboardButton('Поспать')
   markup.add(button1, button2, button3)
   bot.send_message(message.chat.id, text='Выберите действие', reply_markup=markup)

@bot.message_handler(func=lambda x: True)
def work(message):

    if message.text == 'Поиграть':
        play()
        bot.send_message(message.chat.id, 'Питомец поиграл')
    elif message.text == 'Поспать':
        sleep()
        bot.send_message(message.chat.id, 'Питомец поспал')
    elif message.text == 'Покормить':
        feed()
        bot.send_message(message.chat.id, 'Питомец накормлен')


bot.polling(none_stop=True)
