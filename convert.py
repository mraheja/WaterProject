import requests
import json

def convert(adress):
	URL = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + adress + '&key=AIzaSyBmQGSSO5AYhoCSr9eBc5PNiiY8Cp6mNbQ&callback=initMap'
	r = requests.get(URL).json()
	for e in r['results']:
		return (e['geometry']['location'])
