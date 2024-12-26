from order_template import OrderTemplate

class InternationalShipping(OrderTemplate):
    def calculate_shipping_cost(self):
        print("Shipping cost is $300!")