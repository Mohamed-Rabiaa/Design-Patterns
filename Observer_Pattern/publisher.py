from abc import ABC, abstractmethod

class Publisher(ABC):
    """ Publisher Interface """
    @abstractmethod
    def subscribe(self, event_type, subscriber):
        pass
    
    @abstractmethod
    def unsubscribe(self, event_type, subscriber):
        pass

    @abstractmethod
    def notify(self, event_type):
        pass