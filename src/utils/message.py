from typing import List

import emoji

from src.interfaces.IMessageSender import IMessageSender
from src.models.user import User


class Message(IMessageSender):
    def __init__(self, chat_id, bot, message_info=None):
        self.bot = bot
        self.chat_id = chat_id
        self.message_info=message_info
    
    def send_message(self, text: str, reply_markup: List=None, emojize: bool=True, chat_id: int=None) -> None:
        """
        Send message to telegram bot.
        """
        if chat_id is None:
            chat_id = self.chat_id
            
        if emojize:
            text = emoji.emojize(text)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
    
    def send_message_to_all(self,user: User, text: str) -> None:
        """
        Send message to all user
        """
        for u in user.get_all_users():
            self.send_message(
                text=text,
                chat_id=u['_id'],
                )
        