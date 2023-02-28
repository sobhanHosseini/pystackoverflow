from abc import ABC, abstractmethod
from typing import List


class IMessageSender(ABC):
    @abstractmethod
    def send_message(self, chat_id: int, text: str, reply_markup: List=None, emojize: bool=True) -> None:
        pass

    @abstractmethod
    def send_message_to_all(self, message: str) -> None:
        pass
        