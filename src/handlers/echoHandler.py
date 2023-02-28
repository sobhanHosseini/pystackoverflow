from src.base.baseHandler import BaseHandler
from src.utils.message import Message


class EchoHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message, data):
        user = data['user']
        message_sender = data['message_sender']
         
        if user.state == self.states.ask_question:
            user.update(values={'$push': {'current_question': message.text}})
            message_sender.send_message(
                text=user.current_question
            )
        
        
        
