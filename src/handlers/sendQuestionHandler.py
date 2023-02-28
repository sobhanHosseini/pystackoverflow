from src.base.baseHandler import BaseHandler
from src.message import Message
from src.models.question import Question


class SendQuestionHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        message_sender = data['message_sender']
        question = Question(user=user, message_sender=message_sender)
        
        question.save_question()
        message_sender.send(
            text=':check_mark_button: Question saved successfully.',
            reply_markup=self.keyboards.main
            )
        message_sender.send_question_to_all()
        user.reset()
        
