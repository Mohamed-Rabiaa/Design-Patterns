from abc import ABC, abstractmethod
# abstract class representing a pizza
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def process_order(self):
        pass
