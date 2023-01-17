import telebot
from Keys import API

bot = telebot.TeleBot(API)


@bot.message_handler(commands=["start"])
def help (message):
    name= message.chat.first_name
    bot.send_message(message.chat.id,"Hello" + name)
    bot.send_message(message.chat.id,"select /Information  or select /register")
    bot.send_message(message.chat.id,"select /about or select /Help")


@bot.message_handler(commands=["about"])
def send_help_message(msg):
    bot.reply_to(msg, "We keep you updated with the latest car  and share update with user from olx , facebook etc.  !")
    
@bot.message_handler(commands=["Information"])
def send_help_message(msg):
    bot.reply_to(msg, "We keep you updated with the latest car  and share update with user from olx , facebook etc.  !")

@bot.message_handler(commands=["about"])
def send_help_message(msg):
    bot.reply_to(msg, "We keep you updated with the latest car  and share update with user from olx , facebook etc.  !")


print("Telegrame Bot started...")

bot.polling()
