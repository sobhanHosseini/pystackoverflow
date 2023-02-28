from typing import List

from loguru import logger

from interfaces import IMessageSender
from src.dataClass import keys, states
from src.db import db


class User:
    def __init__(self, chat_id: int):
        self.db = db
        self.chat_id = chat_id
        ## check it later
        self.message = message
    
    @property
    def user(self):
        return self.db.users.find_one({'_id': self.chat_id})
    
    @property
    def state(self):
        return self.user.get('state')
    
    @property
    def current_question(self):
        return '\n'.join(self.user.get('current_question', []))
    
    @property    
    def current_question_preview(self):
        """
        get current message
        """
        user = self.user
        if not user.get('current_question'):
            return ''

        question_text = f':pencil: <strong>Question Preview</strong>\n\n'
        question_text += self.question
        question_text += f'\n{"_" * 40}\n When done, click <strong>{keys.send_question}</strong>'
        
        return question_text
    
    def update(self, values, upsert=True):
        self.db.users.update_one(
            {'_id': self.chat_id},
            values,
            upsert=upsert
            )
        
    def update_state(self, state):
        """
        Update user state.
        """
        self.update( 
            values={'$set':{'state':state}},
            upsert=False
            )
            
    def reset(self):
        """
        Empty Current Question Field
        """
        self.update(
            {'$set': 
                {
                 'current_question': [],
                 'state': states.main
                 }
                }
            )
    
    def get_all_users(self) -> List['User']:
        """
        return all users
        """
        return self.db.users.find()
    
    
if __name__ == '__main__':
    user = User(chat_id=577049807)
    print(user.current_question())