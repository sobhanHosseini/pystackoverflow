from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware

class UserMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']
    
    def pre_process(self, message, data):
        print(message)
        print('-'*50)
        print(data)
        
    def post_process(self, message, data, exception=None):
        print('in post process....')