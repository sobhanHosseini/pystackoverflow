import emoji

from src.bot import bot
from src.dataClass.keys import Keys
from src.decorators.bot_handler import bot_handler
from src.handlers import (askQuestionHandler, cancelHandler, echoHandler,
                          settingHandler, startHandler, sendQuestionHandler)

# initial keys data class
keys = Keys()

# initial handlers
start_handelr = startHandler.StartHandler(bot)
ask_question_handler = askQuestionHandler.AskQuestionHandler(bot)
cancel_handler = cancelHandler.CancelHandler(bot)
send_question_handler = sendQuestionHandler.SendQuestionHandler(bot)
setting_handler = settingHandler.SettingHandler(bot)
echo_handler = echoHandler.EchoHandler(bot)

@bot_handler(commands=['start'])
def start(message, data):
    start_handelr.handle(message, data)

@bot_handler(regexp=keys.ask_question)
def ask_question(message, data):
    ask_question_handler.handle(message, data)
    
@bot_handler(regexp=keys.cancel)
def cancel(message, data):
    cancel_handler.handle(message, data)
    
@bot_handler(regexp=keys.send_question)
def send_question(message, data):
    send_question_handler.handle(message, data)
    
@bot_handler(regexp=keys.settings)
def setting(message, data):
    setting_handler.handle(message, data)
    
@bot_handler(func=lambda ـ: True)
def echo(message, data):
    echo_handler.handle(message, data)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    print('-' * 50)
    print('in call back')
    print(call)
    print('-' * 50)