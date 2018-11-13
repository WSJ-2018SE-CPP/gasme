import abc
from geopy.distance import vincenty

class TripCalculatorHeuristic(abc.ABC):
	@abc.abstractmethod
	def calculateHeuristic(self, currentLocation, parentLocation):
		pass

class ShortestStops(TripCalculatorHeuristic):
	"""
	Heuristic that tries to get to the destination in the
	least number of stops as possible.
	"""

	def __init__(self, destination):
		"""
		destination: a Location object for the trip destination.
		"""
		self.destination = destination

	def calculateHeuristic(self, currentLocation, parentLocation):
		return vincenty((currentLocation.lat, currentLocation.lon),
						(self.destination.lat, self.destination.lon)).miles
