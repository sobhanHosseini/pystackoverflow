from src.base.baseHandler import BaseHandler

from src import dataClass


class BaseCallbackQueryHandler(BaseHandler):
    # initial data class
    inlineKeyboards = dataClass.inlineKeyboards
    inlineKeys = dataClass.inlineKeys
    