from dataclasses import dataclass
from typing import Tuple

import emoji
from telebot import types

from src.dataClass import inlineKeys

inlineKeys = inlineKeys.InlineKeys()

def create_keyboard(*keys, reply_row_width=2, inline_row_with=4,
                    resize_keyboard=True, is_inline=False, callback_data=None):
    """
    Create a keyboard with buttons.
    
    :param keys: List of buttons
    :param row_width: Number of buttons in a row.
    :param resize_keyboard: Resize keyboard to small ones (works with reply keys only, not inline keys).
    :param is_inline: If True, create inline keyboard.
    :param callback_data: If not None, use keys text as callback data.
    """
    keys = list(map(emoji.emojize, keys))
    
    # Empty keyboard
    if not keys: 
        return
    
    if is_inline:
        # create inline keyboard
        markup = types.InlineKeyboardMarkup(row_width=reply_row_width)
        
        # set callback data to keys text
        if callback_data is None:
            callback_data = keys
        
        buttons = []
        for key, callback in zip(keys, callback_data):
            button = types.InlineKeyboardButton(key, callback_data=callback)
            buttons.append(button)
    
    markup.add(*buttons)  
    return markup

@dataclass
class InlineKeyboards:
    main:Tuple = create_keyboard(inlineKeys.actions, inlineKeys.like, is_inline=True)
    actions:Tuple = create_keyboard(inlineKeys.back, inlineKeys.answer, inlineKeys.follow, inlineKeys.unfollow)



