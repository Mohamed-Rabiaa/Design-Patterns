# Concrete product class
from pizza import Pizza
from pizza_factory import PizzaFactory

# Concrete creator class
class VeggieCreator(PizzaFactory):
    def create_pizza(self):
        return Veggie()
    
class Veggie(Pizza):
    def prepare(self):
        print('Preparing a Veggie pizza')

    def bake(self):
        print("Baking a Veggie pizza")

    def process_order(self):
        print("Delivering a Veggie pizza")