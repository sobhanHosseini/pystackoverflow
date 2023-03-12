from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from src.models.question import Question


class MainCallBackHandler(BaseCallbackQueryHandler):
    def __init__(self, bot):
        self.bot = bot
    
    def handle(self, call, data):
        user = data['user']
        message_sender = data['message_sender']
        question = Question(user=user, message_sender=message_sender)
        
        message_sender.answer_callback_query(call.id, text=f'Sending file: {call.data}...')
        self.send_file(question, call.message.chat.id, call.data, message_id=call.message.message_id)
    
    def send_file(self, question, chat_id, file_unique_id, message_id=None):
        attachment = question.file_unique_id_to_metadata(file_unique_id)
        if not attachment:
            return
        
        file_id, attachment_type, mime_type = attachment['file_id'], attachment['content_type'], attachment.get('mime_type')
        
        # Send file to user with the appropriate send_file method according to the attachment_type
        send_method = getattr(self.bot, f'send_{attachment_type}')
        send_method(
            chat_id,
            file_id,
            reply_to_message_id=message_id,
            caption=f"<code>{mime_type or ''}</code>"
        )
        