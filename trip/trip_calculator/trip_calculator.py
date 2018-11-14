"""
Trip Cost Calculator.
"""

from trip.location import Location
from trip.geo import getInfo
from trip.trip_calculator.node import TripCalculatorNode
from trip.trip_calculator.grid.grid import Grid
from trip.trip_calculator.heuristics import ShortestStops, CheapestTrip
from trip.trip_calculator.database.utils import *
from geopy.distance import vincenty
from math import ceil
from heapq import heappush, heappop

def calculate_trip(password: str, origin: str, destination: str, tank_capacity=300):
	"""
	Calculates the gas stations stops for the trip.
	
	Args:
	  password: the password to the database.
	  origin: the address string of the origin.
	  destination: the address string of the destination.
	  tank_capacity: the tank capacity for the car, in miles
	
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
	
	# square grid based on tank capacity for efficient neighbor search
	grid = Grid(destination, tank_capacity, cardinalBounds)
	grid.set_grid(gas_stations)
	
	# define the heuristic to be used during the search
	TripCalculatorNode.costCalculator = CheapestTrip(destination)
	
	# frontier and explored states for A* search
	frontier = []
	heappush(frontier, TripCalculatorNode(state=origin, parent=None))
	explored = []
	
	# search
	while True:
		
		# return if frontier is empty
		if len(frontier) == 0:
			return None
		
		# get cost and node of the next element in the frontier
		node = heappop(frontier)
		
		# return if destination within range
		distanceDestination = vincenty((node.state.lat, node.state.lon),
									(destination.lat, destination.lon)).miles
		if distanceDestination <= tank_capacity:
			route = node.get_route()
			route.append(destination)
			return route
		
		# add state of node to explored
		explored.append(node.state)
		
		# for each neighboring station, add to frontier if state not already explored
		for newState in grid.get_neighbors(node.state):
			if newState not in explored:
				heappush(frontier, TripCalculatorNode(state=newState, parent=node))
		

