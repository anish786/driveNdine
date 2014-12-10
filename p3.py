#import p2
#import json

def run(addr1, addr2):	
	trip = [addr1, addr2]

	start_lat, start_lon = addressToCoordinates(addr1)
	dest_lat, dest_lon = addressToCoordinates(addr2)
	trip_coord = [start_lat, start_lon, dest_lat, dest_lon]
	#print str(start_lat) + ' ' + str(start_lon)
	#print str(dest_lat) + ' ' + str(dest_lon)

	restaurants = getRestaurants() 
	initialList = filterRestaurants(restaurants, trip_coord)
	recommendedPlaces = finalTen(initialList, trip)
	return recommendedPlaces

#with open("output.json", 'w') as out:
#	for elem in recommendedPlaces:
#		print str(elem[0]["latitude"]) + ' ' +  str(elem[0]["longitude"])  
#		json.dump(elem[0], out)
#		out.write('\n')

	


