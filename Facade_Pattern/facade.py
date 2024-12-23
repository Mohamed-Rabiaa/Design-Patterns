from location_api import Location
from weather_api import Weather

class Facade():
    def __init__(self):
        self.location = Location()
        self.weather = Weather()

    def show_weather(self):
        """ Finds the location and retrieves its weather information """
        location_data = self.location.find_location()
        if not location_data:
            print("Error: Unable to find location")
            return
        
        location = location_data.get('location')
        if not location:
            print('Error: Invalid location')
            return

        weather_data = self.weather.get_weather(location)
        if not weather_data:
            print("Error: Unable to fetch weather data")
            return
        
        weather = weather_data.get('weather', "No weather information available")
        print(f"Weather in {location}: {weather}")
