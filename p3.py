import p2
#import json

def run(addr1, addr2):	
	trip = [addr1, addr2]

	start_lat, start_lon = p2.addressToCoordinates(addr1)
	dest_lat, dest_lon = p2.addressToCoordinates(addr2)
	trip_coord = [start_lat, start_lon, dest_lat, dest_lon]
	#print str(start_lat) + ' ' + str(start_lon)
	#print str(dest_lat) + ' ' + str(dest_lon)

	restaurants = p2.getRestaurants() 
	initialList = p2.filterRestaurants(restaurants, trip_coord)
	recommendedPlaces = p2.finalTen(initialList, trip)
	return recommendedPlaces

#with open("output.json", 'w') as out:
#	for elem in recommendedPlaces:
#		print str(elem[0]["latitude"]) + ' ' +  str(elem[0]["longitude"])  
#		json.dump(elem[0], out)
#		out.write('\n')

	


