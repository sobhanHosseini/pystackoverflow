from src.base.baseHandler import BaseHandler
from src.utils.message import Message
from src.models.question import Question


class CancelHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        """
        click on cancled
        """
        user = data['user']
        message_sender = data['message_sender']
        question = Question(user=user, message_sender=message_sender)
        
        message_sender.send_message(
            text=':cross_mark: Canceled.',
            reply_markup=self.keyboards.main
            )
        
        question.reset_question()
        user.reset()
