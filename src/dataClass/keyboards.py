from dataclasses import dataclass
from typing import Tuple

import emoji
from telebot import types

from src.dataClass import keys

keys = keys.Keys()

def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    markup =  types.ReplyKeyboardMarkup(
        row_width=row_width,
        resize_keyboard=resize_keyboard
    )
    
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)
    
    return markup

@dataclass
class Keyboards:
    main:Tuple = create_keyboard(keys.ask_question, keys.settings)
    ask_question:Tuple = create_keyboard(keys.cancel, keys.send_question)


