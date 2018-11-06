# run.py
import json, os, flask
from flask import jsonify
from trip.forms import TripForm
from trip.location import Location
from trip.trip_calculator.trip_calculator import calculate_trip
from trip.geo import getInfo
from flask import Flask, render_template, flash, redirect, request
from config import Config
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

def createRoute(origin, destination):
	# route = [Location, Location, ..., Location]
	# where trip[0]    = origin
	#       trip[-1]   = destination
	#       trip[1:-1] = gas stations
    route = calculate_trip(password = args.password,
    					  origin = origin,
    					  destination = destination,
    					  tank_capacity = 300)
    	
    for location in route:
    	print(location.address)

    return route

def createResponse(route):	
    # create JSON response
    stoppoints = [dict() for x in range(len(route))]
    for x in range(0, len(route)):
    	stoppoints[x]["long"] = route[x].lon
    	stoppoints[x]["lat"] = route[x].lat
    	stoppoints[x]["is_gas_station"] = 1

    result = {"status": 0,
    	"trip1": stoppoints,
    	"cost": [1,2],
    	"time": [0.5,1]		
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

#Main page, produce form, receive value inserted in form, pass the result.html
@app.route('/', methods = ['GET', 'POST'])
def index():
	form = TripForm()
	if flask.request.method == 'POST':
		if form.validate_on_submit():
			result = request.form
			form = TripForm()
			
			origin = request.form.get('origin')
			destination = request.form.get('destination')
			gb = request.form.get('brand')
			cb = request.form.get('carBrand')
			cm = request.form.get('carModel')
			cy = request.form.get('carYear')
			hc = request.form.get('highwayMPG')
			cc = request.form.get('cityMPG')
			tc = request.form.get('tankCapacity')
			igl = request.form.get('currentTankLevel')

			#jdata = get_json_file('/Users/wilsenkosasih/desktop/se2/gasme/user_input.json')
			#car, gas, trip = decode_json(jdata)

			check = checkLocation(origin, destination)
			if check == -1:
				result = createErrorResponse(1)
				return (jsonify(result))
				#error = Location("NOT_FOUND","NOT_FOUND","NOT_FOUND","NOT_FOUND")
				#return render_template('result.html', result=result, form=form, origin=error, destination=error, route=[])
			
			route = createRoute(origin,destination)
			result = createResponse(route)
			#return(jsonify(result))
			return render_template('result.html', result=result, form=form, origin=route[0], destination=route[-1], route=route[:-1])
	else:				
	    return render_template("index.html", title='Trip Form', form=form)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contactus.html")
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
