import emoji
from loguru import logger
from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware

from src.bot import bot
from src.models.user import User
from src.utils.message import Message


class UserMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']
    
    def pre_process(self, message, data):
        chat_id = message.chat.id
        msg = Message(
            chat_id=chat_id,
            bot=bot,
            message_info=message
            )
        user = User(chat_id=chat_id)
        
        data['user'] = user
        data['message_sender'] = msg
        data['chat_id'] = chat_id
        message.text = emoji.demojize(message.text)
        
    def post_process(self, message, data, exception=None):
        if exception: 
            logger.error('In userMiddleware exception...')
            print(exception)