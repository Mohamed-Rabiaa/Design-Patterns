from abc import ABC, abstractmethod

class OrderTemplate(ABC):
    """ Abstract base class """
    def process_order(self):
        """ A Template Method that Processes the order"""
        self.validate_order()
        self.calculate_shipping_cost()
        self.process_payment()
        self.generate_invoice()

    def validate_order(self):
        """ Validates the order details """
        print("Order validated!")

    @abstractmethod
    def calculate_shipping_cost(self):
        """ Calcualtes the shipping cost """
        pass

    def process_payment(self):
        """ Processes the payment """
        print("Payment processed!")

    def generate_invoice(self):
        """ Generates the invoice """
        print("Invoice Genrated!")