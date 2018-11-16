from geopy.distance import vincenty

def getDistanceInMiles(location1, location2):
	return vincenty((location1.lat, location1.lon),
			(location2.lat, location2.lon)).miles
			
def getDistanceInMilesFromCoordinates(coord1, coord2):
	return vincenty(coord1, coord2).miles

