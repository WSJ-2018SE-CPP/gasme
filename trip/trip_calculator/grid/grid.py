from math import ceil
from trip.trip_calculator.distance.distance_utils import *

class Grid:
	"""
	A grid for splitting the total coverage of gas stations into blocks that can be traveled
	 to based on the tank mileage. That is, for a gas station in say Los Angeles, we know we 
	 cannot travel to New York on one tank of gas. Therefore, we can eliminate these stations
	 from the the gas station in LA's successor stations. We can efficiently do this by
	 creating a grid based on the tank capacity. Each gas station in a block can only go to 
	 neighboring blocks, so we can eliminite much of the successor space.
	"""
	
	def __init__(self, destination, tank_capacity, cardinalBounds):
		"""
		Creates a Grid structure.

		Args:
		  destination: the destination
		  tank_capacity: the tank_capacity of the car
		  N: the most North latitude
		  S: the most South latitude
		  E: the most East longitude
		  W: the most West logitude
		"""
		
		# instance variables
		self.destination = destination
		self.tank_capacity = tank_capacity
		self.N = cardinalBounds.N
		self.S = cardinalBounds.S
		self.E = cardinalBounds.E
		self.W = cardinalBounds.W
		 
		# boundary points
		top_left     = (self.N, self.W)
		top_right    = (self.N, self.E)
		bottom_left  = (self.S, self.W)
		bottom_right = (self.S, self.E)
		
		# width and height of boundary
		width = max(getDistanceInMilesFromCoordinates(top_left, top_right), getDistanceInMilesFromCoordinates(bottom_left, bottom_right))
		height = max(getDistanceInMilesFromCoordinates(top_left, bottom_left), getDistanceInMilesFromCoordinates(top_right, bottom_right))
		
		# number of rows and columns
		self.grid_rows = ceil(height/tank_capacity)
		self.grid_cols = ceil(width/tank_capacity)
		
		# initialize grid
		self.grid = [[[] for _ in range(self.grid_cols)] for _ in range(self.grid_rows)]
		
	
	def set_grid(self, gas_stations):
		"""
		Places each gas station inside the grid.
		
		Args:
		  gas_stations: a list of gas stations [Location, Location, ...]
		"""
	
		for gas_station in gas_stations:
			lat = gas_station.lat
			lon = gas_station.lon
			row = int(getDistanceInMilesFromCoordinates((lat, lon), (self.N, lon))/self.tank_capacity)
			col = int(getDistanceInMilesFromCoordinates((lat, lon), (lat, self.W))/self.tank_capacity)
			self.grid[row][col].append(gas_station)
	
	
	def get_neighbors(self, gas_station, currentTankLevelInMiles):
		"""
		Gets all neighboring gas stations.
		
		Args:
		  gas_station: the gas station to get neighbors of.
		  currentTankLevelInMiles: the number of miles we can travel on our current tank level
		
		Return:
		  A list of (distanceTraveled, distanceDestination, Location)
		   for each gas station neighbor.
		"""
		
		# latitude and longitude of the gas station
		lat = gas_station.lat
		lon = gas_station.lon
		
		# list of successor stations
		gas_stations = []
		
		# get the row and column of the gas station
		row = int(getDistanceInMilesFromCoordinates((lat, lon), (self.N, lon))/self.tank_capacity)
		col = int(getDistanceInMilesFromCoordinates((lat, lon), (lat, self.W))/self.tank_capacity)
		
		# add gas stations in neighboring blocks
		gas_stations.extend(self._get_all(gas_station, row, col, currentTankLevelInMiles))
		if row > 0:
			gas_stations.extend(self._get_all(gas_station, row-1, col, currentTankLevelInMiles))
		if row < self.grid_rows-1:
			gas_stations.extend(self._get_all(gas_station, row+1, col, currentTankLevelInMiles))
		if col > 0:
			gas_stations.extend(self._get_all(gas_station, row, col-1, currentTankLevelInMiles))
		if col < self.grid_cols-1:
			gas_stations.extend(self._get_all(gas_station, row, col+1, currentTankLevelInMiles))
		if row > 0 and col > 0:
			gas_stations.extend(self._get_all(gas_station, row-1, col-1, currentTankLevelInMiles))
		if row > 0 and col < self.grid_cols-1:
			gas_stations.extend(self._get_all(gas_station, row-1, col+1, currentTankLevelInMiles))
		if row < self.grid_rows-1 and col > 0:
			gas_stations.extend(self._get_all(gas_station, row+1, col-1, currentTankLevelInMiles))
		if row < self.grid_rows-1 and col < self.grid_cols-1:
			gas_stations.extend(self._get_all(gas_station, row+1, col+1, currentTankLevelInMiles))
		
		return gas_stations
	
	
	def _get_all(self, origin, row, col, currentTankLevelInMiles):
		"""
		Get all gas stations and distances from an origin gas station within a block.
		
		Args:
		  origin: the origin gas station
		  row: the row of the block
		  col: the col of the block
		  currentTankLevelInMiles: the number of miles we can travel on our current tank level
		
		Return:
		  A list of (distanceTraveled, distanceDestination, Location) for each
		   gas station in the block from the origin.
		"""
		
		# origin latitude and longitude
		origin_lat = origin.lat
		origin_lon = origin.lon
		
		# list of (distance, Location) to return
		gas_stations = []
		
		# for each station within the block, add it along with the distance to the list
		for gas_station in self.grid[row][col]:
			distanceTraveled = getDistanceInMilesFromCoordinates((origin_lat, origin_lon),
										(gas_station.lat, gas_station.lon))
			if distanceTraveled > currentTankLevelInMiles:
				continue
			gas_stations.append(gas_station)
		
		return gas_stations

