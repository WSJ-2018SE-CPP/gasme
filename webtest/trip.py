from user import User
from location import Location
from geo import getDistance, getRoute

class Trip:
	def __init__(self, origin, dest, stops, gb, cb, cm, cy, hc, cc, tc, igl):
		self.origin = Location(origin)
		self.dest = Location(dest)
		self.stops = stops
		self.user = User(gb, cb, cm, cy, hc, cc, tc, igl)
		#self.route
		#self.final_routes
		self.test(self.origin, self.dest)
		self.test2(self.origin, self.dest)

	 
	def test(self, start, stop):
		distance = getDistance(start.address , stop.address)
		self.distance = distance["distance"]
		self.duration = distance["duration"]
	
	def test2(self, start, stop):
		route = getRoute(start.address , stop.address)
		self.route = route
				
	def intialRoutes(self, origin, dest, user):
		return 0
		
	def findRoute(self, origin, dest, routes):
		return 0
		
	def calRoute(self, final_routes):
		return 0