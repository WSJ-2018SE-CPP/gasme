"""
Trip Cost Calculator.
"""

from trip.location import Location
from trip.geo import getInfo
from trip.trip_calculator.node import Node
from trip.trip_calculator.grid import Grid
from geopy.distance import vincenty
import pymysql
from math import ceil
from heapq import heappush, heappop

# database information
host="gasme-db.cusrpulgblsj.us-west-1.rds.amazonaws.com"
port=3306
dbname='gasme'
user='gasme'

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
	
	# lat and lon bounds
	N = -90
	S = 90
	E = -180
	W = 180
	
	# list of all gas stations as Location
	gas_stations = []
	
	# get, parse and add each gas station
	conn = pymysql.connect(host, user=user, port=port, passwd=password, db=dbname)
	try:
		with conn.cursor() as cursor:
		    sql = 'SELECT * from gas_prices'
		    cursor.execute(sql)
		    all_gas_stations = cursor.fetchall()
		    for gas_station in all_gas_stations:
		   		N = max(N, gas_station[2])
		   		S = min(S, gas_station[2])
		   		E = max(E, gas_station[3])
		   		W = min(W, gas_station[3])
		   		gas_stations.append(
		    		Location(
		    			address=gas_station[0],
		    			name=gas_station[1],
		    			lat=gas_station[2],
		    			lon=gas_station[3]
		    		)
		    	)
	finally:
		conn.close()
	
	# validate gas stations
	if len(gas_stations) == 0:
		print("Could not get any gas stations from the database")
		return None
	
	# square grid based on tank capacity
	grid = Grid(destination, tank_capacity, N, S, E, W)
	grid.set_grid(gas_stations)
	
	# frontier and explored states for A* search
	frontier = []
	heappush(frontier, Node(state=origin,
							parent=None,
							cost=vincenty((origin.lat, origin.lon),
									(destination.lat, destination.lon)).miles))
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
		for distanceTraveled, distanceDestination, newState in grid.get_neighbors(node.state):
			if newState not in explored:
				heappush(frontier, Node(
								state=newState,
								parent=node,
								cost=distanceDestination))
		

