from src.db import db


class User:
    def __init__(self, chat_id):
        self.db = db
        self.chat_id = chat_id
    
    def get_user(self):
        return self.db.users.find_one({'_id': self.chat_id})
    
    def get_state(self):
        user = self.get_user()
        return user.get('state')
    
    def current_question(self):
        """
        get current message
        """
        user = self.get_user()
        if not user or not user.get('current_question'):
            return ''
        
        current_question = '\n\n'.join(current_question)
        return f':right_arrow: Preview Question\n\n {current_question}'
    
    def update(self, condition):
        self.db.users.update_one({'_id': self.chat_id}, condition)
            
    def reset(self):
        self.update({'$set': {'current_question': []}})
        

if __name__ == '__main__':
    u = User(chat_id=577049807)
    print(u.current_question())