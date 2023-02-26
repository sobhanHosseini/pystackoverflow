from src.decorators.bot_handler import bot_handler
from src.message import Message

class StartHandler:
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


