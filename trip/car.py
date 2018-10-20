class Car:
	def __init__(self, cb, cm, cy, hc, cc, tc, igl):
		self.car_brand = cb
		self.car_model = cm
		self.car_year = cy
		self.highway_consumption = hc
		self.city_consumption = cc
		self.tank_capacity = tc
		self.initial_gas_level = igl
	
	def getHwyConsumption(self):
		return self.highway_consumption
		
	def getCityConsumption(self):
		return self.city_consumption
		
	def getTankCapacity(self):
		return self.tank_capacity
		
	def getInitialGasLevel(self):
		return self.initial_gas_level