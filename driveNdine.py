from __future__ import division
import json
import re
from stemming.porter2 import stem
from operator import itemgetter
from math import log
from googlemaps import GoogleMaps
from pygeocoder import Geocoder	


class driveNdine(object):
	def __init__(self):
		gmaps = GoogleMaps()
		pass

	@staticmethod
	def read_line(a_json_string_from_document):
		return json.loads(a_json_string_from_document)

	@staticmethod
	def get_data(info):
		for line in f:
			name = driveNdine.read_line(line)['name']
			address = driveNdine.read_line(line)['full_address']
			longitude = driveNdine.read_line(line)['longitude']
			latitude = driveNdine.read_line(line)['latitude']
			info['name'].append(name)
			info['address'].append(address)
			info['longitude'].append(longitude)
			info['latitude'].append(latitude)

	def travelTime(start, dest):
		#return the travel time in seconds
		directions = gmaps.directions(start, dest)
		time = directions['Directions']['Duration']['seconds']
		return time
		
	@staticmethod
	def addressToCoordinates(address):
		#return the GPS coordinates of an address
		result = Geocoder.geocode(address)
		return result[0].coordinates

if __name__ == '__main__':
	DriveNDine = driveNdine()
	infilename = "restaurants.json"
	f = open(infilename,'r')
	line = 0
	info = {'name': [],'address': [], 'longitude': [], 'latitude': []}
	driveNdine.get_data(info)