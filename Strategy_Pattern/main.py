from context import Context
from car import Car
from train import Train
from plane import Plane

def get_valid_miles():
    """ Prompts the user to enter a valid miles number"""
    while True:
        miles = int(input("How many miles do you want to travel?\n"))
        if miles >= 0:
            return miles
        print("Please choose valid miles!")


if __name__ == '__main__':
    # Instantiating the context with the car strategy as the default option
    context = Context(Car())

    miles = get_valid_miles()

    if miles > 100 and miles <= 300:
        # Changing the strategy to the traing strategy
        context.strategy = Train()

    elif miles > 300:
        context.strategy = Plane()
    
    context.execute_strategy()
