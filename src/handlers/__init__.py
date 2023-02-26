import emoji

from src.bot import bot
from src.decorators.bot_handler import bot_handler
from src.handlers import (askQuestionHandler, cancelHandler, echoHandler,
                          settingHandler, startHandler)

start_handelr = startHandler.StartHandler(bot)
ask_question_handler = askQuestionHandler.AskQuestionHandler(bot)
cancel_handler = cancelHandler.CancelHandler(bot)
setting_handler = settingHandler.SettingHandler(bot)
echo_handler = echoHandler.EchoHandler(bot)

@bot_handler(commands=['start'])
def start(message, data):
    start_handelr.handle(message, data)

@bot_handler(regexp=emoji.emojize(self.keys.ask_question))
def ask_question(message, data):
    ask_question_handler.handle(message, data)
    
@bot_handler(regexp=emoji.emojize(self.keys.cancel))
def cancel(message, data):
    cancel_handler.handle(message, data)
    
@bot_handler(regexp=emoji.emojize(self.keys.settings))
def setting(message, data):
    setting_handler.handle(message, data)
    
@bot_handler(func=lambda ـ: True)
def echo(message, data):
    echo_handler.handle(message, data)