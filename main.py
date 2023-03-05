from telebot import types
import telebot

token = '5977967248:AAFF7fcGDPVfG_qNROS_1CGJ-SbWtV8F0wQ'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message_and_menu(message) :
    bot.send_message(message.chat.id, f'[STATUS]: On', parse_mode='html')

@bot.message_handler(content_types=['text'])
def function(message) :

    #user information for adm
    if (message.text == "/info") :
        bot.send_message(message.chat.id, message)

#EOF
bot.polling(none_stop=True)
