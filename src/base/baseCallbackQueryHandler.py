from abc import ABC, abstractmethod

from src import dataClass


class BaseCallbackQueryHandler(ABC):
    # initial data class
    inlineKeyboards = dataClass.inlineKeyboards
    inlineKeys = dataClass.inlineKeys
    keyboards = dataClass.keyboards
    states = dataClass.states
    
    @abstractmethod
    def handle(self, message, data):
        pass