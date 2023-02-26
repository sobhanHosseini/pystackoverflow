from abc import ABC, abstractmethod

from src import dataClass


class BaseHandler(ABC):
    
    @abstractmethod
    def handle(self, message, data):
        pass