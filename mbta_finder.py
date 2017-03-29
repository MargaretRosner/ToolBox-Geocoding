"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

from urllib.request import urlopen
from urllib.parse import urlencode
import json
from pprint import pprint
url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"



# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    #pprint(response_data)
    #print(response_data["results"][0]["formatted_address"])
    return(response_data["results"][0]["geometry"]["location"])
    #print(response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    params = urlencode({'address':place_name})
    paramsurl = GMAPS_BASE_URL + '?'+params
    data = get_json(paramsurl)
    return (data['lat'], data['lng'])

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    stoplatlng = urlencode({'lat':latitude, 'lng':longitude})

    stopurl = MBTA_BASE_URL + '?' + stoplatlng

    datastop = get_json(stopurl)

    return (datastop['stop_name'], datastop['distance'])


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    latlng = get_lat_long(place_name)
    return get_nearest_station(*latlng)


print(get_lat_long('Fenway Park'))
print(get_nearest_station(42.3466764, -71.0972178))
print(find_stop_near('Fenway Park'))
