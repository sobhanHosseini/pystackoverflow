import emoji
from loguru import logger
from telebot import custom_filters

from src.bot import bot
from src.dataClass import keyboards as kb
from src.dataClass import keys, states
from src.db import db
from src.filters import IsAdmin


class Bot:
    """
    stack overflow telegram bot
    """
    def __init__(self, telebot, mongodb):
        self.bot = telebot
        self.db = mongodb

        # init data class
        self.keys = keys.Keys()
        self.keyboards = kb.Keyboards()
        self.states = states.States()
        
        # add custom filters
        self.bot.add_custom_filter(IsAdmin())
        self.bot.add_custom_filter(custom_filters.TextMatchFilter())
        self.bot.add_custom_filter(custom_filters.TextStartsFilter())

        # register handlers
        self.handlers()

        # run bot
        logger.info('Bot is running...')
        self.bot.infinity_polling()

    def handlers(self):
        @self.bot.message_handler(commands=['start'])    
        def start(message):
            """
             /start command handler
            """
            self.send_message(
                message.chat.id, 
                f'Hey <strong>{message.chat.first_name}</strong>',
                reply_markup=self.keyboards.main,
                )
           
            message.json['_id'] = message.chat.id
            db.users.update_one(
                {'_id': message.chat.id}, 
                {"$set": message.json},
                upsert=True
                )
            self.update_state(message.chat.id, self.states.main)
            
        @self.bot.message_handler(text=[self.keys.exit])
        def exit(message):
            pass

        @self.bot.message_handler(text=[self.keys.settings])
        def settings(message):
            pass

        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, '<strong>You are admin of this group!</strong>')

        @self.bot.message_handler(func=lambda ـ: True)
        def echo(message):
            self.send_message(
                message.chat.id, message.text,
                reply_markup=self.keyboards.main
            )

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text, use_aliases=True)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
    
    def update_state(self, chat_id, state):
        """
        Update user state.
        """
        db.users.update_one(
            {'_id': chat_id}, 
            {'$set':{'state':state}}
            )


if __name__ == '__main__':
    logger.info('Bot started')
    nashenas_bot = Bot(telebot=bot, mongodb=db)
    nashenas_bot.run()
