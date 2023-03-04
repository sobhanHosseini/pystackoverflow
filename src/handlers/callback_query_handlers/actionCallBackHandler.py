from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from loguru import logger

class ActionCallBackHandler(BaseCallbackQueryHandler):
    def __init__(self, bot):
        self.bot = bot
    
    def handle(self, call, data):
        logger.info('in call back handle...')
        print(data)
        print('-' * 50)