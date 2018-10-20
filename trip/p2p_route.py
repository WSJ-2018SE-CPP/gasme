from trip.location import Location


class P2p_route:
	def __init__(self, olat, olog, dlat, dlog, duration, distance):
		self.start_lat = olat
		self.start_log = olog
		self.end_lat = dlat
		self.end_log = dlog
		self.travel_time = duration
		self.mileage = distance
	
	
	# Getters 
	def getStartLat(self):
		return self.start_lat
		
	def getStartLog(self):
		return self.start_log

	def getEndLat(self):
		return self.end_lat
	
	def getEndLog(self):
		return self.end_log
	
	def getTravelTime(self):
		return self.travel_time
		
	def getMileage(self):
		return self.mileage
		
	def to_json(self):
		return {
			'start_lat': self.start_lat,
			'start_log': self.start_log,
		}
