from src.bot import bot


def bot_handler(func=None, commands=None, regexp=None):
    """
     decorstor for register handlers
    """
    def decorator(f):
        if commands is not None:
            bot.message_handler(commands=commands)(f)
        elif regexp is not None:
            bot.message_handler(regexp=regexp)(f)
        elif func is not None:
            bot.message_handler(func=func)(f)
        else:
            bot.message_handler()(f)
        return f
    return decorator