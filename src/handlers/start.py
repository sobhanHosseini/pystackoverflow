from src.message import Message
from src.base.baseHandler import BaseHandler

class StartHandler(BaseHandler):
    def __init__(self, bot):
        self.bot = bot
        
    def handle(self, message):
        """
            /start command handler
        """
        a = Message(message.chat.id, self.bot)
        a.send(
            text='this message is test....',
            )
        
        # message.json['_id'] = message.chat.id
        # db.users.update_one(
        #     {'_id': message.chat.id}, 
        #     {"$set": message.json},
        #     upsert=True
        #     )
        # self.update_state(message.chat.id, self.states.main)


