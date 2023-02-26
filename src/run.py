import emoji
from loguru import logger
from telebot import custom_filters

from src import handlers, middleware
from src.bot import bot
from src.filters import IsAdmin


class Bot:
    """
    stack overflow telegram bot
    """
    def __init__(self):
        # add custom filters
        self.bot.add_custom_filter(IsAdmin())
        self.bot.add_custom_filter(custom_filters.TextMatchFilter())
        self.bot.add_custom_filter(custom_filters.TextStartsFilter())

        # run bot
        logger.info('Bot is running...')
        bot.infinity_polling()
      

if __name__ == '__main__':
    logger.info('Bot started')
    Bot()

