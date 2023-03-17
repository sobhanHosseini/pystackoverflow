import time

from telebot import types

from db import db
from src.dataClass import keys


class CallbackData:
    def __init__(self, chat_id: int, message_id: int, question_id=None):
        self.chat_id = chat_id
        self.message_id = message_id
        self.question_id = question_id
    
    def update(self, reply_markup):
        if not ((reply_markup and isinstance(reply_markup, types.InlineKeyboardMarkup))):
            return
        
        buttons = []
        #TODO add reply markau to db
        
        db.callback_data.update_one(
            {
                'chat_id': self.chat_id,
                'message_id': self.message_id,
                'question_id': self.question_id
            },
            {
                '$set':{
                    'buttons': None,
                    'created_at': time.time()
                }
            },
            upsert=True
        )

    def get_call_info(self):
        return db.callback_data.find_one({'chat_id': self.chat_id, 'message_id': self.message_id})
        
    
   