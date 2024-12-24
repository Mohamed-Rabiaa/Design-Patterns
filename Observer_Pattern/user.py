from subscriber import Subscriber

class User(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        """ Prints the message sent to the subscriber"""
        print(f'Notification for {self.name}: {message}')
