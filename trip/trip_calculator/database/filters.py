import abc

class GasStationFilter(abc.ABC):

	@abc.abstractmethod
	def filter(self, gasStation):
		pass
		
class GasStationBrandFilter(GasStationFilter):
	
	def __init__(self, brand):
		self.brand = brand.lower().strip()
	
	def filter(self, gasStation):
		return self.brand in gasStation[1].lower()

class GasStationBrandMultipleFilter(GasStationFilter):
	
	def __init__(self, brands):
		self.brands = [b.lower().strip() for b in brands]
	
	def filter(self, gasStation):
		gasStationBrand = gasStation[1].lower()
		for acceptableBrand in self.brands:
			if acceptableBrand in gasStationBrand:
				return True
		return False

