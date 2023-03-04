from abc import ABC, abstractmethod

from src import dataClass


class BaseHandler(ABC):
    # initial data class
    keys = dataClass.keys
    keyboards = dataClass.keyboards
    states = dataClass.states
    
    @abstractmethod
    def handle(self, message, data):
        pass