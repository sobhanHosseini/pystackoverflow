from src.bot import bot
from src.middleware.userMiddleware import Middleware

bot.setup_middleware(Middleware())
