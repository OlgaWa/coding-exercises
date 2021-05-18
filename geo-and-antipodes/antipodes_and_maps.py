from folium import Map, Popup
from geopoint import Geopoint


# Getting the latitude and the longitude:
print("Hello! Welcome to the Geo and Antipodes App based on the project The Other Side of The World by Ardit Sulce.\n"
      "First think of a city, it may be for example a place where you are right now.\n"
      "Now find the coordinates (latitude and longitude) of that particular place.\n")

lat = float(input("What is the latitude of that place? (Write the latitude like in this example: 52.23) "))
lon = float(input("What is the longitude of that place? (Write the longitude like in this example: 2.32) "))

print("\nNow I will show you what is exactly on the other side of the world of that place!\n"
      "It may take a while. You will find a html file with a map in the folder of this project :)\n")


# Creating a map with an antipode of the place chosen before:
antipode_latitude = lat * -1
if lon <= 0:
    antipode_longitude = lon + 180
else:
    antipode_longitude = lon - 180

geo_antipode = Geopoint(antipode_latitude, antipode_longitude)
mymap = Map([antipode_latitude, antipode_longitude])

my_popup = Popup("Hello there!")
my_popup.add_to(geo_antipode)

geo_antipode.add_to(mymap)
mymap.save('map.html')


# Showing the current time and the weather in the antipode:
print(geo_antipode.get_time())
print(geo_antipode.get_weather())

print(input("Enter anything to continue."))


# Showing the current time and the weather in the place that the user has chosen at the beginning:
print("And now I will show you the current time and the weather in the place you have chosen at the beginning:\n")

geo_now = Geopoint(lat, lon)
print(geo_now.get_time())
print(geo_now.get_weather())


print("So, are you moving there or not?")
