from src.bot import bot
from src.middleware.userMiddleware import UserMiddleware
from src.middleware.callback_middleware import CallbackMiddleware

c = CallbackMiddleware()
u = UserMiddleware()
bot.setup_middleware(UserMiddleware())
