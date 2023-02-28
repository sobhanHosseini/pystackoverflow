from src.base.baseHandler import BaseHandler
from src.message import Message
from src.models.question import Question


class SendQuestionHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        msg = Message(data['chat_id'], self.bot)
        question = Question(user=user, message_sender=msg)
        
        question.save_question()
        msg.send(
            text=':check_mark_button: Question saved successfully.',
            reply_markup=self.keyboards.main
            )
        msg.send_question_to_all()
        user.reset()
        
