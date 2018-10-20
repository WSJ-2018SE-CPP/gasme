from trip.car import Car

class User:
	def __init__(self, gb, cb, cm, cy, hc, cc, tc, igl):
		self.gas_brand = gb
		self.car = Car(cb, cm, cy, hc, cc, tc, igl)
	
	# Getters
	def getCar(self):
		return self.car
		
	def getGasBrand(self):
		return self.gas_brand
