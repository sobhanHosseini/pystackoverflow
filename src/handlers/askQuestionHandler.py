from src.base.baseHandler import BaseHandler
from src.data import DATA_DIR
from src.utils.message import Message
from src.utils.io import read_file


class AskQuestionHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        message_sender = data['message_sender']
        
        message_sender.send(
            text=read_file(DATA_DIR / 'guide.html'),
            reply_markup=self.keyboards.ask_question
            )
        
        user.update_state(self.states.ask_question)
