from trip.user import User
from trip.location import Location
from trip.p2p_route import P2p_route
from trip.geo import getDistanceDuration, getRoute, getInfo

class Trip:
	def __init__(self, origin, dest, stops, gb, cb, cm, cy, hc, cc, tc, igl):
		o = getInfo(origin)
		self.origin = Location(o["name"], o["long"], o["lat"], o["address"])
		d = getInfo(dest)
		self.dest = Location(d["name"], d["long"], d["lat"], d["address"])
		self.stops = stops
		self.user = User(gb, cb, cm, cy, hc, cc, tc, igl)
		
		#Initial Route
		stop_points = self.getStopPointsLocation(self.origin, self.dest)
		self.route = [P2p_route for x in range(len(stop_points))]
		for x in range(0, len(stop_points)):
			self.route[x] = P2p_route(stop_points[x]["origin_lat"], 
									stop_points[x]["origin_log"],
									stop_points[x]["destination_lat"],
									stop_points[x]["destination_log"],
									stop_points[x]["duration"],
									stop_points[x]["distance"])
		
		#Example on how to get stop points using Address/LongLat with GoogleMap Direction API
		stop_points2 = self.getStopPointsAddress(self.origin.address, self.dest.address)
		stop_points3 = self.getStopPointsLogLat(self.origin.lon, self.origin.lat, self.dest.lon, self.dest.lat)

		#Example on how to get distance/duration using Address/LongLat/Location with GoogleMap Distance Matrix API			
		disdur1 = self.calRouteLogLat(self.origin.lon, self.origin.lat, self.dest.lon, self.dest.lat)
		disdur2 = self.calRouteAddress(self.origin.address, self.dest.address)
		disdur3 = self.calRouteLocation(self.origin, self.dest)
		disdur4 = self.calRouteLogLat(self.route[0].start_log, self.route[0].start_lat, self.dest.lon, self.dest.lat)

		self.distance = disdur4["distance"]
		self.duration = disdur4["duration"]


	#Functions to calculate distance & duration between points given Log/Lat, Location, or Address of Origin 
	#and Destination by utilizing Google Map Distance Matrix API
	#To access duration => disdur["duration"]
	#To access distance => disdur["distance"]
	def calRouteLogLat(self, startlog, startlat, stoplog, stoplat):
		disdur = getDistanceDuration(str(startlat)+','+str(startlog), str(stoplat)+','+str(stoplog))
		return disdur
		
	def calRouteAddress(self, start, stop):
		disdur = getDistanceDuration(start , stop)
		return disdur
	
	def calRouteLocation(self, start, stop):
		disdur = getDistanceDuration(start.address , stop.address)
		return disdur
	
	#Functions to calculate stop points between points given Log/Lat, Location, or Address of Origin 
	#and Destination by utilizing Google Map Directions API
	#To access each small "route", use stop_points[x], where x is 0 to len(stop_points)
	#To access a "route" instruction => stop_points[x]["instruction"]
	#To access a "route" duration => stop_points[x]["duration"]
	#To access a "route" distance => stop_points[x]["distance"]
	#To access a "route" origin latitude => stop_points[x]["origin_lat"]
	#To access a "route" destination latitude => stop_points[x]["destination_lat"]
	#To access a "route" origin longitude => stop_points[x]["origin_log"]
	#To access a "route" destination longitude => stop_points[x]["destination_log"]	
	
	def getStopPointsLogLat(self, startlog, startlat, stoplog, stoplat):
		stop_points = getRoute(str(startlat)+','+str(startlog), str(stoplat)+','+str(stoplog))
		return stop_points
	
	def getStopPointsAddress(self, start, stop):
		stop_points = getRoute(start , stop)
		return stop_points
		
	def getStopPointsLocation(self, start, stop):
		stop_points = getRoute(start.address , stop.address)
		return stop_points
					
	
	def intialRoutes(self, origin, dest, user):
		return 0
	
	#for calculating final route, returns an array of location for stop points
	def findRoute(self, origin, dest, stops = "", brand = "", mpg = "", tankcapacity = "", initialtank = ""):
		#CALL ALGORITHM HERE
	
		#for example, the route returned is initial route
		return self.route
