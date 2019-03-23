import requests
import json

def convert(adress):
	URL = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + adress + '&key=INSERT_KEY&callback=initMap'
	r = requests.get(URL).json()
	for e in r['results']:
		return (e['geometry']['location'])
