import os #for api address
import telebot #for the main bot
from replit import db #for database
key_api = os.environ['key_api'] #pulls the key from secrets

bot = telebot.TeleBot(key_api) #creats a bot linked with the api

@bot.message_handler(commands = ["greet"]) 
def greet(message):
  bot.reply_to(message, "Hello there!") #replies Hello there! when inputted /greet

def remember(message):
	request = message.text.split()
	if len(request) == 3 and request[0].lower() == 'remember':
		return(True)
	return(False) #checks if the syntax for remebering a message is correct

@bot.message_handler(func = remember)
def remeb(message):
  lst = message.text.split()
  db[lst[1]] = lst[2]
  bot.send_message(message.chat.id,"Gotcha!")
  print(db[lst[1]]) #saves the data in database and 


bot.polling()