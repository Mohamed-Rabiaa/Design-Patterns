class Stripe():
    """ Stripe payment gateway"""
    def pay(self, amount, currency):
        """ Process a payment through Stripe """
        print(f"Processing a payment of {amount} {currency} through Stripe")