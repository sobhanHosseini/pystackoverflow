from src.base.baseHandler import BaseHandler
from src.message import Message


class EchoHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        msg = Message(data['chat_id'], self.bot)
        
        if user.state == self.states.ask_question:
            user.update(values={'$push': {'current_question': message.text}})
            msg.send(
                text=user.current_question
            )
        
        
        
