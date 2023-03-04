from src.bot import bot
from src.middleware.userMiddleware import UserMiddleware
from src.middleware.callback_middleware import CallbackMiddleware

bot.setup_middleware([CallbackMiddleware(), UserMiddleware()])
