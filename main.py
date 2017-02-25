# -*- coding: utf-8 -*- 
import telebot

import os
from flask import Flask, request

import config

bot = telebot.TeleBot(config.tocken)
server = Flask(__name__)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == u'Я крутой поц?':
        bot.send_message(message.chat.id, u'Ну да че!')
    else:
        bot.send_message(message.chat.id, message.text)


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    print(bot.get_me())
    bot.polling(none_stop=True)
