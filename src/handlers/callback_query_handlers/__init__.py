from src.bot import bot
from src.dataClass.inlineKeys import InlineKeys
from src.decorators.callback_query_handler import callback_query_handler
from src.handlers.callback_query_handlers import actionCallBackHandler, likeCallBackHandler


# initial keys data class
inlineKeys = InlineKeys()

# initial callback query handlers
actionCallBack = actionCallBackHandler.ActionCallBackHandler(bot)
likeCallBack = likeCallBackHandler.likeCallBackHandler(bot)


@callback_query_handler(func=lambda call: call.data == inlineKeys.actions)
def action(call, data):
    actionCallBack.handle(call, data)
    
@callback_query_handler(func=lambda call: call.data == inlineKeys.like)
def like(call, data):
    likeCallBack.handle(call, data)