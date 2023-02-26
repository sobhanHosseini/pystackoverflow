from src.base.baseHandler import BaseHandler
from src.data import DATA_DIR
from src.message import Message
from src.utils.io import read_file


class AskQuestionHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        msg = Message(data['chat_id'], self.bot)
        msg.send(
            text=read_file(DATA_DIR / 'guide.html'),
            reply_markup=BaseHandler.keyboards.ask_question
            )
        
        user.update_state(BaseHandler.states.ask_question)