import telebot

import config

bot = telebot.TeleBot(config.tocken)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == 'Я клевый поц?':
        bot.send_message(message.chat.id, 'Да!')
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)