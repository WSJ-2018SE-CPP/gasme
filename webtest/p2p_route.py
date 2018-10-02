from location import Location

class P2p_route:
	def __init__(self, start, end, ml, mh, ttl, tth):
		self.start = start
		self.end = end
		
		self.mileage_local = ml
		self.mileage_hwy = mh
		self.travel_time_local = ttl
		self.travel_time_hwy = tth