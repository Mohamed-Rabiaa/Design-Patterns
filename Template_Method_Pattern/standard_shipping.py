from order_template import OrderTemplate

class StandardShipping(OrderTemplate):
    def calculate_shipping_cost(self):
        print("Shipping cost is $50!")