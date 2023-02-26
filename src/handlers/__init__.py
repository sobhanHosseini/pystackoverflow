import src.handlers.startHandler
from src.bot import bot
from src.decorators.bot_handler import bot_handler


s = startHandler.StartHandler(bot)

@bot_handler(commands=['start'])
def start(message):
    s.handle(message)