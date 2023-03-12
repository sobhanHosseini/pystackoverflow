import json

from src.base.baseHandler import BaseHandler
from src.models.question import Question
from src.utils.common import json_encoder
from src.utils.message import Message


class EchoHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        message_sender = data['message_sender']


        if user.state == self.states.ask_question:
            question = Question(user=user, message_sender=message_sender)
            
            question.update(message)
            
            message_sender.send_message(
                text=question.get_text(),
                reply_markup=question.get_keyboard()
            )

        
        
        
