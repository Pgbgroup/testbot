import time
import json
import telebot
#Pgbgroup

#Pgbgroup


BOT_TOKEN = "6513778975:AAGjY6lyWKjAb32Izi7qhyn6gD7looUR9wo"


bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
   try:
    user = message.chat.id
    msg = message.text
    if msg == '/start':

        bot.send_message(user,"Hi")
if __name__ == '__main__':
    bot.polling(none_stop=True)
