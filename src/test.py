from abc import ABC, abstractmethod

class StartHandler(ABC):
    @abstractmethod
    def handler(self, message):
        pass

class MyStartHandler(StartHandler):
    def __init__(self, a):
        self.a = a
    def handler(self, message):
        print("Handling start message:", message)

a = MyStartHandler(1)

print(a.handler('test'))