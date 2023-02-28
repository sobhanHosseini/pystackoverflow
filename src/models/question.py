from loguru import logger

from src.db import db


class Question:
    def __init__(self, user: User, message_sender: IMessageSender):
        self.user = user
        self.message_sender = message_sender
    
    def save_question(self):
        """
        Save question to database
        """
        logger.info('Save question to database.')
        
        db.question.insert_one({
            'chat_id': self.user.user['_id'],
            'question': self.user.user['current_question'],
            'date': self.message_sender.message_info.date
        })
        
    def send_question_to_all(self):
        user = self.user
        text = ':red_question_mark: <strong>New Question</strong>'
        text += user.current_question
        self.message_sender.send_message_to_all(user=user ,text=text)
        
        self.message_sender.send_message(
            chat_id=user.user['_id'],
            text=':check_mark_button: Question sent to all successfully.'
            )
        