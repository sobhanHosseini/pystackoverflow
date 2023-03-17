import concurrent.futures
from typing import List

import emoji
from loguru import logger

from src.interfaces.IMessageSender import IMessageSender
from src.models.callback_data import CallbackData
from src.models.user import User


class Message(IMessageSender):
    def __init__(self, chat_id, bot, message_info=None):
        self.bot = bot
        self.chat_id = chat_id
        self.message_info=message_info
    
    def send_message(
        self,
        text: str,
        reply_markup: List=None, 
        emojize: bool=True,
        chat_id: int=None,
        question_id=None
        ):
        """
        Send message to telegram bot.
        """
        if chat_id is None:
            chat_id = self.chat_id
            
        if emojize:
            text = emoji.emojize(text)

        message = self.bot.send_message(chat_id, text, reply_markup=reply_markup)
  
        callback_data = CallbackData(chat_id, message.message_id, question_id)
        callback_data.update(reply_markup=reply_markup)
        
    def send_message_to_all(self,user: User, text: str, reply_markup: List=None, question_id=None):
        """
        Send message to all user
        """
        # Send to all users in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for u in user.get_all_users():
                executor.submit(
                    self.send_message,
                    text=text,
                    chat_id=u['_id'],
                    reply_markup=reply_markup,
                    question_id=question_id
                )
    
    def edit_message(self, message_id, text=None, reply_markup=None, emojize: bool = True):
        """
        Edit telegram message text and/or reply_markup.
        """
        if emojize and text:
            text = emoji.emojize(text)
        
        # if message text or reply_markup is the same as before, telegram raises an invalid request error
        # so we are doing try/catch to avoid this.
        
        try:
            if text and reply_markup:
                self.bot.edit_message_text(text=text, chat_id=self.chat_id, reply_markup=reply_markup, message_id=message_id)
            elif reply_markup:
                self.bot.edit_message_reply_markup(chat_id=self.chat_id, message_id=message_id, reply_markup=reply_markup)
            elif text:
                self.bot.edit_message_text(text=text, chat_id=self.chat_id, message_id=message_id)
            #TODO
            # self.update_callback_data(chat_id, message_id, reply_markup)
        except Exception as e:
            logger.debug(f'Error editing message: {e}')
    
    def answer_callback_query(self, call_id, text, emojize=True):
        """
        Answer to a callback query.
        """
        if emojize:
            text = emoji.emojize(text)
            
        self.bot.answer_callback_query(call_id, text=text)
    
    

            
        