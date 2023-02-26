import emoji
from loguru import logger
from telebot import custom_filters

from src.bot import bot
from src.data import DATA_DIR
from src.dataClass import keyboards as kb
from src.dataClass import keys, states
from src.db import db
from src.filters import IsAdmin
from src.user import User
from src.utils.io import read_file


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
      
    ####################test###########################  
    def test(callback_query):
        message = callback_query.message
        print(message)
        
    bot.middleware_handler(test)
    ###############################################
    
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
        
        @self.bot.message_handler(regexp=emoji.emojize(self.keys.ask_question))
        def ask_question(message):
            self.send_message_update_state(
                chat_id=message.chat.id,
                text=read_file(DATA_DIR / 'guide.html'),
                state=self.states.ask_question,
                reply_markup=self.keyboards.ask_question
                )
            
        @self.bot.message_handler(regexp=emoji.emojize(self.keys.cancel))
        def cancel(message):
            user = User(chat_id=message.chat.id)
            user.reset_current_question()
            self.send_message_update_state(
                chat_id=message.chat.id,
                text=':cross_mark: Canceld.',
                state=self.states.main,
                reply_markup=self.keyboards.main
                )

        @self.bot.message_handler(regexp=emoji.emojize(self.keys.settings))
        def settings(message):
            pass
        
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, '<strong>You are admin of this group!</strong>')

        @self.bot.message_handler(func=lambda ـ: True)
        def echo(message):
            user = User(chat_id=message.chat.id)
            
            if user.state == self.states.ask_question:
                self.db.users.update_one(
                    {'_id': message.chat.id},
                    {'$push': {'current_question': message.text}}
                )

                self.send_message(
                    chat_id=message.chat.id,
                    text=user.current_question()
                    ) 

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
    
    def update_state(self, chat_id, state):
        """
        Update user state.
        """
        db.users.update_one(
            {'_id': chat_id}, 
            {'$set':{'state':state}}
            )

    def send_message_update_state(self, chat_id, text, state,reply_markup=None):
        """
        send message and change state of user
        """
        self.send_message(
                chat_id,
                text,
                reply_markup=reply_markup
                )
        self.update_state(chat_id, state)
        

if __name__ == '__main__':
    logger.info('Bot started')
    nashenas_bot = Bot(telebot=bot, mongodb=db)
    nashenas_bot.run()
