from src.bot import bot


def callback_query_handler(func=None):
    """
     decorstor for register callback query handlers
    """
    def decorator(f):
        if func is not None:
            bot.callback_query_handler(func=func)(f)
        else:
            bot.callback_query_handler()(f)
        return f
    return decorator