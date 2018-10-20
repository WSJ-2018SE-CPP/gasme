"""
Trip Cost Calculator.
"""

from trip.location import Location
from trip.geo import getInfo
from trip.trip_calculator.node import Node
from geopy.distance import vincenty
import pymysql
from math import ceil

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
	top_left     = (N, W)
	top_right    = (N, E)
	bottom_left  = (S, W)
	bottom_right = (S, E)
	width = max(vincenty(top_left, top_right).miles, vincenty(bottom_left, bottom_right).miles)
	height = max(vincenty(top_left, bottom_left).miles, vincenty(top_right, bottom_right).miles)
	grid = [[[] for _ in range(ceil(width/tank_capacity))] for _ in range(ceil(height/tank_capacity))]
	for gas_station in gas_stations:
		lat = gas_station.lat
		lon = gas_station.lon
		row = int(vincenty((lat, lon), (N, lon)).miles/tank_capacity)
		col = int(vincenty((lat, lon), (lat, W)).miles/tank_capacity)
		grid[row][col].append(gas_station)
	
	# frontier and explored states for A* search
	frontier = [Node(state=origin, parent=None, cost=0)]
	explored = [origin]
	
	print(ceil(width / tank_capacity))
	print(ceil(height / tank_capacity))
	

