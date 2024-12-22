from adapter import Adapter
from stripe import Stripe

if __name__ == '__main__':
    adapter = Adapter(Stripe())

    # Processing Stripe payment
    adapter.payment(100, "EGP")