from location import Location


class P2p_route:
	def __init__(self, olat, olog, dlat, dlog, duration, distance):
		self.start_lat = olat
		self.start_log = olog
		self.end_lat = dlat
		self.end_log = dlog
		self.travel_time = duration
		self.mileage = distance
	
	
	# Getters 
	def getStartLat():
		return self.start_lat
		
	def getStartLog():
		return self.start_log

	def getEndLat():
		return self.end_lat
	
	def getEndLog():
		return self.end_log
	
	def getTravelTime():
		return self.travel_time
		
	def getMileage():
		return self.mileage