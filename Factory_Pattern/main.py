from pepproni import PepproniCreator
from margherita import MargheritaCreator
from veggie import VeggieCreator

pizza_types = {
    'pepproni': PepproniCreator(),
    'margherita': MargheritaCreator(),
    'veggie': VeggieCreator(),
}

def client_code(pizza_factory):
    pizza_factory.prepare()  
    pizza_factory.bake()
    pizza_factory.process_order()   

if __name__ == '__main__':
    pizza = input('What type of pizza do you want? '\
                  '(pepproni, margherita, veggie)\n').lower()

    if pizza in pizza_types:
        client_code(pizza_types[pizza])
    else:
        print('Please enter a valid pizza name')
 