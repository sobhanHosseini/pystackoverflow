import json

from loguru import logger

from interfaces.IMessageSender import IMessageSender
from src import constants
from src.dataClass import keys, inlineKeys
from src.dataClass.inlineKeyboards import create_keyboard
from src.db import db
from src.models.user import User
from src.utils.common import human_readable_size, json_encoder


class Question:
    def __init__(self, user: User, message_sender: IMessageSender):
        self.user = user
        self.message_sender = message_sender
        self.db = db
    
    @property
    def question(self):
        return self.db.question.find_one({'chat_id': self.user.chat_id})
    
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
    

    def update(self, message):
        if message.content_type not in constants.SUPPORTED_CONTENT_TYPES:
            return
        
        elif message.content_type == 'text':
            push_data = {'text': message.html_text}
        else:
            content = getattr(message, message.content_type)
            content = vars(content[-1]) if isinstance(content, list) else vars(content)
            content['content_type'] = message.content_type

            # removing non json serializable data
            content = self.remove_non_json_data(content)
            push_data = {'attachments': content}
            
        # save to database
        # TODO change none
        set_data = {
            'date': message.date,
            'type': None,
            'replied_to_post_id': None
        }
        
        # TODO change none
        db.question.update_one(
            {'chat_id': message.chat.id, 'status': None},
            {
                '$push': push_data,
                '$set': set_data
            },
            upsert=True
        )
    
    @staticmethod
    def remove_non_json_data(json_data):
        return json.loads(json.dumps(json_data, default=json_encoder))
    
    def get_text(self):
        """
        get current message
        """
        question = self.question
        if not question.get('text'):
            return ''

        question_text = f':pencil: <strong>Question Preview</strong>\n\n'
        question_text += '\n'.join(question.get('text', []))
        question_text += f'\n{"_" * 40}\n When done, click <strong>{keys.send_question}</strong>'
        
        return question_text
    
    def get_keyboard(self):
        keys = [inlineKeys.actions, inlineKeys.like,]
        callback_data = [inlineKeys.actions, inlineKeys.like,]

        for attachment in self.question.get('attachments',[]):
            file_name = attachment.get('file_name') or attachment['content_type']
            file_size = human_readable_size(attachment['file_size'])
            keys.append(f"{file_name} - {file_size}")
            callback_data.append(attachment['file_unique_id'])
            
        return create_keyboard(*keys, callback_data=callback_data, is_inline=True)
    
    def reset_question(self):
        self.db.question.update_one(
            {'chat_id': self.user.chat_id},
            {'$set': {'text': [], 'attachments': []}},
            upsert=True
            )
    
    def file_unique_id_to_metadata(self, file_unique_id):
        """
        Get file metadata having a file_id.
        """
        query_result = self.db.question.find_one(
            {'attachments.file_unique_id': file_unique_id},
            {'attachments.$':1}
        )
        if not query_result:
            return
        
        return query_result['attachments'][0]