"""
Trip Cost Calculator.
"""

from trip.location import Location
from trip.geo import getInfo
from trip.trip_calculator.node import TripCalculatorNode
from trip.trip_calculator.grid.grid import Grid
from trip.trip_calculator.heuristics import ShortestStops, CheapestTrip
from trip.trip_calculator.database.utils import *
from trip.trip_calculator.distance.distance_utils import *
from math import ceil
from heapq import heappush, heappop

def calculateTrip(password: str, origin: str, destination: str, mpg=30, tankCapacity=12, initialTankLevel=12):
	"""
	Calculates the gas stations stops for the trip.
	
	Args:
	  password: the password to the database.
	  origin: the address string of the origin.
	  destination: the address string of the destination.
	  mpg: the miles per gallon of the car
	  tankCapacity: the tank capacity, in gallons, of the car
	  initialTankLevel: the initial tank level, in gallons, of the car
	
	Returns:
	  A list of locations including origin, stops and destination for the trip.
	"""
	
	# get the Location of the origin and destination
	origin = Location.fromAddress(origin)
	destination = Location.fromAddress(destination)
	
	# get all gas stations and boundary coordinates
	gas_stations, cardinalBounds = getAllGasStationsAndBounds(password=password)
	
	# validate gas stations
	if len(gas_stations) == 0:
		print("Could not get any gas stations from the database")
		return None
	
	# tank capacity as miles in a full tank
	tankCapacityMiles = mpg * tankCapacity
	
	# square grid based on tank capacity for efficient neighbor search
	grid = Grid(destination, tankCapacityMiles, cardinalBounds)
	grid.set_grid(gas_stations)
	
	# define the heuristic to be used during the search
	TripCalculatorNode.costCalculator = CheapestTrip(destination)
	
	# frontier and explored states for A* search
	frontier = []
	heappush(frontier, TripCalculatorNode(state=origin, parent=None))
	explored = []
	
	# current tank level, initially it is the initial tank level
	# but we assume a full fill up at each stop
	currentTankLevelInMiles = mpg * initialTankLevel
	
	# search
	while True:
		
		# return if frontier is empty
		if len(frontier) == 0:
			return None
		
		# get cost and node of the next element in the frontier
		node = heappop(frontier)
		
		# return if destination within range
		distanceDestination = getDistanceInMiles(node.state, destination)
		if distanceDestination <= currentTankLevelInMiles:
			route = node.get_route()
			route.append(destination)
			return route
		
		# add state of node to explored
		explored.append(node.state)
		
		# for each neighboring station, add to frontier if state not already explored
		for newState in grid.get_neighbors(node.state, currentTankLevelInMiles):
			if newState not in explored:
				heappush(frontier, TripCalculatorNode(state=newState, parent=node))
		
		# update the tank level, assume a full fillup
		currentTankLevelInMiles = mpg * tankCapacity


def getCostOfTrip(trip, mpg, tankCapacity, initialTankLevel):
	"""
	Gets the total cost of a trip.
	
	Args:
	  trip: a list of Locations, where trip[0] is the origin, trip[-1] is 
	        the destination and trip[1:-1] are GasStations
	  mpg: the miles per gallon of the car
	  tankCapacity: the tank capacity, in gallons, of the car
	  initialTankLevel: the initial tank level, in gallons, of the car
	"""
	
	tripCost = 0
	currentTankLevel = initialTankLevel
	for i in range(1, len(trip) - 1):
		currentTankLevel -= getDistanceInMiles(trip[i-1], trip[i]) / mpg
		tripCost += (tankCapacity - currentTankLevel) * trip[i].gasPrice
		currentTankLevel = tankCapacity
	return tripCost


def getRemainingTankLevel(trip, mpg, tankCapacity, initialTankLevel):
	"""
	Gets the tank level at the end of the trip.
	
	Args:
	  trip: a list of Locations, where trip[0] is the origin, trip[-1] is 
	        the destination and trip[1:-1] are GasStations
	  mpg: the miles per gallon of the car
	  tankCapacity: the tank capacity, in gallons, of the car
	  initialTankLevel: the initial tank level, in gallons, of the car
	"""
	
	tankLevelAtSecondToLastStop = (initialTankLevel if len(trip) == 2 else tankCapacity)
	gallonsToLastStop = getDistanceInMiles(trip[-2], trip[-1]) / mpg
	return tankLevelAtSecondToLastStop - gallonsToLastStop

