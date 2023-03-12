from loguru import logger

from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from src.models.question import Question


class BackCallBackHandler(BaseCallbackQueryHandler):
    def __init__(self, bot):
        self.bot = bot
    
    def handle(self, call, data):
        user = data['user']
        message_sender = data['message_sender']
        question = Question(user=user, message_sender=message_sender)
        
        message_sender.answer_callback_query(call.id, text=call.data)
        message_sender.edit_message(call.message.message_id, reply_markup=question.get_keyboard())
        