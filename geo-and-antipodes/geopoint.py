from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from pyowm import OWM
from folium import Marker
import os
from dotenv import load_dotenv

load_dotenv()


class Geopoint (Marker):
    """
    Create a geopoint object with a given latitude and longitude.
    Show timezone, current date, time and weather in this place.
    """

    def __init__(self, latitude, longitude):
        super().__init__(location=[latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude

    def get_time(self):
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=self.latitude, lng=self.longitude)
        time_now = str(datetime.now(timezone(timezone_str)))
        return f"Hello! Welcome in this beautiful place! " \
               f"You are in the {timezone_str} timezone.\n" \
               f"The current time is {time_now[0:10]}, {time_now[11:19]}."

    def get_weather(self):
        api_key = os.environ["WEATHER_API_KEY"]
        owm = OWM(api_key)
        weather_manager = owm.weather_manager()
        weather_now = weather_manager.weather_at_coords(self.latitude, self.longitude)
        w = weather_now.weather
        return f"The weather right now is:\n" \
               f"- {w.temperature('celsius')['temp']} degrees Celsius,\n" \
               f"- {w.detailed_status},\n" \
               f"- rain: {w.rain}.\n"
