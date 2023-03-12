import json

from loguru import logger

from interfaces.IMessageSender import IMessageSender
from src import constants
from src.db import db
from src.models.user import User


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
        """
        send question to all users
        """
        user_info = self.user.user
        username = f"@{user_info['chat'].get('username')}"
        firstname = user_info['chat'].get('first_name')
        text = ':red_question_mark: <strong>New Question</strong>\n'
        text += f":bust_in_silhouette: From: {username or firstname}\n\n"
        text += self.user.current_question
        self.message_sender.send_message_to_all(user=self.user ,text=text)
        
        self.message_sender.send_message(
            chat_id=user_info['_id'],
            text=':check_mark_button: Question sent to all successfully.'
            )
    

    # def update(self, message):
    #     if message.content_type not in constants.SUPPORTED_CONTENT_TYPES:
    #         return
        
    #     elif message.content_type == 'text':
    #         push_data = {'text': message.html_text}
    #     else:
    #         content = getattr(message, message.content_type)
    #         content = vars(content[-1]) if isinstance(content, list) else vars(content)
    #         content['content_type'] = message.content_type

    #         content = self.remove_non_json_data(content)
    #         push_data = {'attachments': content}
            
    #         set_data = {
    #             'data': message.data,
    #             'type': None,
    #             'replied_to_post_id': None
    #         }
    #         set_data = {'date': message.date, 'type': self.post_type, 'replied_to_post_id': replied_to_post_id}
    #         output = self.collection.update_one({'chat.id': message.chat.id, 'status': post_status.PREP}, {
    #             '$push': push_data, '$set': set_data,
    #         }, upsert=True)
            
    
    def remove_non_json_data(json_data):
        return json.loads(json.dumps(json_data, default=json_encoder))
        