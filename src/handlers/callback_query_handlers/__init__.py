from src.bot import bot
from src.dataClass.inlineKeys import InlineKeys
from src.decorators.callback_query_handler import callback_query_handler
from src.handlers.callback_query_handlers import (actionCallBackHandler,
                                                  backCallBackHandler,
                                                  likeCallBackHandler,
                                                  mainCallBackHandler)

# initial keys data class
inlineKeys = InlineKeys()

# initial callback query handlers
actionCallBack = actionCallBackHandler.ActionCallBackHandler(bot)
likeCallBack = likeCallBackHandler.LikeCallBackHandler(bot)
backCallBackHandler = backCallBackHandler.BackCallBackHandler(bot)
mainCallBackHandler = mainCallBackHandler.MainCallBackHandler(bot)


@callback_query_handler(func=lambda call: call.data == inlineKeys.actions)
def action_callback(call, data):
    actionCallBack.handle(call, data)
    
@callback_query_handler(func=lambda call: call.data == inlineKeys.like)
def like_callback(call, data):
    likeCallBack.handle(call, data)
    
@callback_query_handler(func=lambda call: call.data == inlineKeys.back)
def back_callback(call, data):
    backCallBackHandler.handle(call, data)
    
@callback_query_handler(func=lambda call: True)
def main_callback(call, data):
    mainCallBackHandler.handle(call, data)