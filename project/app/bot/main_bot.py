from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
import os
import telebot
import webbrowser
import os
from dotenv import load_dotenv, find_dotenv
from telebot import types
load_dotenv(find_dotenv())

# bot = AsyncTeleBot(settings.TELEGRAM_TOKEN, parse_mode='HTML')

bot = AsyncTeleBot(settings.TELEGRAM_TOKEN, parse_mode='HTML')

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)




# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('MrBeast')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('удалить')
#     btn3 = types.KeyboardButton('edit')
#     markup.add(btn3,btn2)
#     file = open('./tgbot/test.jpg', 'rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)

# def on_click(message):
#     if message.text == 'MrBeast':
#         bot.send_message(message.chat.id, 'MrBeast GO') 
#     elif message.text == 'удалить':
#         bot.send_message(message.chat.id, 'deleted text') 


# bot.polling(none_stop=True)