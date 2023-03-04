from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from loguru import logger

class LikeCallBackHandler(BaseCallbackQueryHandler):
    def __init__(self, bot):
        self.bot = bot
    
    def handle(self, call, data):
        user = data['user']
        message_sender = data['message_sender']
        
        message_sender.answer_callback_query(call.id, text=call.data)
        