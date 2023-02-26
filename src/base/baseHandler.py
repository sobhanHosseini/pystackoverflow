from abc import ABC, abstractmethod
from src.dataClass import keyboards as kb, keys as ky, states as stat

class BaseHandler(ABC):
    
    # init data class
    keys = ky.Keys()
    keyboards = kb.Keyboards()
    states = stat.States()
    
    @abstractmethod
    def handle(self, message, data):
        pass