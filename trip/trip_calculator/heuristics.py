import abc
from geopy.distance import vincenty
from trip.location import GasStation

class TripCalculatorHeuristic(abc.ABC):

	def __init__(self, destination):
		"""
		destination: a Location object for the trip destination.
		"""
		self.destination = destination

	@abc.abstractmethod
	def calculateHeuristic(self, currentLocation, previousLocation):
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
		TripCalculatorHeuristic.__init__(self, destination)

	def calculateHeuristic(self, currentLocation, previousLocation):
		return vincenty((currentLocation.lat, currentLocation.lon),
						(self.destination.lat, self.destination.lon)).miles

class CheapestTrip(TripCalculatorHeuristic):
	"""
	Heuristic that tries to get to the destination by
	spending as least as possible on gas.
	"""
	
	def __init__(self, destination):
		"""
		destination: a Location object for the trip destination.
		"""
		TripCalculatorHeuristic.__init__(self, destination)

	def calculateHeuristic(self, currentLocation, previousLocation):
		currentLocationGasPrice = (
				currentLocation.gasPrice if isinstance(currentLocation, GasStation) else 0)
		distanceToDestination = vincenty(
				(currentLocation.lat, currentLocation.lon),
				(self.destination.lat, self.destination.lon)).miles
		return currentLocationGasPrice * distanceToDestination
		
