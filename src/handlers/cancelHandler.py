from src.base.baseHandler import BaseHandler
from src.message import Message


class CancelHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        """
        click on cancled
        """
        user = data['user']
        msg = Message(data['chat_id'], self.bot)
        msg.send(
            text=':cross_mark: Canceled.',
            reply_markup=self.keyboards.main
            )
        user.update_state(self.states.main)
        user.reset_current_question()
