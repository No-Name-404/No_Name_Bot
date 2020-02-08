#! /usr/bin/python3
import telebot
from telebot import types
from db import db
from SERVICES import No_Name ,BotSystem

# Input user...
TOKEN = 'Token...'
No_Name.NameGroup = '< No_Name >'
No_Name.UrlGroup = 'https://t.me/joinchat/AAAAAFBqSAHafemT3Twrkg'
#------------------------------

# bot system...
bot = telebot.TeleBot(token=TOKEN)
tb = telebot.AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    No_Name.start_command(None,bot,message)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    No_Name.start_command(call,bot,None).Call()

@bot.message_handler(func=lambda m: True)
def Read_messages(message):
    No_Name.Services(bot,message) # SERVICES class...
#------------------------------

# to run...
BotSystem.start(bot)
#------------------------------
