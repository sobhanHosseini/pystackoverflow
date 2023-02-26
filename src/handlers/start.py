from src.decorators.bot_handler import bot_handler
from src.bot import bot


@bot_handler(commands=['start'])    
def start(message):
    """
        /start command handler
    """
    send_message(
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

def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text)

        bot.send_message(chat_id, text, reply_markup=reply_markup)