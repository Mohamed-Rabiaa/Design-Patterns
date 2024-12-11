# Factory (creator) class
from abc import ABC, abstractmethod

class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass

    def prepare(self):
        if not hasattr(self, '_pizza'):
            self._pizza = self.create_pizza()
        self._pizza.prepare()

    def bake(self):
        if not hasattr(self, '_pizza'):
            self._pizza = self.create_pizza()
        self._pizza.bake()

    def process_order(self):
        if not hasattr(self, '_pizza'):
            self._pizza = self.create_pizza()
        self._pizza.process_order()

