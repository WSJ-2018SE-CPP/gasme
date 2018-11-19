from trip.location import GasStation
from trip.trip_calculator.grid.cardinal_bounds import CardinalBounds
import pymysql

# database information
host="gasme-db.cusrpulgblsj.us-west-1.rds.amazonaws.com"
port=3306
dbname='gasme'
user='gasme'

def getAllGasStationsAndBounds(password: str):
	"""
	Gets all gas stations and cardinal bounds, max/min lat and max/min lon, from the database.

	Args:
	  password: the database password

	Returns:
	  [Location], CardinalBounds for all gas stations in the database
	"""

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
		   		if "Canada" in gas_station[0]:
		   			continue
		   		N = max(N, gas_station[2])
		   		S = min(S, gas_station[2])
		   		E = max(E, gas_station[3])
		   		W = min(W, gas_station[3])
		   		gas_stations.append(
		    		GasStation(
		    			address=gas_station[0],
		    			name=gas_station[1],
		    			lat=gas_station[2],
		    			lon=gas_station[3],
		    			gasPrice=float(gas_station[4]),
		    			brand=gas_station[1]
		    		)
		    	)
	finally:
		conn.close()
    
	return gas_stations, CardinalBounds(N=N, S=S, E=E, W=W)
