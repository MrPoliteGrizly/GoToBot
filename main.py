# -*- coding: utf-8 -*- 
import telebot

import config

bot = telebot.TeleBot(config.tocken)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == 'Я крутой поц?':
        bot.send_message(message.chat.id, 'Ну да че!')
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    print(bot.get_me())
    bot.polling(none_stop=True)
