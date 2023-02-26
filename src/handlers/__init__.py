import src.handlers.startHandler
from src.bot import bot
from src.decorators.bot_handler import bot_handler


start_handelr = startHandler.StartHandler(bot)

@bot_handler(commands=['start'])
def start(message, data):
    start_handelr.handle(message, data)