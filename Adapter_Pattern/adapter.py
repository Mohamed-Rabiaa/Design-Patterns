from online_market import OnlineMarket

class Adapter(OnlineMarket):
    """ Adapter to integrate Stripe payments into an OnlineMarket system """
    def __init__(self, stripe):
        self.stripe = stripe

    def payment(self, amount, currency):
        print("Adapting Stripe payment to work with the OnlineMarket system")
        self.stripe.pay(amount, currency)
 
