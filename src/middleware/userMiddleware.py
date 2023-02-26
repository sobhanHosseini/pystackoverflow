from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware

class UserMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']
    
    def pre_process(self, message, data):
        print('in pre process')
        
    def post_process(self, message, data, exception=None):
        print('in post process....')