from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from loguru import logger

class CallBackQueryHandler(BaseCallbackQueryHandler):
    def __init__(self):
        pass
    
    def handle(self):
        logger.info('in call back handle...')