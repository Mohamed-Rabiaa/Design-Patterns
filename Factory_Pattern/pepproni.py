# Concrete product class
from pizza import Pizza
from pizza_factory import PizzaFactory

# Concrete creator class
class PepproniCreator(PizzaFactory):
    def create_pizza(self):
        return Pepproni()
    
class Pepproni(Pizza):
    def prepare(self):
        print('Preparing a Pepproni pizza')

    def bake(self):
        print("Baking a Pepproni pizza")

    def process_order(self):
        print("Delivering a Pepproni pizza")

