from src.base.baseHandler import BaseHandler
from src.message import Message


class StartHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        """
            /start command handler
        """
        user = data['user']
        msg = Message(data['chat_id'], self.bot)
        msg.send(
            text=f'Hey <strong>{message.chat.first_name}</strong>',
            reply_markup=keyboards.main
            )
        
        message.json['_id'] = data['chat_id']
        user.update(values={"$set": message.json})
        user.update_state(states.main)
