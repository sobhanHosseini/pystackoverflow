from src.db import db
from src.dataClass import keys 

class User:
    def __init__(self, chat_id):
        self.db = db
        self.chat_id = chat_id
    
    @property
    def user(self):
        return self.db.users.find_one({'_id': self.chat_id})
    
    @property
    def state(self):
        return self.user.get('state')
    
    @property    
    def current_question(self):
        """
        get current message
        """
        user = self.user
        if not user or not user.get('current_question'):
            return ''
        
        current_question = f':pencil: Question Preview\n\n'
        current_question += '\n'.join(user.get('current_question'))
        current_question += f'\n{"_" * 40}\n When done, click {keys.send_question}'
        return current_question
    
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
            
    def reset_current_question(self):
        """
        Empty Current Question Field
        """
        self.update({'$set': {'current_question': []}})
    
        

if __name__ == '__main__':
    user = User(chat_id=577049807)
    print(user.current_question())