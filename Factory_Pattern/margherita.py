from pizza import Pizza
from pizza_factory import PizzaFactory

# Concrete creator class
class MargheritaCreator(PizzaFactory):
    def create_pizza(self):
        return Margherita()
    
# Concrete product class
class Margherita(Pizza):
    def prepare(self):
        print('Preparing a Margherita pizza')

    def bake(self):
        print("Baking a Margherita pizza")

    def process_order(self):
        print("Delivering a Margherita pizza")