from src.bot import bot
from src.decorators.bot_handler import callback_query_handler
from src.handlers.callback_query_handlers import actionCallBackHandler

actionCallBack = actionCallBackHandler.ActionCallBackHandler(bot)


@callback_query_handler(func=lambda call: True)
def action(call, data):
    actionCallBack.handle(call, data)