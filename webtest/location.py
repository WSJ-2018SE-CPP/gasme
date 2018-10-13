from geo import getInfo

class Location:
	def __init__(self, address, gasprice = 0):
		location = getInfo(address)
		self.name = location["name"]
		self.log = location["long"]
		self.lat = location["lat"]
		self.address = location["address"]
		self.gas_price_per_gal = gasprice
	
	# Getters
	def getName(self):
		return self.name
	
	def getAddress(self):
		return self.address
		
	def getLog(self):
		return self.log
		
	def getLat(self):
		return self.lat
		
	def getGasPrice(self):
		return self.gas_price_per_gal