import json

from src.base.baseHandler import BaseHandler
from src.models.question import Question


class EchoHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        message_sender = data['message_sender']


        if user.state == self.states.ask_question:
            question = Question(user=user, message_sender=message_sender)
            
            question_id = question.update(message)
            message_sender.send_message(
                text=question.get_text(),
                reply_markup=question.get_keyboard(),
                question_id=question_id 
            )

        
        
        
