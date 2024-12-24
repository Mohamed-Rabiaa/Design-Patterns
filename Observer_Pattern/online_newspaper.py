from publisher import Publisher

class OnlineNewspaper(Publisher):
    """ An online Newspaper that sends emails to every subscriber that is interested in 
        the articles of a specific category """
    def __init__(self):
        self._subscribers = {
            'art': [],
            'economic': [],
            'sports': [],
            'technology': [],
        }

    def subscribe(self, event_type, subscriber):
        """ Adds the subscriber to his preferred articles category """
        self._subscribers.get(event_type).append(subscriber)

    def unsubscribe(self, event_type, subscriber):
        """ Removes the subscriber from his preferred articles category """
        self._subscribers.get(event_type).remove(subscriber)

    def notify(self, event_type):
        """ Notifies the users/subscribers about new articles in the categories they
            are interested in """
        for subscriber in self._subscribers.get(event_type):
            self.message = f'There are new {event_type} articles, check them in the link below!'
            subscriber.update(self.message)