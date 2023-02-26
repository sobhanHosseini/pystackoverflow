import src.handlers.start
from src.bot import bot


s = start.StartHandler(bot)
s.handle()