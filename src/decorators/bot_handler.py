import src.bot


def bot_handler(commands=None, regexp=None):
    """
     decorstor for register handlers
    """
    def decorator(func):
        if commands is not None:
            bot.message_handler(commands=commands)(func)
        elif regexp is not None:
            bot.message_handler(regexp=regexp)(func)
        else:
            bot.message_handler()(func)
        return func
    return decorator