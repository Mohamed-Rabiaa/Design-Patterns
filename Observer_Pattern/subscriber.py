from abc import ABC, abstractmethod

class Subscriber(ABC):
    """ Subscriber Interface """
    @abstractmethod
    def update(self, message):
        pass