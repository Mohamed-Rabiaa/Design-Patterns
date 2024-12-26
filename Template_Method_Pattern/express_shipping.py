from order_template import OrderTemplate

class ExpressShipping(OrderTemplate):
    def calculate_shipping_cost(self):
        print("Shipping cost is $100!")