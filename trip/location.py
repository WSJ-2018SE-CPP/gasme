from trip.geo import getInfo

class Location:
	"""
	A Location object containing:
	 - name
	 - longitude
	 - latitude
	 - address
	"""
	
	def __init__(self, name, lon, lat, address):
		"""
		Creates a Location object.
		
		Args:
		  name: the name of the location
		  lon: the longitude
		  lat: the latitude
		  address: the address
		"""
		
		self.name = name
		self.lon = lon
		self.lat = lat
		self.address = address
	
	
	@classmethod
	def fromAddress(cls, address):
		"""
		Creates a Location object from an address string. Gets the
		 additional information from Google API.
		
		Args:
		  address: the address of the location.
		
		Returns:
		  A Location object after getting the necessary data.
		"""
		
		# get the location data
		location = getInfo(address)
		
		# return Location object
		return cls(name = location["name"],
					lon = location["long"],
					lat = location["lat"],
					address = location["address"])


class GasStation(Location):
	"""
	A Gas Station object is a Location with a gas price
	"""
	
	def __init__(self, name, lon, lat, address, gasPrice, brand):
		Location.__init__(self, name, lon, lat, address)
		self.gasPrice = gasPrice
		self.brand = brand
	
	def getGasPrice():
		return self.gasPrice
	
	def getBrand():
		return self.brand
