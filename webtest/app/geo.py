#geo.py

import urllib.request
import requests

def getInfo(address):
	GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
	params = {
		'input': address,
		'inputtype': 'textquery',
		'fields': 'name,place_id,geometry',
		'key': 'AIzaSyDaB2geFvRw5ZEfxXl8jU1VBxi8-TNL-IY'
	}
	
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()
	
	geodata = dict()
	if res['status'] == 'ZERO_RESULTS':
		geodata['lat'] = 'NOT FOUND'
		geodata['long'] = 'NOT FOUND'
		geodata['name'] = 'NOT FOUND'
		geodata['place_id'] = 'NOT FOUND'
	else:
		geodata['lat'] = res['candidates'][0]['geometry']['location']['lat']
		geodata['long'] = res['candidates'][0]['geometry']['location']['lng']
		geodata['name'] = res['candidates'][0]['name']
		geodata['place_id'] = res['candidates'][0]['place_id']

	return geodata
	