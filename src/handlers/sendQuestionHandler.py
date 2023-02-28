from src.base.baseHandler import BaseHandler
from src.models.question import Question
from src.utils.message import Message


class SendQuestionHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        message_sender = data['message_sender']
        question = Question(user=user, message_sender=message_sender)
        
        if not user.user.get('current_question'):
            return message_sender.send_message(
                chat_id=user.user['_id'],
                text=':cross_mark: Question is empty'
                )
            
        question.save_question()
        message_sender.send_message(
            text=':check_mark_button: Question saved successfully.',
            reply_markup=self.keyboards.main
            )
        question.send_question_to_all()
        user.reset()
        
