from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware
from src.user import User

class UserMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']
    
    def pre_process(self, message, data):
        chat_id = message.chat.id
        user = User(chat_id)
        data['user'] = user
        
    def post_process(self, message, data, exception=None):
        if exception: 
            print(exception)