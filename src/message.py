import emoji
from src.user import User


class Message:
    def __init__(self, chat_id, bot):
        self.chat_id = chat_id
        self.bot = bot
    
    def send(self, text, reply_markup=None, emojize=True, chat_id=None):
        """
        Send message to telegram bot.
        """
        if chat_id is None:
            chat_id = self.chat_id
            
        if emojize:
            text = emoji.emojize(text)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
    
    def send_question_to_all(self):
        user = User(self.chat_id)
        
        msg_text = ':red_question_mark: <strong>New Question</strong>'
        msg_text += user.question
        
        for u in user.get_all_user():
            self.send(
                text=msg_text,
                chat_id=u['_id']
                )
        
        self.send(text=':check_mark_button: Question sent to all successfully.')
        