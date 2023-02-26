class Message:
    def __init__(self, chat_id):
        self.chat_id = chat_id
    
    def send(self, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text)

        self.bot.send_message(self.chat_id, text, reply_markup=reply_markup)