# strategy interface
from abc import ABC, abstractmethod

class TravelMethod(ABC):
    @abstractmethod
    def execute(self):
        pass