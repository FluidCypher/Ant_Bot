import os
import telebot
from replit import db
key_api = os.environ['key_api']

bot = telebot.TeleBot(key_api)

@bot.message_handler(commands = ["greet"])
def greet(message):
  bot.reply_to(message, "Hello there!")

def remember(message):
	request = message.text.split()
	if len(request) == 3 and request[0].lower() == 'remember':
		return(True)
	return(False)

@bot.message_handler(func = remember)
def remeb(message):
  lst = message.text.split()
  db[lst[1]] = lst[2]
  bot.send_message(message.chat.id,"Gotcha!")
  print(db[lst[1]])


bot.polling()