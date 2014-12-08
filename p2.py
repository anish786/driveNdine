import json
from math import radians, cos, sin, atan2, sqrt, floor
from googlemaps import GoogleMaps
from pygeocoder import Geocoder

#process the json file of restaurants
#just used to get a dataset for testing:
def getRestaurants():
	restaurants = []

	inFileName='restaurants.json'
	f=open(inFileName,'r')

	for line in f:
		rest = json.loads(line)
		restaurants.append(rest)

	return restaurants

#-------------------------------------------------------------------------------------------------#
# Helper functions:

#return the GPS coordinates of address
def addressToCoordinates(address):
	result = Geocoder.geocode(address) 
	return result[0].coordinates	

#return the travel time from start to dest, in seconds
def travelTime(start, dest):
	gmaps = GoogleMaps()
	directions = gmaps.directions(start, dest)
	time = directions['Directions']['Duration']['seconds']
	return time

#find the distance between two sets of (lat,long) coordinates
def distanceBetween(start_lat, start_lon, dest_lat, dest_lon):
	# need to debug - roundoff errors?
	start_lat, start_lon, dest_lat, dest_lon = map(radians, [start_lat, start_lon, dest_lat, dest_lon])
	dlon = dest_lon - start_lon
	dlat = dest_lat - start_lat
	a = sin(dlat/2.0)**2 + cos(start_lat) * cos(dest_lat) * sin(dlon/2.0)**2
	c = 2.0 * atan2(sqrt(a), sqrt(1.0-a)) 
	R = 3963.1676						#radius of Earth, in miles	
	mi = R * c
	return mi  

#-------------------------------------------------------------------------------------------------#
# Scoring functions:

def getDistanceScore(rest, trip_coord):
	rest_coord = [rest["latitude"], rest["longitude"]]	

	trip_dist = distanceBetween(trip_coord[0], trip_coord[1], trip_coord[2], trip_coord[3])
	start_rest = distanceBetween(trip_coord[0], trip_coord[1], rest_coord[0], rest_coord[1])
	rest_dest = distanceBetween(rest_coord[0], rest_coord[1], trip_coord[2], trip_coord[3])
	additional_dist = (start_rest + rest_dest) - trip_dist
	
	score = (additional_dist/trip_dist)
	return score

def getTimeScore(rest, trip):
	#travelTime function only receives known restAddress
	rest_address = rest["full_address"]	
	
	try:
		trip_time = travelTime(trip[0], trip[1])
		start_rest = travelTime(trip[0], rest_address)
		rest_dest = travelTime(rest_address, trip[1])
		additional_time = (start_rest + rest_dest) - trip_time
	except:
		return -1		

	if (additional_time >= trip_time):
		return 0.0
	else:
		return (1.0 - (additional_time/trip_time))

def getStarScore(restaurant):
#get the restaurant's rating from its dictionary:
	return (restaurant["stars"]/5.0)

#-------------------------------------------------------------------------------------------------#
# Helper functions for ranking function:

def filterRestaurants(restaurants, trip_coord):
	initial_rests = []
	for rest in restaurants:
		rest_score   = getDistanceScore(rest, trip_coord)
		if(rest_score > 1.5):
			continue
		else:
			initial_rests.append([rest, rest_score])	
	
	filtered_set = sorted(initial_rests, key = lambda pair: pair[1])
	
	#filter down to top 50 by getDistanceScore
	if(len(filtered_set) > 50):
		filtered_set = filtered_set[0:50] 

	return filtered_set			

def finalTen(filtered_set, trip):
	filtered_copy = []
	for elem in filtered_set:
		rest_address = elem[0]["full_address"]

		time_score = getTimeScore(elem[0], trip)
		if(time_score is -1):
			continue			# do not include address unrecognized by GoogleMaps API
	
		star_score = getStarScore(elem[0])
		rest_score = 0.6*time_score + 0.4*star_score
		filtered_copy.append([elem[0], rest_score])
	
	final_ten = sorted(filtered_copy, key = lambda pair: pair[1], reverse = True)
	
	#filter down to top 10 by rest_score
	if(len(final_ten) > 10):
		final_ten = final_ten[0:10] 

	return final_ten 			
