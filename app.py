# run.py
import json, os, flask
from flask import jsonify
from trip.forms import TripForm
from trip.location import Location
from trip.trip_calculator.trip_calculator import calculateTrip, getRemainingTankLevel, getCostOfTrip
from trip.geo import getInfo, getDistanceDuration
from flask import Flask, render_template, flash, redirect, request
from config import Config
from flask_cors import CORS, cross_origin
import argparse

# argument parser for password
parser = argparse.ArgumentParser(description='Supply the password.')
parser.add_argument('-p',
            dest='password',
            required=True,
            type=str,
            help='the rds password')
args = parser.parse_args()

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, support_credentials=True)

def checkLocation(origin, destination):
	# Check if Origin/Destination is in the US or exist
    # Change with status on JSON later on
    try:
    	o = getInfo(origin)
    	d = getInfo(destination)
    except:
    	return -1
    
    top = 49.3457868 # north lat
    left = -124.7844079 # west long
    right = -66.9513812 # east long
    bottom =  24.7433195 # south lat
    		
    originbound = o["lat"] < top and o["lat"] > bottom and o["long"] < right and o["long"] > left
    destinationbound = d["lat"] < top and d["lat"] > bottom and d["long"] < right and d["long"] > left
    if not (originbound and destinationbound):
    	return -1
		
    return 0

def createRoute(origin, destination, mpg, tankCapacity, initialTankLevel):
	# route = [Location, Location, ..., Location]
	# where trip[0]    = origin
	#       trip[-1]   = destination
	#       trip[1:-1] = gas stations
    route = calculateTrip(password = args.password,
    					  origin = origin,
    					  destination = destination,
    					  mpg = int(mpg),
						  tankCapacity = int(tankCapacity),
						  initialTankLevel = initialTankLevel
						)
    	
    for location in route:
    	print(location.address)

    return route

def combineRoutes(trip, car):
	route = []
	is_gas_station = []
	gas_level = float(car["initial_gas_level"])*float(car["tank_capacity"])/100

	#gas_price = []
	for i in range(1,len(trip)):

		nextRoute = createRoute(trip[i-1]["address"],
								trip[i]["address"],
								car["highway_consumption"],
								car["tank_capacity"],
						        gas_level
								)
		gas_level = getRemainingTankLevel(nextRoute, 
										float(car["highway_consumption"]), 
										float(car["tank_capacity"]), 
										gas_level)

		is_gas_station = is_gas_station + [0]
		is_gas_station = is_gas_station + [1] * (len(nextRoute) - 2)
		if ( i < len(trip) - 1):
			route = route + nextRoute[:-1 or None]
		else:
			route = route + nextRoute
			is_gas_station = is_gas_station + [0]

	for i in range(0,len(route)):
		print (route[i].address)	

	return route, is_gas_station	

def createResponse(route, is_gas_station, car):	
	# create JSON response
	stoppoints = [dict() for x in range(len(route))]
	time = [{} for x in range(len(route)-1)]
	mileage = [{} for x in range(len(route)-1)]
	gas_price = [{} for x in range(len(route))]
	cost = [{} for x in range(len(route)-1)]
	gallons_to_fuel = [{} for x in range(len(route)-1)]
	station_brand = [{} for x in range(len(route))]

	for x in range(0, len(route)):
		stoppoints[x]["long"] = route[x].lon
		stoppoints[x]["lat"] = route[x].lat
		stoppoints[x]["is_gas_station"] = is_gas_station[x]
		if is_gas_station[x] == 1:
			station_brand[x] = route[x].brand
			gas_price[x] = route[x].gasPrice
		else:
			station_brand[x] = "None"
			gas_price[x] = 0.0
	try:
		for x in range(1, len(route)):
			origin = str(route[x-1].lat) + "," + str(route[x-1].lon)
			dest = str(route[x].lat)  + "," + str(route[x].lon)
			disdur = getDistanceDuration(origin, dest)
			time[x-1] = disdur["duration"]
			mileage[x-1] =  disdur["distance"]
	except:
		return {"status": 2}
			
	gas_level = float(car["initial_gas_level"])*float(car["tank_capacity"])/100
	for x in range(1, len(route)-1):
		if is_gas_station[x]:
			remaining = getRemainingTankLevel(route[x-1:x+1], 
											float(car["highway_consumption"]), 
											float(car["tank_capacity"]), 
											gas_level)
			gallons_to_fuel[x-1] = float(car["tank_capacity"]) - remaining
			cost[x-1] = getCostOfTrip(route[x-1:x+2], 
								float(car["highway_consumption"]), 
								float(car["tank_capacity"]),
								gas_level)
			gas_level = float(car["tank_capacity"])
		else:
			cost[x-1] = 0.0
			gallons_to_fuel[x-1] = 0.0
			gas_level = getRemainingTankLevel(route[x-1:x+1], 
										float(car["highway_consumption"]), 
										float(car["tank_capacity"]), 
										gas_level)
			
	cost[len(route)-2] = 0.0
	gallons_to_fuel[len(route)-2] = 0.0

	status = 0
	if len(route) > 23:
		status = 3

	result = {"status": status,
		"trip1": stoppoints,
		"gas_price": gas_price,	
		"mileage": ["0 mi"] + mileage,
		"time": ["0 hour 0 min"] + time,
		"cost": [0.0] + cost,
		"gallons_to_fuel": [0.0] + gallons_to_fuel,
		"station_brand": station_brand
	}
	return result

def createErrorResponse(status_code):
	result = {"status": status_code}
	return result

def get_json_file(path):
    with open(path) as data_file:
        return json.load(data_file)
    return 0

def decode_json(json_data):
    if json_data:
        #car
        car = dict()
        car["car_brand"] = json_data["car"]["car_brand"]
        car["car_model"] = json_data["car"]["car_model"]
        car["car_year"] = json_data["car"]["car_year"]
        car["highway_consumption"] = json_data["car"]["highway_consumption"]
        car["city_consumption"] = json_data["car"]["city_consumption"]
        car["tank_capacity"] = json_data["car"]["tank_capacity"]
        car["initial_gas_level"] = json_data["car"]["initial_gas_level"]
        car["default"] = json_data["car"]["default"]
        #gas
        gas = dict()
        gas["brand"] = json_data["gas"]["brand"]
        #trip
        trip = []
        for one in json_data["trip"]:
            trip.append({"address": one["address"], "address": one["address"]})
        return car, gas, trip

    return 0

def decode_json_from_post(json_data):
    if json_data:
        #car
        car = dict()
        car["car_brand"] = json_data["selectedCarBrand"]
        car["car_model"] = json_data["selectedMake"]
        car["car_year"] = json_data["selectedYear"]
        car["highway_consumption"] = json_data["selectedHwy"]
        car["city_consumption"] = json_data["selectedLocal"]
        car["tank_capacity"] = json_data["selectedTankCapacity"]
        car["initial_gas_level"] = json_data["selectedGasLevel"]
        #gas
        gas = dict()
        gas["brand"] = json_data["selectedGas"]
        #trip
        trip = []
        for one in json_data["locaitons"]:
            trip.append({"address": one, "address": one})
        return car, gas, trip

    return 0

#Main page, produce form, receive value inserted in form, pass the result.html
@app.route('/', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
	jdata = request.get_json()
	print (jdata)

	car, gas, trip = decode_json_from_post(jdata)
	route, is_gas_station = combineRoutes(trip, car)	
	result = createResponse(route, is_gas_station, car)
	print (result)	
	return(jsonify(result))

	

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contactus.html")
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
