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

