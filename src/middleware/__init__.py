from src.bot import bot
from src.middleware.userMiddleware import UserMiddleware

bot.setup_middleware(UserMiddleware())
