from src.base.baseCallbackQueryHandler import BaseCallbackQueryHandler
from src import constants

class AnswerCallBackHandler(BaseCallbackQueryHandler):
    def __init__(self, bot):
        self.bot = bot
    
    def handle(self, call, data):
        user = data['user']
        message_sender = data['message_sender']

        message_sender.answer_callback_query(call.id, text=call.data)
        user.update_state(self.states.answer_question)
        message_sender.send_message(
            text=constants.ANSWER_QUESTION_START_MESSAGE.format(first_name=user.user['chat']['first_name']),
            reply_markup=self.keyboards.answer_question
        )
        