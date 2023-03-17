from loguru import logger

from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from src.models.question import Question
from src.models.callback_data import CallbackData

class BackCallBackHandler(BaseCallbackQueryHandler):
    def __init__(self, bot):
        self.bot = bot
    
    def handle(self, call, data):
        user = data['user']
        message_sender = data['message_sender']
        callback_data = CallbackData(call.message.chat.id, call.message.message_id)
        question_id = callback_data.get_call_info()['question_id']
        question = Question(user=user, message_sender=message_sender, question_id=question_id)
        
        message_sender.answer_callback_query(call.id, text=call.data)
        message_sender.edit_message(call.message.message_id, reply_markup=question.get_keyboard())
        