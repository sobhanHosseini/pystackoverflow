from src.base.baseHandler import BaseHandler
from src.utils.message import Message


class StartHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        """
            /start command handler
        """
        user = data['user']
        message_sender = data['message_sender']
        
        message_sender.send_message(
            text=f'Hey <strong>{message.chat.first_name}</strong>',
            reply_markup=self.keyboards.main
            )
        
        message.json['_id'] = data['chat_id']
        user.update(values={"$set": message.json})
        user.reset()
