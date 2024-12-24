from online_newspaper import OnlineNewspaper
from user import User

if __name__ == '__main__':
    online_newspaper = OnlineNewspaper()

    ahmed = User("Ahmed")
    online_newspaper.subscribe('technology', ahmed)

    mahmoud = User("Mahmoud")
    online_newspaper.subscribe('sports', mahmoud)

    hani = User("Hani")
    online_newspaper.subscribe('art', hani)
    online_newspaper.subscribe('technology', hani)

    # Notifiying subscribed users about new Technology articles
    online_newspaper.notify('technology')

    # Notifiying subscribed users about new sports articles
    online_newspaper.notify('sports')

    # Notifiying subscribed users about new art articles
    online_newspaper.notify('art')
