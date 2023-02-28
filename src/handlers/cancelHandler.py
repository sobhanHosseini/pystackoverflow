from src.base.baseHandler import BaseHandler
from src.utils.message import Message


class CancelHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        """
        click on cancled
        """
        user = data['user']
        message_sender = data['message_sender']
         
        message_sender.send(
            text=':cross_mark: Canceled.',
            reply_markup=self.keyboards.main
            )
        user.reset()
