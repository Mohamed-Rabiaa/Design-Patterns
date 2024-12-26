from standard_shipping import StandardShipping
from express_shipping import ExpressShipping
from international_shipping import InternationalShipping

shipping_types = {'standard', 'express', 'international'}

def client_code(order_template):
    """ 
    Client code calls the template method to execute the algorithm 
    it works with objects through the interface of their base class 
    """
    order_template.process_order()

def validate_shipping_type():
    while True:
        shipping =input('What type of shipping do you want? (standard, express, international)\n')
        
        if shipping in shipping_types:
            return shipping
          
        print("Please choose a valid shipping type!")
        

if __name__ == '__main__':
    order_confirm = input("Do you want to confirm the order? (yes or no)\n")

    if order_confirm == 'yes':
        shipping = validate_shipping_type()

        if shipping == 'standard':
            client_code(StandardShipping())

        elif shipping == 'express':
            client_code(ExpressShipping())

        else:
            client_code(InternationalShipping())