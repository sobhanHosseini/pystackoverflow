from abc import ABC, abstractmethod


class BaseHandler(ABC):
    
    @abstractmethod
    def handler(self, message):
        pass