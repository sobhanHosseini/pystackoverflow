import os

import telebot
from telebot import apihelper

# apihelper.ENABLE_MIDDLEWARE = True

bot = telebot.TeleBot(
    os.environ['TELEGRAM_BOT_TOKEN'],
    parse_mode='HTML',
    use_class_middlewares=True
    )   
