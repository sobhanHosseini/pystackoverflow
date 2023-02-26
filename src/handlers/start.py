from src.decorators.bot_handler import bot_handler


class StartHandler:
    def __init__(self, bot):
        self.bot = bot
        
    @bot_handler(commands=['start'])    
    def handle(message):
        """
            /start command handler
        """
        a = Message(message.chat.id, self.bot)
        a.send(
            message.chat.id, 
            # f'Hey <strong>{message.chat.first_name}</strong>',
            'this message is test....',
            # reply_markup=self.keyboards.main,
            )
        
        # message.json['_id'] = message.chat.id
        # db.users.update_one(
        #     {'_id': message.chat.id}, 
        #     {"$set": message.json},
        #     upsert=True
        #     )
        # self.update_state(message.chat.id, self.states.main)


