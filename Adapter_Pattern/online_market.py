class OnlineMarket():
    """ An online market that accepts Paypal payments only """
    def payment(self, amount, currency):
        """ Process a payment through PayPal """
        print(f"Processing a payment of {amount} {currency} through Paypal")