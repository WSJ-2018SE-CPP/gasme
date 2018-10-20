#geo.py

import urllib
import requests

def getInfo(address):
	GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
	params = {
		'input': address,
		'inputtype': 'textquery',
		'fields': 'name,place_id,geometry,formatted_address',
		'key': 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY'
	}
	
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()
	
	if res['status'] != 'ZERO_RESULTS':
		geodata = dict()
		geodata['address'] = res['candidates'][0]['formatted_address']
		geodata['lat'] = res['candidates'][0]['geometry']['location']['lat']
		geodata['long'] = res['candidates'][0]['geometry']['location']['lng']
		geodata['name'] = res['candidates'][0]['name']
		geodata['place_id'] = res['candidates'][0]['place_id']
		return geodata
	else:
		raise Exception("Could not get data for address: %s" % address)

def getDistanceDuration(origin, destination):
	GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'
	params = {
		'units' : 'imperial',
		'origins' : origin,
		'destinations' : destination,
		'key': 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY'
	}
	
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()
	
	trip = dict()
	if res['rows'][0]['elements'][0]['status'] == 'NOT_FOUND':
		trip['distance'] = 'NOT_FOUND'
		trip['duration'] = 'NOT_FOUND'
	else:
		trip['distance'] = res['rows'][0]['elements'][0]['distance']['text']
		trip['duration'] = res['rows'][0]['elements'][0]['duration']['text']
	#need to check if route too far
	return trip

def getRoute(origin, destination):
	GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json'
	params = {
		'origin' : origin,
		'destination' : destination,
		'key': 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY'
	}
	
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()
	
	route = dict()
	
	if res['status'] == 'OK':
		route = res['routes'][0]['legs'][0]['steps']
	else:
		route = 0
		
	routes = [dict() for x in range(len(route))]

	for x in range(0, len(route)):
		routes[x]['instruction'] = route[x]['html_instructions']
		routes[x]['duration'] = route[x]['duration']['text'] 
		routes[x]['distance'] = route[x]['distance']['text'] 
		routes[x]['origin_lat'] = route[x]['start_location']['lat']
		routes[x]['destination_lat'] = route[x]['end_location']['lat']
		routes[x]['origin_log'] = route[x]['start_location']['lng']
		routes[x]['destination_log'] = route[x]['end_location']['lng']

		#routes = routes + route[x]['html_instructions'] + ','
		#routes = routes + route[x]['duration']['text'] + ','		
		#routes = routes + route[x]['distance']['text'] + '    |||     '
				
	return routes
	

def getEuclideanDistance(l1, l2):
	"""
	Gets the Euclidean distance between two points represented at (lat, long)
	
	Args:
	  l1: (lat, long) for the first point
	  l2: (lat, long) for the second point
	Return:
	  The Euclidea distance between the two points.
	"""
