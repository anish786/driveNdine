from __future__ import division
from operator import itemgetter
from utility import TextProcess
import math
from googlemaps import GoogleMaps
from pygeocoder import Geocoder




def getRestaurants():
	restaurants = []

	inFileName='restaurants.json'
	f=open(inFileName,'r')

	for i in range(0, 14303):
		rest = TextProcess.read_line(f.readline())
		restaurants.append(rest)

	return restaurants




def travelTime(start, dest):
	#return the travel time in seconds
	gmaps = GoogleMaps()
	directions = gmaps.directions(start, dest)
	time = directions['Directions']['Duration']['seconds']
	return time




def addressToCoordinates(address):
	#return the GPS coordinates of an address
	result = Geocoder.geocode(address)
	return result[0].coordinates	






def distanceBetween(x1, y1, x2, y2):
#input values as degrees, returns distance between the two points

#convert to radians

	R = 3963.1676

	lat1 = math.radians(x1)
	lon1 = math.radians(x2)
	lat2 = math.radians(y1)
	lon2 = math.radians(y2)

	#dlon = lon2 - lon1
	#dlat = lat2 - lat1

	#a = math.pow((math.sin(dlat/2)), 2) + math.cos(lat1) * math.cos(lat2)*math.pow((math.sin(dlon/2)), 2)
	#c = 2 * math.asin(math.sqrt(a))

	#distance = R * c

	 # convert decimal degrees to radians 
    	#lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

   	# haversine formula 
    	dlon = lon2 - lon1 
    	dlat = lat2 - lat1 
    	a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    	c = 2 * math.asin(math.sqrt(a))

	mi = R * c
	return mi

def measureSpots(lat1, long1, lat2, long2, n):
	#using a linear approximation, return n points equally spaced on a straight line between the start and destination
	ms = []
	float_n = 1.0*n
	for i in range(0,n+1):
		ms.append([lat1 + ((1.0*i)/float_n)*(lat2-lat1), long1 + ((1.0*i)/float_n)*(long2-long1)])

	return ms



def getInitialList(restaurants, trip):

	startGPS = addressToCoordinates(trip[0])
	goalGPS = addressToCoordinates(trip[1])
	startLat = startGPS[0]
	startLong = startGPS[1]
	goalLat = goalGPS[0]
	goalLong = goalGPS[1]
	
	tripDistance = distanceBetween(startLat, startLong, goalLat, goalLong)
	numberOfSpots =  int(math.floor(tripDistance/20))

	spots = measureSpots(startLat, startLong, goalLat, goalLong, numberOfSpots)

	initialRests = []

	for i in range(0, len(restaurants)):
		currLat = restaurants[i]["latitude"]
		currLong = restaurants[i]["longitude"]

		if(distanceBetween(startLat, startLong, currLat, currLong) > tripDistance):
			#print "Distance between 			
			continue

		for j in range(0, len(spots)):
			if(distanceBetween(currLat, currLong, spots[j][0], spots[j][1]) < 50):
				initialRests.append(restaurants[i])
				break

	return initialRests

def getDistanceScore(rest, trip):

	tripTime = travelTime(trip[0], trip[1])


	
	restAddress = rest["full_adress"]
	start2rest = travelTime(trip[0], restAddress)
	rest2dest = travelTime(restAddress, trip[1])

	additionalTime = (start2rest + rest2dest) - tripTime

	score = (additionalTime / tripTime)

	return score





def getStarScore(restaurant):
#get the restaurant's rating from its dictionary:
	return (restaurant["stars"]/5.0)



def ranker(initialRests, trip):
	
	sortedRanks = []

	for i in range(0, len(initialRests)):
		pair  = []
		distScore = getDistanceScore(initialRests[i], trip)
		starScore = getStarScore(initialRests[i])

		pair.append(initialRests[i])

		alpha = 0.4
		beta = 0.6

		score = alpha * (distScore) + beta * (starScore)

		pair.append(score)

		sortedRanks.append(pair)

	sorted(sortedRanks, key = lambda pair: pair[1])

	return sortedRanks



# For testing:
addr1 = "Phoenix, AZ"
addr2 = "De Forest, WI"

trip = []
trip.append(addr1)
trip.append(addr2)

restaurants = getRestaurants()
print str(len(restaurants))
initialList = getInitialList(restaurants, trip)
recommendedPlaces = ranker(initialList, trip)

print str(len(recommendedPlaces))












