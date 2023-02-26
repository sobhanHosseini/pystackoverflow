from abc import ABC, abstractmethod
from src.dataClass import keyboards, keys, states

class BaseHandler(ABC):
    
    # init data class
    keys = keys.Keys()
    keyboards = keyboards.Keyboards()
    states = states.States()
    
    @abstractmethod
    def handle(self, message, data):
        pass