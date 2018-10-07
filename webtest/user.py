from car import Car

class User:
	def __init__(self, gb, cb, cm, cy, hc, cc, tc, igl):
		self.gas_brand = gb
		self.car = Car(cb, cm, cy, hc, cc, tc, igl)
	
	# Getters
	def getCar():
		return self.car
		
	def getGasBrand():
		return self.gas_brand