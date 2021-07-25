import os  #for api address
import telebot  #for the main bot
from replit import db  #for database
import time

key_api = os.environ['key_api']  #pulls the key from secrets

bot = telebot.TeleBot(key_api)  #creats a bot linked with the api


@bot.message_handler(commands=["greet"])
def greet(message):
    bot.reply_to(message,"Hello there!")  #replies Hello there! when inputted /greet


def remember(message):
	request = message.text.split()
	if len(request) == 3 and request[0].lower() == 'remember':
			return (True)
	return (False)  #checks if the syntax for remebering a message is correct


@bot.message_handler(func=remember)
def remeb(message):
	lst = message.text.split()
	db[lst[1]] = lst[2]
	bot.send_message(message.chat.id, "Gotcha!")
	print(db[lst[1]])  #saves the data in database and replies Gotcha! to the user

def remind(message) :
  request = message.text.split()
  if len(request)== 2 and request[0].lower() == "remind": 
    return(True)
  return(False)  #checks if the syntax for reminding a message is correct

@bot.message_handler(func= remind)
def remi(message):
  lst = message.text.split()
  val = db[lst[1]]
  bot.send_message(message.chat.id,val)
  print(val)   #extracts the data from the database and replies it to the user

@bot.message_handler(commands=['remind'])
def remindall(message):
	keys = db.keys()
	for i in keys:
		bot.send_message(message.chat.id,i)   #returns all the keys remembered by the database

while True: #Keeps the bot from becoming inactive time to time
  try:
    bot.polling()
  except Exception:
    time.sleep(5)

