import p2
import sys

# For testing:
addr1 = sys.argv[1]
addr2 = sys.argv[2]
trip = [addr1, addr2]

start_lat, start_lon = p2.addressToCoordinates(addr1)
dest_lat, dest_lon = p2.addressToCoordinates(addr2)
trip_coord = [start_lat, start_lon, dest_lat, dest_lon]


restaurants = p2.getRestaurants()
initialList = p2.filterRestaurants(restaurants, trip_coord)
recommendedPlaces = p2.finalTen(initialList, trip)

for elem in recommendedPlaces:
	print 'score ' + str(elem[1])
	


