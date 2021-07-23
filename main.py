import os
import telebot
key_api = os.environ['key_api']

bot = telebot.TeleBot(key_api)

@bot.message_handler(commands = ["greet"])
def greet(message):
  bot.reply_to(message, "Hello there!")

bot.polling()